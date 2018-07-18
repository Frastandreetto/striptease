#from program_viewer import main
from PyQt5 import QtCore, QtWidgets
import sys
import os
import websocket
import json
import numpy as np
import time
import astropy.time as at
import datetime as dt
from program_viewer.ui.main_window import Ui_MainWindow
from web.rest.base import Connection
from web.ws.base import WsBase

N_SEC = 20

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()

        self.conn = Connection()
        self.conn.login('stefano.sartor','lucciola88')

        self.ws_dx =  WsBase(self.conn)
        self.ws_sx =  WsBase(self.conn)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


    async def __recv(self,url,ws,wdg):
        await ws.connect(url)
        t0 = time.time()

        data = np.ndarray([0], dtype=np.int32)
        ts = np.ndarray([0],dtype=dt.datetime)

        while True:
            pkt = await ws.recv()
            t1 = time.time()
            tt = at.Time(pkt['mjd'], format='mjd')
            data = np.append(data,pkt['DEMU1'])
            ts   = np.append(ts,tt.to_datetime())

            if t1 - t0 > 0.2:
                t0 = t1
                wdg.axes.cla()
                wdg.axes.plot(ts,data)
                wdg.draw()
            if (ts[-1] - ts[0]).total_seconds() >= N_SEC:
                break
        print("rotating buffer from now on")
        while True:
            pkt = await ws.recv()

            data[0] = pkt['DEMU1']
            data = np.roll(data,-1)

            tt = at.Time(pkt['mjd'], format='mjd')
            ts[0] = tt.to_datetime()
            #print(ts[0])
            ts = np.roll(ts,-1)
            t1 = time.time()
            if t1 - t0 > 0.2:
                t0 = t1
                wdg.axes.cla()
                wdg.axes.plot(ts,data)
                wdg.draw()

    async def recv_dx(self,url):
        await self.__recv(url,self.ws_dx,self.ui.plot_dx)

    async def recv_sx(self,url):
        await self.__recv(url,self.ws_sx,self.ui.plot_sx)

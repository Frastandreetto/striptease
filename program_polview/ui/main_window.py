# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1551, 1149)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMaximumSize(QtCore.QSize(300, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.polarimeter_tree = QtWidgets.QTreeWidget(self.groupBox)
        self.polarimeter_tree.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.polarimeter_tree.setObjectName("polarimeter_tree")
        self.horizontalLayout_4.addWidget(self.polarimeter_tree)
        self.horizontalLayout_3.addWidget(self.groupBox)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tab_group = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_group.setObjectName("tab_group")
        self.tab_pwr = QtWidgets.QWidget()
        self.tab_pwr.setObjectName("tab_pwr")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_pwr)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pwr_q1 = CustomWidget(self.tab_pwr)
        self.pwr_q1.setObjectName("pwr_q1")
        self.gridLayout_2.addWidget(self.pwr_q1, 0, 0, 1, 1)
        self.pwr_q2 = CustomWidget(self.tab_pwr)
        self.pwr_q2.setObjectName("pwr_q2")
        self.gridLayout_2.addWidget(self.pwr_q2, 0, 1, 1, 1)
        self.pwr_u1 = CustomWidget(self.tab_pwr)
        self.pwr_u1.setObjectName("pwr_u1")
        self.gridLayout_2.addWidget(self.pwr_u1, 1, 0, 1, 1)
        self.pwr_u2 = CustomWidget(self.tab_pwr)
        self.pwr_u2.setObjectName("pwr_u2")
        self.gridLayout_2.addWidget(self.pwr_u2, 1, 1, 1, 1)
        self.tab_group.addTab(self.tab_pwr, "")
        self.tab_dem = QtWidgets.QWidget()
        self.tab_dem.setObjectName("tab_dem")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_dem)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.dem_q1 = CustomWidget(self.tab_dem)
        self.dem_q1.setObjectName("dem_q1")
        self.gridLayout_3.addWidget(self.dem_q1, 0, 0, 1, 1)
        self.dem_q2 = CustomWidget(self.tab_dem)
        self.dem_q2.setObjectName("dem_q2")
        self.gridLayout_3.addWidget(self.dem_q2, 0, 1, 1, 1)
        self.dem_u1 = CustomWidget(self.tab_dem)
        self.dem_u1.setObjectName("dem_u1")
        self.gridLayout_3.addWidget(self.dem_u1, 1, 0, 1, 1)
        self.dem_u2 = CustomWidget(self.tab_dem)
        self.dem_u2.setObjectName("dem_u2")
        self.gridLayout_3.addWidget(self.dem_u2, 1, 1, 1, 1)
        self.tab_group.addTab(self.tab_dem, "")
        self.tab_lna = QtWidgets.QWidget()
        self.tab_lna.setObjectName("tab_lna")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab_lna)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.tab_lna)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.ig = CustomWidget(self.frame)
        self.ig.setObjectName("ig")
        self.gridLayout.addWidget(self.ig, 0, 1, 1, 1)
        self.id = CustomWidget(self.frame)
        self.id.setObjectName("id")
        self.gridLayout.addWidget(self.id, 0, 0, 1, 1)
        self.vd = CustomWidget(self.frame)
        self.vd.setObjectName("vd")
        self.gridLayout.addWidget(self.vd, 1, 0, 1, 1)
        self.vg = CustomWidget(self.frame)
        self.vg.setObjectName("vg")
        self.gridLayout.addWidget(self.vg, 1, 1, 1, 1)
        self.horizontalLayout.addWidget(self.frame)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_lna)
        self.groupBox_3.setMaximumSize(QtCore.QSize(120, 16777215))
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hk0 = QtWidgets.QCheckBox(self.groupBox_3)
        self.hk0.setObjectName("hk0")
        self.verticalLayout.addWidget(self.hk0)
        self.hk1 = QtWidgets.QCheckBox(self.groupBox_3)
        self.hk1.setObjectName("hk1")
        self.verticalLayout.addWidget(self.hk1)
        self.hk2 = QtWidgets.QCheckBox(self.groupBox_3)
        self.hk2.setObjectName("hk2")
        self.verticalLayout.addWidget(self.hk2)
        self.hk5 = QtWidgets.QCheckBox(self.groupBox_3)
        self.hk5.setObjectName("hk5")
        self.verticalLayout.addWidget(self.hk5)
        self.hk4 = QtWidgets.QCheckBox(self.groupBox_3)
        self.hk4.setObjectName("hk4")
        self.verticalLayout.addWidget(self.hk4)
        self.hk3 = QtWidgets.QCheckBox(self.groupBox_3)
        self.hk3.setObjectName("hk3")
        self.verticalLayout.addWidget(self.hk3)
        self.hk4a = QtWidgets.QCheckBox(self.groupBox_3)
        self.hk4a.setObjectName("hk4a")
        self.verticalLayout.addWidget(self.hk4a)
        self.hk5a = QtWidgets.QCheckBox(self.groupBox_3)
        self.hk5a.setObjectName("hk5a")
        self.verticalLayout.addWidget(self.hk5a)
        self.horizontalLayout.addWidget(self.groupBox_3)
        self.tab_group.addTab(self.tab_lna, "")
        self.tab_temp = QtWidgets.QWidget()
        self.tab_temp.setObjectName("tab_temp")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_temp)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.widget = QuadPlotWidget(self.tab_temp)
        self.widget.setObjectName("widget")
        self.gridLayout_4.addWidget(self.widget, 0, 0, 1, 1)
        self.tab_group.addTab(self.tab_temp, "")
        self.verticalLayout_4.addWidget(self.tab_group)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 300))
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.stats_tree = QtWidgets.QTreeWidget(self.groupBox_2)
        self.stats_tree.setColumnCount(2)
        self.stats_tree.setObjectName("stats_tree")
        self.stats_tree.headerItem().setText(0, "Polarimeter")
        self.horizontalLayout_2.addWidget(self.stats_tree)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1551, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tab_group.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Polarimeter"))
        self.tab_group.setTabText(self.tab_group.indexOf(self.tab_pwr), _translate("MainWindow", "Total power"))
        self.tab_group.setTabText(self.tab_group.indexOf(self.tab_dem), _translate("MainWindow", "Demodulated"))
        self.groupBox_3.setTitle(_translate("MainWindow", "GroupBox"))
        self.hk0.setText(_translate("MainWindow", "HK0 (HA1)"))
        self.hk1.setText(_translate("MainWindow", "HK1 (HA2)"))
        self.hk2.setText(_translate("MainWindow", "HK2 (HA3)"))
        self.hk5.setText(_translate("MainWindow", "HK5 (HB1)"))
        self.hk4.setText(_translate("MainWindow", "HK4 (HB2)"))
        self.hk3.setText(_translate("MainWindow", "HK3 (HB3)"))
        self.hk4a.setText(_translate("MainWindow", "HK4A"))
        self.hk5a.setText(_translate("MainWindow", "HK5A"))
        self.tab_group.setTabText(self.tab_group.indexOf(self.tab_lna), _translate("MainWindow", "LNA biases"))
        self.tab_group.setTabText(self.tab_group.indexOf(self.tab_temp), _translate("MainWindow", "Temperatures"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Statistics"))
        self.stats_tree.headerItem().setText(1, _translate("MainWindow", "average"))

from widgets.plot.pyqtgraph_plot import CustomWidget, QuadPlotWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


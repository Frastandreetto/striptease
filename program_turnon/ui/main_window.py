# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(964, 429)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_board_on = QtWidgets.QPushButton(self.centralwidget)
        self.btn_board_on.setObjectName("btn_board_on")
        self.horizontalLayout_2.addWidget(self.btn_board_on)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.list_channels = QtWidgets.QComboBox(self.centralwidget)
        self.list_channels.setObjectName("list_channels")
        self.horizontalLayout.addWidget(self.list_channels)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.list_pol_mode = QtWidgets.QComboBox(self.centralwidget)
        self.list_pol_mode.setObjectName("list_pol_mode")
        self.horizontalLayout_6.addWidget(self.list_pol_mode)
        self.btn_pol_on = QtWidgets.QPushButton(self.centralwidget)
        self.btn_pol_on.setObjectName("btn_pol_on")
        self.horizontalLayout_6.addWidget(self.btn_pol_on)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.table_calibration = QtWidgets.QTableWidget(self.centralwidget)
        self.table_calibration.setObjectName("table_calibration")
        self.table_calibration.setColumnCount(0)
        self.table_calibration.setRowCount(0)
        self.verticalLayout.addWidget(self.table_calibration)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.step_calib = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.step_calib.setMaximum(1.0)
        self.step_calib.setSingleStep(0.1)
        self.step_calib.setProperty("value", 1.0)
        self.step_calib.setObjectName("step_calib")
        self.horizontalLayout_3.addWidget(self.step_calib)
        self.btn_apply_calib = QtWidgets.QPushButton(self.centralwidget)
        self.btn_apply_calib.setObjectName("btn_apply_calib")
        self.horizontalLayout_3.addWidget(self.btn_apply_calib)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 254, 68))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.listWidget = QtWidgets.QListWidget(self.scrollAreaWidgetContents)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 254, 68))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setObjectName("listWidget")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.table_sci = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_sci.sizePolicy().hasHeightForWidth())
        self.table_sci.setSizePolicy(sizePolicy)
        self.table_sci.setObjectName("table_sci")
        self.table_sci.setColumnCount(0)
        self.table_sci.setRowCount(0)
        self.horizontalLayout_4.addWidget(self.table_sci)
        self.plot_sci = PolMplCanvas(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plot_sci.sizePolicy().hasHeightForWidth())
        self.plot_sci.setSizePolicy(sizePolicy)
        self.plot_sci.setObjectName("plot_sci")
        self.horizontalLayout_4.addWidget(self.plot_sci)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.table_hk = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_hk.sizePolicy().hasHeightForWidth())
        self.table_hk.setSizePolicy(sizePolicy)
        self.table_hk.setObjectName("table_hk")
        self.table_hk.setColumnCount(0)
        self.table_hk.setRowCount(0)
        self.horizontalLayout_5.addWidget(self.table_hk)
        self.plot_hk = PolMplCanvas(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plot_hk.sizePolicy().hasHeightForWidth())
        self.plot_hk.setSizePolicy(sizePolicy)
        self.plot_hk.setObjectName("plot_hk")
        self.horizontalLayout_5.addWidget(self.plot_hk)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menu = QtWidgets.QMenuBar(MainWindow)
        self.menu.setGeometry(QtCore.QRect(0, 0, 964, 22))
        self.menu.setObjectName("menu")
        self.menuFile = QtWidgets.QMenu(self.menu)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menu)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionload_board_file = QtWidgets.QAction(MainWindow)
        self.actionload_board_file.setObjectName("actionload_board_file")
        self.actionload_pol_calibration = QtWidgets.QAction(MainWindow)
        self.actionload_pol_calibration.setObjectName("actionload_pol_calibration")
        self.menuFile.addAction(self.actionload_board_file)
        self.menuFile.addAction(self.actionload_pol_calibration)
        self.menu.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_board_on.setText(_translate("MainWindow", "Board ON"))
        self.label.setText(_translate("MainWindow", "select channel"))
        self.btn_pol_on.setText(_translate("MainWindow", "Pol ON"))
        self.btn_apply_calib.setText(_translate("MainWindow", "apply"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionload_board_file.setText(_translate("MainWindow", "load board file"))
        self.actionload_pol_calibration.setText(_translate("MainWindow", "load pol calibration"))


from widgets.plot.pol import PolMplCanvas


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window_i2c.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1345, 660)
        self.central_widget = QtWidgets.QWidget(MainWindow)
        self.central_widget.setObjectName("central_widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.central_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.setup_group = QtWidgets.QGroupBox(self.central_widget)
        self.setup_group.setObjectName("setup_group")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.setup_group)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.setup = QtWidgets.QWidget(self.setup_group)
        self.setup.setObjectName("setup")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.setup)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.out_channel_label = QtWidgets.QLabel(self.setup)
        self.out_channel_label.setObjectName("out_channel_label")
        self.horizontalLayout_2.addWidget(self.out_channel_label)
        self.channel_line = QtWidgets.QLineEdit(self.setup)
        self.channel_line.setObjectName("channel_line")
        self.horizontalLayout_2.addWidget(self.channel_line)
        self.duration_label = QtWidgets.QLabel(self.setup)
        self.duration_label.setObjectName("duration_label")
        self.horizontalLayout_2.addWidget(self.duration_label)
        self.duration_line = QtWidgets.QLineEdit(self.setup)
        self.duration_line.setObjectName("duration_line")
        self.horizontalLayout_2.addWidget(self.duration_line)
        self.gain_label = QtWidgets.QLabel(self.setup)
        self.gain_label.setObjectName("gain_label")
        self.horizontalLayout_2.addWidget(self.gain_label)
        self.gain_line = QtWidgets.QLineEdit(self.setup)
        self.gain_line.setObjectName("gain_line")
        self.horizontalLayout_2.addWidget(self.gain_line)
        self.delay_label = QtWidgets.QLabel(self.setup)
        self.delay_label.setObjectName("delay_label")
        self.horizontalLayout_2.addWidget(self.delay_label)
        self.delay_line = QtWidgets.QLineEdit(self.setup)
        self.delay_line.setObjectName("delay_line")
        self.horizontalLayout_2.addWidget(self.delay_line)
        self.pixmap = QtWidgets.QLabel(self.setup)
        self.pixmap.setMaximumSize(QtCore.QSize(16000, 16000))
        self.pixmap.setAutoFillBackground(False)
        self.pixmap.setText("")
        self.pixmap.setPixmap(QtGui.QPixmap("../../../../../../../Desktop/BoDoDi/BoDoDi_version1_1.png"))
        self.pixmap.setScaledContents(False)
        self.pixmap.setWordWrap(True)
        self.pixmap.setObjectName("pixmap")
        self.horizontalLayout_2.addWidget(self.pixmap)
        self.label = QtWidgets.QLabel(self.setup)
        self.label.setText("")
        #import os
        #os.chdir("../../../../../../../Desktop/BoDoDi/version2_korrekt.png")
        #self.label.setPixmap(QtGui.QPixmap("version2_korrekt.png"))
        self.label.setPixmap(QtGui.QPixmap("../../../../../../../Desktop/BoDoDi/version2_korrekt.png"))
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout_7.addWidget(self.setup)
        self.verticalLayout.addWidget(self.setup_group)
        self.button_widgets = QtWidgets.QWidget(self.central_widget)
        self.button_widgets.setObjectName("button_widgets")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.button_widgets)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.start_button = QtWidgets.QPushButton(self.button_widgets)
        self.start_button.setObjectName("start_button")
        self.horizontalLayout.addWidget(self.start_button)
        self.stop_button = QtWidgets.QPushButton(self.button_widgets)
        self.stop_button.setObjectName("stop_button")
        self.horizontalLayout.addWidget(self.stop_button)
        self.viewButton = QtWidgets.QPushButton(self.button_widgets)
        self.viewButton.setObjectName("viewButton")
        self.horizontalLayout.addWidget(self.viewButton)
        self.pushButton = QtWidgets.QPushButton(self.button_widgets)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.button_widgets)
        MainWindow.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1345, 31))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionconfiguration_file = QtWidgets.QAction(MainWindow)
        self.actionconfiguration_file.setCheckable(False)
        self.actionconfiguration_file.setObjectName("actionconfiguration_file")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionconfiguration_file)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.setup_group.setTitle(_translate("MainWindow", "Out"))
        self.out_channel_label.setText(_translate("MainWindow", "Channel"))
        self.duration_label.setText(_translate("MainWindow", "Duration:"))
        self.gain_label.setText(_translate("MainWindow", "Gain:"))
        self.delay_label.setText(_translate("MainWindow", "Delay:"))
        self.start_button.setText(_translate("MainWindow", "Start"))
        self.stop_button.setText(_translate("MainWindow", "Stop"))
        self.viewButton.setText(_translate("MainWindow", "Experiment: Voltage/Time"))
        self.pushButton.setText(_translate("MainWindow", "Temperature/Time"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSave.setText(_translate("MainWindow", "save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionconfiguration_file.setText(_translate("MainWindow", "configuration file"))
        self.actionconfiguration_file.setToolTip(_translate("MainWindow", "open"))
        self.actionconfiguration_file.setShortcut(_translate("MainWindow", "Ctrl+O"))

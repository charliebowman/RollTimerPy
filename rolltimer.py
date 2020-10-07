import sys

########################### GUI LAYOUT ########################################
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QSettings
from PyQt5.QtGui import QPalette, QIcon
from PyQt5.QtWidgets import QPushButton, QAction, QFileDialog, \
     QMessageBox, QApplication

######################### FILE DIALOG #########################################

from pathlib import Path

########################## SERIAL #############################################
import serial
from typing import Iterator, Tuple
from serial.tools.list_ports import comports

######################### IMAGE PROCESSING ####################################
from PIL import Image

######################## SOUND PROCESSING #####################################
import wave, struct, math, random

# Object for access to the serial port
ser = serial.Serial(timeout=0)
SER_BAUDRATE = 115200

# Setting constants
SETTING_PORT_NAME = 'port_name'
SETTING_MESSAGE = 'message'

######################### GLOBAL VARIABLES ####################################


def gen_serial_ports() -> Iterator[Tuple[str, str]]:
    """Return all available serial ports."""
    ports = comports()
    return ((p.description, p.device) for p in ports)

def PNG_transmit():
    try:
        #Relative Path
        img = Image.open("picture.jpg")
        print(img.mode)
          
        #converting image to bitmap
        print(img.tobitmap())
          
        print(type(img.tobitmap()))
    except IOError: 
        pass

class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 382)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setObjectName("tabWidget")
        self.modeTab = QtWidgets.QWidget()
        self.modeTab.setObjectName("modeTab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.modeTab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridButtonLayout = QtWidgets.QGridLayout()
        self.gridButtonLayout.setObjectName("gridButtonLayout")
        self.comboBox = QtWidgets.QComboBox(self.modeTab)
        self.comboBox.setObjectName("comboBox")
        self.gridButtonLayout.addWidget(self.comboBox, 0, 0)
        self.portButton = QtWidgets.QPushButton(self.modeTab)
        self.portButton.setObjectName("portButton")
        self.gridButtonLayout.addWidget(self.portButton,0,1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridButtonLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.gridButtonLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.modeLabel = QtWidgets.QLabel(self.modeTab)
        self.modeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.modeLabel.setObjectName("modeLabel")
        self.verticalLayout.addWidget(self.modeLabel)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem2)
        self.volumeLabel = QtWidgets.QLabel(self.modeTab)
        self.volumeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.volumeLabel.setObjectName("volumeLabel")
        self.verticalLayout.addWidget(self.volumeLabel)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem3)
        self.backgroundButton = QtWidgets.QPushButton(self.modeTab)
        self.backgroundButton.setObjectName("backgroundButton")
        self.verticalLayout.addWidget(self.backgroundButton)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem4)
        self.gridLayout_4.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.modeTab, "")
        self.alarmTab = QtWidgets.QWidget()
        self.alarmTab.setObjectName("alarmTab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.alarmTab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.alarmTab)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.alarmTab)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 2, 0, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.alarmTab)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 2, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.alarmTab)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.alarmtimesLabel = QtWidgets.QLabel(self.alarmTab)
        self.alarmtimesLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.alarmtimesLabel.setObjectName("alarmtimesLabel")
        self.gridLayout.addWidget(self.alarmtimesLabel, 0, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.alarmsoundButton = QtWidgets.QPushButton(self.alarmTab)
        self.alarmsoundButton.setObjectName("alarmsoundButton")
        self.gridLayout_2.addWidget(self.alarmsoundButton, 3, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 2, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.timeLabel = QtWidgets.QLabel(self.alarmTab)
        self.timeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.timeLabel.setObjectName("timeLabel")
        self.gridLayout_5.addWidget(self.timeLabel, 1, 0, 1, 1)
        self.tabWidget.addTab(self.alarmTab, "")
        self.sensorsTab = QtWidgets.QWidget()
        self.sensorsTab.setObjectName("sensorsTab")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.sensorsTab)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.accelLabel = QtWidgets.QLabel(self.sensorsTab)
        self.accelLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.accelLabel.setObjectName("accelLabel")
        self.horizontalLayout_4.addWidget(self.accelLabel)
        self.xyzLabel = QtWidgets.QLabel(self.sensorsTab)
        self.xyzLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.xyzLabel.setObjectName("xyzLabel")
        self.horizontalLayout_4.addWidget(self.xyzLabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.temperatureLabel = QtWidgets.QLabel(self.sensorsTab)
        self.temperatureLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.temperatureLabel.setObjectName("temperatureLabel")
        self.horizontalLayout_5.addWidget(self.temperatureLabel)
        self.tempLabel = QtWidgets.QLabel(self.sensorsTab)
        self.tempLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.tempLabel.setObjectName("tempLabel")
        self.horizontalLayout_5.addWidget(self.tempLabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.humidityLabel = QtWidgets.QLabel(self.sensorsTab)
        self.humidityLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.humidityLabel.setObjectName("humidityLabel")
        self.horizontalLayout_6.addWidget(self.humidityLabel)
        self.humidLabel = QtWidgets.QLabel(self.sensorsTab)
        self.humidLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.humidLabel.setObjectName("humidLabel")
        self.horizontalLayout_6.addWidget(self.humidLabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.gridLayout_6.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.sensorsTab, "")
        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ################ CONNECT/DISCONNCECT BUTTONS #########################
        self.disconnect_btn = QtWidgets.QPushButton("DISCONNECT", self.modeTab)
        self.disconnect_btn.setObjectName("portButton")
        self.gridButtonLayout.addWidget(self.disconnect_btn, 0, 1)

        self.disconnect_btn.setVisible(False)
        self.portButton.pressed.connect(self.on_connect_btn_pressed)
        self.disconnect_btn.pressed.connect(self.on_disconnect_btn_pressed)

       ################# FILE DIALOG ########################################

        self.backgroundButton.clicked.connect(self.showPNGDialog)
        self.alarmsoundButton.clicked.connect(self.showWAVDialog)

        # Update combobox ports
        self.update_com_ports()

        ##################### TIMER SETTINGS #################################
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.displayTime)
        self.timer.start()

    def showWAVDialog(self):

        home_dir = str(Path.home())
        fname = QFileDialog.getOpenFileName(self, 'RollTimer', home_dir, \
                 "WAV (*.wav *.WAV)")

        print(open(fname[0], 'rb').read())
        #ser.write(open((fname[0]).read()))

    def showPNGDialog(self):

        home_dir = str(Path.home())
        fname = QFileDialog.getOpenFileName(self, 'RollTimer', home_dir, \
                 "Image (*.png *.PNG)")

        try:
            #Relative Path
            img = Image.open(fname[0])
            print(img.mode)

            img = img.convert(mode ="1")
            
            #converting image to bitmap
            print(img.tobitmap())
            
            #print(type(img.tobitmap()))
        except IOError: 
            pass


    def displayTime(self):
        self.timeLabel.setText(QtCore.QDateTime.currentDateTime().toString())

    def _load_settings(self) -> None:
        """Load settings on startup."""
        settings = QSettings()

        # port name
        port_name = settings.value(SETTING_PORT_NAME)
        if port_name is not None:
            index = self.comboBox.findData(port_name)
            if index > -1:
                self.comboBox.setCurrentIndex(index)


    def _save_settings(self) -> None:
        """Save settings on shutdown."""
        settings = QSettings()
        settings.setValue(SETTING_PORT_NAME, self.port)

    def show_error_message(self, msg: str) -> None:
        """Show a Message Box with the error message."""
        QMessageBox.critical(self, QApplication.applicationName(), str(msg))

    def update_com_ports(self) -> None:
        """Update COM Port list in GUI."""
        for name, device in gen_serial_ports():
            self.comboBox.addItem(name, device)

    @property
    def port(self) -> str:
        """Return the current serial port."""
        return self.comboBox.currentData()


    def on_connect_btn_pressed(self) -> None:
        """Open serial connection to the specified port."""
        if ser.is_open:
            ser.close()
        ser.port = self.port
        ser.baudrate = SER_BAUDRATE

        try:
            ser.open()
        except Exception as e:
            self.show_error_message(str(e))

        if ser.is_open:
            self.portButton.setVisible(False)
            self.disconnect_btn.setVisible(True)
            self.comboBox.setDisabled(True)

    def on_disconnect_btn_pressed(self) -> None:
        """Close current serial connection."""
        if ser.is_open:
            ser.close()

        if not ser.is_open:
            self.portButton.setVisible(True)
            self.disconnect_btn.setVisible(False)
            self.comboBox.setEnabled(True)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RollTimer"))
        self.portButton.setText(_translate("MainWindow", "CONNECT"))
        self.modeLabel.setText(_translate("MainWindow", "TEMPERATURE AND HUMIDITY "))
        self.volumeLabel.setText(_translate("MainWindow", "70%"))
        self.backgroundButton.setText(_translate("MainWindow", "SET ROLLTIMER BACKGROUND"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.modeTab), _translate("MainWindow", "Mode"))
        self.alarmtimesLabel.setText(_translate("MainWindow", "ALARM TIMES"))
        self.alarmsoundButton.setText(_translate("MainWindow", "SET ALARM SOUND"))
        self.timeLabel.setText(_translate("MainWindow", "TIME"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.alarmTab), _translate("MainWindow", "Alarm"))
        self.accelLabel.setText(_translate("MainWindow", "ACCELEROMETER"))
        self.xyzLabel.setText(_translate("MainWindow", "X: 20    Y: 20    Z: 220"))
        self.temperatureLabel.setText(_translate("MainWindow", "TEMPERATURE"))
        self.tempLabel.setText(_translate("MainWindow", "220"))
        self.humidityLabel.setText(_translate("MainWindow", "HUMIDITY"))
        self.humidLabel.setText(_translate("MainWindow", "55"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sensorsTab), _translate("MainWindow", "Sensors"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    palette = QPalette()
    palette.setColor(QPalette.Background, Qt.darkGray)
    app.setPalette(palette)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

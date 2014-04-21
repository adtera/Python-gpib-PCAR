# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dashboard.ui'
#
# Created: Mon Apr 21 20:02:18 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1053, 718)
        MainWindow.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../usr/share/pixmaps/cubeview48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setToolTip("")
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtGui.QTabWidget.Rounded)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.init_button = QtGui.QPushButton(self.centralwidget)
        self.init_button.setGeometry(QtCore.QRect(830, 350, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setItalic(True)
        self.init_button.setFont(font)
        self.init_button.setObjectName("init_button")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(15, 9, 270, 21))
        font = QtGui.QFont()
        font.setFamily("URW Chancery L")
        font.setPointSize(12)
        font.setWeight(75)
        font.setItalic(True)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.fetch_data = QtGui.QCheckBox(self.centralwidget)
        self.fetch_data.setEnabled(True)
        self.fetch_data.setGeometry(QtCore.QRect(830, 320, 121, 27))
        self.fetch_data.setChecked(True)
        self.fetch_data.setObjectName("fetch_data")
        self.total_readings = QtGui.QLabel(self.centralwidget)
        self.total_readings.setGeometry(QtCore.QRect(990, 390, 51, 16))
        self.total_readings.setFrameShape(QtGui.QFrame.Box)
        self.total_readings.setFrameShadow(QtGui.QFrame.Sunken)
        self.total_readings.setText("")
        self.total_readings.setObjectName("total_readings")
        self.Save_data = QtGui.QPushButton(self.centralwidget)
        self.Save_data.setGeometry(QtCore.QRect(670, 0, 151, 27))
        self.Save_data.setObjectName("Save_data")
        self.dIdVgraph = PlotWidget(self.centralwidget)
        self.dIdVgraph.setGeometry(QtCore.QRect(10, 30, 811, 371))
        self.dIdVgraph.setObjectName("dIdVgraph")
        self.state_dc = QtGui.QPushButton(self.centralwidget)
        self.state_dc.setGeometry(QtCore.QRect(830, 220, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setWeight(75)
        font.setItalic(True)
        font.setBold(True)
        self.state_dc.setFont(font)
        self.state_dc.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.state_dc.setObjectName("state_dc")
        self.nvpr = QtGui.QLabel(self.centralwidget)
        self.nvpr.setGeometry(QtCore.QRect(830, 290, 211, 21))
        self.nvpr.setAutoFillBackground(True)
        self.nvpr.setObjectName("nvpr")
        self.dIdVfit = QtGui.QLabel(self.centralwidget)
        self.dIdVfit.setGeometry(QtCore.QRect(490, 410, 281, 17))
        self.dIdVfit.setObjectName("dIdVfit")
        self.instrumenttools = QtGui.QToolBox(self.centralwidget)
        self.instrumenttools.setGeometry(QtCore.QRect(830, 0, 211, 221))
        self.instrumenttools.setFrameShape(QtGui.QFrame.StyledPanel)
        self.instrumenttools.setFrameShadow(QtGui.QFrame.Raised)
        self.instrumenttools.setLineWidth(2)
        self.instrumenttools.setMidLineWidth(1)
        self.instrumenttools.setObjectName("instrumenttools")
        self.page = QtGui.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 209, 157))
        self.page.setObjectName("page")
        self.label_5 = QtGui.QLabel(self.page)
        self.label_5.setGeometry(QtCore.QRect(100, 80, 91, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setItalic(True)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.current_start = QtGui.QDoubleSpinBox(self.page)
        self.current_start.setGeometry(QtCore.QRect(0, 0, 101, 31))
        self.current_start.setWrapping(False)
        self.current_start.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        self.current_start.setAccelerated(True)
        self.current_start.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToNearestValue)
        self.current_start.setDecimals(3)
        self.current_start.setMinimum(-105.0)
        self.current_start.setMaximum(105.0)
        self.current_start.setSingleStep(0.001)
        self.current_start.setProperty("value", -40.0)
        self.current_start.setObjectName("current_start")
        self.num_points = QtGui.QDoubleSpinBox(self.page)
        self.num_points.setGeometry(QtCore.QRect(0, 80, 101, 30))
        self.num_points.setWrapping(False)
        self.num_points.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        self.num_points.setAccelerated(True)
        self.num_points.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToNearestValue)
        self.num_points.setSuffix("")
        self.num_points.setDecimals(0)
        self.num_points.setMinimum(0.0)
        self.num_points.setMaximum(1000.0)
        self.num_points.setSingleStep(1.0)
        self.num_points.setProperty("value", 200.0)
        self.num_points.setObjectName("num_points")
        self.pw_label = QtGui.QLabel(self.page)
        self.pw_label.setGeometry(QtCore.QRect(100, -40, 51, 17))
        self.pw_label.setObjectName("pw_label")
        self.label_3 = QtGui.QLabel(self.page)
        self.label_3.setGeometry(QtCore.QRect(100, 40, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setItalic(True)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.current_stop = QtGui.QDoubleSpinBox(self.page)
        self.current_stop.setGeometry(QtCore.QRect(0, 40, 101, 31))
        self.current_stop.setWrapping(False)
        self.current_stop.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        self.current_stop.setAccelerated(True)
        self.current_stop.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToNearestValue)
        self.current_stop.setDecimals(3)
        self.current_stop.setMinimum(-105.0)
        self.current_stop.setMaximum(105.0)
        self.current_stop.setSingleStep(0.001)
        self.current_stop.setProperty("value", 40.0)
        self.current_stop.setObjectName("current_stop")
        self.label_4 = QtGui.QLabel(self.page)
        self.label_4.setGeometry(QtCore.QRect(100, 0, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setItalic(True)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pulse_width = QtGui.QDoubleSpinBox(self.page)
        self.pulse_width.setGeometry(QtCore.QRect(0, 120, 101, 30))
        self.pulse_width.setWrapping(False)
        self.pulse_width.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        self.pulse_width.setAccelerated(True)
        self.pulse_width.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToNearestValue)
        self.pulse_width.setDecimals(3)
        self.pulse_width.setMinimum(100.0)
        self.pulse_width.setMaximum(2000.0)
        self.pulse_width.setSingleStep(5.0)
        self.pulse_width.setProperty("value", 100.0)
        self.pulse_width.setObjectName("pulse_width")
        self.label_6 = QtGui.QLabel(self.page)
        self.label_6.setGeometry(QtCore.QRect(100, 120, 81, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setItalic(True)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.instrumenttools.addItem(self.page, "")
        self.page_2 = QtGui.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 209, 157))
        self.page_2.setObjectName("page_2")
        self.v6 = QtGui.QRadioButton(self.page_2)
        self.v6.setGeometry(QtCore.QRect(130, 40, 71, 22))
        self.v6.setObjectName("v6")
        self.v2 = QtGui.QRadioButton(self.page_2)
        self.v2.setGeometry(QtCore.QRect(60, 10, 71, 22))
        self.v2.setChecked(True)
        self.v2.setObjectName("v2")
        self.v3 = QtGui.QRadioButton(self.page_2)
        self.v3.setGeometry(QtCore.QRect(130, 10, 81, 22))
        self.v3.setChecked(False)
        self.v3.setObjectName("v3")
        self.v1 = QtGui.QRadioButton(self.page_2)
        self.v1.setGeometry(QtCore.QRect(0, 10, 60, 22))
        self.v1.setChecked(False)
        self.v1.setObjectName("v1")
        self.v5 = QtGui.QRadioButton(self.page_2)
        self.v5.setGeometry(QtCore.QRect(60, 40, 71, 22))
        self.v5.setChecked(False)
        self.v5.setObjectName("v5")
        self.v4 = QtGui.QRadioButton(self.page_2)
        self.v4.setGeometry(QtCore.QRect(0, 40, 71, 22))
        self.v4.setChecked(False)
        self.v4.setObjectName("v4")
        self.instrumenttools.addItem(self.page_2, "")
        self.messages = QtGui.QTextBrowser(self.centralwidget)
        self.messages.setGeometry(QtCore.QRect(10, 410, 471, 161))
        self.messages.setFrameShape(QtGui.QFrame.StyledPanel)
        self.messages.setObjectName("messages")
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(920, 440, 121, 21))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(920, 460, 121, 21))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(810, 420, 231, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setObjectName("label_2")
        self.position = QtGui.QLabel(self.centralwidget)
        self.position.setGeometry(QtCore.QRect(820, 490, 101, 17))
        self.position.setObjectName("position")
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(810, 440, 98, 20))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(810, 460, 98, 21))
        self.pushButton_4.setObjectName("pushButton_4")
        self.a_1 = QtGui.QLabel(self.centralwidget)
        self.a_1.setGeometry(QtCore.QRect(930, 490, 21, 17))
        self.a_1.setText("")
        self.a_1.setObjectName("a_1")
        self.a_2 = QtGui.QLabel(self.centralwidget)
        self.a_2.setGeometry(QtCore.QRect(960, 490, 21, 17))
        self.a_2.setText("")
        self.a_2.setObjectName("a_2")
        self.a_3 = QtGui.QLabel(self.centralwidget)
        self.a_3.setGeometry(QtCore.QRect(990, 490, 21, 17))
        self.a_3.setText("")
        self.a_3.setObjectName("a_3")
        self.a_4 = QtGui.QLabel(self.centralwidget)
        self.a_4.setGeometry(QtCore.QRect(1020, 490, 21, 17))
        self.a_4.setText("")
        self.a_4.setObjectName("a_4")
        self.temp_graph = PlotWidget(self.centralwidget)
        self.temp_graph.setGeometry(QtCore.QRect(490, 540, 561, 171))
        self.temp_graph.setObjectName("temp_graph")
        self.curvelist = QtGui.QComboBox(self.centralwidget)
        self.curvelist.setGeometry(QtCore.QRect(540, 510, 141, 27))
        self.curvelist.setObjectName("curvelist")
        self.input_list = QtGui.QComboBox(self.centralwidget)
        self.input_list.setGeometry(QtCore.QRect(490, 510, 41, 27))
        self.input_list.setObjectName("input_list")
        self.input_list.addItem("")
        self.input_list.addItem("")
        self.input_list.addItem("")
        self.input_list.addItem("")
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(490, 490, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(9)
        font.setItalic(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(690, 500, 121, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.update_button = QtGui.QPushButton(self.centralwidget)
        self.update_button.setGeometry(QtCore.QRect(960, 320, 81, 21))
        self.update_button.setObjectName("update_button")
        self.temperature = QtGui.QLabel(self.centralwidget)
        self.temperature.setGeometry(QtCore.QRect(930, 520, 111, 20))
        self.temperature.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.temperature.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.temperature.setMargin(2)
        self.temperature.setObjectName("temperature")
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(830, 390, 151, 16))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.state_pd = QtGui.QPushButton(self.centralwidget)
        self.state_pd.setGeometry(QtCore.QRect(940, 220, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setWeight(75)
        font.setItalic(True)
        font.setBold(True)
        self.state_pd.setFont(font)
        self.state_pd.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.state_pd.setObjectName("state_pd")
        self.Save_data_2 = QtGui.QPushButton(self.centralwidget)
        self.Save_data_2.setGeometry(QtCore.QRect(940, 260, 101, 27))
        self.Save_data_2.setObjectName("Save_data_2")
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(490, 440, 101, 17))
        self.label_9.setObjectName("label_9")
        self.live_monitor = QtGui.QLCDNumber(self.centralwidget)
        self.live_monitor.setGeometry(QtCore.QRect(590, 440, 131, 20))
        self.live_monitor.setAutoFillBackground(False)
        self.live_monitor.setStyleSheet("QLCDNumber{color:rgb(85, 85, 255);background-color:rgb(0, 170, 255);}")
        self.live_monitor.setFrameShape(QtGui.QFrame.Panel)
        self.live_monitor.setSmallDecimalPoint(False)
        self.live_monitor.setNumDigits(10)
        self.live_monitor.setObjectName("live_monitor")
        self.pushButton_6 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(830, 260, 101, 27))
        self.pushButton_6.setObjectName("pushButton_6")
        self.temp_res_graph = PlotWidget(self.centralwidget)
        self.temp_res_graph.setGeometry(QtCore.QRect(10, 580, 471, 131))
        self.temp_res_graph.setObjectName("temp_res_graph")
        self.comments = QtGui.QLineEdit(self.centralwidget)
        self.comments.setGeometry(QtCore.QRect(330, 0, 281, 27))
        self.comments.setObjectName("comments")
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionSave_as = QtGui.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")

        self.retranslateUi(MainWindow)
        self.instrumenttools.setCurrentIndex(0)
        self.instrumenttools.layout().setSpacing(6)
        QtCore.QObject.connect(self.init_button, QtCore.SIGNAL("clicked()"), MainWindow.start_measuring)
        QtCore.QObject.connect(self.Save_data, QtCore.SIGNAL("clicked()"), MainWindow.dump_to_file)
        QtCore.QObject.connect(self.v1, QtCore.SIGNAL("clicked()"), MainWindow.set_vc)
        QtCore.QObject.connect(self.v4, QtCore.SIGNAL("clicked()"), MainWindow.set_vc)
        QtCore.QObject.connect(self.v2, QtCore.SIGNAL("clicked()"), MainWindow.set_vc)
        QtCore.QObject.connect(self.v5, QtCore.SIGNAL("clicked()"), MainWindow.set_vc)
        QtCore.QObject.connect(self.v3, QtCore.SIGNAL("clicked()"), MainWindow.set_vc)
        QtCore.QObject.connect(self.v6, QtCore.SIGNAL("clicked()"), MainWindow.set_vc)
        QtCore.QObject.connect(self.state_dc, QtCore.SIGNAL("clicked()"), MainWindow.arm_DC)
        QtCore.QObject.connect(self.current_stop, QtCore.SIGNAL("valueChanged(double)"), MainWindow.set_current_stop)
        QtCore.QObject.connect(self.current_start, QtCore.SIGNAL("valueChanged(double)"), MainWindow.set_current_start)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), MainWindow.stepper_back)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL("clicked()"), MainWindow.stepper_fwd)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL("clicked()"), MainWindow.disable_stepper)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL("clicked()"), MainWindow.enable_stepper)
        QtCore.QObject.connect(self.curvelist, QtCore.SIGNAL("currentIndexChanged(int)"), MainWindow.select_temperature_curve)
        QtCore.QObject.connect(self.input_list, QtCore.SIGNAL("currentIndexChanged(QString)"), MainWindow.select_temperature_input)
        QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL("clicked()"), MainWindow.load_temperature_parameters)
        QtCore.QObject.connect(self.update_button, QtCore.SIGNAL("clicked()"), MainWindow.update_buffer)
        QtCore.QObject.connect(self.num_points, QtCore.SIGNAL("valueChanged(double)"), MainWindow.set_points)
        QtCore.QObject.connect(self.pulse_width, QtCore.SIGNAL("valueChanged(double)"), MainWindow.set_pulse_width)
        QtCore.QObject.connect(self.state_pd, QtCore.SIGNAL("clicked()"), MainWindow.arm_PD)
        QtCore.QObject.connect(self.Save_data_2, QtCore.SIGNAL("clicked()"), MainWindow.abort_all)
        QtCore.QObject.connect(self.pushButton_6, QtCore.SIGNAL("clicked()"), MainWindow.arm_delta)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "PCAR Spectroscopy", None, QtGui.QApplication.UnicodeUTF8))
        self.init_button.setText(QtGui.QApplication.translate("MainWindow", "Start measurements", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Point Contact Andreev Reflection Spectroscopy", None, QtGui.QApplication.UnicodeUTF8))
        self.fetch_data.setText(QtGui.QApplication.translate("MainWindow", "Auto update", None, QtGui.QApplication.UnicodeUTF8))
        self.Save_data.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.state_dc.setText(QtGui.QApplication.translate("MainWindow", "ARM DC", None, QtGui.QApplication.UnicodeUTF8))
        self.nvpr.setText(QtGui.QApplication.translate("MainWindow", "             nanovoltmeter", None, QtGui.QApplication.UnicodeUTF8))
        self.dIdVfit.setText(QtGui.QApplication.translate("MainWindow", "dI/dV =", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Number of points", None, QtGui.QApplication.UnicodeUTF8))
        self.current_start.setSuffix(QtGui.QApplication.translate("MainWindow", "mA", None, QtGui.QApplication.UnicodeUTF8))
        self.pw_label.setText(QtGui.QApplication.translate("MainWindow", "100", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "stop current", None, QtGui.QApplication.UnicodeUTF8))
        self.current_stop.setSuffix(QtGui.QApplication.translate("MainWindow", "mA", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Start current", None, QtGui.QApplication.UnicodeUTF8))
        self.pulse_width.setSuffix(QtGui.QApplication.translate("MainWindow", "uS", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Pulse Width", None, QtGui.QApplication.UnicodeUTF8))
        self.instrumenttools.setItemText(self.instrumenttools.indexOf(self.page), QtGui.QApplication.translate("MainWindow", "Current Pulse settings", None, QtGui.QApplication.UnicodeUTF8))
        self.v6.setText(QtGui.QApplication.translate("MainWindow", "100V", None, QtGui.QApplication.UnicodeUTF8))
        self.v2.setText(QtGui.QApplication.translate("MainWindow", "10mV", None, QtGui.QApplication.UnicodeUTF8))
        self.v3.setText(QtGui.QApplication.translate("MainWindow", "100mV", None, QtGui.QApplication.UnicodeUTF8))
        self.v1.setText(QtGui.QApplication.translate("MainWindow", "1mV", None, QtGui.QApplication.UnicodeUTF8))
        self.v5.setText(QtGui.QApplication.translate("MainWindow", "10V", None, QtGui.QApplication.UnicodeUTF8))
        self.v4.setText(QtGui.QApplication.translate("MainWindow", "1V", None, QtGui.QApplication.UnicodeUTF8))
        self.instrumenttools.setItemText(self.instrumenttools.indexOf(self.page_2), QtGui.QApplication.translate("MainWindow", "Nanovoltmeter range", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Backward", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "Forward", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Tip sample distance settings", None, QtGui.QApplication.UnicodeUTF8))
        self.position.setText(QtGui.QApplication.translate("MainWindow", "Position:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("MainWindow", "Enable", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("MainWindow", "disable", None, QtGui.QApplication.UnicodeUTF8))
        self.input_list.setItemText(0, QtGui.QApplication.translate("MainWindow", "A", None, QtGui.QApplication.UnicodeUTF8))
        self.input_list.setItemText(1, QtGui.QApplication.translate("MainWindow", "B", None, QtGui.QApplication.UnicodeUTF8))
        self.input_list.setItemText(2, QtGui.QApplication.translate("MainWindow", "C", None, QtGui.QApplication.UnicodeUTF8))
        self.input_list.setItemText(3, QtGui.QApplication.translate("MainWindow", "D", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "T sensor input, calibration curve", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setText(QtGui.QApplication.translate("MainWindow", "Load Parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.update_button.setText(QtGui.QApplication.translate("MainWindow", "Update", None, QtGui.QApplication.UnicodeUTF8))
        self.temperature.setText(QtGui.QApplication.translate("MainWindow", "0 K", None, QtGui.QApplication.UnicodeUTF8))
        self.state_pd.setText(QtGui.QApplication.translate("MainWindow", "ARM PD", None, QtGui.QApplication.UnicodeUTF8))
        self.Save_data_2.setText(QtGui.QApplication.translate("MainWindow", "Abort", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "Monitor", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_6.setText(QtGui.QApplication.translate("MainWindow", "Monitor", None, QtGui.QApplication.UnicodeUTF8))
        self.comments.setText(QtGui.QApplication.translate("MainWindow", "comments...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_as.setText(QtGui.QApplication.translate("MainWindow", "Save as", None, QtGui.QApplication.UnicodeUTF8))

from pyqtgraph import PlotWidget

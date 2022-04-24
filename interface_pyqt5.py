# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface_pyqt5.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(530, 467)
        MainWindow.setMinimumSize(QtCore.QSize(530, 467))
        MainWindow.setMaximumSize(QtCore.QSize(530, 467))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/file_download_FILL0_wght400_GRAD200_opsz24.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/file_download_FILL0_wght400_GRAD200_opsz24.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/file_download_FILL0_wght400_GRAD200_opsz24.svg"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/file_download_FILL0_wght400_GRAD200_opsz24.svg"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/file_download_FILL0_wght400_GRAD200_opsz24.svg"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/file_download_FILL0_wght400_GRAD200_opsz24.svg"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/file_download_FILL0_wght400_GRAD200_opsz24.svg"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/file_download_FILL0_wght400_GRAD200_opsz24.svg"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QWidget {\n"
"    color: white;\n"
"    background-color: #121212;\n"
"    border-radius: 10px;\n"
"}\n"
"QMainWindow {\n"
"    background-color: #121212;\n"
"    border-radius: 10px;\n"
"}")
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget{\n"
"border-radius: 10px;\n"
"background-color: rgb(53, 0, 39);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(30, 240, 471, 23))
        self.progressBar.setToolTipDuration(-1)
        self.progressBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar.setStyleSheet("QProgressBar{\n"
"background_color: rgb(124,113,116);\n"
"border-radius: 10px;\n"
"color: white;\n"
"}\n"
"QProgressBar::chunk{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(201, 87, 149, 255), stop:1 rgba(179, 65, 244, 255));\n"
"border-radius: 10px;\n"
"}")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.lineEdit_page_id = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_page_id.setGeometry(QtCore.QRect(220, 40, 281, 22))
        font = QtGui.QFont()
        font.setKerning(True)
        self.lineEdit_page_id.setFont(font)
        self.lineEdit_page_id.setTabletTracking(True)
        self.lineEdit_page_id.setStyleSheet("QLineEdit{\n"
"border-radius: 10px;\n"
"color: white;\n"
"}")
        self.lineEdit_page_id.setFrame(True)
        self.lineEdit_page_id.setCursorPosition(0)
        self.lineEdit_page_id.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_page_id.setClearButtonEnabled(True)
        self.lineEdit_page_id.setObjectName("lineEdit_page_id")
        self.textEdit_report = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_report.setGeometry(QtCore.QRect(30, 300, 471, 141))
        self.textEdit_report.setStyleSheet("QTextEdit{\n"
"border-radius: 10px;\n"
"color: white;\n"
"}")
        self.textEdit_report.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textEdit_report.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_report.setReadOnly(True)
        self.textEdit_report.setObjectName("textEdit_report")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 531, 471))
        self.frame.setStyleSheet("QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(68,56,72);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(60, 10, 401, 16))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 131, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(30, 100, 171, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(30, 270, 101, 20))
        self.label_4.setObjectName("label_4")
        self.fill_settings = QtWidgets.QToolButton(self.frame)
        self.fill_settings.setGeometry(QtCore.QRect(410, 130, 24, 24))
        self.fill_settings.setAccessibleDescription("")
        self.fill_settings.setAutoFillBackground(False)
        self.fill_settings.setStyleSheet("QToolButton{\n"
"background-color: rgb(160, 95, 182)\n"
"}")
        self.fill_settings.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/arrow_circle_right_FILL0_wght400_GRAD200_opsz24.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fill_settings.setIcon(icon1)
        self.fill_settings.setIconSize(QtCore.QSize(24, 24))
        self.fill_settings.setShortcut("")
        self.fill_settings.setObjectName("fill_settings")
        self.save_settings = QtWidgets.QToolButton(self.frame)
        self.save_settings.setGeometry(QtCore.QRect(440, 130, 24, 24))
        self.save_settings.setAccessibleDescription("")
        self.save_settings.setAutoFillBackground(False)
        self.save_settings.setStyleSheet("QToolButton{\n"
"background-color: rgb(160, 95, 182)\n"
"}")
        self.save_settings.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/add_task_FILL0_wght400_GRAD200_opsz24.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_settings.setIcon(icon2)
        self.save_settings.setIconSize(QtCore.QSize(24, 24))
        self.save_settings.setObjectName("save_settings")
        self.clear_settings = QtWidgets.QToolButton(self.frame)
        self.clear_settings.setGeometry(QtCore.QRect(470, 130, 24, 24))
        self.clear_settings.setWhatsThis("")
        self.clear_settings.setAccessibleName("")
        self.clear_settings.setAccessibleDescription("")
        self.clear_settings.setAutoFillBackground(False)
        self.clear_settings.setStyleSheet("QToolButton{\n"
"background-color: rgb(160, 95, 182)\n"
"}")
        self.clear_settings.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/cancel_FILL0_wght400_GRAD200_opsz24.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clear_settings.setIcon(icon3)
        self.clear_settings.setIconSize(QtCore.QSize(24, 24))
        self.clear_settings.setObjectName("clear_settings")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(30, 70, 181, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit_token_id = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_token_id.setGeometry(QtCore.QRect(220, 70, 281, 22))
        self.lineEdit_token_id.setStyleSheet("QLineEdit{\n"
"border-radius: 10px;\n"
"color: white;\n"
"}")
        self.lineEdit_token_id.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.lineEdit_token_id.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_token_id.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_token_id.setClearButtonEnabled(True)
        self.lineEdit_token_id.setObjectName("lineEdit_token_id")
        self.lineEdit_token = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_token.setGeometry(QtCore.QRect(220, 100, 281, 22))
        self.lineEdit_token.setStyleSheet("QLineEdit{\n"
"border-radius: 10px;\n"
"color: white;\n"
"}")
        self.lineEdit_token.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.lineEdit_token.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_token.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_token.setClearButtonEnabled(True)
        self.lineEdit_token.setObjectName("lineEdit_token")
        self.pushButton_start_copy = QtWidgets.QPushButton(self.frame)
        self.pushButton_start_copy.setGeometry(QtCore.QRect(30, 160, 471, 28))
        self.pushButton_start_copy.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_start_copy.setStyleSheet("QPushButton{\n"
"border-radius: 10px;\n"
"background-color: rgb(160, 95, 182)\n"
"}")
        self.pushButton_start_copy.setObjectName("pushButton_start_copy")
        self.pushButton_stop_copy = QtWidgets.QPushButton(self.frame)
        self.pushButton_stop_copy.setGeometry(QtCore.QRect(30, 200, 471, 28))
        self.pushButton_stop_copy.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_stop_copy.setStyleSheet("QPushButton{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 110);\n"
"}")
        self.pushButton_stop_copy.setObjectName("pushButton_stop_copy")
        self.frame.raise_()
        self.progressBar.raise_()
        self.lineEdit_page_id.raise_()
        self.textEdit_report.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menu_exit = QtWidgets.QAction(MainWindow)
        self.menu_exit.setMenuRole(QtWidgets.QAction.QuitRole)
        self.menu_exit.setObjectName("menu_exit")
        self.menu_clear_settings = QtWidgets.QAction(MainWindow)
        self.menu_clear_settings.setObjectName("menu_clear_settings")
        self.menu_save_settings = QtWidgets.QAction(MainWindow)
        self.menu_save_settings.setCheckable(False)
        self.menu_save_settings.setObjectName("menu_save_settings")
        self.menu_fill_settings = QtWidgets.QAction(MainWindow)
        self.menu_fill_settings.setMenuRole(QtWidgets.QAction.ApplicationSpecificRole)
        self.menu_fill_settings.setObjectName("menu_fill_settings")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Курсовой проект «Резервное копирование»"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">Резервное копирование фотографий из профиля VKontakte</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Укажите id страницы:</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Укажите токен для Я.Диска:</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Ход выполнения:</span></p></body></html>"))
        self.fill_settings.setToolTip(_translate("MainWindow", "Загрузить сохраненные настройки"))
        self.save_settings.setToolTip(_translate("MainWindow", "Сохранить введенные настройки"))
        self.clear_settings.setToolTip(_translate("MainWindow", "<html><head/><body><p>Очистить поля и очистить сохраненные настройки</p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Укажите токен для страницы:</span></p></body></html>"))
        self.pushButton_start_copy.setText(_translate("MainWindow", "Запуск резервного копирования"))
        self.pushButton_stop_copy.setText(_translate("MainWindow", "Остановка резервного копирования"))
        self.menu_exit.setText(_translate("MainWindow", "Выход"))
        self.menu_exit.setShortcut(_translate("MainWindow", "Esc"))
        self.menu_clear_settings.setText(_translate("MainWindow", "Очистить настройки"))
        self.menu_clear_settings.setShortcut(_translate("MainWindow", "Shift+Del"))
        self.menu_save_settings.setText(_translate("MainWindow", "Сохранить настройки по умолчанию"))
        self.menu_save_settings.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.menu_fill_settings.setText(_translate("MainWindow", "Заполнить данными по умолчанию"))
        self.menu_fill_settings.setShortcut(_translate("MainWindow", "Ctrl+O"))
import files_rc

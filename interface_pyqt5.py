# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface_pyqt5.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QLabel,
    QLineEdit, QMainWindow, QProgressBar, QPushButton,
    QSizePolicy, QTabWidget, QTextEdit, QToolButton,
    QVBoxLayout, QWidget)
import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(530, 559)
        MainWindow.setMinimumSize(QSize(530, 559))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon()
        icon.addFile(u":/icons/icons/file_download_FILL0_wght400_GRAD200_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/icons/icons/file_download_FILL0_wght400_GRAD200_opsz24.svg", QSize(), QIcon.Normal, QIcon.On)
        icon.addFile(u":/icons/icons/file_download_FILL0_wght400_GRAD200_opsz24.svg", QSize(), QIcon.Disabled, QIcon.Off)
        icon.addFile(u":/icons/icons/file_download_FILL0_wght400_GRAD200_opsz24.svg", QSize(), QIcon.Disabled, QIcon.On)
        icon.addFile(u":/icons/icons/file_download_FILL0_wght400_GRAD200_opsz24.svg", QSize(), QIcon.Active, QIcon.Off)
        icon.addFile(u":/icons/icons/file_download_FILL0_wght400_GRAD200_opsz24.svg", QSize(), QIcon.Active, QIcon.On)
        icon.addFile(u":/icons/icons/file_download_FILL0_wght400_GRAD200_opsz24.svg", QSize(), QIcon.Selected, QIcon.Off)
        icon.addFile(u":/icons/icons/file_download_FILL0_wght400_GRAD200_opsz24.svg", QSize(), QIcon.Selected, QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"QWidget {\n"
"	color: white;\n"
"	background-color: #121212;\n"
"	border-radius: 10px;\n"
"}\n"
"QMainWindow {\n"
"	background-color: #121212;\n"
"	border-radius: 10px;\n"
"}")
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setDockOptions(QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks)
        self.menu_exit = QAction(MainWindow)
        self.menu_exit.setObjectName(u"menu_exit")
        self.menu_exit.setMenuRole(QAction.QuitRole)
        self.menu_clear_settings = QAction(MainWindow)
        self.menu_clear_settings.setObjectName(u"menu_clear_settings")
        self.menu_save_settings = QAction(MainWindow)
        self.menu_save_settings.setObjectName(u"menu_save_settings")
        self.menu_save_settings.setCheckable(False)
        self.menu_fill_settings = QAction(MainWindow)
        self.menu_fill_settings.setObjectName(u"menu_fill_settings")
        self.menu_fill_settings.setMenuRole(QAction.ApplicationSpecificRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setTabletTracking(True)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"QWidget{\n"
"border-radius: 10px;\n"
"background-color: rgb(53, 0, 39);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(68,56,72);\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 10, 401, 16))
        self.label.setTextFormat(Qt.AutoText)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 40, 131, 16))
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 100, 171, 16))
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 270, 101, 20))
        self.fill_settings = QToolButton(self.frame)
        self.fill_settings.setObjectName(u"fill_settings")
        self.fill_settings.setGeometry(QRect(410, 130, 24, 24))
        self.fill_settings.setCursor(QCursor(Qt.PointingHandCursor))
        self.fill_settings.setAutoFillBackground(False)
        self.fill_settings.setStyleSheet(u"QToolButton{\n"
"background-color: rgb(160, 95, 182)\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/arrow_circle_right_FILL0_wght400_GRAD200_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.fill_settings.setIcon(icon1)
        self.fill_settings.setIconSize(QSize(24, 24))
        self.save_settings = QToolButton(self.frame)
        self.save_settings.setObjectName(u"save_settings")
        self.save_settings.setGeometry(QRect(440, 130, 24, 24))
        self.save_settings.setCursor(QCursor(Qt.PointingHandCursor))
        self.save_settings.setAutoFillBackground(False)
        self.save_settings.setStyleSheet(u"QToolButton{\n"
"background-color: rgb(160, 95, 182)\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/add_task_FILL0_wght400_GRAD200_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.save_settings.setIcon(icon2)
        self.save_settings.setIconSize(QSize(24, 24))
        self.clear_settings = QToolButton(self.frame)
        self.clear_settings.setObjectName(u"clear_settings")
        self.clear_settings.setGeometry(QRect(470, 130, 24, 24))
        self.clear_settings.setCursor(QCursor(Qt.PointingHandCursor))
        self.clear_settings.setAutoFillBackground(False)
        self.clear_settings.setStyleSheet(u"QToolButton{\n"
"background-color: rgb(160, 95, 182)\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/cancel_FILL0_wght400_GRAD200_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.clear_settings.setIcon(icon3)
        self.clear_settings.setIconSize(QSize(24, 24))
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 70, 181, 16))
        self.lineEdit_token_id = QLineEdit(self.frame)
        self.lineEdit_token_id.setObjectName(u"lineEdit_token_id")
        self.lineEdit_token_id.setGeometry(QRect(210, 70, 281, 22))
        self.lineEdit_token_id.setStyleSheet(u"QLineEdit{\n"
"border-radius: 10px;\n"
"color: white;\n"
"}")
        self.lineEdit_token_id.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.lineEdit_token_id.setEchoMode(QLineEdit.Password)
        self.lineEdit_token_id.setAlignment(Qt.AlignCenter)
        self.lineEdit_token_id.setClearButtonEnabled(True)
        self.lineEdit_token = QLineEdit(self.frame)
        self.lineEdit_token.setObjectName(u"lineEdit_token")
        self.lineEdit_token.setGeometry(QRect(210, 100, 281, 22))
        self.lineEdit_token.setStyleSheet(u"QLineEdit{\n"
"border-radius: 10px;\n"
"color: white;\n"
"}")
        self.lineEdit_token.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.lineEdit_token.setEchoMode(QLineEdit.Password)
        self.lineEdit_token.setAlignment(Qt.AlignCenter)
        self.lineEdit_token.setClearButtonEnabled(True)
        self.pushButton_start_copy = QPushButton(self.frame)
        self.pushButton_start_copy.setObjectName(u"pushButton_start_copy")
        self.pushButton_start_copy.setGeometry(QRect(20, 160, 471, 28))
        self.pushButton_start_copy.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_start_copy.setStyleSheet(u"QPushButton{\n"
"border-radius: 10px;\n"
"background-color: rgb(160, 95, 182)\n"
"}")
        self.pushButton_stop_copy = QPushButton(self.frame)
        self.pushButton_stop_copy.setObjectName(u"pushButton_stop_copy")
        self.pushButton_stop_copy.setGeometry(QRect(20, 200, 471, 28))
        self.pushButton_stop_copy.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_stop_copy.setStyleSheet(u"QPushButton{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 110);\n"
"}")
        self.check_box_profile = QCheckBox(self.frame)
        self.check_box_profile.setObjectName(u"check_box_profile")
        self.check_box_profile.setGeometry(QRect(90, 130, 101, 21))
        self.check_box_profile.setCursor(QCursor(Qt.PointingHandCursor))
        self.check_box_profile.setStyleSheet(u"QCheckBox\n"
"{\n"
"border : 2px solid rgb(160, 95, 182);\n"
"}\n"
"QCheckBox::indicator\n"
"{\n"
"border : 2px solid rgb(160, 95, 182);\n"
"width : 20px;\n"
"height : 20px;\n"
"border-radius :12px;\n"
"image: url(:/icons/icons/radio_button_unchecked_FILL0_wght400_GRAD200_opsz24.svg);\n"
"}\n"
"QCheckBox::indicator:checked\n"
"{\n"
"border : 2px solid rgb(160, 95, 182);\n"
"width : 20px;\n"
"height : 20px;\n"
"border-radius :12px;\n"
"background-color: rgb(160, 95, 182);\n"
"image: url(:/icons/icons/check_circle_FILL0_wght400_GRAD200_opsz24.svg);\n"
"}")
        self.check_box_profile.setChecked(True)
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 130, 61, 16))
        self.check_box_wall = QCheckBox(self.frame)
        self.check_box_wall.setObjectName(u"check_box_wall")
        self.check_box_wall.setGeometry(QRect(200, 130, 91, 20))
        self.check_box_wall.setCursor(QCursor(Qt.PointingHandCursor))
        self.check_box_wall.setStyleSheet(u"QCheckBox\n"
"{\n"
"border : 2px solid rgb(160, 95, 182);\n"
"}\n"
"QCheckBox::indicator\n"
"{\n"
"border : 2px solid rgb(160, 95, 182);\n"
"width : 20px;\n"
"height : 20px;\n"
"border-radius :12px;\n"
"image: url(:/icons/icons/radio_button_unchecked_FILL0_wght400_GRAD200_opsz24.svg);\n"
"}\n"
"QCheckBox::indicator:checked\n"
"{\n"
"border : 2px solid rgb(160, 95, 182);\n"
"width : 20px;\n"
"height : 20px;\n"
"border-radius :12px;\n"
"background-color: rgb(160, 95, 182);\n"
"image: url(:/icons/icons/check_circle_FILL0_wght400_GRAD200_opsz24.svg);\n"
"}")
        self.check_box_wall.setChecked(True)
        self.check_box_album = QCheckBox(self.frame)
        self.check_box_album.setObjectName(u"check_box_album")
        self.check_box_album.setGeometry(QRect(300, 130, 101, 20))
        self.check_box_album.setCursor(QCursor(Qt.PointingHandCursor))
        self.check_box_album.setStyleSheet(u"QCheckBox\n"
"{\n"
"border : 2px solid rgb(160, 95, 182);\n"
"}\n"
"QCheckBox::indicator\n"
"{\n"
"border : 2px solid rgb(160, 95, 182);\n"
"width : 20px;\n"
"height : 20px;\n"
"border-radius :12px;\n"
"image: url(:/icons/icons/radio_button_unchecked_FILL0_wght400_GRAD200_opsz24.svg);\n"
"}\n"
"QCheckBox::indicator:checked\n"
"{\n"
"border : 2px solid rgb(160, 95, 182);\n"
"width : 20px;\n"
"height : 20px;\n"
"border-radius :12px;\n"
"background-color: rgb(160, 95, 182);\n"
"image: url(:/icons/icons/check_circle_FILL0_wght400_GRAD200_opsz24.svg);\n"
"}")
        self.check_box_album.setChecked(True)
        self.check_box_album.setTristate(False)
        self.lineEdit_page_id = QLineEdit(self.frame)
        self.lineEdit_page_id.setObjectName(u"lineEdit_page_id")
        self.lineEdit_page_id.setGeometry(QRect(210, 40, 281, 22))
        font = QFont()
        font.setKerning(True)
        self.lineEdit_page_id.setFont(font)
        self.lineEdit_page_id.setTabletTracking(True)
        self.lineEdit_page_id.setStyleSheet(u"QLineEdit{\n"
"border-radius: 10px;\n"
"color: white;\n"
"}")
        self.lineEdit_page_id.setFrame(True)
        self.lineEdit_page_id.setCursorPosition(0)
        self.lineEdit_page_id.setAlignment(Qt.AlignCenter)
        self.lineEdit_page_id.setClearButtonEnabled(True)
        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(20, 240, 471, 24))
        self.progressBar.setToolTipDuration(-1)
        self.progressBar.setLayoutDirection(Qt.LeftToRight)
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"background_color: rgb(124,113,116);\n"
"border-radius: 10px;\n"
"color: white;\n"
"}\n"
"QProgressBar::chunk{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(201, 87, 149, 255), stop:1 rgba(179, 65, 244, 255));\n"
"border-radius: 10px;\n"
"}")
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.textEdit_report = QTextEdit(self.frame)
        self.textEdit_report.setObjectName(u"textEdit_report")
        self.textEdit_report.setGeometry(QRect(20, 300, 471, 221))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_report.sizePolicy().hasHeightForWidth())
        self.textEdit_report.setSizePolicy(sizePolicy)
        self.textEdit_report.setStyleSheet(u"QTextEdit{\n"
"border-radius: 10px;\n"
"color: white;\n"
"background-color: rgb(52, 0, 39);\n"
"}")
        self.textEdit_report.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.textEdit_report.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_report.setReadOnly(True)
        self.textEdit_report.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041a\u0443\u0440\u0441\u043e\u0432\u043e\u0439 \u043f\u0440\u043e\u0435\u043a\u0442 \u00ab\u0420\u0435\u0437\u0435\u0440\u0432\u043d\u043e\u0435 \u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435\u00bb", None))
        self.menu_exit.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
#if QT_CONFIG(shortcut)
        self.menu_exit.setShortcut(QCoreApplication.translate("MainWindow", u"Esc", None))
#endif // QT_CONFIG(shortcut)
        self.menu_clear_settings.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
#if QT_CONFIG(shortcut)
        self.menu_clear_settings.setShortcut(QCoreApplication.translate("MainWindow", u"Shift+Del", None))
#endif // QT_CONFIG(shortcut)
        self.menu_save_settings.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u043f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e", None))
#if QT_CONFIG(shortcut)
        self.menu_save_settings.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.menu_fill_settings.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u043e\u043b\u043d\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u043c\u0438 \u043f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e", None))
#if QT_CONFIG(shortcut)
        self.menu_fill_settings.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">\u0420\u0435\u0437\u0435\u0440\u0432\u043d\u043e\u0435 \u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0444\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u0439 \u0438\u0437 \u043f\u0440\u043e\u0444\u0438\u043b\u044f VKontakte</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">\u0423\u043a\u0430\u0436\u0438\u0442\u0435 id \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b:</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u0442\u043e\u043a\u0435\u043d \u0434\u043b\u044f \u042f.\u0414\u0438\u0441\u043a\u0430:</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">\u0425\u043e\u0434 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f:</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.fill_settings.setToolTip(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u043d\u044b\u0435 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.fill_settings.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.fill_settings.setText("")
#if QT_CONFIG(shortcut)
        self.fill_settings.setShortcut("")
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.save_settings.setToolTip(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0432\u0432\u0435\u0434\u0435\u043d\u043d\u044b\u0435 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.save_settings.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.save_settings.setText("")
#if QT_CONFIG(tooltip)
        self.clear_settings.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u043f\u043e\u043b\u044f \u0438 \u043e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u043d\u044b\u0435 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.clear_settings.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.clear_settings.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.clear_settings.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.clear_settings.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u0442\u043e\u043a\u0435\u043d \u0434\u043b\u044f \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b:</span></p></body></html>", None))
        self.pushButton_start_copy.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u043a \u0440\u0435\u0437\u0435\u0440\u0432\u043d\u043e\u0433\u043e \u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f", None))
        self.pushButton_stop_copy.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0430 \u0440\u0435\u0437\u0435\u0440\u0432\u043d\u043e\u0433\u043e \u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f", None))
        self.check_box_profile.setText(QCoreApplication.translate("MainWindow", u"\u0430\u0432\u0430\u0442\u0430\u0440\u044b", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430:</span></p></body></html>", None))
        self.check_box_wall.setText(QCoreApplication.translate("MainWindow", u"\u0441\u0442\u0435\u043d\u044b", None))
        self.check_box_album.setText(QCoreApplication.translate("MainWindow", u"\u0430\u043b\u044c\u0431\u043e\u043c\u043e\u0432", None))
    # retranslateUi


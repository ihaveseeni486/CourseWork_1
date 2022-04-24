import YaDisk  # самописно для работы с Я.диском
from interface_pyqt5 import Ui_MainWindow   # самописно для создания графического интерфейса
from PyQt5 import QtWidgets # , QtGui, QtCore
from PyQt5.QtWidgets import QAction
import configparser
import os
import sys
import time


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # подключение к кнопкам
        self.ui.pushButton_start_copy.clicked.connect(self.btnClicked)
        self.ui.fill_settings.clicked.connect(self.fill_settings_pressed)
        self.ui.save_settings.clicked.connect(self.save_settings_pressed)
        self.ui.clear_settings.clicked.connect(self.clear_settings_pressed)

    def ProgressBarSetValueAndColor(self, value, color_not_failed, time_to_sleep):
        self.ui.progressBar.setValue(value)
        if color_not_failed:
            # вернем цвет прогрессбару
            self.ui.progressBar.setStyleSheet("""QProgressBar{
                                                background_color: rgb(124,113,116);
                                                border-radius: 10px;
                                                color: white;
                                            }
                                            QProgressBar::chunk{
                                                background-color: qlineargradient(spread:pad, 
                                                    x1:0, y1:0, x2:1, y2:0, 
                                                    stop:0 rgba(201, 87, 149, 255), 
                                                    stop:1 rgba(179, 65, 244, 255));
                                                border-radius: 10px;
                                            }""")
        else:
            # подкрасим прогрессбар красным, если ошибка
            self.ui.progressBar.setStyleSheet("""QProgressBar{
                                                background_color: rgb(124,113,116);
                                                border-radius: 10px;
                                                color: white;
                                            }
                                            QProgressBar::chunk{
                                                background-color: qlineargradient(spread:pad, 
                                                    x1:0, y1:0, x2:1, y2:0, 
                                                    stop:0 rgba(201, 87, 149, 255), 
                                                    stop:1 rgba(221, 0, 0, 255));
                                                border-radius: 10px;
                                            }""")
        time.sleep(time_to_sleep) # просто для красоты анимации прогрессбара, а то слишком быстро все делает =)

    def fill_settings_pressed(self):
        self.ui.label_4.setText("Вы нажали на заполнение!")
        self.ui.label_4.adjustSize()

    def save_settings_pressed(self):
        self.ui.label_4.setText("Вы нажали на сохранение!")
        self.ui.label_4.adjustSize()

    def clear_settings_pressed(self):
        self.ui.textEdit_report.setText("")
        self.ProgressBarSetValueAndColor(0, True, 0.05)
        self.ui.textEdit_report.append("Запуск очистки сохраненных настроек...")
        self.ui.lineEdit_page_id.setText("")
        self.ProgressBarSetValueAndColor(10, True, 0.05)
        self.ui.lineEdit_token.setText("")
        self.ProgressBarSetValueAndColor(20, True, 0.05)
        self.ui.lineEdit_token_id.setText("")
        self.ProgressBarSetValueAndColor(30, True, 0.05)

        if os.path.exists("settings.ini"):
            try:
                self.ui.textEdit_report.append("Старт очистки файла настроек...")
                self.ProgressBarSetValueAndColor(40, True, 0.05)
                config = configparser.ConfigParser()
                config.read("settings.ini")
                config["VK"]["token"] = ""
                config["YandexDisk"]["token"] = ""
                config.write(config)
                self.ui.textEdit_report.append("Настройки очищены")
                self.ProgressBarSetValueAndColor(100, True, 0)
            except Exception as ex_mess:
                self.ui.textEdit_report.append(f"Ошибка очистки файла настроек: {ex_mess}")
                self.ProgressBarSetValueAndColor(100, False, 0)
        else:
            self.ui.textEdit_report.append("Предсохраненных настроек не обнаружено")
            self.ui.textEdit_report.append("Настройки очищены")
            self.ProgressBarSetValueAndColor(100, True, 0)

    # def menu_exit_pressed(self):
    #    self.close()

    def btnClicked(self):
        self.ui.label_4.setText("Вы нажали на кнопку!")
        # Если не использовать, то часть текста исчезнет.
        self.ui.label_4.adjustSize()


if __name__ == '__main__':

    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()

    sys.exit(app.exec())

    # config = configparser.ConfigParser()
    # config.read("settings.ini")
    # token_for_vk = config["VK"]["token"]
    # token_for_disk = config["YandexDisk"]["token"]
    #
    # ya = YaDisk.YandexDisk(token=token_for_disk)
    # resp = ya.upload_file_to_disk("test/filemini.txt", "filemini.txt")
    # if resp:
    #     print("Успешно загружен файл на диск")
    # else:
    #     print("Ошибка при загрузке файла на диск")

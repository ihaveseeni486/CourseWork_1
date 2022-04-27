import YaDisk  # самописно для работы с Я.диском
from interface_pyqt5 import Ui_MainWindow   # самописно для создания графического интерфейса
from PyQt5 import QtWidgets, QtCore
import configparser
import os
import sys


class ProgressHandler(QtCore.QThread):
    my_signal = QtCore.pyqtSignal(int, bool, float, str)

    def __init__(self, page_id, token_id, token_for_disk):
        super().__init__()
        self.page_id = page_id
        self.token_id = token_id
        self.token_for_disk = token_for_disk

    def run(self):
        self.my_signal.emit(24, True, 0, "Проверка токена для соединения с Я.диском...")
        ya = YaDisk.YandexDisk(token=self.token_for_disk)
        self.my_signal.emit(40, True, 0, "Верификация пройдена")
        self.my_signal.emit(43, True, 0, "Запуск загрузки файла...")
        resp = ya.upload_file_to_disk("test", "filemini.txt")
        if resp == "":
            self.my_signal.emit(100, True, 0, "Успешно загружен файл на диск")
        else:
            self.my_signal.emit(100, False, 0, f"Ошибка при загрузке файла на диск:\r"
                                               f"    {resp}")


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.handler = ProgressHandler("", "", "")
        self.handler.my_signal.connect(self.progressbar_set_value_and_color)

        # подключение к кнопкам
        self.ui.pushButton_start_copy.clicked.connect(self.btnClickedStartCopy)
        self.ui.pushButton_stop_copy.clicked.connect(self.btnClickedStopCopy)

        # self.ui.pushButton_start_copy.clicked.connect(lambda: self.handler.start())
        # self.ui.pushButton_stop_copy.clicked.connect(lambda: self.handler_copy.terminate())

        self.ui.fill_settings.clicked.connect(self.fill_settings_pressed)
        self.ui.save_settings.clicked.connect(self.save_settings_pressed)
        self.ui.clear_settings.clicked.connect(self.clear_settings_pressed)

    def progressbar_set_value_and_color(self, value, color_not_failed, time_to_sleep, what_to_post):
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
        if what_to_post == "":
            self.ui.textEdit_report.setText("")
        else:
            self.ui.textEdit_report.append(what_to_post)
        if value == 100:
            self.ui.pushButton_start_copy.setEnabled(True)
        # if time_to_sleep != 0:
            # time.sleep(time_to_sleep) # просто для красоты анимации прогрессбара, а то слишком быстро все делает =)
            # переводим в миллисекунды
            # time_to_sleep *= 1000
            # self.handler.wait(int(time_to_sleep))

    def fill_settings_pressed(self):
        self.progressbar_set_value_and_color(0, True, 0, "")
        self.progressbar_set_value_and_color(10, True, 0.5, "Запуск заполнения из предсохраненных настроек...")

        path_to_check = os.path.abspath("settings.ini")
        if os.path.isfile(path_to_check):
            try:
                self.progressbar_set_value_and_color(40, True, 0.5, "Старт чтения файла настроек...")
                config = configparser.ConfigParser()
                config.read("settings.ini")

                self.ui.lineEdit_page_id.setText(config["VK"]["id"])
                self.ui.lineEdit_token_id.setText(config["VK"]["token"])
                self.ui.lineEdit_token.setText(config["YandexDisk"]["token"])

                self.progressbar_set_value_and_color(100, True, 0, "Настройки заполнены")
            except Exception as ex_mess:
                self.progressbar_set_value_and_color(100, False, 0, f"Ошибка считывания файла настроек: {ex_mess}")
        else:
            self.progressbar_set_value_and_color(100, False, 0,
                                                 "Предсохраненных настроек не обнаружено\nНастройки не загружены")

    def save_settings_pressed(self):
        self.progressbar_set_value_and_color(0, True, 0, "")
        self.progressbar_set_value_and_color(40, True, 0.05, "Запуск сохранения настроек...")

        try:
            config = configparser.ConfigParser()
            config.add_section("VK")
            config.add_section("YandexDisk")
            config.set("VK", "id", self.ui.lineEdit_page_id.text())
            config.set("VK", "token", self.ui.lineEdit_token_id.text())
            config.set("YandexDisk", "token", self.ui.lineEdit_token.text())

            self.progressbar_set_value_and_color(70, True, 0.5, "Сохранение settings.ini")
            with open('settings.ini', 'w') as configfile:
                config.write(configfile)

            self.progressbar_set_value_and_color(100, True, 0, "Настройки сохранены")
        except Exception as ex_mess:
            self.progressbar_set_value_and_color(100, False, 0, f"Ошибка обновления файла настроек: {ex_mess}")

    def clear_settings_pressed(self):
        self.progressbar_set_value_and_color(0, True, 0.05, "")
        self.ui.lineEdit_page_id.setText("")
        self.ui.lineEdit_token.setText("")
        self.ui.lineEdit_token_id.setText("")
        self.progressbar_set_value_and_color(30, True, 0.05, "Запуск очистки сохраненных настроек...")

        if os.path.isfile(os.getcwd() + "settings.ini"):
            try:
                self.progressbar_set_value_and_color(40, True, 0.05, "Старт очистки файла настроек...")
                config = configparser.ConfigParser()
                config.read("settings.ini")
                config["VK"]["id"] = ""
                config["VK"]["token"] = ""
                config["YandexDisk"]["token"] = ""
                with open('settings.ini', 'w') as configfile:
                    config.write(configfile)
                self.progressbar_set_value_and_color(100, True, 0, "Настройки очищены")
            except Exception as ex_mess:
                self.progressbar_set_value_and_color(100, False, 0, f"Ошибка очистки файла настроек: {ex_mess}")
        else:
            self.progressbar_set_value_and_color(100, True, 0, "Предсохраненных настроек не обнаружено\rНастройки очищены")

    # def menu_exit_pressed(self):
    #    self.close()

    def btnClickedStartCopy(self):
        self.progressbar_set_value_and_color(0, True, 0, "")
        self.progressbar_set_value_and_color(10, True, 0.5, "Проверка параметров для запуска резервного копирования...")

        lineEdit_page_id = self.ui.lineEdit_page_id.text()
        lineEdit_token_id = self.ui.lineEdit_token_id.text()
        lineEdit_token = self.ui.lineEdit_token.text()
        if lineEdit_page_id != "" and lineEdit_token_id != "" and lineEdit_token != "":
            self.progressbar_set_value_and_color(20, True, 0, "Запуск резервного копирования...")
            self.ui.pushButton_start_copy.setEnabled(False)
            self.handler = ProgressHandler(lineEdit_page_id, lineEdit_token_id, lineEdit_token)
            self.handler.my_signal.connect(self.progressbar_set_value_and_color)
            self.handler.start()
        else:
            self.progressbar_set_value_and_color(100, False, 0, "Поля с входными данными не могут быть пустыми.")

    def btnClickedStopCopy(self):
        try:
            if self.handler.isRunning():
                self.progressbar_set_value_and_color(98, False, 0, "\nОстановка процесса резервного копирования...")
                self.handler.terminate()
                if not self.handler.isRunning():
                    self.progressbar_set_value_and_color(100, True, 0,
                                                     "Процесс резервного копирования прерван по инициативе пользователя")
                else:
                    self.progressbar_set_value_and_color(100, False, 0,
                                                         "Процесс резервного копирования ПОЧЕМУ-ТО НЕ ПРЕРВАН")
            else:
                self.progressbar_set_value_and_color(0, True, 0, "Процесс не запущен, нечего останавливать")
        except Exception as exc:
            self.progressbar_set_value_and_color(100, False, 0, f"Непредвиденная ошибка: {exc}")


if __name__ == '__main__':

    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()

    sys.exit(app.exec())

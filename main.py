import YaDisk  # самописно для работы с Я.диском
import VKwork  # самописно для работы с vk
from interface_pyqt5 import Ui_MainWindow   # самописно для создания графического интерфейса
from PyQt5 import QtWidgets, QtCore
import configparser
import os
import sys
import datetime


class ProgressHandler(QtCore.QThread):
    my_signal = QtCore.pyqtSignal(int, bool, str)

    def __init__(self, page_id, token_id, token_for_disk):
        super().__init__()
        self.page_id = page_id
        self.token_id = token_id
        self.token_for_disk = token_for_disk
        self.daemon = True

    def run(self):
        self.my_signal.emit(12, True, "Проверка данных для соединения с VK...")
        vk_user_try = VKwork.VkStuff(token=self.token_id, user_id=self.page_id)
        vk_resp = vk_user_try.get_user()
        if vk_resp == "Пользователь VK с введенными данными найден":
            self.my_signal.emit(22, True, vk_resp)
        else:
            self.my_signal.emit(100, False, vk_resp)
            return

        self.my_signal.emit(24, True, "Получение информации о фото из VK...")
        vk_resp = vk_user_try.get_photos()
        if "Информация о фото получена" in vk_resp:
            self.my_signal.emit(26, True, vk_resp)
        else:
            self.my_signal.emit(100, False, vk_resp)
            return

        self.my_signal.emit(28, True, "Получение списка альбомов с фото из VK...")
        vk_resp = vk_user_try.get_albums()
        if "Список альбомов получен" in vk_resp:
            self.my_signal.emit(26, True, vk_resp)
        else:
            self.my_signal.emit(100, False, vk_resp)
            return

        self.my_signal.emit(38, True, "Инициализация соединения с Я.диском...")
        ya = YaDisk.YandexDisk(token=self.token_for_disk)
        self.my_signal.emit(40, True, "Инициализация пройдена")

        # name_folder_dump_now = datetime.datetime.now().strftime("%Y-%m-%d %H.%M")
        name_folder_dump_now = datetime.datetime.now().strftime("%Y-%m-%d %H %M")

        all_photo_info = vk_user_try.get_photos()
        self.my_signal.emit(43, True, "Запуск загрузки файлов....\n[1]Загрузка аватарок...")
        for item in vk_user_try.photo_info_dict.get("items"):
            if item["album_id"] == -6:
                best_to_load = vk_user_try.get_best_photo(item)
                self.my_signal.emit(43, True, f'    Загрузка аватарки: {best_to_load}')
                resp = ya.upload_file_to_disk(
                                                file_path_folder=f"dumpVK/{name_folder_dump_now}/profile",
                                                file_url=best_to_load,
                                                file_name=f'{item["likes"]["count"]} {name_folder_dump_now}.jpg'
                                             )
                if resp != "":
                    self.my_signal.emit(43, False, f"      Ошибка при загрузке аватарки на диск (файл пропущен):\r"
                                                    f"    {resp}")

        self.my_signal.emit(59, True, "[2]Загрузка фото со стены...")
        self.my_signal.emit(69, True, "[3]Загрузка фото из альбомов...")

        #self.my_signal.emit(100, True, "Загрузка завершена")


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

        self.ui.fill_settings.clicked.connect(self.fill_settings_pressed)
        self.ui.save_settings.clicked.connect(self.save_settings_pressed)
        self.ui.clear_settings.clicked.connect(self.clear_settings_pressed)

    def progressbar_set_value_and_color(self, value, color_not_failed, what_to_post):
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

    def fill_settings_pressed(self):
        self.progressbar_set_value_and_color(0, True, "")
        self.progressbar_set_value_and_color(10, True, "Запуск заполнения из предсохраненных настроек...")

        path_to_check = os.path.abspath("settings.ini")
        if os.path.isfile(path_to_check):
            try:
                self.progressbar_set_value_and_color(40, True, "Старт чтения файла настроек...")
                config = configparser.ConfigParser()
                config.read("settings.ini")

                self.ui.lineEdit_page_id.setText(config["VK"]["id"])
                self.ui.lineEdit_token_id.setText(config["VK"]["token"])
                self.ui.lineEdit_token.setText(config["YandexDisk"]["token"])

                self.progressbar_set_value_and_color(100, True, "Настройки заполнены")
            except Exception as ex_mess:
                self.progressbar_set_value_and_color(100, False, f"Ошибка считывания файла настроек: {ex_mess}")
        else:
            self.progressbar_set_value_and_color(100, False,
                                                 "Предсохраненных настроек не обнаружено\nНастройки не загружены")

    def save_settings_pressed(self):
        self.progressbar_set_value_and_color(0, True, "")
        self.progressbar_set_value_and_color(40, True, "Запуск сохранения настроек...")

        try:
            config = configparser.ConfigParser()
            config.add_section("VK")
            config.add_section("YandexDisk")
            config.set("VK", "id", self.ui.lineEdit_page_id.text())
            config.set("VK", "token", self.ui.lineEdit_token_id.text())
            config.set("YandexDisk", "token", self.ui.lineEdit_token.text())

            self.progressbar_set_value_and_color(70, True, "Сохранение settings.ini")
            with open('settings.ini', 'w') as configfile:
                config.write(configfile)

            self.progressbar_set_value_and_color(100, True, "Настройки сохранены")
        except Exception as ex_mess:
            self.progressbar_set_value_and_color(100, False, f"Ошибка обновления файла настроек: {ex_mess}")

    def clear_settings_pressed(self):
        self.progressbar_set_value_and_color(0, True, "")
        self.ui.lineEdit_page_id.setText("")
        self.ui.lineEdit_token.setText("")
        self.ui.lineEdit_token_id.setText("")
        self.progressbar_set_value_and_color(30, True, "Запуск очистки сохраненных настроек...")

        if os.path.isfile(os.getcwd() + "settings.ini"):
            try:
                self.progressbar_set_value_and_color(40, True, "Старт очистки файла настроек...")
                config = configparser.ConfigParser()
                config.read("settings.ini")
                config["VK"]["id"] = ""
                config["VK"]["token"] = ""
                config["YandexDisk"]["token"] = ""
                with open('settings.ini', 'w') as configfile:
                    config.write(configfile)
                self.progressbar_set_value_and_color(100, True, "Настройки очищены")
            except Exception as ex_mess:
                self.progressbar_set_value_and_color(100, False, f"Ошибка очистки файла настроек: {ex_mess}")
        else:
            self.progressbar_set_value_and_color(100, True, "Предсохраненных настроек не обнаружено\rНастройки очищены")

    # def menu_exit_pressed(self):
    #    self.close()

    def btnClickedStartCopy(self):
        self.progressbar_set_value_and_color(0, True, "")
        self.progressbar_set_value_and_color(10, True, "Проверка параметров для запуска резервного копирования...")

        lineEdit_page_id = self.ui.lineEdit_page_id.text()
        lineEdit_token_id = self.ui.lineEdit_token_id.text()
        lineEdit_token = self.ui.lineEdit_token.text()
        if lineEdit_page_id != "" and lineEdit_token_id != "" and lineEdit_token != "":
            self.progressbar_set_value_and_color(20, True, "Входные данные заполнены, проверка корректности...")
            self.ui.pushButton_start_copy.setEnabled(False)
            self.handler = ProgressHandler(lineEdit_page_id, lineEdit_token_id, lineEdit_token)
            self.handler.my_signal.connect(self.progressbar_set_value_and_color)
            self.handler.start()
        else:
            self.progressbar_set_value_and_color(100, False, "Поля с входными данными не могут быть пустыми.")

    def btnClickedStopCopy(self):
        try:
            if self.handler.isRunning():
                self.progressbar_set_value_and_color(98, False, "\nОстановка процесса резервного копирования...")
                self.handler.terminate()
                if not self.handler.isRunning():
                    self.progressbar_set_value_and_color(100, True,
                                                     "Процесс резервного копирования прерван по инициативе пользователя")
                else:
                    self.progressbar_set_value_and_color(100, False,
                                                         "Процесс резервного копирования ПОЧЕМУ-ТО НЕ ПРЕРВАН")
            else:
                self.progressbar_set_value_and_color(0, True, "Процесс не запущен, нечего останавливать")
        except Exception as exc:
            self.progressbar_set_value_and_color(100, False, f"Непредвиденная ошибка: {exc}")


if __name__ == '__main__':

    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()

    sys.exit(app.exec())

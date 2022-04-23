import YaDisk  # самописно для работы с Я.диском
from interface_pyqt5 import Ui_MainWindow   # самописно для создания графического интерфейса
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QAction
import configparser
import sys


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # подключение клик-сигнал к слоту btnClicked
        self.ui.pushButton_start_copy.clicked.connect(self.btnClicked)


    def btnClicked(self):
        self.ui.label_4.setText("Вы нажали на кнопку!")
        # Если не использовать, то часть текста исчезнет.
        self.ui.label_4.adjustSize()

    def mouseClickEvent(self):
        self.ui.label_4.setText("Вы нажали на сохранение!")
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

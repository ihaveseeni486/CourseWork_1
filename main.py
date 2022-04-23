import YaDisk

TOKEN = ""

if __name__ == '__main__':
    ya = YaDisk.YandexDisk(token=TOKEN)
    resp = ya.upload_file_to_disk("test/filemini.txt", "filemini.txt")
    if resp:
        print("Успешно загружен файл на диск")
    else:
        print("Ошибка при загрузке файла на диск")

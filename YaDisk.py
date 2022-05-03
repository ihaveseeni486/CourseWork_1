import time
import datetime
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


class YandexDisk:

    def __init__(self, token):
        self.token = token
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

    def get_headers(self):
        return {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Authorization': 'OAuth {}'.format(self.token)
            }

    def get_files_in_list(self):
        url_files = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        resp = requests.get(url_files, headers=headers, verify=False)
        return resp.json()

    def check_and_create_cloud_folders(self, file_path_folder, headers):
        # создадим папки
        url = 'https://cloud-api.yandex.net/v1/disk/resources/'
        folders = file_path_folder.split('/')
        m_folder = ""
        for folder in folders:
            m_folder = f'{m_folder}/{folder}'
            param_folder = {'path': f"{m_folder}", 'owerwrite': 'true'}
            resp = requests.put(url, headers=headers, params=param_folder, verify=False)
            error = resp.json().get("message")
            if error is not None and "уже существует" not in error:
                return resp.json()
        return ""

    def get_upload_link(self, file_path_folder, file_name, file_url=None):
        headers = self.get_headers()

        # создадим папки
        checked_folders = self.check_and_create_cloud_folders(file_path_folder, headers)
        if checked_folders != "":
            return checked_folders

        # получим ссылку на загрузку файла
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload/'
        all_path = f"{file_path_folder}/{file_name}"
        param = {'path': all_path, 'owerwrite': 'true'}
        resp = requests.get(url, headers=headers, params=param, verify=False)
        return resp.json()

    def upload_file_to_disk_from_local(self, file_path_folder, file_name):
        # для загрузки файла из локального пути
        ahref_json = self.get_upload_link(
            file_path_folder=file_path_folder,
            file_name=file_name
        )

        ahref = ahref_json.get("href")
        if ahref != 0 and ahref is not None:
            resp = requests.put(url=ahref, data=open(file_name, 'rb'), verify=False)
            resp.raise_for_status()
            if resp.status_code == 201:
                return ""
            else:
                return f"{resp.status_code}: {resp.reason}"
        else:
            return f'{ahref_json.get("message")}'

    def check_file_name(self, file_path_folder, file_name, headers):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/'
        all_path = f"{file_path_folder}/{file_name}.jpg"
        param = {'path': all_path}
        resp = requests.get(url=url, headers=headers, params=param, verify=False)
        if resp.status_code == 404:  # файл по пути с таким именем не найден
            return False
        else:
            return True

    def upload_file_to_disk(self, file_path_folder, file_name, file_url=None):
        # для загрузки файлов по url
        headers = self.get_headers()

        # проверим (и создадим) папки
        checked_folders = self.check_and_create_cloud_folders(file_path_folder, headers)
        if checked_folders != "":
            return checked_folders

        # проверим, есть ли уже файлы с таким именем по пути
        checked_name = self.check_file_name(file_path_folder, file_name, headers)
        if checked_name:
            name_folder_dump_now = datetime.datetime.now().strftime("%Y-%m-%d %H.%M")
            file_name = f'{file_name} {name_folder_dump_now}.jpg'
        else:
            file_name = f'{file_name}.jpg'

        # post
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload/'
        all_path = f"{file_path_folder}/{file_name}"
        param = {'path': all_path,
                 # 'owerwrite': 'true',
                 'replace': 'true',
                 'url': file_url
                 }
        resp = requests.post(url=url, headers=headers, params=param, verify=False)
        # resp.raise_for_status()
        if resp.status_code == 201 or resp.status_code == 202:
            # запрос принят сервером, нужно проверить статус операции
            time.sleep(1)
            url_operation_id = resp.json().get("href")
            resp = requests.get(url=url_operation_id, headers=headers, verify=False)
            status_oper = resp.json().get("status")
            if status_oper == "success" or status_oper == "in-progress":
                return ""
            else:
                return f"Статус асинхронной операции: {status_oper}"
        else:
            return f"{resp.status_code}: {resp.reason}"



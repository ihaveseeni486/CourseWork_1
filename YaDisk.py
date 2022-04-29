import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


class YandexDisk:

    def __init__(self, token):
        self.token = token
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

    def get_headers(self):
        return {
                'Content-Type': 'application/json',
                'Authorization': 'OAuth {}'.format(self.token)
            }

    def get_files_in_list(self):
        url_files = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        resp = requests.get(url_files, headers=headers, verify=False)
        return resp.json()

    def get_upload_link(self, file_path_folder, file_name, file_url=None):
        headers = self.get_headers()
        param = {'path': f"{file_path_folder}", 'owerwrite': 'true'}

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

        # получим ссылку на загрузку файла
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload/'
        all_path = f"{file_path_folder}/{file_name}"
        param = {'path': all_path, 'owerwrite': 'true'}
        resp = requests.get(url, headers=headers, params=param, verify=False)
        return resp.json()

    def upload_file_to_disk(self, file_path_folder, file_name, file_url=None):
        ahref_json = ""
        if isinstance(file_url, str):
            ahref_json = self.get_upload_link(
                                                file_path_folder=file_path_folder,
                                                file_name=file_name,
                                                file_url=file_url
                                             )
        else:
            ahref_json = self.get_upload_link(
                                                file_path_folder=file_path_folder,
                                                file_name=file_name
                                             )

        ahref = ahref_json.get("href")
        if ahref != 0 and ahref is not None:
            if isinstance(file_url, str):
                try:
                    headers = self.get_headers()
                    params = {
                              'path': f'{ahref}',
                              'url': f'{file_url}',
                              'owerwrite': 'true'
                              }
                    resp = requests.put(headers=headers, params=params, url=ahref, verify=False)
                except Exception as exex:
                    return exex["message"]
            else:
                resp = requests.put(url=ahref, data=open(file_name, 'rb'), verify=False)
            resp.raise_for_status()
            if resp.status_code == 201:
                return ""
            else:
                return f"{resp.status_code}: {resp.reason}"
        else:
            return f'{ahref_json.get("message")}'



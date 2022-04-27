import requests


class YandexDisk:

    def __init__(self, token):
        self.token = token

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

    def get_upload_link(self, file_path_folder, file_name):
        headers = self.get_headers()
        param = {'path': f"{file_path_folder}", 'owerwrite': 'true'}

        # создадим папку
        url = 'https://cloud-api.yandex.net/v1/disk/resources/'
        resp = requests.put(url, headers=headers, params=param, verify=False)

        # загрузим файл
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload/'
        all_path = f"{file_path_folder}/{file_name}"
        param = {'path': all_path, 'owerwrite': 'true'}
        resp = requests.get(url, headers=headers, params=param, verify=False)
        return resp.json()

    def upload_file_to_disk(self, file_path_folder, file_name):
        ahref_json = self.get_upload_link(file_path_folder, file_name)
        ahref = ahref_json.get("href")
        if ahref != 0 and ahref is not None:
            resp = requests.put(ahref, data=open(file_name, 'rb'), verify=False)
            resp.raise_for_status()
            if resp.status_code == 201:
                return ""
            else:
                return f"{resp.status_code}: {resp.reason}"
        else:
            return f'{ahref_json.get("message")}'

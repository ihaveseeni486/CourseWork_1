import requests
import OpenSSL


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

    def get_upload_link(self, file_path_disk):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload/'
        headers = self.get_headers()
        param = {'path': file_path_disk, 'owerwrite': 'true'}
        resp = requests.get(url, headers=headers, params=param, verify=False)
        return resp.json()

    def upload_file_to_disk(self, file_path_disk, file_name):
        ahref_json = self.get_upload_link(file_path_disk)
        ahref = ahref_json.get("href")
        if ahref != 0:
            resp = requests.put(ahref, data=open(file_name, 'rb'), verify=False)
            resp.raise_for_status()
            if resp.status_code == 201:
                return True
            else:
                return False
        else:
            return False
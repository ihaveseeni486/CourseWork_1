import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


class VkStuff:

    def __init__(self, user_id, token):
        self.user_id = user_id
        self.token = token
        self.id = 0
        self.album_id_dict = {}    # json ответ getAlbums
        self.photo_info_dict = {}  # json ответ photos.get
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

    def get_user(self):
        url = "https://api.vk.com/method/users.get"
        headers = {'Content-Type': 'application/json'}
        params = {'access_token': self.token, 'user_ids': self.user_id, 'v': '5.131'}

        resp = requests.get(url, headers=headers, params=params, verify=False)
        resp_json = resp.json().get("response")
        if resp_json is not None:
            self.id = resp_json[0].get("id")
        else:
            self.id = 0

        if self.id != 0 and self.id is not None:
            return "Пользователь VK с введенными данными найден"
        else:
            message = resp.json().get("error")
            return f'Пользователь VK не найден:\n    {message.get("error_code")} {message.get("error_msg")}'

    def get_albums(self):
        url = "https://api.vk.com/method/photos.getAlbums"
        headers = {'Content-Type': 'application/json'}
        params = {
                    'access_token': self.token,
                    'owner_id': self.id,
                    'v': '5.131'
                 }
        resp = requests.get(url, headers=headers, params=params, verify=False)
        resp_json = resp.json().get("response")
        if resp_json is not None:
            albums_count = resp_json.get("count")
            self.album_id_dict = resp_json
            return f"Список альбомов получен: {albums_count} шт."
        else:
            self.album_id_dict = {}
            message = resp.json().get("error")
            return f'Список альбомов с фото не получен:\n    {message.get("error_code")} {message.get("error_msg")}'

    def get_photos(self):
        url = "https://api.vk.com/method/photos.getAll"
        headers = {'Content-Type': 'application/json'}

        params = {
                    'access_token': self.token,
                    'owner_id': self.id,
                    'extended': 1,
                    # 'photo_sizes': 1,
                    'v': '5.131'
                 }
        resp = requests.get(url, headers=headers, params=params, verify=False)
        resp_json = resp.json().get("response")
        if resp_json is not None:
            photo_count = resp_json.get("count")
            self.photo_info_dict = resp_json
            return f"Информация о фото получена: {photo_count} шт."
        else:
            self.photo_info_dict = ""
            message = resp.json().get("error")
            return f'Информация о фото не получена:\n    {message.get("error_code")} {message.get("error_msg")}'

    def get_best_photo(self, item):
        best_url = ""
        max_height = 0
        for size in item["sizes"]:
            if int(size["height"]) > max_height:
                max_height = int(size["height"])
                best_url = size["url"]
        return best_url

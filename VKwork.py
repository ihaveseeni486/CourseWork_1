import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


class VkStuff:

    def __init__(self, user_id, token):
        self.user_id = user_id
        self.token = token
        self.id = 0
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

    def get_user(self):
        url = "https://api.vk.com/method/users.get"
        headers = {'Content-Type': 'application/json'}
        params = {'access_token': self.token, 'user_ids': self.user_id, 'v': '5.131'}

        # request_send =f"https://api.vk.com/method/users.get?access_token={self.token}&user_ids={self.user_id}&v=5.131"
        # resp = requests.get(request_send, verify=False)

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

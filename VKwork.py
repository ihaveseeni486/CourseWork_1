import requests


class VkStuff:

    def __init__(self, user_id, token):
        self.user_id = user_id
        self.token = token

    def get_user(self):
        request_send = f"https://api.vk.com/method/users.get?access_token={self.token}&user_ids={self.user_id}&v=5.131"
        resp = requests.get(request_send, verify=False)
        return resp.json()

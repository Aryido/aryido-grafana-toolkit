class BaseApi:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token

    def generate_header(self):
        return {
            "Accept": "application/json",
            "Content-Type": "application/json",
            'Authorization': "Bearer {0}".format(self.token)
        }

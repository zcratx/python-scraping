import requests


class BearerAuth(requests.auth.AuthBase):
    def __int__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers["authorization"] = "Bearer"+self.token
        return r
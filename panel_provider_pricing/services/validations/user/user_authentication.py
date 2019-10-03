from django.contrib.auth import authenticate


class UserAuthentication():

    def __init__(self, user_params):
         username = user_params["username"]
         password = user_params["password"]


    def passed(self):
        if authenticate(username=self.username, password=self.password):
            return True
        else:
            return False

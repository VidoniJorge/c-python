from flask_login import UserMixin

class UserData():
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password

class UserModel(UserMixin):
    def __init__(self, user_data: UserData) -> None:
        print(user_data)
        self.id = user_data.username
        self.password = user_data.password

    @staticmethod
    def query(username):
        user_data = UserData(username=username, password=username*2)
        return UserModel(user_data=user_data)


    def is_authenticated(self):
        return True
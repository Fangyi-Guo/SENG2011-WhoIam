class Admin:

    def __init__(self, username, userId, userId):
        self._username = username
        self._password = password
        self._userId = userId

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, new_username):
        self._username = new_username

    @password.setter
    def password(self, new_password):
        self._password = new_password

    @property
    def password(self):
        return self._password

    @property
    def userId(self):
        return self._userId
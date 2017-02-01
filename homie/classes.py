from homie.db import save_user, save_log

class User:
    def __init__(self, id, username, password, chat_id):
        self.id = id
        self.username = username
        self.password = password
        self.chat_id = chat_id
        
    def save(self):
        save_user(self)

class Log:
    def __init__(self, id, user, action, date):
        self.id = id
        self.user = user
        self.action = action
        self.date = date
        
    def save(self):
        save_log(self)

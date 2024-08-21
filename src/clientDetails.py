from datetime import datetime
import pytz

class ClientDetails:
    def __init__(self, id, name, surname, number, email, birthday, last_check_up):
        self.id = id
        self.name = name
        self.surname = surname
        self.number = number
        self.email = email
        self.birthday = birthday
        self.last_check_up = last_check_up

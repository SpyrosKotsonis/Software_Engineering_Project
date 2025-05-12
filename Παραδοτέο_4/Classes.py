class Log_Entry:
    log_id = 0
    TimeStamp = 0
    User = "Spyros"
    request = "GET"
    Action = ""

class User:
    def __init__(self, id, name, email):
        self.user_id = id
        self.Name = name 
        self.Email = email

class Employee(User):
    def __init__(self, id, name, email, position):
        super().__init__(id, name, email)
        self.position = position

class Admin(User):
    def __init__(self, id, name, email):
        super().__init__(id, name, email)


class Equipment:
    def __init__(self, id, name, status):
        self.equipment_id = id
        self.name = name
        self.status = status

class Request:
    def __init__(self, id, user, equipment, date, status):
        self.request_id = id
        self.user = user
        self.equipment = equipment
        self.date = date
        self.status = status

class Repair_Request(Request):
    def __init__(self, id, user, equipment, date, status, repair_details):
        super().__init__(id, user, equipment, date, status)
        self.repair_details = repair_details

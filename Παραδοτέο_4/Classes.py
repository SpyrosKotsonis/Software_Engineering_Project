class Log_Entry:
    log_id = 0
    TimeStamp = 0
    User = "Spyros"
    request = "GET"
    Action = ""

class User:
    user_id = 0 
    Name = ""
    Email = ""
    def __init__(id, name, email):
        user_id = id
        Name = name 
        Email = email

class Request:
    request_id = 0
    user = User(1100596, "Spyros", "spiro.kotsonis@gmail.com") 
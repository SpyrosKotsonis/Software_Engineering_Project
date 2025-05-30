class Account:
    def __init__(self, id, name, email):
        self.user_id = id
        self.Name = name 
        self.Email = email

class User(Account):
    def __init__(self, id, name, email, position):
        super().__init__(id, name, email)
        self.position = position

class Admin(Account):
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

class Equipment_Queue:
    def __init__(self, equipment_id):
        self.equipment = equipment_id
        self.User_Order = []  # List to hold user IDs in the queue
        
    def Add_User_to_Queue(self, user_id):
        self.User_Order.append(user_id)

class DB_Manager:
    def Check_Account_Details(self, username, password):
        pass
    
    def Equipment_querry(self, searrch_term):
        pass
    
    def Check_Equipment_Status(self, equipment_id):
        pass
    
    def Store_Request(self, request: Request):
        pass

class Screen:
    
    def display(self):
        pass

class User_Main_Screen(Screen):
    
    def Manage_Equipment(self):
        pass

class Admin_Main_Screen(Screen):
    
    def Create_Account(self):
        pass
    
    def Account_Created_Message(self):
        pass

class Search_Screen(Screen):
    
    def Search_Equipment(self):
        pass
    
class Search_Results_Screen(Screen):
    
    def Display_Results(self, results):
        pass
    
    def Select_Equipment(self):
        pass
    
class Unavailable_Equipment_Screen(Screen):
    
    def Add_To_Queue(self):
        pass

class Request_Screen(Screen):
    
    def Confirm_Rquest(self):
        pass

class Account_Creation_Screen(Screen):
    
    def Enter_Account_Details(self):
        pass
    
    def Failure_Message():
        print("Account creation failed. Please try again.")

class Log_Entry:
    def __init__(self):
        pass
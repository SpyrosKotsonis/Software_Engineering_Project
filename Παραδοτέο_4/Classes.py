from datetime import datetime

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
    def __init__(self):
        self.equipment_list = []
        self.requests = []
        self.queues = {}
        
    def Check_Account_Details(self, username, password):
        pass
    
    def equipment_query(self, search_term):

        matching_equipment = []

        for equipment in self.equipment_list:
            if search_term.lower() in equipment.name.lower():
                matching_equipment.append(equipment)

        return matching_equipment

    
    def Check_Equipment_Status(self, equipment_id):
        for e in self.equipment_list:
            if e.equipment_id == equipment_id:
                return e.status
        return None

    def Store_Request(self, request: Request):
        self.requests.append(request)
        
    def add_equipment(self, equipment):
        self.equipment_list.append(equipment)


    def get_equipment_by_id(self, equipment_id):
        for e in self.equipment_list:
            if e.equipment_id == equipment_id:
                return e
        return None

    def add_to_queue(self, equipment_id, user_id):
        if equipment_id not in self.queues:
            self.queues[equipment_id] = Equipment_Queue(equipment_id)
        self.queues[equipment_id].Add_User_to_Queue(user_id)

    def get_queue(self, equipment_id):
        return self.queues.get(equipment_id)

    

class Screen:
    
    def display(self):
        pass

class User_Main_Screen(Screen):
    def __init__(self, db_manager, user):
        self.db = db_manager
        self.user = user

    def manage_equipment(self):
        print("Enter search term for equipment:")
        term = input()
        results = self.db.equipment_query(term)
        screen = Search_Results_Screen(self.db, self.user, results)
        screen.display()

class Admin_Main_Screen(Screen):
    
    def Create_Account(self):
        pass
    
    def Account_Created_Message(self):
        pass

class Search_Screen(Screen):
    
    def Search_Equipment(self):
        pass
    
class Search_Results_Screen(Screen):
    def __init__(self, db_manager, user, results):
        self.db = db_manager
        self.user = user
        self.results = results

    def display(self):
        if not self.results:
            print("No equipment found.")
            return
        print("\nSearch Results:")
        for eq in self.results:
            print(f"{eq.equipment_id}) {eq.name} - {'Available' if eq.status else 'Not Available'}")

        eq_id = int(input("\nSelect equipment ID to request: "))
        equipment = self.db.get_equipment_by_id(eq_id)
        if not equipment:
            print("Invalid selection.")
            return

        if equipment.status:
            screen = Request_Screen(self.db, self.user, equipment)
        else:
            screen = Unavailable_Equipment_Screen(self.db, self.user, equipment)
        screen.display()

    
class Unavailable_Equipment_Screen(Screen):
    def __init__(self, db_manager, user, equipment):
        self.db = db_manager
        self.user = user
        self.equipment = equipment

    def display(self):
        print(f"\nThe equipment '{self.equipment.name}' is currently unavailable.")
        choice = input("Would you like to join the waitlist? (yes/no): ").strip().lower()
        if choice == "yes":
            self.db.add_to_queue(self.equipment.equipment_id, self.user.user_id)
            print("Added to waitlist. Admin notified.")
        else:
            print("Request cancelled.")

class Request_Screen(Screen):
    def __init__(self, db_manager, user, equipment):
        self.db = db_manager
        self.user = user
        self.equipment = equipment

    def display(self):
        print("\nRequest Form:")
        justification = input("Enter justification: ")
        comments = input("Additional comments: ")

        req = Request(
            id=len(self.db.requests) + 1,
            user=self.user,
            equipment=self.equipment,
            date=datetime.now().strftime('%Y-%m-%d %H:%M'),
            status="pending"
        )
        self.db.Store_Request(req)
        print("Request submitted.")
        print("Admin has been notified.")

class Account_Creation_Screen(Screen):
    
    def Enter_Account_Details(self):
        pass
    
    def Failure_Message():
        print("Account creation failed. Please try again.")

class Log_Entry:
    def __init__(self):
        pass
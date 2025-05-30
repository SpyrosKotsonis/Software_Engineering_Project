from Classes import DB_Manager, Equipment, User, User_Main_Screen

# Setup
db = DB_Manager()
db.add_equipment(Equipment(1, "Camera", True))
db.add_equipment(Equipment(2, "Tripod", False))

user = User(101, "Alice", "alice@example.com", "Student")

# Launch user main screen
screen = User_Main_Screen(db, user)
screen.manage_equipment()
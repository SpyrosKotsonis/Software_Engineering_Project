from Classes import DB_Manager, Admin_Main_Screen

db = DB_Manager()
admin_screen = Admin_Main_Screen(db)
admin_screen.create_account()

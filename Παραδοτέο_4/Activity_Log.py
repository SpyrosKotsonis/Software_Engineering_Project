from Classes import DB_Manager, User, Log_Screen

db = DB_Manager()
user = User(1, "Alice", "alice@example.com", "Student")

# Simulate some activity logs
db.log_activity("Ο χρήστης Alice έκανε αίτηση για εξοπλισμό.")
db.log_activity("Ο διαχειριστής ενέκρινε την αίτηση της Alice.")
db.log_activity("Ο χρήστης Alice επέστρεψε τον εξοπλισμό.")

# View history screen
history_screen = Log_Screen(db, user)
history_screen.display()


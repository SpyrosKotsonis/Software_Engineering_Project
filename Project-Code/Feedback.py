from datetime import datetime
from typing import List

class Feedback:
	def __init__(self, content, author, role, timestamp=None):
		self.content = content
		self.author = author
		self.role = role
		self.timestamp = timestamp if timestamp else datetime.now()
		self.replies: List[Reply] = []
	def __repr__(self):
		return f"[{self.timestamp.strftime('%Y-%m-%d %H:%M')}] {self.author} {self.role}: {self.content}"

class Reply:
	def __init__(self, content, author, role, timestamp=None):
		self.content = content
		self.author = author
		self.role = role
		self.timestamp = timestamp if timestamp else datetime.now()
	def __repr__(self):
		return f" ------> [{self.timestamp.strftime('%Y-%m-%d %H:%M')}] ({self.role}) {self.author}: {self.content}"

class User:
	def __init__(self, username, role):
		self.username = username
		self.role = role
		return

class UserAdminDatabase:
	def __init__(self):
		self.users = {
		User("admin_user", "admin"),
		User("normal_user", "user")
		}
		self.feedback_list: List[Feedback] = []

	def is_admin(self):
		return self.role == "admin"


class FeedbackDatabase:
	def __init__(self):
		self.Feedback = [
			Feedback("Το σύστημα χρειάζεται βελτίωση στο UI.", "normal_user", "user", "datetime.now")
		]
		self.Reply = [
			Reply("Ευχαριστούμε για τα σχόλια!", "admin_user", "admin")
		]


	def get_all_feedback(self):
		return sorted(self.feedback_list, key=lambda fb: fb.timestamp, reverse=True)

	def add_feedback(self, feedback: Feedback):
		self.feedback_list.append(feedback)

	def add_reply(self, feedback_index, reply: Reply):
		if 0 <= feedback_index < len(self.feedback_list):
		self.feedback_list[feedback_index].replies.append(reply)

	def handle_post(self, user: User):
		print("\n>> Ανάρτηση Σχολίου")
		if user.is_admin():
			print("✖ Οι διαχειριστές δεν μπορούν να κάνουν σχόλια. Χρησιμοποιήστε τις Ανακοινώσεις.")
		else if user.is_user():
			content = input("Πληκτρολογήστε το σχόλιο σας:\n> ")
			new_feedback = Feedback(content=content, author=user.username)
			self.db.add_feedback(new_feedback)
			print("✔ Το σχόλιο καταχωρήθηκε.")
			self.open_feedback_center(user.username)
		return

	def handle_reply(self, user: User):
		print("\n>> Διαχείριση Σχολίων - Απάντηση")
		answer = input("Πληκτρολογήστε την απάντησή σας:\n> ")
		role_header = "admin" if user.is_admin() else "user"
		reply = Reply(content=answer, author=user.username, role=role_header)
		self.db.add_reply(index, reply)
		print("Η απάντηση καταχωρήθηκε.")
		self.open_feedback_center(user.username)

class HomeScreen:
	def start_FbCscreen(self):
		return FeedbackCenterScreen()

class FeedbackCenterScreen:
    def __init__(self, Database):
        self.Database = FeedbackDatabase()

    def user_feedbac_flowk(self, user: User):
        feedback = self.Database.get_all_feedback()
        choice = input("\nΘέλετε να προσθέσετε απάντηση στο σχόλιο; (yes/no): ").strip().lower()
        if choice == "yes":
            self.Database.handle_reply(new_reply)
            self.Database.add_reply(new_reply)
            print("Η απάντηση προστέθηκε με επιτυχία.")
        else:
            print("Επιστροφή στην Οθόνη Διαχείρισης Feedback.")
            choice = input("\nΘέλετε να προσθέσετε καινούργιο σχόλιο; (yes/no): ").strip().lower()
        if choice == "yes":
            return AdminCheck
        else:
            print("Επιστροφή στην Οθόνη Διαχείρισης Feedback.")
            return

class AdminCheck:
    def __init__(self, Database):
        self.Database.is_admin
        if 'True': return NewCommentScreen
        else: return FeedbackCenterScreen

class NewCommentScreen:
    def __init__(self, Database):
        self.Database = FeedbackDatabase()
        self.Database.handle_reply(new_reply)
        self.Database.add_reply(new_reply)
        print("Η απάντηση προστέθηκε με επιτυχία.")
        return	FeedbackCenterScreen
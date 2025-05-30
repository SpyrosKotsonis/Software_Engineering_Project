
from datetime import datetime
from typing import List

class Announcement:
    def __init__(self, content, author, timestamp=None):
        self.content = content
        self.author = author
        self.timestamp = timestamp if timestamp else datetime.now()

    def __repr__(self):
        return f"[{self.timestamp.strftime('%Y-%m-%d %H:%M')}] {self.author}: {self.content}"


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
        return

class AnouncementDatabase:
	def __init__(self):
		self.Announcements = [
			Announcement("Καλώς ήρθατε στο σύστημα!", "admin_user")
			Announcement("Η συντήρηση θα γίνει την Παρασκευή.", "admin_user")
		]
	def get_announcements(self):
		return sorted(self.announcements, key=lambda a: a.timestamp, reverse=True)
	def add_announcement(self, announcement):
		self.announcements.append(announcement)

class HomeScreen:
	def start_Ascreen(self):
		return AnnouncementSystem()

class AnnouncementSystem:
    def __init__(self, Database):
        self.Database = AnnouncementDatabse
    def access_announcement_center(self):
        if user.is_admin():
            self.admin_announcement_flow(user)
        else:
            self.user_announcement_flow(user)

    def user_announcement_flow(self, user: User):
        announcements = self.Database.get_announcements()

    def admin_announcement_flow(self, admin: User):
        announcements = self.Database.get_announcements()

        choice = input("\nΘέλετε να προσθέσετε νέα ανακοίνωση; (yes/no): ").strip().lower()
        if choice == "yes":
            content = input("Πληκτρολογήστε το περιεχόμενο της ανακοίνωσης:\n> ")
            new_announcement = Announcement(content=content, author=admin.username)
            self.Database.add_announcement(new_announcement)
            print("Η ανακοίνωση προστέθηκε με επιτυχία.")
        else:
            print("Επιστροφή στην Οθόνη Διαχείρισης Ανακοινώσεων.")
            return
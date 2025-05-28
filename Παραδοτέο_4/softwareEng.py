
class StartScreen:
    def __init__(self, db):
        self.db = db

    def display(self):
        print("Καλώς ήρθες στο BlackBox!")
        print("1. Δημιουργία νέου storage")
        print("2. Σύνδεση σε υπάρχον storage")
        choice = input("Επιλογή (1 ή 2): ")

        if choice == "1":
            CreationScreen(self.db).display()
        elif choice == "2":
            SigninScreen(self.db).display()
        else:
            print("Μη έγκυρη επιλογή.")


class SelectionClass:
    def __init__(self):
        self.signin = SigninClass()
        self.creation = CreationClass()

    def checkSelection(self):
        print("Καλώς ήρθες στο BlackBox!")
        print("1. Δημιουργία νέου storage")
        print("2. Σύνδεση σε υπάρχον storage")
        choice = input("Επιλογή (1 ή 2): ")

        if choice == "1":
            screen = CreationScreen()
            screen.display()
            screen.insertData()
            AdminMainScreen().display()

        elif choice == "2":
            screen = SigninScreen()
            screen.display()
            role = screen.insertAccount()
            if role == "admin":
                AdminMainScreen().display()
            elif role == "user":
                UserMainScreen().display()
            else:
                RejectionScreen().display()
        else:
            print("Μη έγκυρη επιλογή.")
            ErrorScreen().display()


class SigninClass:
    def __init__(self, db):
        self.db = db

    def doSignin(self):
        username = input("Δώσε όνομα χρήστη: ")
        return self.db.identifyAccount(username)


class SigninScreen:
    def __init__(self, db):
        self.signin = SigninClass(db)

    def display(self):
        role = self.signin.doSignin()
        if role == "admin":
            AdminMainScreen().display()
        elif role == "user":
            UserMainScreen().display()
        else:
            RejectionScreen().display()


class RejectionScreen:
    def display(self):
        pass


class CreationClass:
    def __init__(self, db):
        self.db = db

    def createAccount(self):
        storage_name = input("Όνομα νέου storage: ")
        username = input("Όνομα admin: ")
        self.db.makeAdmin(storage_name, username)
        return username


class CreationScreen:
    def __init__(self, db):
        self.creator = CreationClass(db)

    def display(self):
        print("🆕 Δημιουργία νέου storage και λογαριασμού admin")
        username = self.creator.createAccount()
        AdminMainScreen().display()


class UserMainScreen:
    def display(self):
        print("Καλωσήρθες στην Οθόνη Χρήστη")
        while True:
            print("\n--- Επιλογές ---")
            print("1. Έξοδος")
            choice = input("Επιλογή: ")

            if choice == "1":
                print("Αποσύνδεση...")
                break
            else:
                print("Μη έγκυρη επιλογή.")


class AdminMainScreen:
    def __init__(self):
        self.main = MainClass()

    def display(self):
        print("Καλωσήρθες στην Οθόνη Διαχειριστή")

        while True:
            print("\n--- Επιλογές ---")
            print("1. Διαχείριση Αιτημάτων")
            print("2. Έξοδος")
            choice = input("Επιλογή: ")

            if choice == "1":
                self.selectManageRequest()
            elif choice == "2":
                print("Αποσύνδεση...")
                break
            else:
                print("Μη έγκυρη επιλογή.")

    def selectManageRequest(self):
        self.main.findRequest()

class UserAdminDB:
    def __init__(self):
        # Μοιάζει με βάση: storage_name -> {admins: [...], users: [...]}
        self.storage_accounts = {
            "demo_storage": {
                "admins": ["admin"],
                "users": ["user1", "user2"]
            }
        }

    def makeAdmin(self, storage_name, username):
        if storage_name not in self.storage_accounts:
            self.storage_accounts[storage_name] = {"admins": [], "users": []}
        self.storage_accounts[storage_name]["admins"].append(username)
        print(f"Δημιουργήθηκε νέο storage '{storage_name}'")
        print(f"Ο '{username}' προστέθηκε ως admin.")

    def identifyAccount(self, username):
        for storage, accounts in self.storage_accounts.items():
            if username in accounts["admins"]:
                print(f"Ο χρήστης '{username}' είναι admin στο '{storage}'")
                return "admin"
            elif username in accounts["users"]:
                print(f"Ο χρήστης '{username}' είναι user στο '{storage}'")
                return "user"
        print(f"Ο χρήστης '{username}' δεν βρέθηκε.")
        return None


class MainClass:
    def __init__(self):
        self.request_handler = RequestClass()

    def findRequest(self):
        requests = self.request_handler.getRequests()
        print("Αιτήματα:")
        for i, r in enumerate(requests):
            print(f"{i + 1}. {r}")
        choice = int(input("Επίλεξε αριθμό αιτήματος: ")) - 1
        action = input("Έγκριση (a) ή Απόρριψη (r); ")
        approved = action.lower() == 'a'
        success = self.request_handler.handleRequest(choice, approve=approved)
        if success:
            if approved:
                RequestApprovalScreen().display()
            else:
                RequestRejectionScreen().display()
        else:
            print("Αποτυχία στην επεξεργασία.")


class RequestClass:
    def __init__(self):
        self.db = RequestDB()

    def getRequests(self):
        return self.db.queryRequest()

    def handleRequest(self, index, approve=True):
        status = "Εγκρίθηκε" if approve else "Απορρίφθηκε"
        return self.db.updateRequest(index, status)


class RequestDB:
    def __init__(self):
        self.requests = ["Αίτημα 1", "Αίτημα 2"]

    def queryRequest(self):
        return self.requests

    def updateRequest(self, index, status):
        if 0 <= index < len(self.requests):
            if "[Εγκρίθηκε]" in self.requests[index] or "[Απορρίφθηκε]" in self.requests[index]:
                print("❌ Το αίτημα έχει ήδη επεξεργαστεί.")
                return False
            self.requests[index] += f" - [{status}]"
            return True
        return False


class DBManager:
    def __init__(self):
        self.storages = []

    def create_storage(self, name):
        if name in self.storages:
            print("Το storage υπάρχει ήδη.")
            return False
        self.storages.append(name)
        print(f"✅ Δημιουργήθηκε νέο storage '{name}'")
        return True


class ErrorScreen:
    def display(self):
        pass


class ManagementClass:
    def __init__(self):
        self.db = RequestDB()

    def manageRequest(self):
        self.db.updateRequest()


class RequestScreen:
    def __init__(self):
        self.choice = RequestChoiceClass()

    def display(self):
        pass

    def makeChoice(self):
        pass


class RequestManagementScreen:
    def __init__(self):
        self.management = ManagementClass()

    def display(self):
        pass

    def selectRequest(self):
        self.management.manageRequest()


class RequestChoiceClass:
    def __init__(self):
        self.db = RequestDB()

    def makeDecision(self):
        pass


class RequestApprovalScreen:
    def display(self):
        print("✅ Το αίτημα εγκρίθηκε!")


class RequestRejectionScreen:
    def display(self):
        print("❌ Το αίτημα απορρίφθηκε.")



if __name__ == "__main__":
    shared_user_db = UserAdminDB()
    StartScreen(shared_user_db).display()
#ΟΡΓΑΝΩΣΗ ΕΞΟΠΛΙΣΜΟΥ
class Equipment:
    def __init__(self, equipment_id, name, type_, description, tags=[], comments=[]):
        self.equipment_id = equipment_id
        self.name = name
        self.type = type_
        self.description = description
        self.tags = tags

    def __repr__(self):
        return f"<Equipment {self.equipment_id}: {self.name}>"


class Admin:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.role = 'admin'

    def select_equipment(self):
        print("Ο admin επιλέγει εξοπλισμό.")

    def add_equipment(self, equipment, db, logs, notifications):
        db.save_equipment(equipment)
        logs.save_record(f"Προσθήκη εξοπλισμού: {equipment.name}", self.username)
        notifications.announcements(f"Νέος εξοπλισμός προστέθηκε: {equipment.name}")

    def remove_equipment(self, equipment_id, db, logs, notifications):
        removed = db.delete_equipment(equipment_id)
        if removed:
            logs.save_record(f"Αφαίρεση εξοπλισμού: {removed.name}", self.username)
            notifications.announcements(f"Ο εξοπλισμός αφαιρέθηκε: {removed.name}")


class Logs:
    def __init__(self):
        self.records = []

    def save_record(self, action, admin_name):
        record = f"{admin_name} - {action}"
        self.records.append(record)
        print("Log:", record)


class Notifications:
    def announcements(self, message):
        print("ΑΝΑΚΟΙΝΩΣΗ:", message)


class Database:
    def __init__(self):
        self.equipment_store = {}

    def save_equipment(self, equipment):
        self.equipment_store[equipment.equipment_id] = equipment
        print(f"[DB] Equipment saved: {equipment}")

    def delete_equipment(self, equipment_id):
        return self.equipment_store.pop(equipment_id, None)


# Use Case 

def organize_equipment_flow():
    # Instances
    db = Database()
    logs = Logs()
    notifications = Notifications()
    admin = Admin(user_id=1, username="admin_user")

    print(">> Επιλογή: Οργάνωση Εξοπλισμού")
    choice = input("Θέλετε να προσθέσετε ή να αφαιρέσετε εξοπλισμό; (add/remove): ").strip().lower()

    if choice == "add":
        # ADD Equipment
        print("\n-- Εισαγωγή στοιχείων εξοπλισμού --")
        eid = int(input("ID: "))
        name = input("Όνομα: ")
        type_ = input("Τύπος: ")
        desc = input("Περιγραφή: ")
        tags = input("Tags (comma separated): ").split(',')

        equipment = Equipment(equipment_id=eid, name=name, type_=type_, description=desc, tags=tags, comments=[comment])
        admin.add_equipment(equipment, db, logs, notifications)

    elif choice == "remove":
        # Remove Equipment
        print("\n-- Αφαίρεση εξοπλισμού --")
        eid = int(input("Εισάγετε το ID του εξοπλισμού προς διαγραφή: "))
        admin.remove_equipment(eid, db, logs, notifications)

    else:
        print("Μη έγκυρη επιλογή.")
{
organize_equipment_flow()
}

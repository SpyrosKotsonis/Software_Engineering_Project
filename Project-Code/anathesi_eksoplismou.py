# ------------------------
# Database and Models
# ------------------------

class Equipment:
    def __init__(self, equipment_id, name, status="available"):
        self.equipment_id = equipment_id
        self.name = name
        self.status = status

class Employee:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name

class DB:
    def __init__(self):
        self.equipment = [
            Equipment(1, "Laptop A"),
            Equipment(2, "Printer B"),
            Equipment(3, "Router C")
        ]

class EmployeeDB:
    def __init__(self):
        self.employees = [
            Employee(1, "Maria"),
            Employee(2, "Nikos"),
            Employee(3, "Giannis")
        ]

class LogsAndStatusDB:
    def __init__(self):
        self.logs = []
        self.status = {}

    def log_assignment(self, equipment_id, employee_ids, details):
        self.logs.append({
            "equipment_id": equipment_id,
            "assigned_to": employee_ids,
            "details": details
        })
        self.status[equipment_id] = "assigned"

    def log_repair(self, equipment_id):
        self.logs.append({
            "equipment_id": equipment_id,
            "action": "sent for repair"
        })
        self.status[equipment_id] = "under repair"

# ------------------------
# Logic Managers
# ------------------------

class DBManager:
    def __init__(self, db):
        self.db = db

    def query_equipment(self, keyword):
        return [e for e in self.db.equipment if keyword.lower() in e.name.lower()]

class ManageSearchClass:
    def __init__(self, db):
        self.dbManager = DBManager(db)

    def query_equipment(self, keyword):
        return self.dbManager.query_equipment(keyword)

class ManageRepairClass:
    def __init__(self, log_db):
        self.log_db = log_db

    def send_for_repair(self, equipment_id):
        self.log_db.log_repair(equipment_id)
        print(f"Equipment {equipment_id} sent for repair.")

class ManageSelectionScreen:
    def __init__(self, employee_db):
        self.employee_db = employee_db

    def query_employees(self):
        return self.employee_db.employees

# ------------------------
# UI Simulation (Console)
# ------------------------

class System:
    def __init__(self):
        self.db = DB()
        self.employee_db = EmployeeDB()
        self.log_db = LogsAndStatusDB()

    def start_assignment_flow(self):
        print("\n--- Equipment Assignment ---")
        keyword = input("Search for equipment (keyword): ")
        search_manager = ManageSearchClass(self.db)
        results = search_manager.query_equipment(keyword)

        if not results:
            print("No equipment found.")
            return

        print("\nAvailable Equipment:")
        for e in results:
            print(f"[{e.equipment_id}] {e.name} - Status: {e.status}")
        
        eq_choice = int(input("Select equipment ID: "))
        if input("Send to repair? (y/n): ").lower() == 'y':
            repair_manager = ManageRepairClass(self.log_db)
            repair_manager.send_for_repair(eq_choice)
            return

        # Proceed to assignment
        selection_manager = ManageSelectionScreen(self.employee_db)
        employees = selection_manager.query_employees()
        print("\nAvailable Employees:")
        for emp in employees:
            print(f"[{emp.employee_id}] {emp.name}")
        
        emp_ids = input("Enter employee IDs (comma-separated): ")
        selected_emp_ids = [int(eid.strip()) for eid in emp_ids.split(",")]

        print("\n--- Confirmation ---")
        confirm = input("Confirm assignment? (y/n): ")
        if confirm.lower() != 'y':
            print("Assignment cancelled.")
            return

        # Collect assignment details
        print("\n--- Additional Info ---")
        time = input("Estimated time: ")
        cost = input("Estimated cost: ")
        profit = input("Estimated profit: ")
        comments = input("Comments: ")

        details = {
            "time": time,
            "cost": cost,
            "profit": profit,
            "comments": comments
        }

        final = input("\nFinal confirmation (y/n): ")
        if final.lower() == 'y':
            self.log_db.log_assignment(eq_choice, selected_emp_ids, details)
            print("Assignment completed and logged.")
        else:
            print("Final confirmation declined.")

    def show_logs(self):
        print("\n--- Logs ---")
        for log in self.log_db.logs:
            print(log)

# ------------------------
# Run Simulation
# ------------------------

if __name__ == "__main__":
    system = System()
    system.start_assignment_flow()
    system.show_logs()
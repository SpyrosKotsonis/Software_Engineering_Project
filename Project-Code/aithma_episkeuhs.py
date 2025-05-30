# ------------------------
# Entity Classes
# ------------------------

class Equipment:
    def __init__(self, id: str, name: str, status: str = "available"):
        self.id = id
        self.name = name
        self.status = status

class Request:
    def __init__(self, id: int, equipment: Equipment, details: str):
        self.id = id
        self.equipment = equipment
        self.details = details

# ------------------------
# Simulated Database
# ------------------------

class DB:
    def __init__(self):
        self.equipment_list: List[Equipment] = [
            Equipment("1", "Laptop HP"),
            Equipment("2", "Printer Canon"),
            Equipment("3", "Router TP-Link"),
            Equipment("4", "Scanner Epson")
        ]

    def get_equipment(self, query: str) -> List[Equipment]:
        return [eq for eq in self.equipment_list if query.lower() in eq.name.lower()]

# ------------------------
# Control Classes
# ------------------------

class ManageSearchClass:
    def __init__(self, db: DB):
        self.db = db

    def search_equipment(self, query: str) -> List[Equipment]:
        return self.db.get_equipment(query)

class ManageRepairRequestClass:
    def __init__(self):
        self.request_id_counter = 1
        self.requests: List[Request] = []

    def create_repair_request(self, equipment: Equipment, details: str) -> Request:
        request = Request(id=self.request_id_counter, equipment=equipment, details=details)
        self.requests.append(request)
        self.request_id_counter += 1
        equipment.status = "under repair"
        return request

# ------------------------
# UI / Boundary Classes
# ------------------------

class MainScreen:
    def display(self):
        print("=== Κεντρική Οθόνη ===")
        print("1. Αναζήτηση εξοπλισμού για επισκευή")

class SearchScreen:
    def display(self):
        print("\n=== Οθόνη Αναζήτησης ===")

    def start_search(self, manager: ManageSearchClass, query: str) -> List[Equipment]:
        return manager.search_equipment(query)

class SearchResultScreen:
    def display(self):
        print("\n=== Αποτελέσματα Αναζήτησης ===")

    def show_results(self, results: List[Equipment]):
        for eq in results:
            print(f"[{eq.id}] {eq.name} (Κατάσταση: {eq.status})")

    def select_equipment(self, results: List[Equipment], equipment_id: str) -> Equipment:
        for eq in results:
            if eq.id == equipment_id:
                print(f"Επιλέχθηκε εξοπλισμός: {eq.name}")
                return eq
        raise ValueError("Δεν βρέθηκε εξοπλισμός με αυτό το ID.")

class RepairRequestScreen:
    def display(self):
        print("\n=== Οθόνη Αίτησης Επισκευής ===")

    def submit(self, manager: ManageRepairRequestClass, equipment: Equipment, details: str) -> Request:
        return manager.create_repair_request(equipment, details)

# ------------------------
# Application Flow
# ------------------------

def run_repair_flow():
    db = DB()
    search_manager = ManageSearchClass(db)
    repair_manager = ManageRepairRequestClass()

    # UI Screens
    main = MainScreen()
    search_screen = SearchScreen()
    results_screen = SearchResultScreen()
    repair_screen = RepairRequestScreen()

    # Flow
    main.display()
    input("Πάτησε Enter για να ξεκινήσεις...")

    search_screen.display()
    query = input("Αναζήτησε εξοπλισμό (λέξη-κλειδί): ")
    results = search_screen.start_search(search_manager, query)

    if not results:
        print("Δεν βρέθηκε εξοπλισμός.")
        return

    results_screen.display()
    results_screen.show_results(results)

    chosen_id = input("Εισάγετε το ID του εξοπλισμού που θέλετε να επισκευαστεί: ")
    selected_equipment = results_screen.select_equipment(results, chosen_id)

    repair_screen.display()
    problem_desc = input("Περιγραφή προβλήματος: ")
    request = repair_screen.submit(repair_manager, selected_equipment, problem_desc)

    print("\n✅ Η αίτηση επισκευής καταχωρήθηκε με ID:", request.id)
    print("Εξοπλισμός:", request.equipment.name)
    print("Κατάσταση:", request.equipment.status)
    print("Λεπτομέρειες:", request.details)

# ------------------------
# Run Program
# ------------------------

if __name__ == "__main__":
    run_repair_flow()

# Entity classes
class Equipment:
    def __init__(self, id: str, name: str, status: str):
        self.id = id
        self.name = name
        self.status = status

class Request:
    def __init__(self, id: int, equipment: Equipment, details: str):
        self.id = id
        self.equipment = equipment
        self.details = details

# Simulated database
class DB:
    def __init__(self):
        self.equipment_list: List[Equipment] = []

    def get_equipment(self, query: str) -> List[Equipment]:
        return [eq for eq in self.equipment_list if query.lower() in eq.name.lower()]

# Control class for managing search
class ManageSearchClass:
    def __init__(self, db: DB):
        self.db = db

    def search_equipment(self, query: str) -> List[Equipment]:
        return self.db.get_equipment(query)

# Control class for managing repair requests
class ManageRepairRequestClass:
    def create_repair_request(self, equipment: Equipment, details: str) -> Request:
        return Request(id=1, equipment=equipment, details=details)

# Boundary/UI classes
class MainScreen:
    def display(self):
        print("Displaying main screen.")

class SearchScreen:
    def display(self):
        print("Displaying search screen.")

    def start_search(self, manager: ManageSearchClass, query: str) -> List[Equipment]:
        return manager.search_equipment(query)

class SearchResultScreen:
    def display(self):
        print("Displaying search results.")

    def show_results(self, results: List[Equipment]):
        for eq in results:
            print(f"Found equipment: {eq.name}")

    def select_equipment(self, equipment: Equipment) -> Equipment:
        print(f"Selected equipment: {equipment.name}")
        return equipment

class RepairRequestScreen:
    def display(self):
        print("Displaying repair request screen.")

    def submit(self, manager: ManageRepairRequestClass, equipment: Equipment, details: str) -> Request:
        return manager.create_repair_request(equipment, details)

# Return a list of class names to confirm definitions
[class_.__name__ for class_ in [
    Equipment, Request, DB, ManageSearchClass, ManageRepairRequestClass, 
    MainScreen, SearchScreen, SearchResultScreen, RepairRequestScreen
]]

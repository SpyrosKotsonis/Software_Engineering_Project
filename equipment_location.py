#ΕΝΤΟΠΙΣΜΟΣ ΕΞΟΠΛΗΣΜΟΥ
from typing import List

class Equipment:
    def __init__(self, equipment_id, name, status, availability, cost, rental_cost, location, user):
        self.equipment_id = equipment_id
        self.name = name
        self.status = status
        self.availability = availability
        self.cost = cost
        self.rental_cost = rental_cost
        self.location = location
        self.user = user

class EquipmentHistory:
    def __init__(self, equipment_id, use_date, user, status, location):
        self.equipment_id = equipment_id
        self.use_date = use_date
        self.user = user
        self.status = status
        self.location = location

class Database:
    def __init__(self):
        # mock database
        self.equipment = [
            Equipment(1, "Crane", "Available", 1, 10000, 300, "Warehouse A", "None"),
            Equipment(2, "Drill", "Unavailable", 0, 500, 50, "Warehouse B", "User1")
        ]
        self.history = [
            EquipmentHistory(1, "2024-01-01", "UserX", "Operational", "Warehouse A")
        ]
    
    def search_equipment(self, category=None, available=None, status=None, location=None) -> List[Equipment]:
        results = []
        for eq in self.equipment:
            if category and category.lower() not in eq.name.lower():
                continue
            if available is not None and eq.availability != available:
                continue
            if status and status.lower() != eq.status.lower():
                continue
            if location and location.lower() not in eq.location.lower():
                continue
            results.append(eq)
        return results

    def get_equipment_history(self, equipment_id):
        return [h for h in self.history if h.equipment_id == equipment_id]

class HomeScreen:
    def start_search(self):
        return SearchScreen()

class SearchScreen:
    def __init__(self):
        self.database = Database()

    def search_equipment(self, criteria):
        results = self.database.search_equipment(
            category=criteria.get("category"),
            available=criteria.get("available"),
            status=criteria.get("status"),
            location=criteria.get("location")
        )
        return SearchResultScreen().return_search(results)

class SearchResultScreen:
    def return_search(self, results: List[Equipment]):
        print("Search Results:")
        for eq in results:
            print(f"{eq.equipment_id}: {eq.name} - {eq.status} @ {eq.location}")
        return results

class EquipmentDetailsScreen:
    def __init__(self, database: Database):
        self.database = database

    def details_view(self, equipment: Equipment):
        print("\nEquipment Details:")
        print(f"ID: {equipment.equipment_id}")
        print(f"Name: {equipment.name}")
        print(f"Status: {equipment.status}")
        print(f"Availability: {equipment.availability}")
        print(f"Cost: {equipment.cost}")
        print(f"Rental Cost: {equipment.rental_cost}")
        print(f"Location: {equipment.location}")
        print(f"User: {equipment.user}")
        print("\nHistory:")
        history = self.database.get_equipment_history(equipment.equipment_id)
        for h in history:
            print(f"- {h.use_date}: {h.user} - {h.status} @ {h.location}")

# Use case 
def run_equipment_search_use_case():
    # User starts from Home Screen
    home = HomeScreen()
    search_screen = home.start_search()

    # Criteria entered
    criteria = {
        "category": "Crane",
        "available": 1,
        "status": "Available",
        "location": "Warehouse A"
    }

    # System searches and returns results
    results = search_screen.search_equipment(criteria)

    # User selects first equipment
    if results:
        selected_equipment = results[0]
        EquipmentDetailsScreen(search_screen.database).details_view(selected_equipment)

run_equipment_search_use_case()

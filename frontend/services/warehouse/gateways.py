import requests

# ============================================================
#                           ITEMS
# ============================================================
class ItemsGateway:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get_items(self):
        r = requests.get(f"{self.base_url}/items")
        r.raise_for_status()
        return r.json()

    def get_item(self, name: str):
        r = requests.get(f"{self.base_url}/items/{name}")
        r.raise_for_status()
        return r.json()

    def create_item(self, data: dict):
        r = requests.post(f"{self.base_url}/items", json=data)
        r.raise_for_status()
        return r.json()

    def update_item(self, item_id: int, data: dict):
        r = requests.put(f"{self.base_url}/items/{item_id}", json=data)
        r.raise_for_status()
        return r.json()

    def delete_item(self, item_id: int):
        r = requests.delete(f"{self.base_url}/items/{item_id}")
        r.raise_for_status()
        return r.json()


# ============================================================
#                         CATEGORIES
# ============================================================
class CategoriesGateway:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get_categories(self):
        r = requests.get(f"{self.base_url}/categories")
        r.raise_for_status()
        return r.json()

    def create_category(self, data: dict):
        r = requests.post(f"{self.base_url}/categories", json=data)
        r.raise_for_status()
        return r.json()
    

# ============================================================
#                         SECTIONS
# ============================================================
class SectionsGateway:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get_sections(self):
        r = requests.get(f"{self.base_url}/sections")
        r.raise_for_status()
        return r.json()

    def create_section(self, data: dict):
        r = requests.post(f"{self.base_url}/sections", json=data)
        r.raise_for_status()
        return r.json()
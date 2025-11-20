from .gateways import ItemsGateway, CategoriesGateway, SectionsGateway


# ============================================================
#                           ITEMS
# ============================================================
class ItemsUsecase:
    def __init__(self, gateway: ItemsGateway):
        self.gateway = gateway

    def list_items(self):
        return self.gateway.get_items()

    def get_item(self, name: str):
        return self.gateway.get_item(name)

    def add_item(self, item_data: dict):
        return self.gateway.create_item(item_data)

    def modify_item(self, name: str, item_data: dict):
        return self.gateway.update_item(name, item_data)

    def remove_item(self, name: str):
        return self.gateway.delete_item(name)


# ============================================================
#                         CATEGORIES
# ============================================================
class CategoriesUsecase:
    def __init__(self, gateway: CategoriesGateway):
        self.gateway = gateway

    def list_categories(self):
        return self.gateway.get_categories()

    def add_category(self, category_data: dict):
        return self.gateway.create_category(category_data)


# ============================================================
#                         SECTIONS
# ============================================================
class SectionsUsecase:
    def __init__(self, gateway: SectionsGateway):
        self.gateway = gateway

    def list_sections(self):
        return self.gateway.get_sections()

    def add_section(self, section_data: dict):
        return self.gateway.create_section(section_data)
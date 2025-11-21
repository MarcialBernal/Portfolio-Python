import streamlit as st

from services.warehouse.usecases import (
    ItemsUsecase,
    CategoriesUsecase,
    SectionsUsecase,
)
from services.warehouse.gateways import (
    ItemsGateway,
    CategoriesGateway,
    SectionsGateway,
)

# ============================================================
#   CONFIG
# ============================================================

st.set_page_config(
    page_title="Warehouse Panel",
    page_icon="📦",
    layout="wide",
)

BASE_URL = "http://localhost:8000"

@st.cache_resource
def get_services(base_url: str):
    items_gateway = ItemsGateway(base_url)
    categories_gateway = CategoriesGateway(base_url)
    sections_gateway = SectionsGateway(base_url)

    items_service = ItemsUsecase(items_gateway)
    categories_service = CategoriesUsecase(categories_gateway)
    sections_service = SectionsUsecase(sections_gateway)

    return items_service, categories_service, sections_service


items_service, categories_service, sections_service = get_services(BASE_URL)


# ============================================================
#   CACHED DATA
# ============================================================

@st.cache_data
def get_items():
    return items_service.list_items()

@st.cache_data
def get_categories():
    return categories_service.list_categories()

@st.cache_data
def get_sections():
    return sections_service.list_sections()

def refresh_cache():
    st.cache_data.clear()


# ============================================================
#   TITLE
# ============================================================

st.title("📦 Warehouse Dashboard")
st.write("Manage Items, Categories and Sections")

# ============================================================
#   TABS
# ============================================================

tab_items, tab_categories, tab_sections = st.tabs(
    ["📦 Items", "🏷️ Categories", "📁 Sections"]
)

# ============================================================
#   TAB ITEMS
# ============================================================

with tab_items:
    st.header("Items Inventory")

    # BACKEND DATA (cacheadas)
    items = get_items()
    categories = get_categories()
    sections = get_sections()


    # METRICS
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Items", len(items))
    col2.metric("Categories", len(categories))
    col3.metric("Sections", len(sections))


    # TABLE ITEMS
    st.subheader("Item List")
    st.dataframe(items, use_container_width=True)


    # CREATE ITEM
    st.subheader("➕ Create Item")
    with st.form("create_item_form"):
        c1, c2 = st.columns(2)
        with c1:
            name = st.text_input("Item Name")
            # Dropdown para categorías
            category_options = [cat["name"] for cat in get_categories()]
            category_name = st.selectbox("Category", options=category_options)
            price = st.number_input("Price", min_value=0.0, format="%.2f")
        with c2:
            # Dropdown para secciones
            section_options = [sec["code"] for sec in get_sections()]
            section_code = st.selectbox("Section", options=section_options)
            quantity = st.number_input("Quantity", min_value=0)

        submit_item = st.form_submit_button("Create Item")

        if submit_item:
            data = {
                "name": name,
                "category_name": category_name,
                "section_code": section_code,
                "quantity": quantity,
                "price": price,
            }
            try:
                items_service.add_item(data)
                st.success("Item created successfully")
                refresh_cache()
                st.rerun()
            except Exception:
                st.error("Failed to create item. Please check your input.")


    # SEARCH ITEM
    st.subheader("🔎 Search Item")
    search_q = st.text_input("Search by name")

    if st.button("Search"):
        if search_q.strip():
            try:
                result = items_service.get_item(search_q.strip())
                st.table(result)
            except Exception:
                st.error("Item not found or something went wrong.")
        else:
            st.info("Please enter a search term.")


    # MODIFY ITEM 
    st.subheader("✏️ Modify Item")

    modify_name = st.text_input("Item name to modify")

    if st.button("Load item"):
        if modify_name.strip():
            try:
                item = items_service.get_item(modify_name.strip())
                st.session_state["item_to_modify"] = item
                st.success("Item loaded. Now modify fields.")
            except Exception:
                st.error("Item not found or something went wrong.")
        else:
            st.info("Enter a name.")

    # If an item was loaded → show editable form
    if "item_to_modify" in st.session_state:

        item = st.session_state["item_to_modify"]

        new_name = st.text_input("Name", value=item["name"])
        new_price = st.number_input("Price", value=item["price"])
        new_category = st.text_input("Category name", value=item["category_name"])
        new_section = st.text_input("Section code", value=item["section_code"])

        if st.button("Save changes"):
            update_payload = {
                "name": new_name,
                "price": new_price,
                "category_name": new_category,
                "section_code": new_section
            }

            try:
                updated = items_service.modify_item(item["name"], update_payload)
                st.success("Item updated successfully!")
                st.table(updated)
                st.cache_data.clear()
                st.rerun()
            except Exception:
                st.error("Failed to update item. Check your input.")


    # DELETE ITEM
    st.subheader("🗑️ Delete Item")
    item_name_delete = st.text_input("Item Name to Delete")

    if st.button("Delete Item"):
        if item_name_delete.strip():
            try:
                items_service.remove_item(item_name_delete.strip())
                st.success("Item removed")
                refresh_cache()
                st.rerun()
            except Exception:
                st.error("Item not found or something went wrong.")
        else:
            st.info("Please enter an item name.")


# ============================================================
#   TAB CATEGORIES
# ============================================================

with tab_categories:
    st.header("Categories")

    categories = get_categories()
    st.dataframe(categories, use_container_width=True)

    st.subheader("➕ Create Category")
    with st.form("create_category_form"):
        name = st.text_input("Category Name")

        submit_cat = st.form_submit_button("Create Category")
        if submit_cat:
            try:
                categories_service.add_category({"name": name})
                st.success("Category created")
                refresh_cache()
                st.rerun()
            except Exception as e:
                st.error(e)


# ============================================================
#   TAB SECTIONS
# ============================================================

with tab_sections:
    st.header("Sections")

    sections = get_sections()
    st.dataframe(sections, use_container_width=True)

    st.subheader("➕ Create Section")
    with st.form("create_section_form"):
        code = st.text_input("Section Code")

        submit_sec = st.form_submit_button("Create Section")
        if submit_sec:
            try:
                sections_service.add_section({"code": code})
                st.success("Section created")
                refresh_cache()
                st.rerun()
            except Exception as e:
                st.error(e)

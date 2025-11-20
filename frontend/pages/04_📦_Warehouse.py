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

# Initialize gateways
items_gateway = ItemsGateway(BASE_URL)
categories_gateway = CategoriesGateway(BASE_URL)
sections_gateway = SectionsGateway(BASE_URL)

# Initialize usecases
items_uc = ItemsUsecase(items_gateway)
categories_uc = CategoriesUsecase(categories_gateway)
sections_uc = SectionsUsecase(sections_gateway)


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

    # BACKEND DATA
    items = items_uc.list_items()
    categories = categories_uc.list_categories()
    sections = sections_uc.list_sections()

    # METRICS
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Items", len(items))
    col2.metric("Categories", len(categories))
    col3.metric("Sections", len(sections))

    # TABLE ITEMS
    st.subheader("Item List")
    st.dataframe(items, width='stretch')

    # CREATE ITEM
    st.subheader("➕ Create Item")
    with st.form("create_item_form"):
        c1, c2 = st.columns(2)
        with c1:
            name = st.text_input("Item Name")
            category_name = st.text_input("Category Name")
        with c2:
            section_code = st.text_input("Section Code")
            quantity = st.number_input("Quantity", min_value=0)

        submit_item = st.form_submit_button("Create Item")

        if submit_item:
            data = {
                "name": name,
                "category_name": category_name,
                "section_code": section_code,
                "quantity": quantity,
            }
            try:
                items_uc.add_item(data)
                st.success("Item created successfully")
                st.rerun()
            except Exception as e:
                st.error(e)
                
                
    # SEARCH ITEM
    st.subheader("🔎 Search Item")
    search_q = st.text_input("Search by name")

    if st.button("Search"):
        if search_q.strip():
            try:
                search_results = items_uc.get_item(search_q.strip())

                if search_results:
                    st.table(search_results)
                else:
                    st.info("No items found.")

            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.info("Please enter a search term.")

    
    """     
    # EDIT ITEM 
    st.subheader("✏️ Edit Item")

    all_items = items_uc.list_items()
    if not all_items:
        st.info("No items available to edit.")
    else:
        # dropdown shows "id - name"
        options = {f'{it["id"]} - {it["name"]}': it["id"] for it in all_items}
        sel_label = st.selectbox("Select item to edit", options=list(options.keys()))
        selected_id = options[sel_label]

        # load current values
        current = next((it for it in all_items if it["id"] == selected_id), None)
        if current:
            with st.form("edit_item"):
                e1, e2 = st.columns(2)
                with e1:
                    new_name = st.text_input("Name", value=current.get("name",""))
                    new_category = st.text_input("Category", value=current.get("category_name",""))
                with e2:
                    new_section = st.text_input("Section", value=current.get("section_code",""))
                    new_qty = st.number_input("Quantity", min_value=0, value=int(current.get("quantity",0)))
                save = st.form_submit_button("Save changes")
                if save:
                    update_payload = {
                        "name": new_name,
                        "category_name": new_category,
                        "section_code": new_section,
                        "quantity": new_qty,
                    }
                    try:
                        items_uc.modify_item(selected_id, update_payload)
                        st.success("Item updated.")
                        st.rerun()
                    except Exception as e:
                        st.error(f"Update failed: {e}")
    """

    # DELETE ITEM
    st.subheader("🗑️ Delete Item")
    item_id_delete = st.number_input("Item ID", min_value=1, step=1)
    if st.button("Delete Item"):
        try:
            items_uc.remove_item(item_id_delete)
            st.success("Item removed")
            st.rerun()
        except Exception as e:
            st.error(e)


# ============================================================
#   TAB CATEGORIES
# ============================================================

with tab_categories:
    st.header("Categories")

    categories = categories_uc.list_categories()
    st.dataframe(categories, width='stretch')

    st.subheader("➕ Create Category")
    with st.form("create_category_form"):
        name = st.text_input("Category Name")

        submit_cat = st.form_submit_button("Create Category")
        if submit_cat:
            try:
                categories_uc.add_category({"name": name})
                st.success("Category created")
                st.rerun()
            except Exception as e:
                st.error(e)


# ============================================================
#   TAB SECTIONS
# ============================================================

with tab_sections:
    st.header("Sections")

    sections = sections_uc.list_sections()
    st.dataframe(sections, width='stretch')

    st.subheader("➕ Create Section")
    with st.form("create_section_form"):
        code = st.text_input("Section Code")

        submit_sec = st.form_submit_button("Create Section")
        if submit_sec:
            try:
                sections_uc.add_section({"code": code})
                st.success("Section created")
                st.rerun()
            except Exception as e:
                st.error(e)
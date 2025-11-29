import streamlit as st
import pandas as pd
import io


@st.cache_data
def file_converter(file):
    # Detectar extensión
    if file.name.endswith(".xlsx"):
        excel_file = pd.read_excel(file, engine="openpyxl")
    else:
        excel_file = pd.read_excel(file)
    
    csv_file = excel_file.to_csv(index=False).encode('utf-8')
    return csv_file


st.set_page_config(
    page_title=" Excel Converter",
    page_icon="📄",
    )

st.title("📄 Excel to CSV Converter")

uploaded_file = st.file_uploader("Upload an Excel file", type=["xls", "xlsx"])

if uploaded_file:
    try:
        st.success(f"File '{uploaded_file.name}' uploaded successfully!")
        
    except:
        st.error("An error ocurred, maybe the file type its not correct")
        

    
    if st.button("Convert to CSV"):
        
        try:
            csv = file_converter(uploaded_file)
            file_preview = pd.read_csv(io.BytesIO(csv))
            st.write("✅ File Preview:")
            st.dataframe(file_preview.head())

            
            st.download_button(
                label="⬇️ Download CSV file",
                data=csv,
                file_name=uploaded_file.name.replace(".xlsx", ".csv").replace(".xls", ".csv"),
                mime="text/csv"
            )
            
        except:
            st.error("An error has ocurred")
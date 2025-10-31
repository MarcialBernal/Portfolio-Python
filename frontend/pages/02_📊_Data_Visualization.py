import streamlit as st
import pandas as pd
from services.data_visual import Plots

st.set_page_config(
    page_title="Data Visualization", 
    page_icon="📊",
    layout= "wide",
    )

st.markdown("# 📊 Data Visualization")
st.sidebar.header("Processed Data")

with st.expander("Introduction", expanded=True):
    st.markdown("""
                A dashboard built with Python, Pandas, Plotly, and Streamlit to demonstrate practical data visualization and analysis skills.
                The application processes uploaded DataFrames, allowing users to explore data through multiple visualization types and customizable parameters.
                It showcases proficiency in data manipulation, interactive plotting, and front-end integration for analytical tools.
                
                
                Developed to illustrate my ability to build user-driven, data-centric interfaces that combine clarity, interactivity, and functionality.
                """)
    
try:
    test_df = pd.read_csv('data/Mental_Health_and_Social_Media_Balance_Dataset.csv')
    st.success(f"Test data set uploaded successfully!")
    plot = Plots()
    
    with st.container():
        col1, col2 = st.columns(2)
        
        with col1:
            plot.pie_plot(
                test_df, 
                names_col='Social_Media_Platform', 
                title='Average User Social Media Platform'
            )
            
        with col2:
            plot.bar_plot(
                test_df, 
                values_col='Happiness_Index(1-10)', 
                names_col='Social_Media_Platform', 
                title='Average Happiness by Social Media Platform'
            )
    
except:
        st.error("An error has ocurred")





# Interactive plots
uploaded_file = st.file_uploader("Upload an CSV file", type=["csv"])

if uploaded_file:
    try:
        st.success(f"File '{uploaded_file.name}' uploaded successfully!")
        
    except:
        st.error("An error has ocurred, maybe the file type its not correct")



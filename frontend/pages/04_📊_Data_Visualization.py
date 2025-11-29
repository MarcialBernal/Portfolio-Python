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
                x_col='Social_Media_Platform', 
                title='Average User Social Media Platform'
            )
            
        with col2:
            plot.bar_plot(
                test_df, 
                y_col='Happiness_Index(1-10)', 
                x_col='Social_Media_Platform', 
                title='Average Happiness by Social Media Platform'
            )
            
    with st.container():
        col1, col2 = st.columns(2)
        
        with col1:
            plot.line_plot(
                test_df, 
                x_col='Days_Without_Social_Media', 
                y_col='Sleep_Quality(1-10)', 
                title='Average Sleep Quality vs Days Without Social Media'
                )
            
        with col2:
            plot.screen_vs_sleep_plot(
                test_df,
                x_col='Daily_Screen_Time(hrs)',
                y_col='Sleep_Quality(1-10)',
                size_col='Happiness_Index(1-10)',
                color_col='Social_Media_Platform',
                title="Daily Screen Time vs Sleep Quality"
            )
except:
        st.error("An error has ocurred")





# Interactive plots
uploaded_file = st.file_uploader("Upload an CSV file", type=["csv"])

if uploaded_file:
    try:
        st.success(f"File '{uploaded_file.name}' uploaded successfully!")
        df = pd.read_csv(uploaded_file)
        
        plot_type= st.selectbox("Select chart type", ["Pie", "Bar", "Line"])
        col1 = st.selectbox("Select first column", df.columns)
        col2 = None
        if plot_type in ["Bar", "Line"]:
            col2 = st.selectbox("Select second column", df.columns)
            
        if st.button("Update Chart"):
            plot.interactive_plot(df, plot_type, col1, col2)

    except:
        st.error("An error has ocurred, maybe the file type its not correct")



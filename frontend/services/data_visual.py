import streamlit as st 
import plotly.express as px

class Plots:
    def __init__(self):
        pass

    def pie_plot(self, df, names_col="Social_Media_Platform", title="Pie Chart"):
        counts = df.groupby(names_col).size().reset_index(name="User_Count")
        fig = px.pie(counts, values="User_Count", names=names_col, title=title)
        st.plotly_chart(fig)

    def bar_plot(self, df, values_col, names_col, title="Bar Chart"):
        df = df.groupby(names_col)[values_col].mean().reset_index()
        fig = px.bar(df, x=names_col, y=values_col, title=title, color=names_col)
        st.plotly_chart(fig)


    def line_plot(self, df, x_col, y_col, title="Line Chart"):
        fig = px.line(df, x=x_col, y=y_col, title=title)
        st.plotly_chart(fig)
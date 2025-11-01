import streamlit as st 
import plotly.express as px 
import pandas as pd

class Plots:
    def __init__(self):
        pass
#######
    def pie_plot(self, df, x_col, title="Pie Chart"):
        counts = df.groupby(x_col).size().reset_index(name="User_Count")
        fig = px.pie(counts, values="User_Count", names=x_col, title=title)
        st.plotly_chart(fig)

#######
    def bar_plot(self, df, y_col, x_col, title="Bar Chart"):
        if pd.api.types.is_numeric_dtype(df[y_col]):
            df = df.groupby(x_col)[y_col].mean().reset_index()
        else:
            df = df.groupby(x_col).size().reset_index(name=y_col)

        fig = px.bar(df, x=x_col, y=y_col, color=x_col, title=title)
        st.plotly_chart(fig)

#######
    def line_plot(self, df, x_col, y_col, title="Line Chart"):
        df[x_col] = pd.to_numeric(df[x_col], errors='coerce')
        df[y_col] = pd.to_numeric(df[y_col], errors='coerce')
        df_clean = df.dropna(subset=[x_col, y_col])

        if df_clean.empty:
            st.warning("No valid numeric data to plot the line chart.")
            return
        
        df_grouped = df_clean.groupby(x_col, as_index=False)[y_col].mean()
        fig = px.line(df_grouped, x=x_col, y=y_col, markers=True, title=title)
        st.plotly_chart(fig)
    
#######    
    def screen_vs_sleep_plot(self, df, x_col, y_col, size_col, color_col, title="Scatter Chart"):
        fig = px.scatter(
            df,
            x=x_col,
            y=y_col,
            size=size_col,
            color=color_col,
            hover_data=[size_col, color_col, 'Gender'],
            title=title,
            size_max=40)
        st.plotly_chart(fig)
    
#######        
    def interactive_plot(self, df, plot_type, col1, col2):
        plot_map = {
            "Pie": self.pie_plot,
            "Bar": self.bar_plot,
            "Line": self.line_plot
        }

        plot = plot_map.get(plot_type)
        if not plot:
            raise ValueError(f"Plot type '{plot_type}' not recognized")

        params = {}
        if plot_type == "Pie":
            params = {"x_col": col1}
        elif plot_type in ["Bar", "Line"]:
            params = {"x_col": col1, "y_col": col2}

        plot(df, **params)
            
    
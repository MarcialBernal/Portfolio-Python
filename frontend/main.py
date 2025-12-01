import streamlit as st 
from dotenv import load_dotenv

load_dotenv()


def main():
    st.set_page_config(
    page_title="Marcial Bernal",
    page_icon="🌮",
    )
    
    st.sidebar.success("Select a project above.")

    st.write("# Marcial Bernal 💻🐍")
    
    st.subheader("🙋‍♂️ Welcome")
    st.markdown("""
            👋 Hello, and thank you for visiting my portfolio!
                Here you’ll find a variety of Python projects, 
                ranging from Machine Learning and Data Science — including data visualization, DataFrame manipulation, and analytics — to practical tools 
                like web scrapers, file converters, and chatbots.
                
                This space represents my continuous journey of 
                learning and building useful, creative, and efficient solutions 
                that make everyday tasks simpler and smarter 🚀.
            """)
    
    st.write("#### 🍳 About Me")
    st.write('''
                Before diving into code, I spent 10 years as a chef from Mexico 🌵, a career that taught me creativity, precision, and passion for the details.
                Today, I bring that same energy to programming — I’ve been developing personal projects and building useful tools 
                for the construction company where I currently work for the past two years.

                The 🌮(taco) in my logo isn’t random — it’s a small nod to my roots in the kitchen and my approach to coding: a blend of technique, flavor, and constant experimentation.
             ''')
    
    
    

if __name__ == "__main__":
    main()
import streamlit as st
import pandas as pd
import numpy as np
import streamlit as st
st.set_page_config(layout="wide")
with open("style.css", "r", encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

with open("index.html") as f:
    html = f.read()
def Test():
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    col1,col2=st.columns(2)
    with col1:
        st.line_chart(chart_data)
    with col2:
        st.line_chart(chart_data)

    st.dataframe(chart_data,hide_index=True)


class NavBar:
    def Navbar_Design(self):        
        st.markdown(html, unsafe_allow_html=True)
        col1,col2,col3,col4,col5,col6=st.columns([0.1,0.2,0.2,0.2,0.2,0.1])
        with col2:
            Sales_button=st.button('Sales',key='Sales')
        with col3:
            Purchase_button=st.button('Purchase',key='Purchase')
        if Purchase_button:
            return Test()
NavBar().Navbar_Design()



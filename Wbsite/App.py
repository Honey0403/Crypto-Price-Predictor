# import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
import pandas as pd
# import pickle
# from streamlit_lottie import st_lottie
# import base64
from streamlit_extras.dataframe_explorer import dataframe_explorer
from PIL import Image

from streamlit_extras.customize_running import center_running
import time

st.title("Crypto Price Predictor")



chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.bar_chart(chart_data)

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.line_chart(chart_data)

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.area_chart(chart_data)

Bitcoin = pd.read_csv('Bitcoin.csv')
Bitcoin1 = dataframe_explorer(Bitcoin,case=False)
st.dataframe(Bitcoin1, use_container_width=True)

def example():
    click = st.button("Observe where the 🏃‍♂️ running widget is now!")
    if click:
        center_running()
        time.sleep(2)

example()


# def main_page():
#     st.markdown("# Main page ")
#     st.sidebar.markdown("# Main page 🎈")

# def page2():
#     st.markdown("Bitcoin")
#     st.sidebar.markdown("Bitcoin")

# def page3():
#     st.markdown("Etherium")
#     st.sidebar.markdown("Etherium")


# def page4():
#     st.markdown("Neocoin")
#     st.sidebar.markdown("Neocoin")


# page_names_to_funcs = {
#     "Home Page": main_page,
#     "Bitcoin": page2,
#     "Etherium": page3,
#     "Neocoin" : page4
# }

# selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
# page_names_to_funcs[selected_page]()

   

import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [52.52, 13.4050],
    columns=['lat', 'lon'])

st.map(df)


"#### Contact Developer"

st.markdown("Programmed with ❤️ by [Muhammad Ahsan](https://www.linkedin.com/in/muhammad-ahsan/)")

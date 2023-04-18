import streamlit as st # import streamlit
import seaborn as sns # import seaborn
import pandas as pd # import pandas
diamonds=sns.load_dataset('diamonds')  # load dataset
st.write(diamonds.head()) # write dataset
# describe dataset
st.write(diamonds.describe())
# plot dataset
st.write(sns.pairplot(diamonds))

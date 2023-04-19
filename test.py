# I need a website and automation of work with product descriptions in streamlit
import streamlit as st
import pandas as pd
import numpy as np
import time
import os
import re
import requests
import json
import csv
import datetime
import time
import sys
data=np.random.randn(10,2)
st.write(data.shape)
st.line_chart(data[:,0])
st.bar_chart(data[:,0])
st.write(len(data))
selectbox=st.sidebar.selectbox('Select',('1','2','3'))
st.write(selectbox)
sidebar=st.sidebar.slider('Select',0,10)
st.write(sidebar)
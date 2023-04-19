import streamlit as st
import re
st.title('Product Description Automation')

product_name = st.text_input('Product Name:')
product_description = st.textarea('Product Description:')
pattern = r'\b([A-Z][a-z]+(?: [A-Z][a-z]+)*)\b'
matches = re.findall(pattern, product_description)
results = ', '.join(matches)
if st.button('Process'):
    st.write(f'Product Name: {product_name}')
    st.write(f'Results: {results}')
if __name__ == '__main__':
    st.set_page_config(page_title='Product Description Automation')


import streamlit as st
from pdfRead import extract_details
from app import main_function
import shutil, os

st.title('Jupyter Notebook Summarizer')
st.write('Studies visualization and code to give accurate summary along with the insights from Jupyter Notebook')
file_upload = st.file_uploader('Choose a file', type=['pdf'])

summary_button = st.button('Summarize')
if summary_button:
    if file_upload:
        if os.path.exists('Images/'):
            shutil.rmtree('Images/')
        extract_details(file_upload)
        lines_of_code = len(open(f'output.txt', encoding='UTF-8').readlines())
        total_images = len(os.listdir('Images'))
        st.markdown(f'''**Extraction results**\n
        Lines of code/text:  {lines_of_code}\n\tImages/visualizations:  {total_images} 
        ''')
        with st.spinner():
            print("------------------------------------------------------")
            response = main_function()
            response = response.replace('*','')
            st.text_area('Code Summary',response, height= 250, label_visibility='collapsed')

    else: st.write('Please upload a file!')

# Jupyter Notebook Summary

This Jupyter Notebook Summarizer is designed to provide concise and insightful summaries of Jupyter notebooks, including both textual content and visualizations. It extracts text and images from PDF files, typically containing Jupyter notebook content, and processes them to generate summaries.

## Setup Instructions

1. *Requirements* : Ensure you have the necessary Python libraries installed. You can install them using pip:
   `pip install requirements.txt`
2. *Environment Variables* : You need to set up your OpenAI API key. You can either set it as an environment variable or directly provide it in the code.
3. *File Upload*: Upload a PDF file containing the Jupyter notebook content.
4. *Summarization*: Click on the "Summarize" button to initiate the summarization process.

# How It Works
The summarization process involves the following steps:

1. *Text Extraction*: The tool extracts text content from each page of the PDF file, preserving the structure of the Jupyter notebook.
2. *Image Extraction*: Images/visualizations embedded within the PDF are also extracted and saved separately.
3. *Summarization*: The extracted text and images are analyzed to generate a concise summary of the Jupyter notebook content. The tool utilizes OpenAI's GPT-3.5 model for natural language processing.
4. *Insights Generation*: For images/visualizations, the tool generates insights by analyzing the content and context of each image. This includes identifying visualization types, extracting numerical data, and providing descriptive summaries.

#Note
The input jupyter notebook for the summary should be present in the local directory of codebase
   



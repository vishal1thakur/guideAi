from flask import request, jsonify
from api import api as blueprint
import openai
import os
import PyPDF2

openai.api_key = os.getenv("OPENAI_API_KEY")

def load_pdf(file_path):
    # Open the PDF file
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        
        # Extract text from each page
        document_text = ''
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            document_text += page.extractText()
            
    return document_text
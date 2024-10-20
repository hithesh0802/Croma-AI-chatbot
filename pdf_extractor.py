import re
import pdfplumber

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text

def clean_pdf_text(text):
    # Cleaning extracted text from the PDF
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'\d+', '', text)  # Remove numbers
    text = re.sub(r'[^A-Za-z,. ]+', ' ', text)  # Keep only letters and punctuation
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def extract_sections(pdf_text):
    # Extract sections such as header, subject, content, etc.
    sections = {}

    # Example for extracting header and content
    header_pattern = r"(\w+ \d{1,2}, \d{4})\nTo,\n(.*?)\n\n"
    header_match = re.search(header_pattern, pdf_text, re.DOTALL)
    if header_match:
        sections['header'] = {
            'date': header_match.group(1),
            'recipient': header_match.group(2).replace("\n", " ")
        }

    # Add more regex patterns for other sections as needed

    return {'sections': sections, 'pdf_text': pdf_text}

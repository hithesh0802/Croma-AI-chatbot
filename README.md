Croma Competitive Intelligence Chatbot:
This project implements a competitive intelligence chatbot for Croma, designed to analyze and compare business strategies, performance, and market positioning of competitors like Reliance Digital and Vijay Sales. The chatbot leverages advanced NLP models to provide insights from various sources including investor presentations, media reports, and annual reports.

Project Overview
The chatbot performs:

Text Analysis using BERT for extracting relevant business information.
Text Summarization and Comparisons using T5 for generating concise, human-readable insights.
Web scraping for extracting and processing data from PDFs, CSV files, and other external data sources.

LIVE CHATBOT URL:
Access the chatbot here:  https://croma-ai-chatbot.onrender.com/

Features
Compare competitor marketing strategies, business models, customer segments, and more.
Summarize key differentiators from financial reports and market analysis.
Provide actionable insights based on the latest data.

Technical Stack:
Frontend : Dialogflow, Google Cloud Platform.
Backend : Flask (for webhook), Ngrok (for testing),pdfplumber,BeautifulSoup(for web scraping).
Data Sources : Publicly available data (annual reports, investor presentations, etc.).
Machine Learning Models : 
BERT : Fine-tuned to generate concise, task-specific summaries and responses for competitive strategy comparisons.
T5 : Contextual text extraction and understanding, enabling accurate competitor intelligence analysis.
Deployment: Render

Installation
Clone the repository:

bash
Copy code
git clone https://github.com/username/croma-chatbot.git
cd croma-chatbot
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the Flask app:

bash
Copy code
python app.py
Access the app locally:

arduino
Copy code
http://127.0.0.1:5000/

Usage
Navigate to the provided chatbot URL.
Input queries related to business strategy comparisons, performance analysis, or customer trends.
Receive concise, data-driven responses comparing companies like Reliance Digital, Vijay Sales, and others.
Contributing
Please create an issue or pull request for any bug fixes or feature requests.

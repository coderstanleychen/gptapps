from flask import Flask, render_template, request, jsonify
import os
from pathlib import Path
from llama_index import download_loader
from llama_index import GPTSimpleVectorIndex

os.environ['OPENAI_API_KEY'] = "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"

app = Flask(__name__)

# Load PDF data and create the index
CJKPDFReader = download_loader("CJKPDFReader")
loader = CJKPDFReader()
pdfDocuments = loader.load_data(file=Path('./pdf/The Little Book of OAuth 2.0 RFCs.pdf'))
pdf_index = GPTSimpleVectorIndex.from_documents(pdfDocuments)

# Define the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define the query page
@app.route('/query', methods=['POST'])
def query():
    query_text = request.form['user_input']
    print(query_text)
    response = pdf_index.query(query_text)
    print(response)
    return str(response)
    #return render_template('result.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)

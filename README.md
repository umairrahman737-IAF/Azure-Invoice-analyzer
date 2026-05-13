# Azure-Invoice-analyzer
An AI-powered Invoice OCR web application built with Streamlit and Azure AI Vision.
This app extracts printed and handwritten text from invoice images and automatically identifies important details such as:  
    -💰 Invoice Amount
    -📅 Invoice Date
    -🧾 Invoice Number
    
🚀 Features
    -Upload invoice images (jpg, jpeg, png)
    -OCR using Azure AI Vision
    -Extract printed & handwritten text
    -Smart data extraction using Regex
    -Download extracted text as .txt
    -Clean and responsive Streamlit UI
🛠️ Tech Stack
    -Python
    -Streamlit
    -Azure AI Vision
    -Pillow (PIL)
    -Regex
📂 Project Structure
    .
    ├── exp8.py
    ├── README.md
⚙️ Installation
1️⃣ Clone the Repository
    -git clone https://github.com/your-username/invoice-analyzer.git
    -cd invoice-analyzer
2️⃣ Create Virtual Environment (Optional)
    -python -m venv venv

Activate environment:
Windows
    -venv\Scripts\activate
Linux / Mac
    -source venv/bin/activate
    
📦 Install Dependencies
    -pip install streamlit azure-ai-vision-imageanalysis pillow
    
🔑 Configure Azure AI Vision

Open the Python file and replace:
    -ENDPOINT = "AZURE_ENDPOINT_HERE"
    -KEY = "AZURE_KEY_HERE"

with your actual Azure AI Vision credentials.
You can get them from:
    -Azure Portal
    -Azure AI Vision Service
    
▶️ Run the Application
    -streamlit run exp8.py
    
🖼️ Application Preview
Features Included
    -Invoice image preview
    -OCR text extraction
    -Amount detection
    -Date extraction
    -Invoice number detection
    -Download extracted text

📥 Supported File Formats
    -JPG
    -JPEG
    -PNG
    
🧠 How It Works
    -User uploads invoice image
    -Azure OCR analyzes image
    -Extracted text is displayed
    -Regex identifies key invoice details
    -User can download extracted text
    
🔮 Future Improvements
    -PDF invoice support
    -Multiple invoice upload
    -Export to Excel/CSV
    -Database integration
    -Better invoice field detection using AI
    
👨‍💻 Author
    -Built using Azure AI Vision + Streamlit

📜 License
    -This project is open-source and available under the MIT License.



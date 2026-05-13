# Azure-Invoice-analyzer

An AI-powered Invoice OCR web application built with Streamlit and Azure AI Vision.

This app extracts printed and handwritten text from invoice images and automatically identifies important details such as:

- 💰 Invoice Amount
- 📅 Invoice Date
- 🧾 Invoice Number

---

## 🚀 Features

- Upload invoice images (jpg, jpeg, png)
- OCR using Azure AI Vision
- Extract printed & handwritten text
- Smart data extraction using Regex
- Download extracted text as `.txt`
- Clean and responsive Streamlit UI

---

## 🛠 Tech Stack

- Python
- Streamlit
- Azure AI Vision
- Pillow (PIL)
- Regex

---

## 📁 Project Structure

```bash
invoice-analyzer/
│── exp8.py
│── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/invoice-analyzer.git
cd invoice-analyzer
```

### 2. Create Virtual Environment (Optional)

```bash
python -m venv venv
```

### 3. Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install streamlit azure-ai-vision-imageanalysis pillow
```

---

## 🔑 Configure Azure AI Vision

Open the Python file and replace:

```python
ENDPOINT = "AZURE_ENDPOINT_HERE"
KEY = "AZURE_KEY_HERE"
```

with your actual Azure AI Vision credentials.

You can get them from:

- Azure Portal
- Azure AI Vision Service

---

## ▶️ Run the Application

```bash
streamlit run exp8.py
```

---

## 🖼 Application Preview Features Included

- Invoice image preview
- OCR text extraction
- Amount detection
- Date extraction
- Invoice number detection
- Download extracted text

---

## 📂 Supported File Formats

- JPG
- JPEG
- PNG

---

## 🧠 How It Works

1. User uploads invoice image
2. Azure OCR analyzes image
3. Extracted text is displayed
4. Regex identifies key invoice details
5. User can download extracted text

---

## 🚀 Future Improvements

- PDF invoice support
- Multiple invoice upload
- Export to Excel/CSV
- Database integration
- Better invoice field detection using AI

---

## 👨‍💻 Author

Built using Azure AI Vision + Streamlit

---

## 📜 License

This project is open-source and available under the MIT License.

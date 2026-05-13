import streamlit as st
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential
from PIL import Image
import io
import re

# =========================
# 🔑 CONFIG (PUT YOUR KEYS)
# =========================
ENDPOINT = "AZURE_ENDPOINT_HERE"
KEY = "AZURE_KEY_HERE"

# =========================
# 🎨 UI DESIGN
# =========================
st.set_page_config(page_title="Invoice OCR", layout="wide")

st.markdown("""
    <h1 style='text-align: center; color: #4CAF50;'>📄 Invoice  Analyzer</h1>
    <p style='text-align: center;'>Extract printed & handwritten text using Azure OCR</p>
""", unsafe_allow_html=True)

# Upload section
st.sidebar.header("📤 Upload Invoice")
uploaded_file = st.sidebar.file_uploader("Choose an image", type=["jpg", "png", "jpeg"])

# =========================
# 🔌 Azure Client
# =========================
client = ImageAnalysisClient(
    endpoint=ENDPOINT,
    credential=AzureKeyCredential(KEY)
)

# =========================
# 🖼️ MAIN UI
# =========================
if uploaded_file:
    col1, col2 = st.columns(2)

    # 📷 Image Preview
    with col1:
        st.subheader("🖼️ Uploaded Invoice")
        image = Image.open(uploaded_file)
        st.image(image, use_column_width=True)

    # 🧠 OCR Processing
    with col2:
        st.subheader("📝 Extracted Text")

        uploaded_file.seek(0)
        image_bytes = uploaded_file.read()

        result = client.analyze(
            image_data=image_bytes,
            visual_features=[VisualFeatures.READ]
        )

        extracted_text = ""
        for block in result.read.blocks:
            for line in block.lines:
                extracted_text += line.text + "\n"

        st.text_area("OCR Output", extracted_text, height=300)

        # =========================
        # 🔍 Smart Data Extraction
        # =========================
        st.subheader("📊 Key Information")

        amount = re.findall(r"\$\d+\.\d+|\d+\.\d{2}", extracted_text)
        date = re.findall(r"\d{2}/\d{2}/\d{4}", extracted_text)
        invoice_no = re.findall(r"Invoice\s*No[:\-]?\s*\d+", extracted_text, re.IGNORECASE)

        colA, colB, colC = st.columns(3)

        with colA:
            st.metric("💰 Amount", amount[0] if amount else "Not Found")

        with colB:
            st.metric("📅 Date", date[0] if date else "Not Found")

        with colC:
            st.metric("🧾 Invoice No", invoice_no[0] if invoice_no else "Not Found")

        # =========================
        # ⬇️ Download Option
        # =========================
        st.download_button(
            label="⬇️ Download Text",
            data=extracted_text,
            file_name="invoice_text.txt",
            mime="text/plain"
        )

else:
    st.info("👈 Upload an invoice image to start OCR")

# =========================
# 🎨 FOOTER
# =========================
st.markdown("---")
st.markdown("<p style='text-align:center;'>Built using Azure AI Vision + Streamlit</p>", unsafe_allow_html=True)
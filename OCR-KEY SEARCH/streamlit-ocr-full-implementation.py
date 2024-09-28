import streamlit as st
from transformers import AutoModel
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from PIL import Image
import numpy as np
import torch
import warnings
import re
import os

warnings.simplefilter("ignore")

hf_token = "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"
from PIL import Image
@st.cache_resource
def load_model():
    # Load tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained('ucaslcl/GOT-OCR2_0', trust_remote_code=True, use_auth_token=hf_token)
    model = AutoModel.from_pretrained('ucaslcl/GOT-OCR2_0', trust_remote_code=True, 
                                      low_cpu_mem_usage=True, 
                                      device_map='cuda' if torch.cuda.is_available() else 'cpu', 
                                      use_safetensors=True, 
                                      pad_token_id=tokenizer.eos_token_id, 
                                      use_auth_token=hf_token)
    model = model.eval()
    return tokenizer, model

tokenizer, model = load_model()

# Perform OCR function
def perform_ocr(image):
    # Convert the uploaded file to a PIL image
    pil_image = Image.open(image).convert('RGB')
    
    # Convert PIL image to numpy array
    image_np = np.array(pil_image)
    
    # Save the image temporarily
    image_file = "temp_image.png"
    Image.fromarray(image_np).save(image_file)
    
    # Perform OCR with the model
    with torch.no_grad():
        ocr_result = model.chat(tokenizer, image_file, ocr_type='ocr')
    
    # Remove the temporary image file
    os.remove(image_file)
    
    return ocr_result

# Function to highlight search term with a different color (e.g., light blue)
def highlight_text(text, query):
    # Use regex to wrap the search query with a span for styling
    pattern = re.compile(re.escape(query), re.IGNORECASE)
    highlighted_text = pattern.sub(f"<span style='background-color: #ADD8E6; color: black;'>{query}</span>", text)
    return highlighted_text

# Search functionality to search within OCR result, highlight, and return the modified text
def search_text(ocr_result, query):
    # If no query is provided, return the original OCR result
    if not query:
        return ocr_result, "No matches found."

    # Highlight the searched term in the OCR text
    highlighted_result = highlight_text(ocr_result, query)
    
    # Split OCR result into lines and search for the query
    lines = ocr_result.split('\n')
    matching_lines = [line for line in lines if query.lower() in line.lower()]
    
    if matching_lines:
        return highlighted_result, '\n'.join(matching_lines)  # Return highlighted text and matched lines
    else:
        return highlighted_result, "No matches found."

# Streamlit app
def main():
    st.title("OCR and Text Search App")

    # File uploader
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Perform OCR
        if st.button("Run OCR"):
            with st.spinner("Performing OCR..."):
                ocr_result = perform_ocr(uploaded_file)
            st.session_state.ocr_result = ocr_result
            st.success("OCR completed!")

        # Display OCR result if available
        if 'ocr_result' in st.session_state:
            st.subheader("OCR Result:")
            st.text_area("", st.session_state.ocr_result, height=200)

            # Search functionality
            search_query = st.text_input("Enter search term:")
            if search_query:
                highlighted_text, search_results = search_text(st.session_state.ocr_result, search_query)
                st.markdown(highlighted_text, unsafe_allow_html=True)
                st.subheader("Search Results:")
                st.write(search_results)

if __name__ == "__main__":
    main()


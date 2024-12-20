# OCR and Text Search App 📸🔍

This repository contains a **Streamlit-based application** that performs **Optical Character Recognition (OCR)** on uploaded images and enables users to **search** and **highlight** specific text within the extracted results.

## Features ✨
- **OCR**: Extracts text from uploaded images using the `ucaslcl/GOT-OCR2_0` model. 📝
- **Search**: Allows users to search for specific terms in the OCR results, highlighting matches. 🔎
- **Interactive UI**: Provides an easy-to-use interface for image uploading, OCR processing, and text search. 🖥️
- **Dynamic Text Highlighting**: Highlights search terms in the OCR results using a distinct color. 🎨

## Installation and Setup ⚙️

### Prerequisites 📋
- Python 3.8 or later 🐍
- Access to the **Hugging Face** model repository with a valid authentication token 🔑

### Steps to Install 🚀
1. **Clone the Repository**  
   ```bash
   git clone https://github.com/akhil-varsh/ocr-key-word-search.git
   cd ocr-key-word-search
   ```

2. **Install Dependencies**  
   Install the required Python packages listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Your Hugging Face Token**  
   Replace `REPLACE_YOUR_HF_TOKEN` in the code with your Hugging Face API token.  
   If you don’t have one, create an account at [Hugging Face](https://huggingface.co/) and generate an API token. 📝

4. **Run the App**  
   Launch the application with the following command:
   ```bash
   streamlit run app.py
   ```

## Usage 🛠️

1. **Upload an Image**  
   - Click the "Choose an image..." button to upload a `.jpg`, `.jpeg`, or `.png` file. 🖼️

2. **Run OCR**  
   - Click the "Run OCR" button to extract text from the uploaded image. ⚡

3. **Search Text**  
   - Enter a term in the search input field to highlight matches in the OCR result. 🔍
   - View all matched lines under "Search Results." 📑

4. **View OCR Output**  
   - Check the OCR results in the text area displayed below the "OCR Result" section. 💬

## File Structure 📂

```plaintext
ocr-key-search-app/
├── app.py              # Main Streamlit application code 💻
├── requirements.txt    # Python dependencies 📦
├── README.md           # Documentation for the project 📄
```

## Dependencies 📜

- **Streamlit**: For building the web interface. 🖥️
- **Transformers**: For accessing and running the GOT-OCR2_0 model. 🤖
- **Pillow**: For image handling. 🖼️
- **NumPy**: For image processing. 🔢
- **PyTorch**: Required by the OCR model for inference. ⚡

## Acknowledgments 🙏
- **Hugging Face**: Providing the `ucaslcl/GOT-OCR2_0` model. 🤝
- **Streamlit**: For making interactive web apps simple to build. 🏗️

## Future Improvements 🚀
- Add support for multi-language OCR. 🌍
- Include an option to download the OCR results as a text file. 💾
- Improve search functionality with regex support. 🔠
- Optimize performance for large images. 🚀

## License 📜
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 🔓

Feel free to contribute or raise issues to improve the app! 🌟

---

<p align="center">
  Made with ❤️ by Akhil
</p>


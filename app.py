import os
from dotenv import load_dotenv
import streamlit as st
from PIL import Image
import google.generativeai as genai
import logging
from datetime import datetime

# Load environment variables from a .env file
load_dotenv()

# Configure Google API key
google_api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=google_api_key)

# Initialize the generative model
model = genai.GenerativeModel('gemini-pro-vision')

# Configure logging
log_file = 'invoice_extractor.log'
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)

def get_gemini_response(input_text, image_data, prompt):
    """Generate a response using the Gemini Pro Vision model."""
    response = model.generate_content((input_text, image_data[0], prompt))
    return response.text

def input_image_setup(uploaded_file):
    """Process the uploaded image file."""
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Set Streamlit page configuration
st.set_page_config(page_title="Invoice Extractor")

# Streamlit UI components
st.header("Invoice Extractor")
input_prompt = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader('Choose an Invoice image...', type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

# Button to trigger the invoice analysis
submit = st.button("Tell me about the invoice")

# Default input prompt for the generative model
default_input_prompt = """
You are an expert in understanding invoices.
You will receive input images as invoices &
you will have to answer questions based on the input image
"""

if submit:
    try:
        # Record timestamp for image upload
        image_upload_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        logger.info(f"Image uploaded at {image_upload_time}")

        # Process the uploaded image
        image_data = input_image_setup(uploaded_file)
        
        # Record timestamp for user input prompt
        input_prompt_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        logger.info(f"User input prompt received at {input_prompt_time}: {input_prompt}")
        
        # Generate response using the generative model
        response = get_gemini_response(default_input_prompt, image_data, input_prompt)
        
        # Record timestamp for successful execution
        success_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        logger.info(f"Invoice analysis successful at {success_time}")
        
        # Log the generated response
        logger.info(f"Generated response: {response}")
        
        # Display the response
        st.subheader("The Response is")
        st.write(response)
        
    except Exception as e:
        # Record timestamp for errors
        error_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        logger.error(f"Error during invoice analysis at {error_time}: {e}")
        st.error("Error during invoice analysis. Please check the logs for details.")

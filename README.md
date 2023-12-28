# Invoice Extractor

This Streamlit application uses the Google Generative AI model (Gemini Pro Vision) to analyze invoice images. Users can upload an invoice image and provide an input prompt to receive information about the invoice from the generative model.

# Table of Contents

1. [Prerequisites](#prerequisites)
    - [Python >=3.10](https://www.python.org/)
    - [Streamlit](https://streamlit.io/)
    - [Google Generative AI](https://makersuite.google.com/app/apikey)

2. [Installation](#installation)
    1. [Clone the repository](#clone-the-repository)
    2. [Install the required dependencies](#install-the-required-dependencies)
    3. [Set up the environment variables](#set-up-the-environment-variables)

3. [Usage](#usage)
    - [Run the Streamlit application](#run-the-streamlit-application)

4. [Logging](#logging)
    - [Log events](#log-events)


## Prerequisites

Before running the application, ensure that you have the following installed:

- [Python >=3.10](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Google Generative AI](https://makersuite.google.com/app/apikey)

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/sandeepreddygantla/Invoice-Extractor-Project-with-LLM.git
   ```
## Install the required dependencies:
2. Install Required Libraries 
   ```
   pip install -r requirements.txt
   ```

## Set up the environment variables:
3. Create a .env file in the project root directory and add your Google API key:
   
   ```
   GOOGLE_API_KEY="your_api_key_here"
   ```
## Usage
4. Run the Streamlit application:

   ```
    streamlit run app.py
   ```
   
Upload an invoice image and enter an input prompt to analyze the invoice and receive a response.

## Logging
The application logs various events, including image upload, user input prompt, successful execution, errors, and the generated response. Log entries are stored in the invoice_extractor.log file.

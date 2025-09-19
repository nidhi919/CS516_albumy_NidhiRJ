# CS516 Homework 1

**Forked from:** [greyli/albumy](https://github.com/greyli/albumy)  
**Changes:** Added ML features for alternate text generation and image search.


---

## Project Overview

This project extends the Albumy web application by adding machine learning features.

- **Alt Text Generation:** Generates descriptive alternative text using the Azure Vision API if users do not provide their own descriptions.  
- **Object Detection in images & Image Search:** Detects objects in images, tags them, and tag-based search.

- **Alt text gen commit url:** https://github.com/nidhi919/CS516_albumy_NidhiRJ/commit/b7aa65e
- **Image search commit url:** https://github.com/nidhi919/CS516_albumy_NidhiRJ/commit/5c75da5

The application is built with **Python**, **Flask**, and **SQLAlchemy**, and relies on Azure Vision API for ML functionality.

---

## Prerequisites

- Python 3.9+  
- Azure Vision API subscription (key and endpoint)  

---

## Installation

1. **Clone the repository**

- git clone https://github.com/nidhi919/CS516_albumy_NidhiRJ.git
- cd CS516_albumy_NidhiRJ


2. **Create a virtual environment**
- for Windows:
  python -m venv venv
- for macOS/Linux:
  venv\Scripts\activate
- Then:
  source venv/bin/activate


3. **Install dependencies**
- pip install -r requirements.txt


4. **Configure Azure Vision API**
- Create an Azure Cognitive Services account if you don’t have one.
- Get your endpoint URL and API key.

5. **Create a file called .env in the root directory with the following content:**
- AZURE_VISION_KEY=your_api_key_here
- AZURE_VISION_ENDPOINT=your_endpoint_here

6. **Initialize the database**
- flask db upgrade


7. **Run the albumy application**
- flask run

8. **Open http://127.0.0.1:5000 in your browser**

# How to use it:

1. Upload images: Go to /upload and upload a photo.

2. View alt text: On the photo sidebar, along with the tags listed.

3. Search by tag: Use the search bar on the homepage to find images by detected tags of objects in uploaded image.


# Credits
- Original albumy project: greyli/albumy
- Azure vision API


CS516_albumy_NidhiRJ

Forked from greyli/albumy
.
This version includes ML-powered features:

Automatic alternative text generation for uploaded images using Azure Vision API.

Image search by objects detected in images using Azure Vision API.

Features

Users can upload images and optionally provide descriptions.

If no description is provided, the app automatically generates alt text.

Uploaded images are automatically analyzed to detect objects for searchable tags.

Users can search for images using keywords corresponding to detected objects.

Requirements

Python 3.10+ (tested on 3.10)

Azure account for Vision API (free tier works)

Install dependencies:

pip install -r requirements.txt

Setup

Clone the repository

git clone https://github.com/nidhi919/CS516_albumy_NidhiRJ.git
cd CS516_albumy_NidhiRJ


Create a virtual environment

python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate


Install dependencies

pip install -r requirements.txt


Configure Azure Vision API

Create an Azure Cognitive Services account if you don’t have one.

Get your endpoint URL and API key.

Create a file called .env in the root directory with the following content:

AZURE_VISION_KEY=your_api_key_here
AZURE_VISION_ENDPOINT=your_endpoint_here


Note: Do not commit .env to the repository.

Initialize the database

flask db upgrade


Run the application

flask run


Open http://127.0.0.1:5000
 in your browser.

Usage

Upload images: Go to /upload and upload a photo.

View alt text: Inspect the image or hover over it (screen readers will use alt text).

Search by object: Use the search bar on the homepage to find images by detected objects.

Notes

The app uses Azure Vision API for both alt-text generation and object detection.

Uploaded images are stored locally in uploads/.

Profile pictures do not use automatic alt-text generation.

Credits

Original albumy project: greyli/albumy

Azure Cognitive Services Vision API: documentation
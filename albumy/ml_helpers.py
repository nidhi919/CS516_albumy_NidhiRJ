import os
from dotenv import load_dotenv
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

# Load .env
load_dotenv()

# Azure Computer Vision keys
AZURE_CV_KEY = os.getenv("AZURE_COMPUTER_VISION_KEY")
AZURE_CV_ENDPOINT = os.getenv("AZURE_COMPUTER_VISION_ENDPOINT")

# Initialize Azure CV client
cv_client = ComputerVisionClient(AZURE_CV_ENDPOINT, CognitiveServicesCredentials(AZURE_CV_KEY))

def generate_alt_text(image_path):
    
    try:
        with open(image_path, "rb") as image_stream:
            description = cv_client.describe_image_in_stream(image_stream)
        if description.captions:
            return description.captions[0].text
    except Exception as e:
        print(f"[Error] generate_alt_text: {e}")
    return "No description available."

def detect_objects(image_path):
    
    try:
        with open(image_path, "rb") as image_stream:
            analysis = cv_client.analyze_image_in_stream(
                image_stream, visual_features=[VisualFeatureTypes.tags]
            )
        return [tag.name for tag in analysis.tags] if analysis.tags else []
    except Exception as e:
        print(f"[Error] detect_objects: {e}")
        return []

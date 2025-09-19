
import os
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

# Retrieve endpoint and key from environment variables
endpoint = os.getenv("AZURE_COMPUTER_VISION_ENDPOINT")
key = os.getenv("AZURE_COMPUTER_VISION_KEY")

if not endpoint or not key:
    raise ValueError("Azure Vision endpoint and key must be set in environment variables.")

# Initialize the Image Analysis client
client = ImageAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(key))

def generate_alt_text(image_path: str) -> str:
   
    try:
        with open(image_path, "rb") as image_file:
            image_bytes = image_file.read()

        
        result = client.analyze(
            image_data=image_bytes,
            visual_features=[VisualFeatures.CAPTION]
        )

       
        if result and result.caption:
            return result.caption.text
        else:
            return "No description available."

    except Exception as e:
      
        print(f"[Image Analysis Error]: {e}")
        return "No description available."

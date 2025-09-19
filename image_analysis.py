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


def parse_analysis(result: dict) -> list[str]:
 #extracting object names, tags, and dense captions from Azure response dict
    tags = set()

    if "tagsResult" in result and "values" in result["tagsResult"]:
        for tag in result["tagsResult"]["values"]:
            tags.add(tag["name"])

    if "objectsResult" in result and "values" in result["objectsResult"]:
        for obj in result["objectsResult"]["values"]:
            if "tags" in obj and obj["tags"]:
                for t in obj["tags"]:
                    tags.add(t["name"])

    if "denseCaptionsResult" in result and "values" in result["denseCaptionsResult"]:
        for cap in result["denseCaptionsResult"]["values"]:
            tags.add(cap["text"])

    return list(tags)


import json

from PIL import Image
import io
def detect_objects(image_path: str) -> list[str]:
    """Detect objects, tags, and captions in an image using Azure."""
    try:
        with open(image_path, "rb") as image_file:
            image_bytes = image_file.read()

        # calling azure thing
        result = client.analyze(
            image_data=image_bytes,
            visual_features=[
                VisualFeatures.OBJECTS,
                VisualFeatures.TAGS,
                VisualFeatures.DENSE_CAPTIONS
            ]
        )

        # changing the result to a dictionary for parsing
        result_dict = result.as_dict()
        print("DEBUG full result:", result_dict)  
        final_tags = parse_analysis(result_dict)
        print("DEBUG detected objects:", final_tags)  
        return final_tags

    except Exception as e:
        print(f"[Object Detection Error]: {e}")
        return []

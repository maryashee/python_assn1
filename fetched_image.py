import os
import requests
import uuid
from urllib.parse import urlparse

url = input("Enter the URL of an image: ")

folder = "Fetched_Images"
os.makedirs(folder, exist_ok=True)

try:
    response = requests.get(url)
    response.raise_for_status()

    # Extract filename safely
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)  # gets the last part after "/"

    # If filename is empty, or too messy, generate a simple one
    if not filename or "." not in filename:
        filename = f"image_{uuid.uuid4().hex}.jpg"

    path = os.path.join(folder, filename)

    # Save image
    with open(path, "wb") as f:
        f.write(response.content)

    print(f"✅ Image saved successfully at: {path}")

except requests.exceptions.RequestException as e:
    print(f"⚠️ Error fetching image: {e}")

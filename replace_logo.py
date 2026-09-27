import sys
from PIL import Image

src = "/Users/juggernut/.gemini/antigravity/brain/25816d68-228f-4ad0-b1e4-6b0d91e69444/.user_uploaded/media_1790430885927.jpg"

try:
    img = Image.open(src)
    # Save as webp
    img.save("static/main/logo/logo.webp", "WEBP")
    img.save("static/dash/assets/images/logo.webp", "WEBP")
    # Save as png
    img.save("static/main/logo/logo.png", "PNG")
    print("Logos successfully replaced!")
except Exception as e:
    print(f"Error: {e}")

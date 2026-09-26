from PIL import Image
import os

os.makedirs('static/main/images', exist_ok=True)
img = Image.open('/Users/juggernut/.gemini/antigravity/brain/25816d68-228f-4ad0-b1e4-6b0d91e69444/.user_uploaded/media_1790418865290.jpg')
img.save('static/main/images/og_graph.webp', 'WEBP')
print("Image converted and saved to static/main/images/og_graph.webp")

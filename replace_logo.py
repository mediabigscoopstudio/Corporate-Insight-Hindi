from PIL import Image
import os

source_img = '/Users/juggernut/.gemini/antigravity/brain/25816d68-228f-4ad0-b1e4-6b0d91e69444/.user_uploaded/media_1790419704773.jpg'
img = Image.open(source_img)

# Ensure directories exist
os.makedirs('static/main/logo', exist_ok=True)
os.makedirs('static/dash/assets/images', exist_ok=True)

# Main webp and png
img.save('static/main/logo/logo.webp', 'WEBP')
img.save('static/main/logo/logo.png', 'PNG')

# Dash webp
img.save('static/dash/assets/images/logo.webp', 'WEBP')

# For favicon (Vector.webp), usually it's square, but let's just use the same image
# or we can crop/resize it to a small square? Let's just save as is for now, 
# or maybe resize to maintain aspect ratio but small. Let's just use the same.
img.save('static/main/logo/Vector.webp', 'WEBP')

print("Logos successfully replaced in static directories.")

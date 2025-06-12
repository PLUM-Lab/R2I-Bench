import os
import pandas as pd
from instance import *

# Simulated model interface (replace this with your actual image generation logic)
def generate_image_from_prompt(prompt):
    from PIL import Image, ImageDraw
    img = Image.new('RGB', (512, 512), color='white')
    draw = ImageDraw.Draw(img)
    draw.text((10, 10), prompt[:100], fill='black')  # Simplified example
    return img

base_path = "data/prompts"
save_path = "save"

for entry in category_subcategory_list:
    category = entry["category"]
    subcategory = entry["subcategory"]
    filename = f"{category}_{subcategory}.csv"
    csv_path = os.path.join(base_path, category, filename)
    
    if not os.path.exists(csv_path):
        print(f"File does not exist: {csv_path}")
        continue
    
    df = pd.read_csv(csv_path, encoding="utf-8")
    
    for i, row in df.iterrows():
        prompt = row["Prompt"]
        data_id = row.get("id", i)   
        
        # Call the image generation model
        image = generate_image_from_prompt(prompt)
        
        save_dir = os.path.join(save_path, category, subcategory)
        os.makedirs(save_dir, exist_ok=True)
        image_name = f"{category}_{subcategory}_{data_id}.png"
        image_path = os.path.join(save_dir, image_name)
        
        image.save(image_path)
        print(f"Image saved: {image_path}")

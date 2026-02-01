#!/usr/bin/env python3
from PIL import Image
import os
import glob

# Configuration
INPUT_DIR = "images"
MAX_WIDTH = 1200
MAX_HEIGHT = 1200
QUALITY = 50

# Supported image formats
SUPPORTED_FORMATS = ('.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG')

def resize_image(input_path):
    """Resize image while maintaining aspect ratio"""
    try:
        with Image.open(input_path) as img:
            # Get original dimensions
            width, height = img.size

            # Calculate new dimensions maintaining aspect ratio
            if width > MAX_WIDTH or height > MAX_HEIGHT:
                ratio = min(MAX_WIDTH / width, MAX_HEIGHT / height)
                new_width = int(width * ratio)
                new_height = int(height * ratio)

                # Resize image
                img_resized = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

                # Save with appropriate format
                if input_path.lower().endswith('.png'):
                    img_resized.save(input_path, 'PNG', optimize=True)
                else:
                    img_resized.save(input_path, 'JPEG', quality=QUALITY, optimize=True)

                print(f"✓ Resized: {os.path.basename(input_path)} ({width}x{height} -> {new_width}x{new_height})")
            else:
                print(f"- Skipped: {os.path.basename(input_path)} (already small enough)")

    except Exception as e:
        print(f"✗ Error processing {input_path}: {e}")

def main():
    # Change to script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    # Check if images directory exists
    if not os.path.exists(INPUT_DIR):
        print(f"Error: '{INPUT_DIR}' directory not found!")
        return

    # Find all image files
    image_files = []
    for ext in SUPPORTED_FORMATS:
        image_files.extend(glob.glob(os.path.join(INPUT_DIR, f"*{ext}")))

    if not image_files:
        print(f"No images found in '{INPUT_DIR}' directory!")
        return

    print(f"Found {len(image_files)} images to resize...")
    print(f"Max dimensions: {MAX_WIDTH}x{MAX_HEIGHT}, Quality: {QUALITY}")
    print("-" * 50)

    # Resize each image
    for image_path in image_files:
        resize_image(image_path)

    print("-" * 50)
    print("Done!")

if __name__ == "__main__":
    main()

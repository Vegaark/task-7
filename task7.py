import os
import time
from PIL import Image

def resize_images(input_folder, output_folder, size=(800, 800), output_format="PNG"):

    # Create input folder if missing
    if not os.path.exists(input_folder):
        os.makedirs(input_folder)
        print("'input_images' folder created. Add images and the program will continue automatically.")

    # Create output folder if missing
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    print("\nWaiting for images...")

    # Wait until there are images
    while True:
        files = [f for f in os.listdir(input_folder)
                 if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp", ".bmp", ".gif"))]

        if files:
            print(f" {len(files)} images detected. Processing...\n")
            break

        time.sleep(2)  # Wait a little before checking again

    # Process files
    for file in files:
        file_path = os.path.join(input_folder, file)

        try:
            with Image.open(file_path) as img:
                resized = img.resize(size)

                new_name = os.path.splitext(file)[0] + "." + output_format.lower()
                save_path = os.path.join(output_folder, new_name)

                resized.save(save_path, output_format)
                print(f"Processed: {save_path}")

        except Exception as e:
            print(f" Error processing {file}: {e}")

    print("\n Task Completed!")


if __name__ == "__main__":
    input_folder = "input_images"
    output_folder = "output_images"

    resize_images(input_folder, output_folder)

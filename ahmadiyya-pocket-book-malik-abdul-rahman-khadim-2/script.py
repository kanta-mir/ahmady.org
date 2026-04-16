import os
from PIL import Image

# ===== CONFIG =====
INPUT_FOLDER = "img"
OUTPUT_FOLDER = "output_pages"

TARGET_WIDTH = 1200
TARGET_HEIGHT = 1600

BACKGROUND_COLOR = (255, 255, 255)  # white (use (0,0,0) for black)

# ==================

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def process_image(input_path, output_path):
    img = Image.open(input_path).convert("RGB")

    # keep aspect ratio
    img.thumbnail((TARGET_WIDTH, TARGET_HEIGHT), Image.LANCZOS)

    # create new blank canvas
    new_img = Image.new("RGB", (TARGET_WIDTH, TARGET_HEIGHT), BACKGROUND_COLOR)

    # center image
    x = (TARGET_WIDTH - img.width) // 2
    y = (TARGET_HEIGHT - img.height) // 2

    new_img.paste(img, (x, y))

    new_img.save(output_path, "JPEG", quality=90, optimize=True)


def process_folder():
    files = sorted(os.listdir(INPUT_FOLDER))

    for file in files:
        if file.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
            input_path = os.path.join(INPUT_FOLDER, file)

            # normalize naming (important for your viewer)
            name = os.path.splitext(file)[0]
            output_file = f"{name}.jpg"

            output_path = os.path.join(OUTPUT_FOLDER, output_file)

            print(f"Processing {file}...")
            process_image(input_path, output_path)

    print("✅ Done!")


if __name__ == "__main__":
    process_folder()
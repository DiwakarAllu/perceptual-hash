from pathlib import Path
from PIL import Image, ImageEnhance

SOURCE = Path("samples/original.jpg")
OUTPUT_DIR = Path("samples/generated")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

image = Image.open(SOURCE)

# 1. Resize
resized = image.resize(
    (image.width // 2, image.height // 2)
)
resized.save(OUTPUT_DIR / "resized.jpg", quality=90)

# 2. Strong JPEG compression
image.save(
    OUTPUT_DIR / "compressed.jpg",
    quality=20
)

# 3. Grayscale
grayscale = image.convert("L")
grayscale.save(OUTPUT_DIR / "grayscale.jpg")

# 4. Brightness change
brightened = ImageEnhance.Brightness(image).enhance(1.5)
brightened.save(OUTPUT_DIR / "brightened.jpg")

# 5. Contrast change
contrasted = ImageEnhance.Contrast(image).enhance(1.8)
contrasted.save(OUTPUT_DIR / "contrasted.jpg")

# 6. Crop the edges
left = image.width // 10
top = image.height // 10
right = image.width - left
bottom = image.height - top

cropped = image.crop((left, top, right, bottom))
cropped.save(OUTPUT_DIR / "cropped.jpg")

# 7. Small rotation
rotated = image.rotate(
    5,
    expand=True,
    fillcolor="white"
)
rotated.save(OUTPUT_DIR / "rotated.jpg")

print(f"Generated {len(list(OUTPUT_DIR.glob('*.jpg')))} variants.")
print(f"Saved to: {OUTPUT_DIR}")

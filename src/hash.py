from pathlib import Path

from PIL import Image
import imagehash


SOURCE = Path("samples/original.jpg")
VARIANTS_DIR = Path("samples/generated")

# Lower distance = more visually similar
MATCH_THRESHOLD = 10


def calculate_hash(image_path: Path):
    image = Image.open(image_path)
    return imagehash.phash(image)


def main():
    original_hash = calculate_hash(SOURCE)

    print(f"Original: {SOURCE}")
    print(f"pHash:    {original_hash}")
    print()

    print(f"{'Image':<20} {'Distance':<10} {'Result'}")
    print("-" * 50)

    for image_path in sorted(VARIANTS_DIR.glob("*.jpg")):
        variant_hash = calculate_hash(image_path)

        # Hamming distance between the two perceptual hashes
        distance = original_hash - variant_hash

        result = (
            "MATCH"
            if distance <= MATCH_THRESHOLD
            else "DIFFERENT"
        )

        print(
            f"{image_path.name:<20} "
            f"{distance:<10} "
            f"{result}"
        )


if __name__ == "__main__":
    main()

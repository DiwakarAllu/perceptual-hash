from pathlib import Path

from PIL import Image
import imagehash


SOURCE = Path("samples/original.jpg")
VARIANTS_DIR = Path("samples/generated")


def main():
    original = Image.open(SOURCE)

    # Calculate the reference hash once
    original_hash = imagehash.phash(original)

    print("Original pHash:")
    print(original_hash)
    print()

    results = []

    for path in sorted(VARIANTS_DIR.glob("*.jpg")):
        image = Image.open(path)
        variant_hash = imagehash.phash(image)

        distance = original_hash - variant_hash

        results.append((path.name, distance))

    # Sort from most similar to least similar
    results.sort(key=lambda x: x[1])

    print(f"{'IMAGE':<25} {'HAMMING DISTANCE'}")
    print("-" * 45)

    for name, distance in results:
        print(f"{name:<25} {distance}")

    print()
    print("Lowest distance = most similar")


if __name__ == "__main__":
    main()

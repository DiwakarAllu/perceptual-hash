from pathlib import Path

from PIL import Image
import imagehash


SAMPLES_DIR = Path("samples")
VARIANTS_DIR = SAMPLES_DIR / "generated"

# Maximum Hamming distance we consider a potential match.
THRESHOLD = 10


def fingerprint(path: Path):
    """
    Generate a perceptual fingerprint for an image.
    """
    with Image.open(path) as image:
        return imagehash.phash(image)


def build_index():
    """
    Build a simple in-memory fingerprint index.
    """

    index = {}

    for path in VARIANTS_DIR.glob("*.jpg"):
        index[path.name] = fingerprint(path)

    return index


def search(query_path: Path, index):
    """
    Compare a query image against every fingerprint
    in the index.
    """

    query_hash = fingerprint(query_path)

    matches = []

    for filename, stored_hash in index.items():
        distance = query_hash - stored_hash

        matches.append({
            "filename": filename,
            "distance": distance,
        })

    # Closest fingerprints first
    matches.sort(key=lambda item: item["distance"])

    return matches


def main():

    print("Building fingerprint index...")

    index = build_index()

    print(f"Indexed {len(index)} images.")
    print()

    query = SAMPLES_DIR / "original.jpg"

    print(f"Query: {query}")
    print()

    results = search(query, index)

    print(f"{'IMAGE':<25} {'DISTANCE':<10} {'RESULT'}")
    print("-" * 55)

    for result in results:

        distance = result["distance"]

        if distance <= THRESHOLD:
            status = "MATCH"
        else:
            status = "NO MATCH"

        print(
            f"{result['filename']:<25}"
            f"{distance:<10}"
            f"{status}"
        )


if __name__ == "__main__":
    main()

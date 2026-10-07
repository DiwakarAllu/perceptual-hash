# Perceptual Hash

A small Python project for computing perceptual hashes (pHash), comparing them
with Hamming distance, and generating altered images for robustness experiments.

## Setup

Use Python 3.9 or newer:

```bash
python -m pip install -r requirements.txt
```

## Compute and compare hashes

```python
from src.hash import hamming_distance, perceptual_hash

original = perceptual_hash("samples/original.jpg")
modified = perceptual_hash("samples/variants/original_brightness.jpg")

print("Original:", original)
print("Modified:", modified)
print("Bit differences:", hamming_distance(original, modified))
```

## Generate image variants

From the project root, run:

```bash
python -m src.generate_variants
```

This reads `samples/original.jpg`, writes resized, rotated, brightness,
contrast, and grayscale versions to `samples/variants/`, and prints each
variant's pHash. To choose another input or output directory:

```bash
python -m src.generate_variants path/to/image.jpg --output-dir path/to/output
```

## Run tests

```bash
python -m unittest discover -s tests
```

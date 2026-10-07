import random
import time

import imagehash


def random_hash():
    """
    Create a random 64-bit perceptual hash.
    """

    value = random.getrandbits(64)
    return imagehash.hex_to_hash(f"{value:016x}")


def build_database(size, target_hash):
    """
    Create a simulated fingerprint database.

    target_hash is inserted into the database so
    we know a match exists.
    """

    database = []

    for _ in range(size):
        database.append(random_hash())

    # Hide the real fingerprint somewhere in the database
    position = random.randint(0, size - 1)
    database[position] = target_hash

    return database, position


def search(database, query):
    """
    Naïve linear search.

    Compare the query against every fingerprint.
    """

    best_distance = float("inf")
    best_position = None

    for position, stored_hash in enumerate(database):

        distance = query - stored_hash

        if distance < best_distance:
            best_distance = distance
            best_position = position

    return best_position, best_distance


def benchmark(size, query):
    database, expected_position = build_database(
        size,
        query
    )

    start = time.perf_counter()

    position, distance = search(
        database,
        query
    )

    elapsed = time.perf_counter() - start

    return (
        elapsed,
        position,
        expected_position,
        distance
    )


def main():

    # Our "known bad media" fingerprint
    query = random_hash()

    sizes = [
        10,
        100,
        1_000,
        10_000,
        100_000,
    ]

    print(
        f"{'DATABASE':<15}"
        f"{'TIME (sec)':<15}"
        f"{'DISTANCE':<12}"
        f"{'FOUND'}"
    )

    print("-" * 55)

    for size in sizes:

        elapsed, position, expected, distance = benchmark(
            size,
            query
        )

        found = position == expected

        print(
            f"{size:<15}"
            f"{elapsed:<15.6f}"
            f"{distance:<12}"
            f"{found}"
        )


if __name__ == "__main__":
    main()

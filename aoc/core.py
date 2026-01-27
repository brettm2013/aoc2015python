from pathlib import Path
import time


INPUT_DIR = Path(__file__).resolve().parent.parent / "inputs"


def load_input(day: int) -> str:
    path = INPUT_DIR / f"day{day:02d}.txt"
    return path.read_text().rstrip("\n")


def timeit(fn):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = fn(*args, **kwargs)
        elapsed = (time.perf_counter() - start) * 1000
        return result, elapsed

    return wrapper

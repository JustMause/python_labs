import re
from collections import Counter


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if not text:
        return ""

    result = text

    if yo2e:
        result = result.replace('ё', 'е').replace('Ё', 'Е')

    if casefold:
        result = result.casefold()

    result = re.sub(r'[\t\r\n\v\f]', ' ', result)
    result = re.sub(r' +', ' ', result)
    result = result.strip()

    return result


def tokenize(text: str) -> list[str]:
    if not text:
        return []

    tokens = re.findall(r'\b[\w-]+\b', text)

    return tokens


def count_freq(tokens: list[str]) -> dict[str, int]:
    return dict(Counter(tokens))


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    if not freq:
        return []

    sorted_items = sorted(
        freq.items(),
        key=lambda x: (-x[1], x[0])
    )

    return sorted_items[:n]

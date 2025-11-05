import re


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if not text:
        return ""
    result = text
    if casefold:
        result = result.casefold()
    if yo2e:
        result = result.replace('ё', 'е').replace('Ё', 'Е')
    special_simvols = ['\t', '\r', '\n']
    for simvol in special_simvols:
        result = result.replace(simvol, ' ')
    result = ' '.join(result.split())

    return result

def tokenize(text: str) -> list[str]:
    if not text:
        return []
    pattern = r'\w+(?:-\w+)*'
    tokens = re.findall(pattern, text)
    return tokens

def count_freq(tokens: list[str]) -> dict[str, int]:
    freq_dict = {}
    for token in tokens:
        freq_dict[token] = freq_dict.get(token, 0) + 1

    return freq_dict

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    if not freq:
        return []
    sorted_items = sorted(freq.items(),key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]

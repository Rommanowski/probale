# ── konfiguracja ────────────────────────────────────────────────
N = 5   # rozmiar zbioru
M = 3   # długość porządku odwiedzin
# ────────────────────────────────────────────────────────────────


def oczekiwana_liczba(n, m):
    """P(n, m) = n * (n-1) * ... * (n-m+1)"""
    result = 1
    for i in range(n, n - m, -1):
        result *= i
    return result


def generate_orders(data: list, m: int, current: list = None, n: int = 0):
    """Generuje wszystkie m-elementowe porządki (permutacje) ze zbioru data."""
    if current is None:
        current = []

    if len(current) == m:
        print(n + 1, current)
        return n + 1

    for elem in data:
        new_current = current.copy()
        new_data = data.copy()

        new_current.append(elem)
        new_data.remove(elem)

        n = generate_orders(new_data, m, new_current, n)

    return n


# ── zadanie 1 ────────────────────────────────────────────────────
data = list(range(1, N + 1))  # zbiór {1, 2, ..., N}

print(f"Liczba porządków (N = {N}, M {M}) = {oczekiwana_liczba(N, M)}\n")

generate_orders(data, M)
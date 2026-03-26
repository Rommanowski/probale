# ── konfiguracja ────────────────────────────────────────────────
N = 5   # rozmiar zbioru
M = 3   # rozmiar podzbioru
# ────────────────────────────────────────────────────────────────


def oczekiwana_liczba(n, m):
    """C(n+m-1, m) = (n+m-1)! / (m! * (n-1)!)"""
    licznik = 1
    for i in range(n + m - 1, n - 1, -1):
        licznik *= i
    mianownik = 1
    for i in range(1, m + 1):
        mianownik *= i
    return licznik // mianownik


def generate_subsets(data: list, m: int, current: list = None, n: int = 0):
    """Generuje wszystkie m-elementowe podzbiory z powtórzeniami (porządek niemalejący)."""
    if current is None:
        current = []

    if len(current) == m:
        print(n + 1, current)
        return n + 1

    # zaczynamy od ostatniego dodanego elementu (porządek niemalejący)
    start = current[-1] if current else data[0]
    for elem in data:
        if elem < start:
            continue
        n = generate_subsets(data, m, current + [elem], n)

    return n


# ── zadanie 2 ────────────────────────────────────────────────────
data = list(range(1, N + 1))  # zbiór {1, 2, ..., N}

print(f"Liczba podzbiorów C({N}+{M}-1,{M}) = {oczekiwana_liczba(N, M)}\n")

subsets_count = generate_subsets(data, M)
print(f"\nn = {N}, m = {M}, liczba podzbiorów: {subsets_count}")

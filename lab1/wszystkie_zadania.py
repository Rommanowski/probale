# ══════════════════════════════════════════════════════════════════
#  MP lab 1 – Wszystkie zadania (bez bezpowt)
# ══════════════════════════════════════════════════════════════════

PLIK = "dane/MPI lab 1 - spain.txt"


# ── klasa City (wspólna dla zadań 1u i 2u) ───────────────────────

class City:
    def __init__(self, id: int, name: str, population: int, lat: float, lon: float):
        self.id = id
        self.name = name
        self.population = population
        self.lat = lat
        self.lon = lon

    def __str__(self):
        return self.name

    def __lt__(self, other):
        return self.id < other.id

    def distance(self, other):
        return ((self.lat - other.lat)**2 + (self.lon - other.lon)**2)**0.5


# ── funkcje pomocnicze ───────────────────────────────────────────

def oczekiwana_wariacje(n, m):
    """V(n, m) = n * (n-1) * ... * (n-m+1)"""
    result = 1
    for i in range(n, n - m, -1):
        result *= i
    return result


def oczekiwana_kombinacje(n, m):
    """C(n+m-1, m) = (n+m-1)! / (m! * (n-1)!)"""
    licznik = 1
    for i in range(n + m - 1, n - 1, -1):
        licznik *= i
    mianownik = 1
    for i in range(1, m + 1):
        mianownik *= i
    return licznik // mianownik


# ── generatory ───────────────────────────────────────────────────

def generate_orders(data: list, m: int, current: list = None, n: int = 0, results: list = None):
    """Generuje wszystkie m-elementowe porządki (wariacje bez powtórzeń) ze zbioru data."""
    if current is None:
        current = []
    if results is None:
        results = []

    if len(current) == m:
        results.append(current[:])
        return (n + 1, results)

    for elem in data:
        new_current = current.copy()
        new_data = data.copy()

        new_current.append(elem)
        new_data.remove(elem)

        n, results = generate_orders(new_data, m, new_current, n, results)

    return (n, results)


def generate_subsets(data: list, m: int, current: list = None, n: int = 0, results: list = None):
    """Generuje wszystkie m-elementowe podzbiory z powtórzeniami (porządek niemalejący)."""
    if current is None:
        current = []
    if results is None:
        results = []

    if len(current) == m:
        results.append(current[:])
        return (n + 1, results)

    start = current[-1] if current else data[0]
    for elem in data:
        if elem < start:
            continue
        n, results = generate_subsets(data, m, current + [elem], n, results)

    return (n, results)


def cycle_distance(order: list):
    """Liczy długość trasy-cyklu: miasto1 -> miasto2 -> ... -> miasto1."""
    total = 0
    for i in range(len(order) - 1):
        total += order[i].distance(order[i + 1])
    total += order[-1].distance(order[0])
    return total


# ══════════════════════════════════════════════════════════════════
#  ZADANIE 1 – wariacje bez powtórzeń (liczby)
# ══════════════════════════════════════════════════════════════════

def zadanie1(N=5, M=3):
    print("=" * 60)
    print("ZADANIE 1 – wariacje bez powtórzeń (liczby)")
    print("=" * 60)

    data = list(range(1, N + 1))

    print(f"Liczba porządków (N = {N}, M = {M}) = {oczekiwana_wariacje(N, M)}\n")

    n = 0
    def _gen(data, m, current=None, n=0):
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
            n = _gen(new_data, m, new_current, n)
        return n

    _gen(data, M)
    print()


# ══════════════════════════════════════════════════════════════════
#  ZADANIE 1u – najkrótsza trasa-cykl (wariacje na miastach)
# ══════════════════════════════════════════════════════════════════

def zadanie1u(cities, N=5, M=3):
    print("=" * 60)
    print("ZADANIE 1u – najkrótsza trasa-cykl (wariacje na miastach)")
    print("=" * 60)

    data = cities[:N]
    print(f"Miasta: {[str(c) for c in data]}\n")

    orders_count, orders = generate_orders(data, M)

    best_order = min(orders, key=cycle_distance)
    best_distance = cycle_distance(best_order)

    print(f"Najkrótsza trasa-cykl ({M} z {N} miast):")
    print(f"  Trasa:    {' -> '.join(str(c) for c in best_order)} -> {best_order[0]}")
    print(f"  Długość:  {best_distance:.4f}")
    print()


# ══════════════════════════════════════════════════════════════════
#  ZADANIE 2 – kombinacje z powtórzeniami (liczby)
# ══════════════════════════════════════════════════════════════════

def zadanie2(N=5, M=3):
    print("=" * 60)
    print("ZADANIE 2 – kombinacje z powtórzeniami (liczby)")
    print("=" * 60)

    data = list(range(1, N + 1))

    print(f"Liczba podzbiorów C({N}+{M}-1,{M}) = {oczekiwana_kombinacje(N, M)}\n")

    def _gen(data, m, current=None, n=0):
        if current is None:
            current = []
        if len(current) == m:
            print(n + 1, current)
            return n + 1
        start = current[-1] if current else data[0]
        for elem in data:
            if elem < start:
                continue
            n = _gen(data, m, current + [elem], n)
        return n

    subsets_count = _gen(data, M)
    print(f"\nn = {N}, m = {M}, liczba podzbiorów: {subsets_count}")
    print()


# ══════════════════════════════════════════════════════════════════
#  ZADANIE 2u – podzbiory miast (kombinacje bez powtórzeń)
# ══════════════════════════════════════════════════════════════════

def zadanie2u(cities, N=6, M=4):
    print("=" * 60)
    print("ZADANIE 2u – podzbiory miast (kombinacje bez powtórzeń)")
    print("=" * 60)

    data = cities[:N]
    print(f"Miasta: {[str(c) for c in data]}\n")

    total_population = sum(c.population for c in data)
    low  = 0.4 * total_population
    high = 0.6 * total_population

    print(f"Łączna populacja {N} miast: {total_population}")
    print(f"Przedział 40%-60%: [{low:.1f}, {high:.1f}]\n")

    subsets_count, subsets = generate_subsets(data, M)

    favorable = sum(
        1 for subset in subsets
        if low <= sum(c.population for c in set(subset)) <= high
    )

    probability = favorable / subsets_count

    print(f"Liczba wszystkich podzbiorów:    {subsets_count}")
    print(f"Liczba sprzyjających podzbiorów: {favorable}")
    print(f"Prawdopodobieństwo:              {probability:.4f} ({probability*100:.2f}%)")
    print()


# ══════════════════════════════════════════════════════════════════
#  MAIN
# ══════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    # wczytanie miast
    with open(PLIK, "r") as file:
        all_cities: list[City] = []
        for line in file.readlines()[1:]:
            parts = line.strip().split()
            if len(parts) >= 5:
                all_cities.append(City(int(parts[0]), parts[1], int(parts[2]), float(parts[3]), float(parts[4])))

    zadanie1(N=5, M=3)
    zadanie1u(all_cities, N=5, M=3)
    zadanie2(N=5, M=3)
    zadanie2u(all_cities, N=6, M=4)

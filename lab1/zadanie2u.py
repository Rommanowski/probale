# ── konfiguracja ────────────────────────────────────────────────
PLIK = "dane/MPI lab 1 - spain.txt"
N = 6   # ile miast bierzemy
M = 4   # rozmiar podzbioru
# ────────────────────────────────────────────────────────────────


class City:
    def __init__(self, id: int, name: str, population: int, lat: float, lon: float):
        self.id = id
        self.name = name
        self.population = population
        self.lat = lat
        self.lon = lon

    def __str__(self):
        return self.name


def generate_subsets(data: list, m: int, current: list = None, n: int = 0, results: list = None):
    """Generuje wszystkie m-elementowe podzbiory bez powtórzeń (kombinacje)."""
    if current is None:
        current = []
    if results is None:
        results = []

    if len(current) == m:
        results.append(current[:])
        return (n + 1, results)

    data_copy = data.copy()
    for elem in data:
        new_current = current.copy()
        new_current.append(elem)
        n, results = generate_subsets(data_copy, m, new_current, n, results)
        data_copy.remove(elem)

    return (n, results)


# ── wczytanie danych ─────────────────────────────────────────────
with open(PLIK, "r") as file:
    data: list[City] = []
    for line in file.readlines()[1:N + 1]:
        parts = line.strip().split()
        data.append(City(int(parts[0]), parts[1], int(parts[2]), float(parts[3]), float(parts[4])))

print(f"Wczytane miasta: {[str(c) for c in data]}\n")

# ── zadanie 2u ───────────────────────────────────────────────────
total_population = sum(c.population for c in data)
low  = 0.4 * total_population
high = 0.6 * total_population

print(f"Łączna populacja {N} miast: {total_population}")
print(f"Przedział 40%-60%: [{low:.1f}, {high:.1f}]\n")

subsets_count, subsets = generate_subsets(data, M)

favorable = sum(
    1 for subset in subsets
    if low <= sum(c.population for c in subset) <= high
)

probability = favorable / subsets_count

print(f"Liczba wszystkich podzbiorów:    {subsets_count}")
print(f"Liczba sprzyjających podzbiorów: {favorable}")
print(f"Prawdopodobieństwo:              {probability:.4f} ({probability*100:.2f}%)")

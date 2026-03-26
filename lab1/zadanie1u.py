# ── konfiguracja ────────────────────────────────────────────────
PLIK = "dane/MPI lab 1 - spain.txt"
N = 5   # ile miast bierzemy
M = 3   # ile miast w trasie
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

    def distance(self, other):
        return ((self.lat - other.lat)**2 + (self.lon - other.lon)**2)**0.5


def generate_orders(data: list, m: int, current: list = None, n: int = 0, results: list = None):
    """Generuje wszystkie m-elementowe porządki, tym razem zbieramy wyniki do listy."""
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


def cycle_distance(order: list):
    """Liczy długość trasy-cyklu: miasto1 -> miasto2 -> ... -> miasto1."""
    total = 0
    for i in range(len(order) - 1):
        total += order[i].distance(order[i + 1])
    total += order[-1].distance(order[0])  # powrót do startu
    return total


# ── wczytanie danych ─────────────────────────────────────────────
with open(PLIK, "r") as file:
    data: list[City] = []
    for line in file.readlines()[1:N + 1]:
        parts = line.strip().split()
        data.append(City(int(parts[0]), parts[1], int(parts[2]), float(parts[3]), float(parts[4])))

print(f"Wczytane miasta: {[str(c) for c in data]}\n")

# ── zadanie 1u ───────────────────────────────────────────────────
orders_count, orders = generate_orders(data, M)

best_order = min(orders, key=cycle_distance)
best_distance = cycle_distance(best_order)

print(f"Najkrótsza trasa-cykl ({M} z {N} miast):")
print(f"  Trasa:    {' -> '.join(str(c) for c in best_order)} -> {best_order[0]}")
print(f"  Długość:  {best_distance:.4f}")

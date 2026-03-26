
# =============================================================================
#  LAB 2 - Generatory liczb losowych o rozkladzie rownomiernym
#  Wszystkie zadania w jednym pliku
# =============================================================================


# ── Klasy generatorow ────────────────────────────────────────────────────────

class LinearGenerator:
    def __init__(self, a: int, c: int, m: int, seed: int = 1):
        self.a = a
        self.c = c
        self.m = m
        self.seed = seed

    def __generate_number(self) -> int:
        self.seed = (self.a * self.seed + self.c) % self.m
        return self.seed

    def generate_probability(self) -> float:
        return self.__generate_number() / self.m

    def generate_probabilities(self, n: int):
        for _ in range(n):
            yield self.generate_probability()

    def generate_number(self, m: int = None) -> int:
        if m is None:
            m = self.m
        return int(m * self.generate_probability())

    def generate_numbers(self, n: int, m: int = None):
        if m is None:
            m = self.m
        for _ in range(n):
            yield self.generate_number(m)

    def random(self) -> float:
        return self.__generate_number() / self.m

    def randint(self, n: int) -> int:
        return self.__generate_number() % n

    def shuffle(self, lst: list) -> None:
        for i in range(len(lst) - 1, 0, -1):
            j = self.randint(i + 1)
            lst[i], lst[j] = lst[j], lst[i]


class RegisterGenerator:
    def __init__(self, p: int, q: int, seed: int = 2**31, accuracy: int = 31):
        self.p = p
        self.q = q
        self.size = p
        self.seed = seed
        self.accuracy = accuracy

    def __generate_bit(self) -> int:
        p_bit = (self.seed >> (self.p - 1)) & 1
        q_bit = (self.seed >> (self.q - 1)) & 1
        bit = p_bit ^ q_bit
        self.seed >>= 1
        self.seed |= bit << (self.size - 1)
        return bit

    def generate_probability(self) -> float:
        result = 0
        weight = 0.5
        for _ in range(self.accuracy):
            if self.__generate_bit() == 1:
                result += weight
            weight /= 2
        return result

    def generate_probabilities(self, n: int):
        for _ in range(n):
            yield self.generate_probability()

    def generate_number(self, m: int = None) -> int:
        if m is None:
            m = 2**self.accuracy
        return int(m * self.generate_probability())

    def generate_numbers(self, n: int, m: int = None):
        if m is None:
            m = 2**self.accuracy
        for _ in range(n):
            yield self.generate_number(m)


# ── Klasa kubelkow ───────────────────────────────────────────────────────────

class Bucket:
    def __init__(self, min_val: float, max_val: float, count: int = 0):
        self.min = min_val
        self.max = max_val
        self.count = count

    def __str__(self):
        return f"[{self.min:.3f} - {self.max:.3f}] {self.count}"


def split_into_buckets(data, bucket_count: int, range_min: float = 0.0, range_max: float = 1.0) -> list:
    span = range_max - range_min
    per_bucket = span / bucket_count
    buckets = [Bucket(range_min + i * per_bucket, range_min + (i + 1) * per_bucket) for i in range(bucket_count)]

    for number in data:
        bucket_id = int((number - range_min) / per_bucket)
        if bucket_id >= bucket_count:
            bucket_id = bucket_count - 1
        if bucket_id < 0:
            bucket_id = 0
        buckets[bucket_id].count += 1

    return buckets


def split_into_buckets_conditional(data, bucket_count: int, condition) -> tuple:
    filtered = [x for x in data if condition(x)]
    if not filtered:
        return [], 0
    range_min = min(filtered)
    range_max = max(filtered)
    buckets = split_into_buckets(filtered, bucket_count, range_min, range_max)
    return buckets, len(filtered)


# =============================================================================
#  ZADANIE 1 - Generator liniowy
# =============================================================================

def zadanie1():
    print("=" * 70)
    print("ZADANIE 1 - Generator liniowy")
    print("=" * 70)

    a = 16807
    c = 0
    m = 2**31 - 1
    seed = 15
    N = 100_000
    K = 10

    print(f"a = {a}, c = {c}, m = {m}")
    print(f"seed = {seed}, N = {N}, K = {K}")

    gen = LinearGenerator(a, c, m, seed)
    probabilities = list(gen.generate_probabilities(N))

    avg = sum(probabilities) / N
    var = sum((x - avg) ** 2 for x in probabilities) / N

    # print(f"\nSrednia  = {avg:.6f}  (oczekiwana: 0.5)")
    # print(f"Wariancja = {var:.6f}  (oczekiwana: {1/12:.6f})")

    buckets = split_into_buckets(probabilities, K)
    print(f"\nBuckets (K={K}):")
    for bucket in buckets:
        print(bucket)


# =============================================================================
#  ZADANIE 2 - Generator oparty na rejestrach przesuwnych
# =============================================================================

def zadanie2():
    print("\n" + "=" * 70)
    print("ZADANIE 2 - Generator oparty na rejestrach przesuwnych")
    print("=" * 70)

    p = 29
    q = 2
    seed = 15
    N = 100_000
    K = 10

    print(f"p = {p}, q = {q}")
    print(f"seed = {seed}, N = {N}, K = {K}")

    gen = RegisterGenerator(p, q, seed)
    probabilities = list(gen.generate_probabilities(N))

    avg = sum(probabilities) / N
    var = sum((x - avg) ** 2 for x in probabilities) / N

    # print(f"\nSrednia   = {avg:.6f}  (oczekiwana: 0.5)")
    # print(f"Wariancja = {var:.6f}  (oczekiwana: {1/12:.6f})")

    print(f"\nBuckets (K={K}):")
    for bucket in split_into_buckets(probabilities, K):
        print(bucket)



# =============================================================================
#  ZADANIE 1U - Monte Carlo: P(sekwencja K orlow pod rzad w N rzutach)
# =============================================================================

def zadanie1u():
    print("\n" + "=" * 70)
    print("ZADANIE 1U - Monte Carlo: P(sekwencja K orlow pod rzad w N rzutach)")
    print("=" * 70)

    N = 10
    K = 3
    proby = 100_000

    gen = LinearGenerator(a=16807, c=0, m=2**31 - 1, seed=12345)
    trafienia = 0
    for _ in range(proby):
        pod_rzad = 0
        znaleziono = False
        for _ in range(N):
            if gen.randint(2) == 1:
                pod_rzad += 1
                if pod_rzad >= K:
                    znaleziono = True
                    break
            else:
                pod_rzad = 0
        if znaleziono:
            trafienia += 1

    wynik = trafienia / proby
    print(f"N = {N}, K = {K}, proby = {proby}")
    print(f"P(co najmniej {K} orlow pod rzad w {N} rzutach) = {wynik:.4f}")


# =============================================================================
#  ZADANIE 2U - Monte Carlo: powierzchnia czesci wspolnej dwoch kol
# =============================================================================

def zadanie2u():
    print("\n" + "=" * 70)
    print("ZADANIE 2U - Monte Carlo: powierzchnia czesci wspolnej dwoch kol")
    print("=" * 70)

    R = 0.8
    proby = 100_000

    gen = LinearGenerator(a=16807, c=0, m=2**31 - 1, seed=12345)
    trafienia = 0
    for _ in range(proby):
        x = gen.random()
        y = gen.random()

        w_kole_srodek = (x - 0.5)**2 + (y - 0.5)**2 <= 0.5**2
        w_kole_R      = x**2 + y**2 <= R**2

        if w_kole_srodek and w_kole_R:
            trafienia += 1

    wynik = trafienia / proby
    print(f"R = {R}, proby = {proby}")
    print(f"Powierzchnia figury = {wynik:.4f}")


# =============================================================================
#  DODATKOWE - Monte Carlo: mississippi bez sasiadujacych liter
# =============================================================================

def dodatkowe():
    print("\n" + "=" * 70)
    print("DODATKOWE - Monte Carlo: mississippi bez sasiadujacych liter")
    print("=" * 70)

    proby = 100_000

    def brak_sasiadow(perm: list) -> bool:
        return all(perm[i] != perm[i+1] for i in range(len(perm)-1))

    gen = LinearGenerator(a=16807, c=0, m=2**31 - 1, seed=12345)
    litery = list("mississippi")
    trafienia = 0
    for _ in range(proby):
        gen.shuffle(litery)
        if brak_sasiadow(litery):
            trafienia += 1

    wynik = trafienia / proby
    print(f"proby = {proby}")
    print(f"P(brak sasiadujacych jednakowych liter) = {wynik:.4f}")


# =============================================================================
#  URUCHOMIENIE WSZYSTKICH ZADAN
# =============================================================================

if __name__ == "__main__":
    zadanie1()
    zadanie2()
    zadanie1u()
    zadanie2u()
    dodatkowe()

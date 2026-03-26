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


class Bucket:
    def __init__(self, min: float, max: float, count: int = 0):
        self.min = min
        self.max = max
        self.count = count

    def __str__(self):
        return f"[{self.min:.3f} - {self.max:.3f}] {self.count}"


def split_into_buckets(data, bucket_count: int, range_min: float = 0.0, range_max: float = 1.0) -> list:
    """Dzieli zakres (range_min, range_max) na K kubełków i zlicza trafienia."""
    span = range_max - range_min
    per_bucket = span / bucket_count
    buckets = [Bucket(range_min + i * per_bucket, range_min + (i + 1) * per_bucket) for i in range(bucket_count)]

    for number in data:
        bucket_id = int((number - range_min) / per_bucket)
        if bucket_id == bucket_count:
            bucket_id -= 1
        buckets[bucket_id].count += 1

    return buckets


def split_into_buckets_conditional(data, bucket_count: int, condition) -> list:
    """
    Równomierność 'warunkowa' — filtruje dane warunkiem,
    potem dzieli zakres filtrowanych danych na K kubełków.
    """
    filtered = [x for x in data if condition(x)]
    if not filtered:
        return [], 0
    range_min = min(filtered)
    range_max = max(filtered)
    buckets = split_into_buckets(filtered, bucket_count, range_min, range_max)
    return buckets, len(filtered)


# ── Parametry ──────────────────────────────────────────────
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

print(f"\nSrednia   = {avg:.6f}  (oczekiwana: 0.5)")
print(f"Wariancja = {var:.6f}  (oczekiwana: {1/12:.6f})")

# -- Równomierność zwykła --
print(f"\nBuckets (K={K}):")
for bucket in split_into_buckets(probabilities, K):
    print(bucket)

# -- Równomierność warunkowa: x > 0.5 --
cond_buckets, cond_count = split_into_buckets_conditional(probabilities, K, lambda x: x > 0.5)
print(f"\nWarunkowe buckets (x > 0.5), liczba elementow: {cond_count}/{N}:")
for bucket in cond_buckets:
    print(bucket)

# -- Równomierność warunkowa: x < 0.3 --
cond_buckets2, cond_count2 = split_into_buckets_conditional(probabilities, K, lambda x: x < 0.3)
print(f"\nWarunkowe buckets (x < 0.3), liczba elementow: {cond_count2}/{N}:")
for bucket in cond_buckets2:
    print(bucket)

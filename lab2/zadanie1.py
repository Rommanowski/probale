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


class Bucket:
    def __init__(self, min: float, max: float, count: int = 0):
        self.min = min
        self.max = max
        self.count = count

    def __str__(self):
        return f"[{self.min:.2f} - {self.max:.2f}] {self.count}"


def split_into_buckets(data, bucket_count: int) -> list:
    per_bucket = 1.0 / bucket_count
    buckets = [Bucket(i * per_bucket, (i + 1) * per_bucket) for i in range(bucket_count)]

    for number in data:
        bucket_id = int(number * bucket_count)
        if bucket_id == bucket_count:  # skrajny przypadek: number == 1.0
            bucket_id -= 1
        buckets[bucket_id].count += 1

    return buckets


# ── Parametry ──────────────────────────────────────────────
a = 16807
c = 0        # generator multiplikatywny
m = 2**31 - 1

seed = 15
N = 100_000
K = 10

print(f"a = {a}, c = {c}, m = {m}")
print(f"seed = {seed}, N = {N}, K = {K}")

linear_generator = LinearGenerator(a, c, m, seed)
probabilities = list(linear_generator.generate_probabilities(N))

avg = sum(probabilities) / N
var = sum((x - avg) ** 2 for x in probabilities) / N

print(f"\nSrednia  = {avg:.6f}  (oczekiwana: 0.5)")
print(f"Wariancja = {var:.6f}  (oczekiwana: {1/12:.6f})")

buckets = split_into_buckets(probabilities, K)

print(f"\nBuckets (K={K}):")
for bucket in buckets:
    print(bucket)

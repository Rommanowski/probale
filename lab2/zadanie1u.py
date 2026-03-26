class LinearGenerator:
    def __init__(self, a: int, c: int, m: int, seed: int = 1):
        self.a = a
        self.c = c
        self.m = m
        self.seed = seed

    def __generate_number(self) -> int:
        self.seed = (self.a * self.seed + self.c) % self.m
        return self.seed

    def randint(self, n: int) -> int:
        return self.__generate_number() % n


def monte_carlo_orly(N: int, K: int, proby: int = 100_000) -> float:
    gen = LinearGenerator(a=16807, c=0, m=2**31 - 1, seed=12345)
    trafienia = 0
    for _ in range(proby):
        orly = sum(gen.randint(2) for _ in range(N))
        if orly == K:
            trafienia += 1
    return trafienia / proby


N = 10
K = 3

wynik = monte_carlo_orly(N, K)
print(f"P(dokladnie {K} orlow z {N} rzutow) = {wynik:.4f}")

class LinearGenerator:
    def __init__(self, a: int, c: int, m: int, seed: int = 1):
        self.a = a
        self.c = c
        self.m = m
        self.seed = seed

    def __generate_number(self) -> int:
        self.seed = (self.a * self.seed + self.c) % self.m
        return self.seed

    def random(self) -> float:
        return self.__generate_number() / self.m


def monte_carlo_powierzchnia(R: float, proby: int = 100_000) -> float:
    gen = LinearGenerator(a=16807, c=0, m=2**31 - 1, seed=12345)
    trafienia = 0
    for _ in range(proby):
        x = gen.random()
        y = gen.random()

        w_kole_srodek = (x - 0.5)**2 + (y - 0.5)**2 <= 0.5**2
        w_kole_R      = x**2 + y**2 <= R**2

        if w_kole_srodek and w_kole_R:
            trafienia += 1

    return trafienia / proby


R = 0.8
wynik = monte_carlo_powierzchnia(R)
print(f"R = {R}")
print(f"Powierzchnia figury = {wynik:.4f}")

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
        """Losuje liczbę całkowitą z zakresu [0, n-1]"""
        return self.__generate_number() % n

    def shuffle(self, lst: list) -> None:
        """Fisher-Yates shuffle"""
        for i in range(len(lst) - 1, 0, -1):
            j = self.randint(i + 1)
            lst[i], lst[j] = lst[j], lst[i]


def brak_sasiadow(perm: list) -> bool:
    return all(perm[i] != perm[i+1] for i in range(len(perm)-1))


def monte_carlo_mississippi(proby: int = 100_000) -> float:
    gen = LinearGenerator(a=16807, c=0, m=2**31 - 1, seed=12345)
    litery = list("mississippi")
    trafienia = 0
    for _ in range(proby):
        gen.shuffle(litery)
        if brak_sasiadow(litery):
            trafienia += 1
    return trafienia / proby


wynik = monte_carlo_mississippi()
print(f"P(brak sasiadujacych jednakowych liter) = {wynik:.4f}")

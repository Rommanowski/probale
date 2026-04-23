import random

def generate_x() -> int:
    prob = random.random()
    if prob < 0.5:
        return 1
    if prob < 0.7:
        return 2
    if prob < 0.9:
        return 3
    return 4

def generate_y(x: int) -> int:
    prob = random.random()
    if x == 1:
        if prob < 0.2:
            return 1
        return 4
    if x == 2:
        return 1
    if x == 3:
        if prob < 0.5:
            return 2
        return 4
    if x == 4:
        return 3

def create_random_vector() -> tuple[int, int]:
    x = generate_x()
    y = generate_y(x)
    return x, y


results = [[0 for _ in range(5)] for _ in range(5)]

for _ in range(100_000):
    x, y = create_random_vector()
    results[x][y] += 1


print("X/Y", end="\t")
for i in range(1, 5):
    print(i, end="\t")
print()
for i in range(1, 5):
    print(i, end="\t")
    for j in range(1, 5):
        print(results[i][j], end="\t")
    print()


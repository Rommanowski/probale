from client_32 import MyClient
import random
import matplotlib.pyplot as plt

client = MyClient()
change_val = client.change_val


if __name__ == '__main__':
    N = 100_000

    nums = [random.random() for _ in range(N)]
    nums = list(map(change_val, nums))
    plt.hist(nums)
    plt.show()
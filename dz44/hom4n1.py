from dz3.dz3nom1 import thv


def swap(pl, k):
    k %= len(pl)
    return pl[-k:] + pl[:-k]

if __name__ == "__main__":
    print(swap(thv(input()), int(input())))

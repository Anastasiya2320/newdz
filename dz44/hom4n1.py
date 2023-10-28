from dz3.dz3nom1 import thv


def swap(pl, k):
    k %= len(pl)
    return pl[-k:] + pl[:-k]

print(swap(thv(input()), int(input())))

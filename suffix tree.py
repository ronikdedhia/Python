class suffix:
    def __init__(self):
        self.index = 0
        self.rank = [0, 0]


def buildSuffixArray(txt, n):
    suffixes = [suffix() for _ in range(n)]
    for i in range(n):
        suffixes[i].index = i
        suffixes[i].rank[0] = (ord(txt[i]) -
                            ord("a"))
        suffixes[i].rank[1] = (ord(txt[i + 1]) -
                            ord("a")) if ((i + 1) < n) else -1
        suffixes = sorted(
            suffixes, key=lambda x: (x.rank[0], x.rank[1]))
        ind = [0] * n
        k = 4

    while (k < 2 * n):
        rank = 0
        prev_rank = suffixes[0].rank[0]
        suffixes[0].rank[0] = rank
        ind[suffixes[0].index] = 0

    for i in range(1, n):
        if (suffixes[i].rank[0] == prev_rank and
                suffixes[i].rank[1] == suffixes[i - 1].rank[1]):
            prev_rank = suffixes[i].rank[0]
            suffixes[i].rank[0] = rank
        else:
            prev_rank = suffixes[i].rank[0]
            rank += 1
            suffixes[i].rank[0] = rank
            ind[suffixes[i].index] = i

    for i in range(n):
        nextindex = suffixes[i].index + k // 2
        suffixes[i].rank[1] = suffixes[ind[nextindex]].rank[0] \
            if (nextindex < n) else -1
        suffixes = sorted(
            suffixes, key=lambda x: (
                x.rank[0], x.rank[1]))
        k *= 2
        suffixArr = [0] * n

    for i in range(n):
        suffixArr[i] = suffixes[i].index
        return suffixArr


def printArr(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
        print()


if __name__ == "__main__":
    txt = input()
    n = len(txt)

    suffixArr = buildSuffixArray(txt, n)
    print("Following is suffix array for", txt)
    printArr(suffixArr, n)

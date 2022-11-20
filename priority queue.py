H = [0]*50
size = -1

def parent(i):
 return (i - 1) // 2

def leftChild(i):
 return ((2 * i) + 1)

def rightChild(i):
 return ((2 * i) + 2)

def shiftUp(i):
    while (i > 0 and H[parent(i)] < H[i]):
        swap(parent(i), i)
        i = parent(i)

def shiftDown(i) :
    maxIndex = i
    l = leftChild(i)

    if (l <= size and H[l] > H[maxIndex]) :
        maxIndex = l
        r = rightChild(i)
        if (r <= size and H[r] > H[maxIndex]) :
            maxIndex = r

    if (i != maxIndex) :
        swap(i, maxIndex)
        shiftDown(maxIndex)
        while (i > 0 and H[parent(i)] < H[i]) :
            swap(parent(i), i)
            i = parent(i)

def shiftDown(i) :
    maxIndex = i
    l = leftChild(i)

    if (l <= size and H[l] > H[maxIndex]) :
        maxIndex = l
    r = rightChild(i)

    if (r <= size and H[r] > H[maxIndex]) :
        maxIndex = r
    if (i != maxIndex) :
        swap(i, maxIndex)
        shiftDown(maxIndex)
        def changePriority(i,p) :
            oldp = H[i]
            H[i] = p

    if (p > oldp) :
        shiftUp(i)

    else :
        shiftDown(i)

def getMax() :
    return H[0]

def Remove(i) :
    H[i] = getMax() + 1

    shiftUp(i)
    extractMax()

def swap(i, j) :

    temp = H[i]
    H[i] = H[j]
    H[j] = temp

    insert(45)
    insert(20)
    insert(14)
    insert(12)
    insert(31)
    insert(7)
    insert(11)
    insert(13)
    insert(7)

    i = 0
    print("Priority Queue : ", end = "")
    while (i <= size) :
        print(H[i], end = " ")
        i += 1

    print()
    print("Node with maximum priority :" , extractMax())
    print("Priority queue after extracting maximum : ", end = "")
    j = 0
    while (j <= size) :
        print(H[j], end = " ")
        j += 1

    print()
    changePriority(2, 49)
    print("Priority queue after priority change : ", end = "")
    k = 0
    while (k <= size) :
        print(H[k], end = " ")
        k += 1

    print()

    Remove(3)
    print("Priority queue after removing the element : ", end = "")
    l = 0
    while (l <= size) :
        print(H[l], end = " ")
        l += 1
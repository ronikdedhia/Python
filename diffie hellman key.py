from random import randint
if __name__ == '__main__':
    P = 23
    G = 9
    print('The Value of P is :%d' % (P))
    print('The Value of G is :%d' % (G))
    # Alice will choose the private key a
    a = 4
    print('The Private Key a for Alice is :%d' % (a))
    # gets the generated key
    x = int(pow(G, a, P))

    # Bob will choose the private key b
    b = 3
    print('The Private Key b for Bob is :%d' % (b))

    # gets the generated key
    y = int(pow(G, b, P))

    # Secret key for Alice
    ka = int(pow(y, a, P))

    # Secret key for Bob
    kb = int(pow(x, b, P))

    print('Secret key for the Alice is : %d' % (ka))
    print('Secret Key for the Bob is : %d' % (kb))

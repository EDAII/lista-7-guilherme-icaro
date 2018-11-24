def reconstruct(i, w):
    itens = []
    size = 0

    while True:
        if taken[i][w]:
            w -= W[i]
            itens.append(i)
            size += 1

        if i == 0:
            break

        i -= 1

    itens.reverse()

    for item in itens:
        print(W[item])

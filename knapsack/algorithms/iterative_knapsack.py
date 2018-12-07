def iterative_knapsack(quantity, weight, iterative_matrix, W, V, visual_iterative_matrix, table, headers):

    for i in range(quantity+2):
        for w in range(weight+1):
            if i == 0 or w == 0:
                iterative_matrix[i][w] = 0
            elif W[i - 1] <= w:
                iterative_matrix[i][w] = max(V[i-1] + iterative_matrix[i-1][w - W[i - 1]], iterative_matrix[i-1][w])
            else:
                iterative_matrix[i][w] = iterative_matrix[i-1][w]

            visual_iterative_matrix[i][w+1] = str(iterative_matrix[i][w])

    table.create_knapsack_matrix(visual_iterative_matrix, headers)

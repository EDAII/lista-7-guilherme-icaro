def iterative_knapsack(quantity, weight, iterative_matrix, W, V, visual_iterative_matrix, table, headers):
    i = 1

    for i in range(weight+1):
        iterative_matrix[0][i] = 0
        visual_iterative_matrix[0][i+1] = str(iterative_matrix[0][i])

    for i in range(quantity+1):
        iterative_matrix[i][1] = 0
        visual_iterative_matrix[i+1][1] = str(iterative_matrix[i][1])

        for w in range(1, weight+1):
            if W[i] <= w:
                iterative_matrix[i][w] = max(
                    V[i] + iterative_matrix[i-1][w - W[i]],
                    iterative_matrix[i-1][w]
                )

                visual_iterative_matrix[i+1][w+1] = str(iterative_matrix[i][w])

            else:
                iterative_matrix[i][w] = iterative_matrix[i-1][w]
                visual_iterative_matrix[i+1][w+1] = str(iterative_matrix[i][w])

        table.create_knapsack_matrix(visual_iterative_matrix, headers)

def recursive_knapsack(i, w, memoization_matrix, W, V, visual_matrix, table, headers):

    if i < 0 or w <= 0:
        return 0

    if memoization_matrix[i][w] != -1:
        return memoization_matrix[i][w]

    if W[i] > w:
        memoization_matrix[i][w] = recursive_knapsack(i - 1, w, memoization_matrix,  W, V, visual_matrix, table, headers)
        return memoization_matrix[i][w]

    not_take = recursive_knapsack(i - 1, w, memoization_matrix,  W, V, visual_matrix, table, headers)
    take = recursive_knapsack(i - 1, w - W[i], memoization_matrix,  W, V, visual_matrix, table, headers) + V[i]

    if take > not_take:
        memoization_matrix[i][w] = take
        visual_matrix[i+1][w+1] = str(memoization_matrix[i][w])
        # taken[i][w] = True
    else:
        memoization_matrix[i][w] = not_take
        visual_matrix[i+1][w+1] = str(memoization_matrix[i][w])

    table.create_knapsack_matrix(visual_matrix, headers)

    return memoization_matrix[i][w]

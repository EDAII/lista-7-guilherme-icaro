from tabulate import tabulate
import random
import numpy

class GenerateTable():

    def create_knapsack_matrix(self, elements, headers):
        matrix = [headers]

        for element in elements:
            matrix.append(element)

        print(tabulate(matrix, headers="firstrow"))

    def build_header(self, backpack_space):
        headers = ["Coins/Capacity"]

        for i in range(0, backpack_space+1, 1):
            headers.append(str(i))

        return headers

    def build_line(self, results):
        pass

    def build_initial_matrix(self, quantity_elements, weight, coins):
        matrix = []

        for i in range(0, len(coins), 1):
            line = []
            line.append(self.build_header_coins(coins, i+1))
            line += self.build_initial_line(weight+1)

            matrix.append(line)

        return matrix

    def build_header_coins(self, coins, quantity):
        coin_list = '{ '

        for i in range(1, quantity, 1):
            if i is 0:
                coin_list += str(coins[i])
            elif i < quantity-1:
                coin_list += (str(coins[i]) + ', ')
            else:
                coin_list += str(coins[i])

        coin_list += ' }'

        return coin_list

    def build_initial_line(self, quantity):
        results = []

        for i in range(0, quantity, 1):
            results.append('-')

        return results

    def update_element_in_matrix(self, matrix, row, column, response):
        matrix[row][column] = str(response)

        return matrix


def recursive_knapsack(i, w):

    if i < 0 or w <= 0:
        return 0

    if memoization_matrix[i][w] != -1:
        return memoization_matrix[i][w]

    if W[i] > w:
        memoization_matrix[i][w] = recursive_knapsack(i - 1, w)
        return memoization_matrix[i][w]

    not_take = recursive_knapsack(i - 1, w)
    take = recursive_knapsack(i - 1, w - W[i]) + V[i]

    if take > not_take:
        memoization_matrix[i][w] = take
        visual_matrix[i][w] = str(memoization_matrix[i][w])
        taken[i][w] = True
    else:
        memoization_matrix[i][w] = not_take
        visual_matrix[i][w] = str(memoization_matrix[i][w])

    # table.create_knapsack_matrix(visual_matrix, headers)

    return memoization_matrix[i][w]

def iterative_knapsack(quantity, weight, iterative_matrix):
    i = 1

    for i in range(weight):
        iterative_matrix[0][i+1] = 0
        visual_iterative_matrix[0][i+1] = str(iterative_matrix[0][i+1])

    i = 1

    for i in range(quantity):
        iterative_matrix[i][1] = 0
        visual_iterative_matrix[i][1] = str(iterative_matrix[i][1])

        w = 2

        for w in range(2, weight+1):
            if W[i] <= w:
                iterative_matrix[i][w] = max(
                    V[i] + iterative_matrix[i-1][w - W[i]],
                    iterative_matrix[i-1][w]
                )

                visual_iterative_matrix[i][w] = str(iterative_matrix[i][w])

            else:
                iterative_matrix[i][w] = iterative_matrix[i-1][w]
                visual_iterative_matrix[i][w] = str(iterative_matrix[i][w])

        # table.create_knapsack_matrix(visual_iterative_matrix, headers)

def unbounded_knapsack(w, n, V, W):

    dp = [0 for i in range(w + 1)]

    ans = 0

    for i in range(w + 1):
        for j in range(n):
            if (W[j] <= i):
                dp[i] = max(dp[i], dp[i - W[j]] + V[j])

    return dp[w]

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

from tabulate import tabulate
import random
import numpy

import algorithms.iterative_knapsack as iterative
import algorithms.recursive_knapsack as recursive
import algorithms.unbounded_knapsack as unbounded
import algorithms.reconstruct_elements as reconstruct

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

        for i in range(len(coins)+1):
            line = []
            line.append(self.build_header_coins(coins, i))
            line += self.build_initial_line(weight+1)

            print(line)

            matrix.append(line)

        return matrix

    def build_header_coins(self, coins, quantity):
        coin_list = '{ '

        for i in range(0, quantity, 1):
            if i < quantity-1:
                coin_list += (str(coins[i]) + ', ')
            else:
                coin_list += str(coins[i])

        coin_list += ' }'

        return coin_list

    def build_initial_line(self, quantity):
        results = []

        for i in range(quantity):
            results.append('-')

        return results

    def update_element_in_matrix(self, matrix, row, column, response):
        matrix[row][column] = str(response)

        return matrix

table = GenerateTable()

WEIGHT = 16
QUANTITY = 5
LIMIT = 100

memoization_matrix = numpy.full((QUANTITY+1, WEIGHT), -1)
visual_matrix = []

W = [1, 5, 10, 25, 50]
V = [1, 5, 10, 25, 50]

headers = table.build_header(WEIGHT)

visual_matrix = table.build_initial_matrix(QUANTITY, WEIGHT, V)

print(visual_matrix)

visual_matrix = table.create_knapsack_matrix(visual_matrix, headers)

# print(tabulate(visual_matrix, headers="firstrow"))

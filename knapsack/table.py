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

import numpy as np


def main():
    test_cases = int(input())

    for i in range(test_cases):
        people_size = tuple(map(int, input().split(' ')))
        matrix = np.zeros((4, people_size[1]))
        north = 0
        south = 1
        west = 2
        east = 3

        for p in range(people_size[0]):
            person = input().split(' ')
            x = int(person[0])
            y = int(person[1])
            direction = person[2]

            if 'N' == direction:
                matrix[north][y + 1] = matrix[north][y + 1] + 1
            elif 'S' == direction:
                matrix[south][y - 1] = matrix[south][y - 1] + 1
            elif 'E' == direction:
                matrix[east][x + 1] = matrix[east][x + 1] + 1
            elif 'W' == direction:
                matrix[west][x - 1] = matrix[west][x - 1] + 1

        x_axis = np.add(np.cumsum(matrix[east]), np.cumsum(matrix[west][::-1])[::-1])
        y_axis = np.add(np.cumsum(matrix[north]), np.cumsum(matrix[south][::-1])[::-1])
        print(f'Case #{i + 1}: {np.argmax(x_axis)} {np.argmax(y_axis)}')

if __name__ == '__main__':
    main()
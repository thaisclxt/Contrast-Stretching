import numpy as np

def contrast_stretching(row, column):
    smaller_range_value = 0
    larger_range_value = 7

    image = [[0] * row] * column
    for x in range(row):
        for y in range(column):
            image[x][y] = int(input())
            print("image[{0}][{1}] = {2}".format(x, y, image[x][y]))

    a = np.array(image).flatten()
    smaller_image_value = min(a)
    larger_image_value = max(a)

    new_image = [[0] * row] * column
    for x in range(row):
        for y in range(column):
            print("({0} - {1}) * (({2} - {3}) / ({4} - {1}) + {3}) ".format(image[x][y], smaller_image_value, larger_range_value, smaller_range_value, larger_image_value))
            new_image[x][y] = (image[x][y] - smaller_image_value) * ((larger_range_value - smaller_range_value) / (larger_image_value - smaller_image_value)) + smaller_range_value

    print(new_image)

row = int(input("Entre com a quantidade de linhas: "))
column = int(input("Entre com a quantidade de colunas: "))

contrast_stretching(row, column)
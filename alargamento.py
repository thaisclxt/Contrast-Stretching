import numpy as np

def contrast_stretching(row, column):
    smaller_range_value = 0
    larger_range_value = 7

    image = np.zeros((row, column), dtype=int)
    for x in range(row):
        for y in range(column):
            image[x][y] = int(input())
    
    a = np.array(image).flatten()
    smaller_image_value = min(a)
    larger_image_value = max(a)

    new_image = np.zeros((row, column), dtype=int)
    for x in range(row):
        for y in range(column):
            new_image[x][y] = round((image[x][y] - smaller_image_value) * ((larger_range_value - smaller_range_value) / (larger_image_value - smaller_image_value)) + smaller_range_value)
            
    print(new_image)

row = int(input("Entre com a quantidade de linhas: "))
column = int(input("Entre com a quantidade de colunas: "))

contrast_stretching(row, column)
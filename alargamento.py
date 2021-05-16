import numpy as np

class Image:
    
    def __init__(self, row: int, column: int, smaller_range_value: int, larger_range_value: int) -> None:
        self.row = row
        self.column = column
        self.a = smaller_range_value
        self.b = larger_range_value

        self.image = self.set_pixels()
        self.c, self.d = self.get_max_and_min()

    def set_pixels(self) -> 'np.ndarray':
        image = np.zeros((self.row, self.column), dtype=int)

        for x in range(self.row):
            for y in range(self.column):
                image[x][y] = int(input())

        return image

    def get_max_and_min(self) -> int:
        f = np.array(self.image).flatten()
        return min(f), max(f)

    def contrast_stretching(self) -> None:
        new_image = np.zeros((self.row, self.column), dtype=int)

        for x in range(self.row):
            for y in range(self.column):
                new_image[x][y] = round((self.image[x][y] - self.c) * ((self.b - self.a) / (self.d - self.c)) + self.a)
                
        print(new_image)

def main() -> None:
    row = int(input("Entre com a quantidade de linhas: "))
    column = int(input("Entre com a quantidade de colunas: "))
    smaller_range_value = int(input("Entre com o menor valor da faixa: "))
    larger_range_value = int(input("Entre com o maior valor da faixa: "))

    image = Image(row, column, smaller_range_value, larger_range_value)
    image.contrast_stretching()

if __name__ == "__main__":
    main()
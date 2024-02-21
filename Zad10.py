#Zad10

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fibonacci_gen = fibonacci_generator()
for _ in range(10):
    print(next(fibonacci_gen))


def read_large_file(file_path, encoding='utf-8'):
    with open(file_path, 'r', encoding=encoding) as file:
        for line in file:
            yield line.strip()

file_path = 'text.txt'
lines_generator = read_large_file(file_path)

for _ in range(3):
    print(next(lines_generator))

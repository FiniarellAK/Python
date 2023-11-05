class Ai:
    def __init__(self, iterable, n):
        self.iterable = iterable
        self.n = n
        self.val1 = 1
        self.val2 = 1
        self.current_idx = 0

    def __next__(self):
        if self.current_idx >= self.n:
            raise StopIteration

        if self.current_idx == 0 or self.current_idx == 1:
            value = 1
        else:
            value = self.val1 + self.val2
            self.val1 = self.val2
            self.val2 = value
        self.current_idx += 1
        return value


class A:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return Ai(self, self.n)


def main():
    a = A(20)
    for i in a:
        print(i)


if __name__ == '__main__':
    main()

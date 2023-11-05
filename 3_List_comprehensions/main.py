def main(i):
    prev = 1
    cur = 1
    counter = 0
    print(prev)
    while counter < i-1:
        yield cur
        cur += prev
        prev = cur - prev
        counter += 1


if __name__ == '__main__':
        Fibonacci = (cur for cur in main(10))
        for i in Fibonacci:
            print(i)
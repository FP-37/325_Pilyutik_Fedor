def main():
    inpt = input().strip().split()
    n = int(inpt[0])
    if len(inpt) < 2:
        for row in [[i + j * n for j in range(n)] for i in range(n)]:
            print(*row)
    else:
        m = int(inpt[1])
        for row in [[i + j * n for j in range(m)] for i in range(n)]:
            print(*row)

if __name__ == "__main__":
    main()
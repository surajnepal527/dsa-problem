def solve(A):
    if A == 1:
        return 0
    if A == 2:
        return 1

    for i in range(2, A):
        if i * i > A:
            break
        if A % i == 0:
            return 0

    return 1


if __name__ == '__main__':
    ans = solve(12)
    print(f'Ans, {ans}')

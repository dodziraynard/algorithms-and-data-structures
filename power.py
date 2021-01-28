def power(a, n):
    if n == 0:
        return 1
    if n == 1:
        return a
    return a * power(a, n-1)


if __name__ == "__main__":
    print(power(3, 5))  # 243

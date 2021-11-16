def check(n):
    summa = 0
    for i in [int(alkio) for alkio in str(n)]:
        summa += i
    if summa % 7 == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    print(check(14)) # False
    print(check(16)) # True
    print(check(123)) # False
    print(check(777)) # True
    print(check(9999999)) # True
    
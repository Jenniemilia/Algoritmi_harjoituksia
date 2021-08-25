def count(s):
    pino = []
    n = len(s)
    for i in range(n):
        pino.append(s[i])
        if len(pino) >= 2 and pino[-2]== "(" and pino[-1] == ")":
            pino.pop()
            pino.pop()
    return len(pino)    

if __name__ == "__main__":
    print(count("(()())")) # 0
    print(count("))))))")) # 6
    print(count("((())(")) # 2
    print(count(")("))
def count(t):
    n = len(t)
    laskuri = 0    
    p= sorted(t)
    for i in range(n):
        if p[i-1] - p[i] == -1:
            continue
        elif p[i-1] - p[i] != -1:          
            laskuri += 1
    return laskuri

if __name__ == "__main__":
    print(count([4, 1, 5, 3])) # 2
    print(count([4, 2, 1, 3])) # 1
    print(count([5, 2, 7, 6, 3, 9])) # 3

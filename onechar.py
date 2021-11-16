def count(s):
    pituus = len(s)
    laskuri = 0
    osajonot = 0
    for i in range(pituus):
        if i != 0 and (s[i-1]) == (s[i]):
            osajonot += 1
        else:
            osajonot = 1
        laskuri += osajonot                
    return laskuri

if __name__ == "__main__":
    print(count("aaa")) # 6
    print(count("abbbcaa")) # 11
    print(count("abcde")) # 5
    
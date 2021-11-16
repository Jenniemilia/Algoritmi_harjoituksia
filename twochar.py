def count(s):
    pituus = len(s)
    ed_erimerkki = -1
    erimerkki = -1
    laskuri = 0

    for i in range(1, pituus):
        if abs(ord(s[i-1]) != ord(s[i])):
            if ed_erimerkki == -1 or s[i] != s[ed_erimerkki]:
                erimerkki = ed_erimerkki
            ed_erimerkki = i -1
        laskuri += ed_erimerkki- erimerkki
                 
    return laskuri

if __name__ == "__main__":
    print(count("aaaa")) # 0
    print(count("abab")) # 6
    print(count("aabacba")) # 8
    
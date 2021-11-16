def count(s):
    merkkijono = s
    laskuri = 0
    kirjaimet = {}

    for i in merkkijono:
        if i not in kirjaimet:
            kirjaimet[i] = 0
        kirjaimet[i] += 1
        laskuri += kirjaimet[i]
    return laskuri

if __name__ == "__main__":
    print(count("aaa")) # 6
    print(count("abcd")) # 4
    print(count("ababca")) # 10
    
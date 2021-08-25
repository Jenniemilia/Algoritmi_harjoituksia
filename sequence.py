
def generate(n:int):
    if n == 1:
        return str(1)
    j = "1" # ensimmainen arvo
    
    def apufunktio(j:str):
        tuloste = "" 
        i = 0
        while i < len(j):
            count = 1
            while i+1 < len(j) and j[i] == j[i+1]:
                count += 1 #laskee monta perakkain
                i += 1
            tuloste = tuloste + str(count) + j[i]
            i += 1
        return tuloste  

    for i in range (n-1):
        j = apufunktio(j)
    return j

if __name__ == "__main__":
    print(generate(1)) # 1
    print(generate(2)) # 11
    print(generate(3)) # 21
    print(generate(4)) # 1211
    print(generate(5)) # 111221
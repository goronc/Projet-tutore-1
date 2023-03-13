def recup_indice(chaine,alphabet):
    i = 0
    while(alphabet[i] != chaine):
            i+=1
    return i
        
          
def chiffrer(chaine,cle,alphabet):
    res = ""
    j = 0
    for i in range(len(chaine)):
        if chaine[i] == " ":
            res += " "
        else:
            decalage = alphabet.index(chaine[i]) + alphabet.index(cle[j % len(cle)])
            res += alphabet[decalage % len(alphabet)]
            j += 1
    return res


def dechiffrer(chaine,cle,alphabet):
    res = ""
    j = 0
    for i in range(len(chaine)):
        if chaine[i] == " ":
            res += " "
        else:
            decalage = alphabet.index(chaine[i]) - alphabet.index(cle[j % len(cle)])
            res += alphabet[decalage % len(alphabet)]
            j += 1
    return res
            


    


alphabet = "abcdefghijklmnopqrstuvwxyz"
chaine = "hello world"
cle = "cle"

x = chiffrer(chaine,cle,alphabet)
print(x)
y =dechiffrer("jppnz aqcpf",cle,alphabet)
print(y)





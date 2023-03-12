import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

alphabet = "abcdefghijklmnopqrstuvwxyz"

def chiffrer(chaine,decalage):  
    res = ''
    for i in range(len(chaine)):    # parcour de la chaine a chiffrer
        j = 0
        if chaine[i] == ' ':    #exception si le caractere est un espace on laisse l'espace
            res += ' '
        else:
            while(alphabet[j] != chaine[i]):    # recherche du caractere a chiffrer dans l'alphabet de référence
                j += 1
            if j + decalage > len(alphabet):    # cas si le caractere + le decalage > 26 
                j = len(alphabet) - j       # si oui on retourne au debut
                res += alphabet[j]
            else:                           # si non on ajoute juste a res le caractere + le decalage
                res += alphabet[j+decalage]
    return res

def dechiffrer(chaine,decalage):
    res = ''
    for i in range(len(chaine)):    # parcour de la chaine a chiffrer
        j = 0
        if chaine[i] == ' ':     #exception si le caractere est un espace on laisse l'espace
            res += ' '
        else:
            while(alphabet[j] != chaine[i]):         # recherche du caractere a chiffrer dans l'alphabet de référence
                j += 1
            if j - decalage < 0:            # cas si le caractere - le decalage < 0
                j = len(alphabet) - abs(j)  # si oui on continue par la fin (valeurs absolus car j < 0 dans ce cas la)
                res += alphabet[j]
            else:                           # si non on ajoute juste a res le caractere - le decalage
                res += alphabet[j-decalage] 
    return res

def frequence_lettre(chaine):
    dico = {}
    for i in range(len(chaine)):
        if chaine[i] in dico.keys():
            dico[chaine[i]] += 1 
        else:
            dico[chaine[i]] = 1 
    return dico

def max_val_dico(dico):
    liste_keys = list(dico.keys())
    liste_keys.remove(" ")
    liste_value = list(dico.values())
    indice = 0
    for i in range(len(liste_value)):
        if liste_value[i] > liste_value[indice]:
            indice = i
    return liste_keys[indice]


def decrypter(chaine,alphabet):
    e_chifrer = max_val_dico(frequence_lettre(chaine))
    print(e_chifrer) 
    return 0

# Test ATTENTION carractere spéciaux non compatible
# 2 possibilitées a choisir pour les caracteres spéciaux  soit les rajoutez a la fin de l'alphabet de reference (abc..xyz!?/:;.?,) soit les laissez tel quel comme les espaces
x = "a force daller en avant il parvint au point ou le brouillard de la fusillade devenait  transparent si bien que les tirailleurs de la ligne ranges et a laffut derriere leur levee de paves et les tirailleurs de la banlieue masses a langle de la rue se montrerent soudainement  quelque chose qui remuait dans la fumee au moment ou gavroche debarrassait de ses cartouches un sergent gisant pres dune borne une balle frappa le cadavre"
y = 3

z = chiffrer(x,y)

w = dechiffrer(z,y)

print(w == x)
freq = frequence_lettre(z)
max_val_dico(frequence_lettre(x))
decrypter(z,alphabet)

# fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
# categories = [i for i in freq.keys()]
# ax.set_title("Fréquence des lettre dans la chaine de caractere")
# ax.set_ylabel("Nb répétition dans la chaine")
# ax.set_xlabel("Lettres")

# ax.bar(categories,  freq.values())
# plt.show()
 

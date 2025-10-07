#### Fonction secondaire


def ispalindrome(p):
    a = str(n)
    b = a[::-1]
    if a == b:
        return True
    else: 
        return False
    
    

#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()

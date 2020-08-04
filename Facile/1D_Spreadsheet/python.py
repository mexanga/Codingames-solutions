import sys
import math
import re

# On récupère le nombre d'entrée
n = int(input())

# On initialise la liste des entrées.
# Cette liste nous permettra d'afficher les entrées une fois traitées.
inputs = list()

# Vérifie si l'argument est "dynamique" (sous la forme de "$0" et "$42")
def isArgDynamic (arg,inputs=inputs):
    match = re.search(r'^\$(\d+)$', str(arg))
    if match is None: return False
    return match.span(1)[1] > 1

# Récupère la valeur de l'argument à l'adresse donnée sous sa forme dynamique (par exemple "0" pour "$0").
# Dans le cas où l'argument donné n'est pas dynamique, on renvoie None.
def getArgDynamic (arg,inputs=inputs):
    match = re.search(r'^\$(\d+)$', arg)
    input = inputs[int(match.group(1))]
    if isinstance(input, list): return None
    return input

# Fonction principale
def main(inputs=inputs):

    # Pour chaque entrée...
    for i in range(n):
        # on récupère les valeurs.
        operation, arg_1, arg_2 = input().split()
        # Si l'opération est VALUE...
        if operation == 'VALUE':
            # ... et que l'argument n'est pas dynamique (soit un nombre), alors...
            if False == isArgDynamic(arg_1):
                #... on ajoute la valeur dans la liste des entrées...
                inputs.append(arg_1)
                #... et on passe à l'entrée suivante.
                continue
        # Sinon on ajoute les valeurs dans la liste des entrées.
        inputs.append([operation, arg_1, arg_2])

    # On initialise les valeurs utilisées pour la boucle.
    #
    # La limite est utilisée pour éviter les boucles infinies.
    # Sa valeur par défaut peut être modifié si nécessaire.
    limit = 10000000;
    #
    # Le curseur correspond à la position de l'entrée.
    # Sa valeur par défaut est -1.
    cursor = -1;

    # On démarre la boucle dans laquelle on traitera les entrées.
    while True:
        # On décrémente la limite.
        limit = limit - 1

        # Si la limite a atteint 0 (voire moins), on arrète la boucle.
        if limit < 1: break

        # On incrémente le curseur. Si sa valeur a atteint n (le nombre d'entrée), on revient à 0.
        cursor = (cursor + 1) % n

        # On déclare la variable input pour faciliter la lecture (voire les performances du programme)
        input = inputs[cursor]

        # Si l'entrée est une chaine de caractère, alors...
        if isinstance(input, str): 
            # ... on converti la valeur en nombre...
            inputs[cursor] = int(input)
            # ... et on passe à l'entrée suivante.
            continue

        # Si l'entrée est un nombre, alors...
        if isinstance(input, int): 
            # ... on passe à l'entrée suivante.
            continue

        # On récupère les valeurs de l'entrée.
        operation, arg_1, arg_2 = input

        # Si le premier argument est "dynamique", alors...
        if isArgDynamic(arg_1):
            # ... on récupère la valeur de l'argument (cf fonction getArgDynamique).
            arg_1 = getArgDynamic(arg_1)

        # Si le second argument est "dynamique", alors...
        if isArgDynamic(arg_2):
            # ... on récupère la valeur de l'argument (cf fonction getArgDynamique).
            arg_2 = getArgDynamic(arg_2)

        # Si l'un des arguments n'a pas pu récupéré sa valeur (soit la valeur vaut None), alors...
        if (arg_1 is None or arg_2 is None):
            # ... on passe à l'entrée suivante.
            continue

        # Si l'opération est "VALUE"...
        if operation == 'VALUE':
            # ... et si le premier argument n'est pas "dynamique", alors...
            if False is isArgDynamic(arg_1):
                # ... on enlève l'entrée dans la liste des entrées...
                inputs.remove(inputs[cursor])
                # ... et on insère la valeur du premier argument dans la liste des entrées à la position donnée.
                inputs.insert(cursor, arg_1)

        # Si l'opération est "ADD", alors...
        if operation == 'ADD':
            # ... on additionne les arguments...
            valeur = int(arg_1) + int(arg_2)
            # ... on enlève l'entrée dans la liste des entrée...
            inputs.remove(inputs[cursor])
            # ... et on insère la valeur de l'addition dans la liste des entrées à la position donnée.
            inputs.insert(cursor, valeur)

        # Si l'opération est "MULT", alors...
        if operation == 'MULT':
            # ... on multiplie les arguments...
            valeur = int(arg_1) * int(arg_2)
            # ... on enlève l'entrée dans la liste des entrée...
            inputs.remove(inputs[cursor])
            # ... et on insère la valeur de la multiplication dans la liste des entrées à la position donnée.
            inputs.insert(cursor, valeur)

        # Si l'opération est "SUB", alors...
        if operation == 'SUB':
            # ... on soustrait les arguments...
            valeur = int(arg_1) - int(arg_2)
            # ... on enlève l'entrée dans la liste des entrée...
            inputs.remove(inputs[cursor])
            # ... et on insère la valeur de la soustraction dans la liste des entrées à la position donnée.
            inputs.insert(cursor, valeur)

        # Si le curseur a atteint la dernière position...
        if cursor == n - 1:
            # ... et que toutes les valeurs de la liste des entrées sont des nombres, alors...
            if all(isinstance(x, int) for x in inputs):
                # ... on arrête la boucle.
                break

    # On affiche chaque valeur de la liste des entrées.
    [print(value) for value in inputs]


# On exécute la fonction principale.
main()

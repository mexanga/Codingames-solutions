import sys
import math

# Don't let the machines win. You are humanity's last hope...

width = int(input())  # Longueur de la map
height = int(input())  # Hauteur de la map

# On initialise la map
map = list() 


# Fonction principale
def main():
    # On initialise la ligne à afficher
    res = ''
    # Pour chaque point sur l'axe y
    for i in range(height):
        line = input()  # On récupère les points (les points ont comme valeur soit 0, soit .)
        points = list(line) # On sépare les points
        map.append(points) # On ajoute la ligne dans la map
    
    # Pour chaque point sur l'axe y (on recommence le parcours)
    for i in range(height):
        # Pour chaque point sur l'axe x
        for j in range(width):
            point = map[i][j] # On récupère le point
            
            # Si le point est '.', alors on passe au point suivant
            if '.' is point: continue
            
            # On récupère les voisins les plus proche du point actuel (droite et bas)
            voisinD = voisinDroite(j,i)
            voisinB = voisinBas(j,i)
            
            # On affiche les coordonnées du point actuel, le voisin de droite le plus proche ainsi que le voisin d'en bas le plus proche.
            # De telles manieres a ce que l'on est un format : x1 y1 x2 y2 x3 y3
            print(f'{j} {i} {voisinD} {voisinB}')


# Récupère le voisin d'en bas le plus proche
# Le point le plus proche doit valoir '0'. 
# Autrement ce ne sont pas ces coordonnées qui seront retournées mais "-1 -1".
# "-1 -1" permet de definir un voisin qui n'existe pas. 
def voisinBas(x,y,*,map=map):

    cursor = y # On définit le curseur à partir des coordonnées données
    limit = len(map) - 1 # On retourne la taille de la map (sur l'axe y).

    # On démarre une boucle while afin d'établir un parcours
    while True:
        cursor = cursor + 1 # On incrémente le curseur

        # Si le curseur a atteint la limite, alors on retourne comme coordonnées "-1 -1".
        # Si la parcours n'a pas été quitté plus tot, cela veut dire que le voisin n'existe pas.
        if cursor > limit: return '-1 -1'

        point = map[cursor][x] # On récupère le point

        # Si le point vaut '.' alors on passe au point suivant.
        if '.' is point: continue
        # Si le point vaut '0' alors on affiche les coordonnées du point.
        if '0' is point: return f'{x} {cursor}'


# Récupère le voisin de droite le plus proche.
# Fonctionne de la même manière que voisin bas.
def voisinDroite(x,y,*,map=map):

    cursor = x # On définit le curseur à partir des coordonnées données.
    limit = len(map[y]) - 1 # On retourne la taille de la map (sur l'axe x).
    
    # On démarre une boucle while afin d'établir un parcours
    while True:
        cursor = cursor + 1 # On inrécremente le curseur

        # Si le curseur a atteint la limite, alors on retourne comme coordonnées "-1 -1".
        # Si la parcours n'a pas été quitté plus tot, cela veut dire que le voisin n'existe pas.
        if cursor > limit: return '-1 -1'

        point = map[y][cursor] # On récupère le point

        # Si le point vaut '.' alors on passe au point suivant.
        if '.' is point: continue
        # Si le point vaut '0' alors on affiche les coordonnées du point.
        if '0' is point: return f'{cursor} {y}'


# On démarre la fonction principale
main()

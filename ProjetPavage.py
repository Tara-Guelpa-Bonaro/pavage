"""
Projet Vasarely
Auteur : T. Guelpa Bonaro
Date : 04.03.2019
Ce programme affiche un pavage déformé inspiré des oeuvres de Vasarely.
"""

import turtle
import math
#from deformation import deformation

limite_inf=-300
limite_sup=300
cote=15
coul1="lime"
coul2="black"
coul3="green"
centre_def=( -200, -150, 0)
r=300
def deformation(p, centre, rayon):
    """ Calcul des coordonnées d'un point suite à la déformation engendrée par la sphère émergeante
    Entrées :p : coordonnées (x, y, z) du point du dalage à tracer (z = 0) AVANT déformation
    centre : coordonnées (X0, Y0, Z0) du centre de la sphère rayon : rayon de la sphère
    Sorties : coordonnées (xprim, yprim, zprim) du point du dallage à tracer APRÈS déformation """
    x, y, z = p
    xprim, yprim, zprim = x, y, z
    xc, yc, zc = centre
    if rayon**2 > zc**2:
        zc = zc if zc <= 0 else -zc
        r = math.sqrt(
            (x - xc) ** 2 + (y - yc) ** 2)
        # distance horizontale depuis le point à dessiner jusqu'à l'axe de la sphère
        rayon_emerge = math.sqrt(rayon ** 2 - zc ** 2)
        # rayon de la partie émergée de la sphère
        rprim = rayon * math.sin(math.acos(-zc / rayon) * r / rayon_emerge)
        if 0 < r <= rayon_emerge:
        # calcul de la déformation dans les autres cas
            xprim = xc + (x - xc) * rprim / r
        # les nouvelles coordonnées sont proportionnelles aux anciennes
            yprim = yc + (y - yc) * rprim / r
        if r <= rayon_emerge:
            beta = math.asin(rprim / rayon)
            zprim = zc + rayon * math.cos(beta)
            if centre[2] > 0:
                zprim = -zprim
        return (xprim, yprim, zprim)
    if __name__ == "__main__": # code de test
        for i in range(-150,150,50):
            for j in range(-150,150,50):
                print(deformation((i,j,0), (0,0,100), 100))
            print()

def hexagone(t=turtle, c=(0,0,0), longueur=20, col1="red", col2="blue", col3="black",d=deformation, centre=(-50, -50, -50), rayon=200) :

    """Trace les lignes des hexagones constituant le pavage.
    Tous les paramètres ont été définis par défaut.
    t correspond au module turtle.
    Le paramètre c correspond au centre de l'hexagone qui est tracé par la fontion.
    la longueur correspond à la longueur des cotés de l'hexagone.
    col1, col2 et col3 correspondent aux couleurs choisies pour les trois losanges constituant l'hexagone.
    d correspond à la fonction déformation.
    Et enfin le parametre "centre" et le paramètre "rayon" correspondent respectivement à la position du centre de la sphère de déformation et à son rayon."""

    def premiere_face(t=turtle, c=(0,0,0), longueur=20, col1="red", centre=(-50, -50, -50), rayon=200) :
        """
        Trace la première face de l'hexagone. Celle en haut à droite.
        :param t: le module turtle
        :param c: le centre de l'hexagone
        :param longueur: la longueur du coté de l'hexagone
        :param col1: La couleur de l'hexagone
        :param centre: Le centre de la sphère déformation
        :param rayon: Le rayon de la sphère de déformation
        :return: Trace la première face de l'hexagone (en haut à droite)
        """
        t.color(col1) # On choisi la première couleur
        t.begin_fill()  # On commence a remplir
        t.down() # On commence a tracer. Le premier losange va pouvoir être tracé

        # Deuxième point (sommet en bas a droite du premier losange) :

        p_x, p_y, p_z= c[0]+longueur, c[1], c[2]

        p = (p_x, p_y, p_z) # Ces coordonnées correspondent au sommet en bas à droite du premier losange avant déformation
        p2 = d(p, centre, rayon)  # Coordonnées du point après déformation

        t.goto(p2[0], p2[1]) # La tortue se déplace aux deux premières coordonnées renvoyées par la fonction déformation

        # Troisième point (sommet en haut à droite du premier losange) :

        p_x = c[0] + longueur * math.cos(math.pi / 3)
        p_y = c[1] + longueur * math.sin(math.pi / 3)

        p = (p_x, p_y, p_z)  # Ces coordonnées correspondent à celles du point avant déformation
        p2 = d(p, centre, rayon)  # Coordonnées du point après déformation

        t.goto(p2[0], p2[1])  # La tortue se déplace aux deux premières coordonnées renvoyées par la fonction déformation

        # Quatrième point (sommet en haut a gauche du premier losange) :

        p_x = c[0] + longueur * math.cos(2 * math.pi / 3)
        p_y = c[1] + longueur * math.sin(2 * math.pi / 3)

        p = (p_x, p_y, p_z)  # Ces coordonnées correspondent a celles du point avant deformation
        p2 = d(p, centre, rayon)  # Coordonnées du point aprés deformation

        t.goto(p2[0], p2[1])  # La tortue se déplace aux deux premières coordonnées renvoyées par la fonction déformation

        # On revient au premier point afin de terminer le premier losange

        p_x, p_y= c[0], c[1]
        p = (p_x, p_y, p_z)  # Coordonnées du point avant déformation

        p2 = d(p, centre, rayon)  # Coordonnées du point après déformation

        t.goto(p2[0], p2[1])  # La tortue se déplace aux coordonnées du point après déformation
        t.end_fill()

    def deuxieme_face(t=turtle, c=(0,0,0), longueur=20, col2="blue", centre=(-50, -50, -50), rayon=200) :
        """
        Trace la deuxième face de l'hexagone. Celle en bas à droite.
        :param t: le module turtle
        :param c: le centre de l'hexagone
        :param longueur: la longueur du coté de l'hexagone
        :param col2: La couleur de l'hexagone
        :param centre: Le centre de la sphère déformation
        :param rayon: Le rayon de la sphère de déformation
        :return: Trace la deuxième face de l'hexagone (en bas à droite)
        """
        t.color(col2) # On sélectionne la deuxième couleur
        t.begin_fill()

        # Deuxième point
        p_x = c[0] + longueur
        p_y = c[1]
        p_z = c[2]

        p = (p_x, p_y, p_z)  # Ces coordonnées correspondent au sommet en haut à droite du deuxième losange avant déformation
        p2 = d(p, centre, rayon)  # Coordonnées du point après déformation

        t.goto(p2[0], p2[1])  # La tortue se déplace aux deux premières coordonnées renvoyées par la fonction déformation

        # Troisième point (sommet en bas à droite du deuxième losange) :

        p_x = c[0] + longueur * math.cos(-math.pi / 3)
        p_y = c[1] + longueur * math.sin(-math.pi / 3)
       

        p = (p_x, p_y, p_z)  # Ces coordonnées correspondent à celles du point avant déformation
        p2 = d(p, centre, rayon)  # Coordonnées du point après déformation

        t.goto(p2[0], p2[1])  # La tortue se déplace aux deux premières coordonnées renvoyées par la fonction déformation

        # Quatrième point (sommet en bas a gauche du deuxieme losange) :

        p_x = c[0] + longueur * math.cos(-2 * math.pi / 3)
        p_y = c[1] + longueur * math.sin(-2 * math.pi / 3)
      

        p = (p_x, p_y, p_z)  # Ces coordonnées correspondent à celles du point avant déformation
        p2 = d(p, centre, rayon)  # Coordonnées du point après déformation

        t.goto(p2[0], p2[1])  # La tortue se déplace aux deux premières coordonnées renvoyées par la fonction déformation

        # On revient au premier point afin de terminer le deuxième losange

        p_x, p_y, p_z = c[0], c[1], c[2]
        p = (p_x, p_y, p_z)  # Coordonnées du point avant deformation

        p2 = d(p, centre, rayon)  # Coordonnées du point après déformation

        t.goto(p2[0], p2[1])  # La tortue se déplace aux coordonnées du point après déformation
        t.end_fill()

    def troisieme_face(t=turtle, c=(0,0,0), longueur=20, col3="black", centre=(-50, -50, -50), rayon=200)  :
        """
        Trace la troisième face de l'hexagone. Celle à gauche.
        :param t: le module turtle
        :param c: le centre de l'hexagone
        :param longueur: la longueur du coté de l'hexagone
        :param col3: La couleur de l'hexagone
        :param centre: Le centre de la sphère déformation
        :param rayon: Le rayon de la sphère de déformation
        :return: Trace la troisème face de l'hexagone (à gauche)
        """
        turtle.color(col3) # On sélectionne la troisième couleur
        turtle.begin_fill()

        # Deuxième point (sommet en haut du troisième losange) :
        p_x, p_y = c[0] + longueur * math.cos(2 * math.pi / 3), c[1] + longueur * math.sin(2 * math.pi / 3)

        p = (p_x, p_y, p_z)  # Ces coordonnées correspondent au sommet en bas à droite du premier losange avant déformation
        p2 = d(p, centre, rayon)  # Coordonnées du point après déformation

        t.goto(p2[0], p2[1])  # La tortue se déplace aux deux premières coordonnées renvoyées par la fonction déformation

        # Troisième point (sommet a gauche du troisième losange) :
        p_x = c[0] - longueur
        p_y = c[1]

        p = (p_x, p_y, p_z)  # Ces coordonnées correspondent à celles du point avant déformation
        p2 = d(p, centre, rayon)  # Coordonnées du point après déformation

        t.goto(p2[0], p2[1])  # La tortue se déplace aux deux premières coordonnées renvoyées par la fonction déformation

        # Quatrième point (sommet en bas du troisième losange) :

        p_x = c[0] + longueur * math.cos(-2 * math.pi / 3)
        p_y = c[1] + longueur * math.sin(-2 * math.pi / 3)

        p = (p_x, p_y, p_z)  # Ces coordonnées correspondent à celles du point avant déformation
        p2 = d(p, centre, rayon)  # Coordonnées du point après déformation

        t.goto(p2[0], p2[1])  # La tortue se déplace aux deux premières coordonnées renvoyées par la fonction déformation

    # On revient au premier point afin de terminer le troisième losange

        p_x, p_y = c[0], c[1]

        p = (p_x, p_y, p_z)  # Coordonnées du point avant déformation
        p2 = d(p, centre, rayon)  # Coordonnées du point après déformation

        t.goto(p2[0], p2[1])  # La tortue se déplace aux coordonnées du point après déformation
        t.end_fill() #Le dernier losange est tracé et rempli. L'hexagone est terminé.
        turtle.up()

    # Code de hexagone
    for numero_face in range(3) :
        p_x = c[0]
        p_y = c[1]
        p_z = c[2]
        p = (p_x, p_y, p_z)  # Coordonnées du premier point de chaque face avant déformation
        p2 = d(p, centre, rayon)  # Coordonnées du point après déformation
        turtle.up()
        t.goto(p2[0], p2[1])  # La tortue se déplace aux coordonnées du point après déformation
        t.speed("fastest")
        if numero_face == 0 :
            premiere_face(t, c, longueur, col1, centre, rayon)
        elif numero_face==1 :
            deuxieme_face(t, c, longueur, col2, centre, rayon)
        else :
            troisieme_face(t, c, longueur, col3, centre, rayon)

def pavage(t=turtle, inf_gauche=-300, sup_droit=300, longueur=20, col1="purple", col2="blue", col3="black", centre=(-50, -50, -80), rayon=200):

    """Trace l'ensemble des hexagones, déformés ou non, constituant le pavage en utilisant la fonction hexagone.
     Cette fonction prend en compte les limites de la zone où se situera le pavage.
     Tous les paramètres ont été définis par défaut.
     inf_ gauche correspond à la coordonnée x et y du point en bas à gauche délimitant la zone à tracer et de même, sup_droit correspond à la coordonnée du point limitant cette zone en haut à droite.
     La longueur correspond à la longueur des cotés de l'hexagone.
     col1, col2 et col3 correspondent aux couleurs choisies pour les trois losanges constituant l'hexagone.
     Et enfin le parametre "centre" et le paramètre "rayon" correspondent respectivement à la position du centre de la sphère de déformation et à son rayon."""

    # On definit les limites de la zone :

    lim_gauche = inf_gauche
    lim_droite = sup_droit
    lim_bas = inf_gauche
    lim_haut = sup_droit

    # On trace une premiere ligne :
    # On definit tout d'abord les coordonnees du centre du premier hexagone de la ligne. Ces coordonnees correspondent a la limite inferieure gauche :
    new_x = lim_gauche
    new_y = lim_bas
    c = (new_x, new_y, 0)
    ligne=1 # On numérote les lignes. En effet, une fois sur 2 le premier hexagone devra avoir son abscisse decalée de 1,5 longueur
    while c[1] <= lim_haut:  # On prevoit les prochaines lignes qui ne devront pas aller au dessus de la limite supérieure
        if ligne%2!=0 :
            new_x = lim_gauche
            while new_x <= lim_droite:
                c = (new_x, new_y, 0)
                hexagone(c=(new_x, new_y, 0), col1 = col1, col2 = col2, col3 = col3, longueur = longueur, centre=centre, rayon = rayon)  # on trace l'hexagone
                new_x = new_x + 3 * longueur  # On ajuste l'abscisse du centre du prochain hexagone de la ligne
        elif ligne%2==0 :
            new_x = lim_gauche + 1.5 * longueur
            while new_x <= lim_droite:
                c = (new_x, new_y, 0)
                hexagone(c=(new_x, new_y, 0), col1 = col1, col2 = col2, col3 = col3, longueur = longueur, centre=centre, rayon = rayon)  # On trace l'hexagone
                new_x = new_x + 3 * longueur  # On ajuste l'abscisse du centre du prochain hexagone de la ligne
        new_y = new_y + (3**0.5)/2 * longueur # On ajuste l'ordonnée du centre du prochain hexagone de la ligne suivante. (3**0.5)/2 a été calculé grace au théorème de Pythagore.
        c = (new_x, new_y, 0)
        ligne=ligne+1
    t.mainloop() # Le pavage est tracé. On laisse afficher la fenêtre.



pavage(inf_gauche=limite_inf, sup_droit=limite_sup, longueur=cote, col1=coul1, col2=coul2, col3=coul3, centre=centre_def, rayon=r)
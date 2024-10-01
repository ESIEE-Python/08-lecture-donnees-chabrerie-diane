"""exercice lecture donnees"""
#### Imports et définition des variables globales
import csv

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    name = filename
    with open(name, 'r', encoding='utf8') as f:
        r = csv.reader(f, delimiter=';')
        l = list(r)
    for i, ll in enumerate(l):
        l[i] = list(map(int, ll))
    return l

def get_list_k(data, k):
    """retourne valeur a indice k"""
    return data[k]

def get_first(l):
    """retourne premiere valeur"""
    return l[0]

def get_last(l):
    """retourne derniere valeur"""
    return l[-1]

def get_max(l):
    """retourne max liste"""
    return max(l)

def get_min(l):
    """retourne min liste"""
    return min(l)

def get_sum(l):
    """retourne somme elt de liste"""
    return sum(l)


#### Fonction principale


def main():
    """fct main"""
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()

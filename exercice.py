#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici
import recettes

# TODO: Définissez vos fonction ici
def comparer(filename1, filename2):
    with open(filename1) as file1, open(filename2) as file2:
        string1, string2 = file1.read(), file2.read()
        minlen = len(string1) if len(string1) <= len(string2) else len(string2)

        for i in range(minlen):
            if string1[i] != string2[i]:

                return f"la {i+1}e lettre est differente: {string1[i]} != {string2[i]}"

        if len(string1) < len(string2):

            return f"le fichier 2 est plus long que le fichier 1 et le premier caractere different est {string2[len(string1)]}" 
        else:

            return f"le fichier 1 est plus long que le fichier 2 et le premier caractere different est {string1[len(string2)]}" 


def triple_espace(filename):
    with open(filename) as file, open("espacer.txt","w") as writefile:
        text = file.read()
        writefile.write(text.replace(" ", "   "))


def grading(filename):
    with open(filename) as file, open("bulletin.txt","w") as bulletin:
        text = file.readlines()
        for note in text:
            for key in PERCENTAGE_TO_LETTER:
                if int(note) >= PERCENTAGE_TO_LETTER[key][0]:
                    bulletin.write(note +" " + key + "\n")
                    break

def livre_recette():
    return None


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    f1name = "exemple.txt"
    f2name = "notes.txt"
    print(comparer(f1name, f2name))
    triple_espace(f1name)
    grading(f2name)
        

    

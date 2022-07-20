import subprocess
import os
from os import listdir
from os.path import isfile, join

#on quitte le repertoire 'ConsolePython'
os.chdir(r'..')

#compte le nombre de fichier dans le dossier 'Python'
count = 0
dir = "Python"
for path in os.listdir(dir):
 if os.path.isfile(os.path.join(dir, path)):
  count += 1

#redirection dans le repertoire 'Python' + ls des fichiers presents
os.chdir(r"Python/")
data = [f for f in listdir(r"chemin_des_fichiers") if isfile(join(r"chemin_des_fichiers", f))]

#on quitte le repertoire 'Python'
os.chdir(r'..')

#on ecrit dans un fichier texte le nom des fichiers presents dans le repertoire "Python"
os.chdir(r"ConsolePython/")
fichier = open("nom_des_fichiers.txt", "w")
fichier.write("\n".join(data))
fichier.close()

#si True on repete le programme d'affichage
while True:

#on lit les noms des fichiers
 fichier = open("nom_des_fichiers.txt", "r")
 i = 0
 liste = []
 for line in fichier:
  i += 1
  print(f"{i}. {line}")
  liste.append(line)
 fichier.close()

 user_choice = input("\nEntrer le numero du programme que vous souhaitez executer, exemple: 1: ")
 while user_choice.isdigit() == False or int(user_choice) <= 0 or int(user_choice) > i:
  user_choice = input("\nVeuillez entrer un numero de script valide, exemple: 1: ")

 print(f"Vous avez décidé d'exécuter le programme {user_choice}.\n")
 os.chdir(r"chemin_des_fichiers")
 subprocess.run(['.\\' + liste[int(user_choice) - 1]], shell=True)
 os.chdir(r'..')

 os.chdir(r"ConsolePython/")

 restart = input("\nVoulez vous executer un autre script ?\nOui: 0\nNon: 1\nVotre saisie: ")
 while restart.isdigit() == False or int(restart) != 0 and int(restart) != 1:
  print("\nVeuillez entrer une valeur valide !")
  restart = input("Voulez vous excuter un autre script ?\nOui: 0\nNon: 1\nVotre saisie: ")

 if int(restart) == 0:
   continue
 else:
   print(exit())

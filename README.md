## Ce dépôt sert au projet 4 de la formation  Développeur d'application Python d'Openclassrooms.  

### Présentation  

Le programme sert à créer et gérer des parties d'échecs suivant les rounds suisses  

### Fonctionnement

Le programme utilise deux fichiers json pour charger et sauvegarder les données, un pour les tournois et un pour les joueurs.
Menu 1 pour les tournois  
Menu 2 pour les joueurs  
Dans le menu 1, vous pouvez soit créer un tournoi, soit consulter les tournois contenus dans le fichier.  
Dans consulter tournois vous pouvez choisir un tournoi, ensuite un round puis un match.
Si le match n'est pas terminé vous pouvez désignez le vainqueur. Quand tous les matchs d'un round sont terminés vous pouvez choisir de terminer le round.  
Le programme créera le prochain round.  
Dans le menu joueurs vous pouvez ajouter un joueur ou consulter la liste des joueurs.  


### Requirement  
[Git](https://git-scm.com)  
[Python](www.python.org)  
[Liste des paquets python](https://github.com/elvisOC/P4/blob/master/requirement.txt)  
Pour installer les paquets, lancer python et écrire la commande pip install *nom du paquet*  
```
pip install pandas
```


### Comment l'utiliser  

#### Télécharger le script
Avec git executer la commande git clone *lien du dépôt* dans un nouveau dossier (il faut l'indiquer dans la commande) 
```
git clone github.com/ElvisOC/P4.git C:\users\%username%\Desktop\Nouveau
```
 

#### Executer le script
Dans le dossier contenant le script :  

```
python main.py
```

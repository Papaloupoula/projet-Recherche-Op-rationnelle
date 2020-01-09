# projet-Recherche-Op-rationnelle

To DO:
  - Faire varier le nombre de mec qu'on sous-traite en fonction du ratio
  - Faire varier k dans le k means
  - Faire les groupes bêtements

  - Optimiser les tournees avec tournees.py
  
  - Faire des descente de gradient sur les groupes 
  - Re-Optimiser
  
  
  - Niquer l'enclos comme au KIRO
  - Partir à Tokyo pour se battre avec des sauces samourais et niquer des geishas

J'ai fait (Bak) :
- Codé une petite descente, mais y a qqs erreurs, voir sur fb pour les détails
- Dans le fichier 'sous_traitance_seuil', j'ai fait le bail de sous-traitance en choisissant un seuil, pr le mmt j'ai laissé 1
- J'ai TOUT passé sur des fonctions pcq les variables globales c'était chiant, si vous comprenez pas tout au pire demandez-moi, j'essairai d'expliquer. Par exemple, puisque les trucs qu'on sous-traitent peuvent changer, j'ai créé des fonctions pour tous les trucs qui utilisent la sous-traitance, typiquement la variable "corresp" de Farjute dans le fichier kmeans, qui est mtn calculée avec une fct "correspondance". Idem pour la création de groupe en faisant varier les tailles de clusters, et pour la descente de gradient (qui s'appuie sur une fonction auxiliaire).
- En parlant de la fonction auxiliaire, c'est sûrement dans celle-ci qu'il y a l'erreur dont je parle sur fb, si vous trouvez c'est cool, mais c'est un merdier sans nom donc j'essaierai de m'en occuper.
- J'ai utilisé des deepcopies à fond sur la descente pcq j'ai câblé et ça a fini par fonctionner, peut-être y en a-t-il qui ne servent à rien, si vous voulez élaguer un peu

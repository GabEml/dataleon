Test technique Dataleon 

J'ai créée une classe Main qui prend une image et qui va la traiter pour dabord la mettre au format RGB puis analyser le documents si ce document possède le mot clé banque /bancaire ou facture alors la le script va encapsuler les informations du document dans une classe pour pouvoir l'utiliser cette classe permet d'avoir des données grossière sur ce document.
puis il a 2 classe de testes qui sont assez basique.

Pour lancer le projet il suffit de lancer python main.py
Pour lancer les testes il suffit de lancer pytest test_main.py
Pour lancer les testes il suffit de lancer pytest test_document.py

Vous pouvez changer le chemin des images pour tester différente images
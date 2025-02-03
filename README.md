Instructions pour exécuter le programme depuis n’importe quelle machine

_____________________________________

Télécharger le projet Django depuis le dépôt ou un fichier compressé contenant l’ensemble du code source.

Si Django n’est pas installé :

pip install django

Si besoin faire une migration de la base de donné :

python manage.py makemigrations

python manage.py migrate 
Démarrer le serveur de développement Django :

python manage.py runserver

Accéder à l’application depuis un navigateur via l’URL : http://127.0.0.1:8000.
Accéder à l’administration de l’application http://127.0.0.1:8000/admin 

User : admin
Mdp : admin

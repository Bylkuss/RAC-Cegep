# Application de Streaming en Tkinter

Cette application permet de gérer des films et des clients via une interface graphique simple construite avec **Python** et **Tkinter**. L'application utilise **Pillow** pour la gestion des images.

## Objectif

L'application permet de visualiser, ajouter, modifier et supprimer des films et des clients dans une interface conviviale. Elle est développée pour offrir une expérience utilisateur simple et intuitive.

## Démarrer l'application

1. Téléchargez l'exécutable `main.exe` dans le dossier `TkinterStreamingApp\dist` :
   - Le fichier exécutable se trouve dans le dossier `TkinterStreamingApp\dist` après avoir généré l'application avec **PyInstaller**.

2. Exécutez l'application :
   - Sur Windows, lancez le fichier `main.exe` :
     ```
     C:\chemin\vers\le\dossier\TkinterStreamingApp\dist\main.exe
     ```

L'application est prête à être utilisée !

## Générer l'exécutable (optionnel)

Si vous souhaitez générer l'exécutable vous-même, vous devez avoir installé **Python 3.10+** et **PyInstaller**. Ensuite, exécutez cette commande pour générer le fichier `.exe` :

```bash
pyinstaller --noconsole --onefile --icon="streaming-tv-app.ico" main.py

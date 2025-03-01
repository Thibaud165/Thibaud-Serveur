import subprocess
from flask import Flask
import os

os.chdir(r"C:\Users\thiba\OneDrive\Documents\Serveur\Minecraft\Perso\Survie Principal B-J")

app = Flask(__name__)

@app.route('/start-server-Survie-Principal-B-J')
def start_server():
    try:
        # Chemin absolu vers le fichier .jar de Minecraft
        subprocess.Popen([
            "java", "-Xmx16G", "-Xms16G", "-jar", 
            "C:\\Users\\thiba\\OneDrive\\Documents\\Serveur\\Minecraft\\Perso\\Survie Principal B-J\\paper-1.21.4-136.jar"
        ], shell=True)
        return "Serveur Minecraft démarré (Survie Principal B-J)."
    except Exception as e:
        return f"Erreur : {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

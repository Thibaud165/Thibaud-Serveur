from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/start-server')
def start_server():
    try:
        subprocess.Popen(["C:\\chemin\\vers\\ton\\serveur.exe"], shell=True)
        return "Serveur Minecraft démarré !"
    except Exception as e:
        return f"Erreur : {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

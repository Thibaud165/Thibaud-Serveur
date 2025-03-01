from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/start-server-Survie-Principal-B-J')
def start_server():
    try:
        subprocess.Popen(["C:\\Users\\thiba\\OneDrive\\Documents\\Serveur\\Minecraft\\Perso\\Survie Principal B-J\\.lunch-server(16Go).bat"], shell=True)
        return "Serveur Minecraft demmarer (Survie Principal B-J)."
    except Exception as e:
        return f"Erreur : {e}"

if __name__ == '__main__':
    app.run(host='192.168.1.165', port=5000)

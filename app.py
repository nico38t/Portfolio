import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'votre_cle_secrete')

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'nicolas.tsigris@gmail.com'
app.config['MAIL_PASSWORD'] = 'ekvbvetilbdbodqf'

mail = Mail(app)

# Exemple de données pour chaque projet
projects = {
    "titanic": {
        "title": "Création d'une base de données",
        "images": [
            "titanic1.jpg",
            "titanic2.jpg",
            "titanic3.jpg"
        ],
        "description": """
            Ce projet consistait à concevoir et exploiter une base de données pour analyser le naufrage du Titanic.
            <ul>
                <li>Modélisation du schéma relationnel (passagers, cabines, billets, etc.)</li>
                <li>Importation et nettoyage des données réelles</li>
                <li>Réalisation de requêtes SQL pour répondre à des problématiques (taux de survie, profils des survivants, etc.)</li>
                <li>Analyse statistique et restitution des résultats</li>
            </ul>
            Ce travail m’a permis de renforcer mes compétences en SQL, en modélisation de données et en analyse de données réelles.
        """
    },
    "linux": {
        "title": "Installation d'un poste de développement",
        "images": [
            "VM-linux.jpg"
        ],
        "description": "Installation d'un environnement de développement sur une machine virtuelle Linux."
    },
    "besoin-client": {
        "title": "Implémentation d'un besoin client",
        "images": [
            "besoin-client.png"
        ],
        "description": "Développement d'un programme optimisé pour classer des dépêches selon différentes catégories."
    },
    "atos": {
        "title": "Création du site d'une entreprise",
        "images": [
            "SAE1.056Image.jpg"
        ],
        "description": "Conception et réalisation en équipe d'un nouveau site pour l'entreprise Atos ayant pour cible des jeunes de troisième."
    },
    "nutri": {
        "title": "Exploitation d'une base de données",
        "images": [
            "nutri.jpg"
        ],
        "description": "Tri de la base de données d'Open Food Facts afin de l'analyser pour répondre à une problématique."
    }
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Récupère les données du formulaire
        message = request.form.get("message")
        name = request.form.get("name")
        first_name = request.form.get("first_name")
        mail_from = request.form.get("mail")
        phone = request.form.get("phone_number")
        obj = request.form.get("object")

        # Vérification stricte de l'email et de l'objet
        if (
            not mail_from or "\n" in mail_from or "\r" in mail_from
            or not obj or "\n" in obj or "\r" in obj
        ):
            flash("Adresse email ou objet invalide.", "danger")
            return redirect(url_for('index'))

        # Prépare le mail
        msg = Message(
            subject=f"Nouveau message portfolio : {obj}",
            sender=app.config['MAIL_USERNAME'],
            recipients=["nicolas.tsigris@outlook.com"],
            body=f"De : {name} {first_name}\nEmail : {mail_from}\nTéléphone : {phone}\n\nMessage :\n{message}",
            reply_to=mail_from.strip()
        )
        mail.send(msg)
        flash("Votre message a bien été envoyé !", "success")
        return redirect(url_for('index'))
    return render_template("index.html")

@app.route("/<project_id>")
def project(project_id):
    project = projects.get(project_id)
    if not project:
        return "Projet non trouvé", 404
    return render_template("project.html", project=project)

@app.route("/titanic")
def project_titanic():
    return render_template("titanic.html")

@app.route("/linux")
def project_linux():
    return render_template("linux.html")

@app.route("/besoin-client")
def project_besoin_client():
    return render_template("besoin-client.html")

@app.route("/atos")
def project_atos():
    return render_template("atos.html")

@app.route("/nutri")
def project_nutri():
    return render_template("nutri.html")

@app.route('/stage')
def stage():
    return render_template('stage.html')

@app.route('/bridge')
def bridge():
    return render_template('bridge.html')

@app.route("/sae3")
def sae3():
    return render_template("SAE3.html")

if __name__ == "__main__":
    app.run(debug=True)
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 15:28:30 2019

@author: utilisateur
"""
from PIL import Image
from io import BytesIO
from flask import Flask, request,make_response, redirect,url_for,render_template



app = Flask(__name__)


@app.route('/contact', methods = ['GET'])
def contact_formulaire():
    return 'en travaux'
@app.route('/contact', methods = ['POST'])  
def contact_traiter_donnees() :  
    return 'en travaux'

@app.route('/hihi')
@app.route('/hehe')
@app.route('/hoho')
def oui():
    return request.path


@app.route('/discussion')
@app.route('/discussion/page/<int:num_page>')
def mon_chat(num_page = 1):
    premier_msg = 1 + 50 * (num_page -1)
    dernier_msg = premier_msg + 50
    return 'affichage des messages {} à {}'.format(premier_msg, dernier_msg)

@app.route('/afficher')
@app.route('/afficher/<nom>.<prenom>')
def afficher(nom=None, prenom = None) :
    if nom is None or prenom is None :
        return "afficher votre nom et prénom dans l'url"
    return "Vous vous appelez {} {} ".format(prenom, nom.upper())

@app.route('/image')
def genere_image():
    mon_image = BytesIO()
    Image.new("RGB", (300,100), "#10C41D").save(mon_image, 'BMP')
    reponse = make_response(mon_image.getvalue())
    reponse.mimetype = "image/bmp"
    return reponse

#@app.route('/404')
#def page_non_trouvee():
#    reponse = "Cette page devrait vous avoir renvoyé une erreur 404"
#    return reponse, 404 #même que "make_response(), il comprend"
@app.errorhandler(404) #exprime toutes les routes posible qui mène à 404
def ma_page_404():
    return "404 :'(", 404


@app.route('/form-example', methods=['GET', 'POST']) #allow both GET and POST requests
def form_example():
    if request.method == 'POST': #this block is only entered when the form is submitted
        return 'Submitted form.'

    return '''<form method="POST">
                  Language: <input type="text" name="language"><br>
                  Framework: <input type="text" name="framework"><br>
                  <input type="submit" value="Submit"><br>
              </form>'''

@app.route('/')
def racine():
    return "Le chemain de 'racine' est : " + request.path
@app.route('/la')
def ici():
    return "Le chemain de 'ici' est: " + request.path


# crée des erreurs 
#@app.route('/profil')
#def profil():
#    if utilisateur_non_id:
#        return redirect(url_for('/login'))
#    return "you are log in"

#login
#@app.route('/login')
#def login(): 

#redirections 
@app.route('/github')
def redirection_git():
    return redirect('https://github.com/Xhiffer/kjlkj')


@app.route('/accueil-html')
def accueil_html():
    mots = ["bonjour", "à", "toi,", "visiteur."]
    puces = ''.join("<li>{}</li>".format(m) for m in mots)
    return """<!DOCTYPE html>
        <html>
            <head>
                <meta charset="utf-8" />
                <title>{titre}</title>
            </head>
        
            <body>
                <h1>{titre}</h1>
                <ul>
                    {puces}
                </ul>
            </body>
        </html>""".format(titre="Bienvenue !", puces=puces)

@app.route('/accueil-flask')
def accueil_flask():
    mots = ['bonjour','à', 'toi','visiteur']
    return render_template('accueil.html',titre = "Bienvenue!", mots = mots)

if __name__ == '__main__':
    app.run(debug=True)
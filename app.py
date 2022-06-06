#Se importa la librería Flask, abort y render_template
from flask import Flask, abort, render_template

#instancia  de la aplicación web
app=Flask(__name__, template_folder='templates')

#Ruta raíz
@app.route('/')

#Controlador quer renderiza la página principal
def index():
    return render_template('index.html')

#Ruta registroempresa
@app.route('/registroempresa')

#Controlador quer renderiza la página  registroempresa
def registroempresa():
    ''' abre la pagina registroempresa'''
    return render_template('registroempresa.html')
#Ruta registropostulante
@app.route('/registropostulante')

#Controlador quer renderiza la página registropostulante
def registropostulante():
    ''' abre la pagina registropostulante'''
    return render_template('registropostulante.html')

#Ruta página accederempresa
@app.route('/accederempresa')

#Controlador quer renderiza la página accederempresa
def accederempresa():
    ''' abre la pagina accederempresa'''
    return render_template('accederempresa.html')

#Ruta página accederpostulante
@app.route('/accederpostulante')

#Controlador quer renderiza la página accederempresa
def accederpostulante():
    ''' abre la pagina accederpostulante'''
    return render_template('accederpostulantea.html')

#Ruta página crearoferta
@app.route('/crearoferta')

#Controlador quer renderiza la página crearoferta
def crearoferta():
    ''' abre la pagina crearoferta'''
    return render_template('crearoferta.html')

#Ruta página crearoferta
@app.route('/ofertas')

#Controlador quer renderiza la página ofertas
def ofertas():
    ''' abre la pagina ofertas'''
    return render_template('ofertas.html')

#Ruta página crearoferta
@app.route('/nosotros')

#Controlador quer renderiza la página ofertas
def nosotros():
    ''' abre la pagina nosotros'''
    return render_template('nosotros.html')

#Ruta página empresaslistado
@app.route('/empresaslistado')

#Controlador quer renderiza la página empresaslistado
def empresaslistado():
    ''' abre la pagina empresaslistado'''
    return render_template('empresaslistado.html')

#Ruta página reclutamiento
@app.route('/reclutamiento')

#Controlador quer renderiza la página reclutamiento
def reclutamiento():
    ''' abre la pagina reclutamiento'''
    return render_template('reclutamiento.html')

#Ruta página avisolegal
@app.route('/avisolegal')

#Controlador quer renderiza la página avisolegal
def avisolegal():
    ''' abre la pagina avisolegal'''
    return render_template('avisolegal.html')

#Función principal que ejecuta la aplicación
if __name__ == '__main__':
    app.run(debug=True)
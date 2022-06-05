#Se importa la librería Flask, abort y render_template
from flask import Flask, abort, render_template

#instancia  de la aplicación web
app=Flask(__name__, template_folder='templates')

#Ruta raíz
@app.route('/')

#Controlador quer renderiza la página principal
def index():
    return render_template('index.html')

#Función principal que ejecuta la aplicación
if __name__ == '__main__':
    app.run(debug=True)
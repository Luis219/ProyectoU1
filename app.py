#Se importa la librería Flask, abort y render_template

import re
import json
import os
from turtle import pos
from markupsafe import escape
from flask import Flask, abort, render_template, request, flash, url_for, redirect
import cryptocode

#instancia  de la aplicación web
app=Flask(__name__, template_folder='templates')
app.secret_key='12345'
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
    return render_template('accederpostulante.html')

#Ruta página crearoferta
@app.route('/crearofertas')

#Controlador quer renderiza la página crearoferta
def crearofertas():
    ''' abre la pagina crearoferta'''
    return render_template('crearofertas.html')

#Ruta página crearoferta
@app.route('/ofertas')

#Controlador quer renderiza la página ofertas
def ofertas():
    ''' abre la pagina ofertas por medio de la funcion ver_ofertas'''
    return ver_ofertas()

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

'''
Parte funcional de la aplicación
'''
titulosOferta=[]
descripcionesOferta=[]
direccionesOferta=[]
@app.route('/nuevaoferta',methods=['POST'])

#función que permite enviar los datos ingresados hacia la tabla
def nuevaoferta(): 
    tituloOferta= request.form.get('titulo')
    descripcionOferta= request.form.get('descripcion')
    direccionOferta= request.form.get('direccion')
  

    #validar que se ingresen datos
    if len(tituloOferta)>0 and len(descripcionOferta)>0 and len(direccionOferta)>0:
       
       #se ingresen los datos a las listas
        titulosOferta.append(tituloOferta)
        descripcionesOferta.append(descripcionOferta)
        direccionesOferta.append(direccionOferta)
          #con path se especifica la ruta del archivo
        path, _=os.path.split(os.path.abspath(__file__))
    
        #se crean los arreglos 
        data={}
        data['titulosOferta']=[]
        data['descripcionesOferta']=[]
        data['direccionesOferta']=[]    
        
        data["titulosOferta"].append(titulosOferta)
        data["descripcionesOferta"].append( descripcionesOferta)
        data["direccionesOferta"].append(direccionesOferta)

         #se escribe en el archivo datos.json
        with open(path+f'/ofertas.json','w') as file:
            json.dump(data, file, indent=4)

        

        return ver_ofertas()
    else:
        #alerta en caso de que existan errores
        flash('Error al ingresar los datos')
        return render_template('crearofertas.html')


diccionario_Empresas={}

@app.route('/nuevoregistroempresa',methods=['POST'])

#función que permite enviar los datos ingresados hacia la tabla
def nuevoregistroempresa(): 
    nombreEmpresa= request.form.get('nombre')
    direccionEmpresa= request.form.get('direccion')
    telefonoEmpresa= request.form.get('telefono')
    correoEmpresa= request.form.get('correo')
    contraseniaEmpresa= request.form.get('contrasenia')

    #cifrado de la contraseña
    cifrado=cryptocode.encrypt(contraseniaEmpresa, "password")

    #validar que se ingresen datos
    if len(nombreEmpresa)>0 and len(direccionEmpresa)>0 and len(telefonoEmpresa)>0 and len(correoEmpresa)>0 and len(contraseniaEmpresa)>0:
     
      
          #con path se especifica la ruta del archivo
        path, _=os.path.split(os.path.abspath(__file__))
    
       #se ingresen los datos a las listas
        with open(path+'/registroempresa.json') as file:
             data_Empresas= json.load(file)
       
        diccionario_Empresas={"nombresEmpresas":nombreEmpresa,"direccionesEmpresas":direccionEmpresa,"telefonosEmpresas":telefonoEmpresa,"correosEmpresas":correoEmpresa,
        "contraseniasEmpresas":cifrado}
        data_Empresas.append(diccionario_Empresas)
    
         #se escribe en el archivo datos.json
        with open(path+f'/registroempresa.json','w') as file:
            json.dump(data_Empresas, file, indent=4)

        return render_template('crearofertas.html', titulosOferta=titulosOferta, descripcionesOferta=descripcionesOferta, direccionesOferta=direccionesOferta)
    else:
        #alerta en caso de que existan errores
        flash('Error al ingresar los datos')
        return render_template('registroempresa.html')




diccionario_Postulantes={}
@app.route('/nuevoregistropostulante',methods=['POST'])

#función que permite guardar los datos
def nuevoregistropostulante(): 

      #con path se especifica la ruta del archivo
    path, _=os.path.split(os.path.abspath(__file__))
    
       #se ingresen los datos a las listas
    with open(path+'/registropostulante.json') as file:
        data_Postulantes= json.load(file)

    nombrePostulante= request.form.get('nombre')
    telefonoPostulante= request.form.get('telefono')
    experienciaPostulante= request.form.get('experiencia')
    correoPostulante= request.form.get('correo')
    contraseniaPostulante= request.form.get('contrasenia')
   


    #cifrado de la contraseña
    cifrado=cryptocode.encrypt(contraseniaPostulante, "password")

    #validar que se ingresen datos
    if len(nombrePostulante)>0 and len(telefonoPostulante)>0 and len(experienciaPostulante)>0 and len(correoPostulante)>0 and len(contraseniaPostulante)>0:
       
       
      
       
        diccionario_Postulantes={'nombrePostulante':nombrePostulante, 'telefonoPostulante':telefonoPostulante,
        'experienciaPostulante':experienciaPostulante, 'correoPostulante': correoPostulante, 'contraseniaPostulante':cifrado}
        
        data_Postulantes.append(diccionario_Postulantes)
        
 
    
         #se escribe en el archivo datos.json
        with open(path+f'/registropostulante.json','w') as file:
            json.dump(data_Postulantes, file, indent=4)

        return render_template('ofertas.html', titulosOferta=titulosOferta, descripcionesOferta=descripcionesOferta, direccionesOferta=direccionesOferta)
    else:
        #alerta en caso de que existan errores
        flash('Error al ingresar los datos')
        return render_template('registropostulante.html')


#Validación de usuarios de empresa

#ruta hacia /ver_datos
@app.route('/validar_usuarios_empresa',methods=['POST'])

#función que permite visualizar las tareas almacenadas
def validar_usuarios_empresa():

    if request.method=='POST':
        correo= request.form.get("correo")
        contrasenia= request.form.get("contrasenia")

    
    
        #con se creay especfica una ruta
        path, _=os.path.split(os.path.abspath(__file__))
    
   #se carga el archivo registroempresas.json
        with open(path+'/registroempresa.json') as file:
          data= json.loads(file.read())
       

         #se recorre cada elemento del diccionario
        for elemento in range(len(data)):
            
            try:

            #descifrado de la contraseña
                descifrado= cryptocode.decrypt(data[elemento]["contraseniasEmpresas"], 'password')
                if correo!=data[elemento]["correosEmpresas"] and contrasenia!=data[elemento][descifrado]:
                    elemento=elemento+1
                    #Si no se valida se retorna un mensaje     
                    flash("Error")
                    return render_template('accederempresa.html')
                else:
                    #Si se valida el usuario se redirige a otra pagona 
                     return render_template('crearofertas.html')
                    
                    
            except KeyError:
                continue
    else:
        flash("Error")
        return render_template('accederempresa.html')
    return  render_template('accederempresa.html')

#Validación de usuarios postulantes

#ruta hacia validar_usuarios_postulantes
@app.route('/validar_usuarios_postulantes',methods=['POST'])

#función que permite visualizar las tareas almacenadas
def validar_usuarios_postulantes():
    if request.method=='POST':
        correo= request.form.get("correo")
        contrasenia= request.form.get("contrasenia")

        path, _=os.path.split(os.path.abspath(__file__))
        
    #se carga el archivo registropoatulanye.json
        with open(path+'/registropostulante.json') as file:
            data= json.loads(file.read())
        
        #se recorre cada elemento del diccionario
        for elemento in range(len(data)):
            
            try:

            #descifrado de la contraseña
                descifrado= cryptocode.decrypt(data[elemento]["contraseniaPostulante"], 'password')
                if correo!=data[elemento]["correoPostulante"] and contrasenia!=data[elemento][descifrado]:
                    elemento=elemento+1
                    #retorna la funcion de ver ofertas       
                    flash(data[elemento]["correoPostulante"])
                    return render_template('accederpostulante.html')
                else:
                    #si se valida retorna la funcion de ver ofertas  
                     return ver_ofertas()
                    
                    
            except KeyError:
                continue
    else:
        flash("Error")
        return render_template('accederpostulante.html')
    return  render_template('accederpostulante.html')

#ruta hacia ver ofertas
@app.route('/ver_ofertas',methods=['POST'])

#función que permite visualizar las tareas almacenadas
def ver_ofertas():
 
    path, _=os.path.split(os.path.abspath(__file__))
    
   #se carga el archivo de las ofertas
    with open(path+'/ofertas.json') as file:
       data= json.load(file)

    for i in data["titulosOferta"]:
        for j in data["descripcionesOferta"]:
            for k in data["direccionesOferta"]:
                titulosOferta=data["titulosOferta"][0]
                descripcionesOferta=data["descripcionesOferta"][0]
                direccionesOferta=data["direccionesOferta"][0]
                return render_template('ofertas.html', titulosOferta=titulosOferta,descripcionesOferta=descripcionesOferta, direccionesOferta=direccionesOferta)
    



#Función principal que ejecuta la aplicación
if __name__ == '__main__':
    app.run(debug=True)
#Se importa la librería Flask, abort y render_template

import re
import json
import os
from turtle import pos
from markupsafe import escape
from flask import Flask, abort, render_template, request, flash, url_for, redirect
from empresa import Usuario

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

        return render_template('ofertas.html', titulosOferta=titulosOferta, descripcionesOferta=descripcionesOferta, direccionesOferta=direccionesOferta)
    else:
        #alerta en caso de que existan errores
        flash('Error al ingresar los datos')
        return render_template('crearofertas.html')

"""
data_Empresas={}
data_Empresas['datos']=[]
@app.route('/nuevoregistroempresa',methods=['POST'])

#función que permite enviar los datos ingresados hacia la tabla
def nuevoregistroempresa(): 
    nombreEmpresa= request.form.get('nombre')
    direccionEmpresa= request.form.get('direccion')
    telefonoEmpresa= request.form.get('telefono')
    correoEmpresa= request.form.get('correo')
    contraseniaEmpresa= request.form.get('contrasenia')

  

    #validar que se ingresen datos
    if len(nombreEmpresa)>0 and len(direccionEmpresa)>0 and len(telefonoEmpresa)>0 and len(correoEmpresa)>0 and len(contraseniaEmpresa)>0:
     
      
         #con path se especifica la ruta del archivo
       path, _=os.path.split(os.path.abspath(__file__))
       
       data_Empresas['datos'].append({"nombresEmpresas":nombreEmpresa,"direccionesEmpresas":direccionEmpresa,"telefonosEmpresas":telefonoEmpresa,"correosEmpresas":correoEmpresa,
        "contraseniasEmpresas":contraseniaEmpresa})
    
         #se escribe en el archivo datos.json
       with open(path+f'/registroempresa.json','w') as file:
            json.dump(data_Empresas, file, indent=4)

       return render_template('crearofertas.html', titulosOferta=titulosOferta, descripcionesOferta=descripcionesOferta, direccionesOferta=direccionesOferta)
    else:
        #alerta en caso de que existan errores
        flash('Error al ingresar los datos')
        return render_template('registroempresa.html')

"""
data_Empresas={}
data_Empresas['datos']=[]
@app.route('/nuevoregistroempresa',methods=['POST'])

#función que permite enviar los datos ingresados hacia la tabla
def nuevoregistroempresa(): 
    nombreEmpresa= request.form.get('nombre')
    direccionEmpresa= request.form.get('direccion')
    telefonoEmpresa= request.form.get('telefono')
    correoEmpresa= request.form.get('correo')
    contraseniaEmpresa= request.form.get('contrasenia')

    nuevaempresa=Usuario(correoEmpresa, contraseniaEmpresa)
    
    
    user=nuevaempresa.__dict__
    data_Empresas['datos']=[user]

    
         #con path se especifica la ruta del archivo
    path, _=os.path.split(os.path.abspath(__file__))

    #se escribe en el archivo datos.json
    with open(path+f'/registroempresa.json','w') as file:
            json.dump(user, file, indent=4)
        
    return render_template('crearofertas.html', titulosOferta=titulosOferta, descripcionesOferta=descripcionesOferta, direccionesOferta=direccionesOferta)
    
   

       






data_Postulantes={}
data_Postulantes['datos']=[]

@app.route('/nuevoregistropostulante',methods=['POST'])

#función que permite guardar los datos
def nuevoregistropostulante(): 
    nombrePostulante= request.form.get('nombre')
    telefonoPostulante= request.form.get('telefono')
    experienciaPostulante= request.form.get('experiencia')
    correoPostulante= request.form.get('correo')
    contraseniaPostulante= request.form.get('contrasenia')

    #validar que se ingresen datos
    if len(nombrePostulante)>0 and len(telefonoPostulante)>0 and len(experienciaPostulante)>0 and len(correoPostulante)>0 and len(contraseniaPostulante)>0:
       
       #se ingresen los datos a las listas
   
       
        data_Postulantes['datos'].append({"nombrePostulante":nombrePostulante, "telefonoPostulante":telefonoPostulante,
        "experienciaPostulante":experienciaPostulante, "correoPostulante": correoPostulante, "contraseniaPostulante":contraseniaPostulante})
        
   
        #con path se especifica la ruta del archivo
        path, _=os.path.split(os.path.abspath(__file__))
    
      
  
    
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
    
    correo= request.form.get("correo")
    contrasenia= request.form.get("contrasenia")

    path, _=os.path.split(os.path.abspath(__file__))
    
   #se carga el archivo registroempresas.json
    with open(path+'/registroempresa.json') as file:
       data= json.load(file)

    
"""
    for elemento in data['datos']:
        for i in range (len(elemento)):
            if correo==elemento["correosEmpresas"][i] and contrasenia==elemento["contraseniasEmpresas"][i]:
                     return render_template('crearofertas.html')
            else:
                     flash("Error")
                     return render_template('accederempresa.html')
"""
         
        
#Validación de usuarios postulantes

#ruta hacia validar_usuarios_postulantes
@app.route('/validar_usuarios_postulantes',methods=['POST'])

#función que permite visualizar las tareas almacenadas
def validar_usuarios_postulantes():
    
    correo= request.form.get("correo")
    contrasenia= request.form.get("contrasenia")

    path, _=os.path.split(os.path.abspath(__file__))
    
   #se carga el archivo registroempresas.json
    with open(path+'/registropostulante.json') as file:
       data= json.load(file)
       

    for i in len(data['datos']):
        ce=(data['datos'])[i].get("correoPostulante")[0]
        co=(data['datos'])[i].get("coPostulante")[0]
        

        if correo==ce and contrasenia==co:
            return render_template('ofertas.html')

        else:
                flash("Error")
                return render_template('accederpostulante.html')

    
    



#Función principal que ejecuta la aplicación
if __name__ == '__main__':
    app.run(debug=True)
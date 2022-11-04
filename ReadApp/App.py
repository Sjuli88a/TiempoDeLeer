from flask import Flask, render_template, request, redirect, url_for
from flaskext.mysql import MySQL

app=Flask(__name__)

#mysql conexion
conexion =MySQL()
app.secret_key = "kacciuwefcuwbechhbwegvuye42u3%"

app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']= 'root'
app.config['MYSQL_DATABASE_PASSWORD']='sebastian'
app.config['MYSQL_DATABASE_DB']= 'readapp2'

conexion.init_app(app)

@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/add_usuario', methods=["POST"])
def add_usuario():

    Nombre=request.form['Nombre']
    Correo=request.form['Correo']
    Contraseña=request.form['Contraseña']
       
    sql = "INSERT INTO usuario (Nombre, Correo, Contraseña) VALUES (%s, %s, %s)"
    datos = (Nombre, Correo, Contraseña)
    conn = conexion.connect()
    cursor = conn.cursor()
    cursor.execute(sql, datos)
    conn.commit()
    return redirect(url_for('inicio'))
    #print(Nombre)
    #print(Correo)
    #print(Contraseña)
    #cursor= MySQL.connection.cursor()
    #cursor.execute('INSERT INTO Usuario (IdUsuario, Nombre, Correo, Contraseña) VALUES (%s, %s, %s, %s)',
    #(Usuario, Nombre, Correo, Contraseña))
    #MySQL.connection.commit()
    #return render_template('Inicio.html')

@app.route('/inicio')
def inicio():
    return render_template ('Inicio.html')

@app.route('/')
def contacto(nombre):
    return render_template ('Inicio.html')

def Pagina_no_existe(error):
    return render_template('404.html'), 404

@app.route('/')
def categoria(nombre):
    return render_template ('categoria.html')


if __name__== '__main__':
    app.register_error_handler(404, Pagina_no_existe)
    app.run(debug=True )
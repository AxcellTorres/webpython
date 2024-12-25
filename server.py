from flask import Flask, render_template, request, render_template_string, url_for, redirect

app = Flask(__name__)

def home():
    return render_template('Login.html')

def menu():
    return render_template('Menu.html')

 #Credenciales de usuario almacenadas en el código 
Usuarios = { 
    "Kobayashi": "Nighttomate1",
    "usuario2": "contraseña2" 
    }
 
 #Función para verificar credenciales 
def verificar_credenciales(username, password): 
    return Usuarios.get(username) == password 
 
@app.route('/') 
def home(): 
    return render_template('Login.html') 
 
@app.route('/login', methods=['POST']) 
def login(): 
     username = request.form['username'] 
     password = request.form['password']
     if verificar_credenciales(username, password): 
        return redirect(url_for('menu')) 
     else: 
        return "Nombre de usuario o contraseña incorrectos" 

@app.route('/menu')
def menu():
    return render_template('Menu.html')
  
    
if __name__ == '__main__': 
     app.run(debug=True)
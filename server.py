from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

 #Credenciales de usuario almacenadas en el código 
Usuarios = { 
    "Ko": "Night",
    "TON": "Pvto" 
    }
 
 #Función para verificar credenciales 
def verificar_credenciales(username, password): 
    return Usuarios.get(username) == password 
 
@app.route('/') 
def home(): 
    return render_template('login.html') 
    
@app.route('/login', methods=['post']) 
def login(): 
     username = request.form['username'] 
     password = request.form['password']
     if verificar_credenciales(username, password): 
        return redirect(url_for('menu')) 
     else: 
        return render_template('login.html', error=True) 

@app.route('/menu')
def menu():
    return render_template('menu.html')
  
    
if __name__ == '__main__': 
     app.run(debug=True)
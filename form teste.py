import pyodbc
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('formulario.html')
   

@app.route('/resultado',methods = ['POST', 'GET'])
def resultado():
   if request.method == 'POST':
      result = request.form
      name = request.form['Name']
      dataN = request.form['Data']
      idade = request.form['Idade']
      genero = request.form['Genero']
      email = request.form['Email']
      objetivo = request.form['Objetivo']
      
      server = 'MAQUINA17-PC\SQLEXPRESS' 
      database = 'testepy' 
      usernamedb = '' 
      password = '' 
      cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+usernamedb+';PWD='+ password)
      cursor = cnxn.cursor()
      sql = "insert into cadastro values('" + name + "','" + dataN + "','" + idade +"','" + genero +"','" + email +"','" + objetivo + "')"
      cursor.execute(sql)
      cursor.commit()
      cursor.close()
      
      return "Usuário Cadastrado!"

      #row = cursor.fetchone()
      #if row != None:
      #   return "Usuario existente na base"
      #else:
      #   return "Usuario não existe"
      #return render_template("resultado.html",result = result)

if __name__ == '__main__':
   app.run(debug = True)

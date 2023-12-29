try:

    from flask import Flask,render_template,url_for,request,session,redirect,send_from_directory
    from flask_wtf.file import FileField 
    from flask_wtf import Form
    from wtforms import SubmitField
    from flask_mysqldb import MySQL
    from werkzeug.utils import secure_filename
    import mysql.connector
    from flask_mail import *
    import os

except:
    print(" Some module are missing..... Contact Harsh_sharan from further assistence!!!")

#defining connection
connection = mysql.connector.connect(host = "localhost",port = "3306", user = "sqluser", password = "password123",database = "user_data")

#definig cursor
cursor = connection.cursor()

#create flask instance
app = Flask(__name__)
app.secret_key = 'secret'

"""
activate this paragraph for sending email...!!! add you gmail id and password in config.json
with open(config.json, 'r') as f:
    param = json.load(f)['param']
mail = Mail(app)


app.config['MAIL_SERVER'] = 'smtp.google.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = param['gmail-user']    
app.config['MAIL_PASSWORD'] = param['gmail-password']  
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
"""

#routing homepage
@app.route('/')
def home():
    return render_template('home.html')

#routing opc loging page (database-- login_data)
@app.route('/ops_login_page')
def login_page():
    return render_template('login.html')

#defining login logic
@app.route('/login', methods = ["POST" , "GET"])
def login():    
    msg= " "    
    if request.method =='POST':
        email = request.form['email']
        password = request.form['password']
        cursor.execute('SELECT * FROM login_data WHERE email=%s AND password =%s',(email, password))
        record  = cursor.fetchone()
        if record:
            session['logged_in'] = True
            session['email'] = record[1]
            return redirect(url_for('upload_homepage'))
        else: 
            msg = "Incorrect username or password!!!"
    return render_template('home.html', msg = msg)

#routing client_login page
@app.route('/client_login')
def client_login_page():
    return render_template('client_login.html')

#routing client login and writing client_login logic
@app.route('/client_login', methods = ["POST" , "GET"])
def client_login():
    msg = ""
    if request.method =='POST':
        email = request.form['email2']
        password = request.form['password2']
        cursor.execute('SELECT * FROM client_user_data WHERE client_email=%s AND client_password =%s',(email, password))
        record  = cursor.fetchone()
        if record:
            session['logged_in'] = True
            session['email'] = record[1]
            return redirect(url_for('download_homepage'))
        else: 
            msg = "Incorrect username or password!!!"
    return render_template('home.html', msg = msg)

#routing registration page for client user(databse--client_user_data)
@app.route('/register_page')
def register_page():
    return render_template('register.html')

#defining registration logic
@app.route('/register', methods = ["POST" , "GET"])
def register():
    
    if request.method =='POST':
        username = request.form['username1']
        email = request.form['email1']
        password = request.form['password1']
        cursor.execute("INSERT INTO client_user_data(client_username, client_email, client_password) VALUES(%s , %s , %s)",(username, email, password))
        connection.commit()
    return render_template('login.html')

#creating home page for upload process
@app.route('/upload_homepage', methods = ["POST" , "GET"])
def upload_homepage():
    form = uploadform()

    return render_template('upload_home.html', form = form)

#routing upload page and it's logic
@app.route('/upload', methods=['POST' , "GET"])
def upload_file():
    uploaded_file = request.files['upload_file']  
    if uploaded_file.filename != '':
        file_path = f'statics/uploads/{uploaded_file.filename}'  
        uploaded_file.save(file_path)
        return 'File uploaded successfully!'
    else:
        return 'No file selected'

#routing download_home_page
@app.route('/download_homepage')
def download_homepage():
    folder_path = 'statics/uploads'  
    files = os.listdir(folder_path)
    return render_template('download.html', files=files)

#routing download send functionality   
@app.route('/download/<filename>')
def download_file(filename):
    folder_path = 'statics/uploads'
    return send_from_directory(folder_path, filename, as_attachment=True)




#creating class uploadform
class uploadform(Form):
    file = FileField()
    submit = SubmitField("Submit")




# Run the application
if __name__ == '__main__':
    app.run(debug=True)




from flask import Flask, render_template, request, redirect, url_for, session
from models import db, Admin, Client
import hashlib

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/consoelec'
app.config['SECRET_KEY'] = 'your_secret_key'
db.init_app(app)

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form.get('username')
        password = request.form.get('password')
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        
        print(f"Login attempt with login: {login}, password: {password}, hashed_password: {hashed_password}")  # Debugging
        
        admin = Admin.query.filter_by(login=login, password=hashed_password).first()
        
        if admin:
            session['admin_id'] = admin.id
            print(f"Login successful for admin id: {admin.id}")  # Debugging
            return redirect(url_for('clients'))
        else:
            print("Login failed: invalid login or password")  # Debugging
            return 'Login Failed'
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('admin_id', None)
    return redirect(url_for('login'))


@app.route('/clients')
def clients():
    if 'admin_id' not in session:
        return redirect(url_for('login'))
    clients = Client.query.all()
    return render_template('clients.html', clients=clients)

@app.route('/client/<int:id>')
def client_details(id):
    if 'admin_id' not in session:
        return redirect(url_for('login'))
    client = Client.query.get_or_404(id)
    return render_template('client_details.html', client=client)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

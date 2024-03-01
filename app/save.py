from flask import Flask
from flask import render_template, request, redirect, url_for, flash

from config import Config
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from models import db, Admin, KHR_Redddy, User

from forms import RegistrationForm

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# Define routes
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle login form submission
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        role = user.user_type
        if user and check_password_hash(user.password_hash, password):
            # Redirect to afterlogin page upon successful login
            return redirect(url_for('afterlogin'))
        else:
            flash('Login unsuccessful. Please check your username and password.', 'danger')
            return redirect(url_for('index'))

    return render_template('index.html')

@app.route('/create_user', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        # Handle create user form submission
        username = request.form['username']
        password = request.form['password']
        
        # Encrypt the password before storing it in the database
        hashed_password = generate_password_hash(password)

        # Create user
        user = User(username=username, password_hash=hashed_password)
        
        # Update the database with the user's information
        db.session.add(user)
        db.session.commit()
        
        flash('User created successfully!', 'success')
        print('User created successfully!')
        print('User added to the database')

        return redirect(url_for('index'))

    return render_template('create_user.html')


@app.route('/afterlogin')
def afterlogin():
    users = User.query.all()
    # Iterating and priting the users
    print(users)
    for user in users:
        print(user.username)
        
    return render_template('afterlogin.html', users=users)

        
@app.route('/events',   )
def events():
    events = {
        'event1': 'Python Workshop',
        'event2': 'Flask Workshop',
        'event3': 'Django Workshop'
    }
    
    return render_template('events.html', events=events)
        

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

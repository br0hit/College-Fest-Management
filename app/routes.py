from flask import render_template, request, redirect, url_for, flash
from forms import RegistrationForm
from flask import Flask
from models import db, Admin, KHR_Redddy, User
from config import Config
import time

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
        
        user = User.query.filter_by(username=username, password=password).first()
        if user:
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
        
        # Create user (implement this)
        flash('User created successfully!', 'success')
        print('User created successfully!')
        
        # Update the database with the user's information
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        print('User added to the database')
        
        return redirect(url_for('index'))

    return render_template('create_user.html')


@app.route('/afterlogin')
def afterlogin():
    users = User.query.all()
    # Iterating and priting the users
    for user in users:
        print(user.username, user.password)
        
    return render_template('afterlogin.html', users=users)

        
@app.route('/events', )
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

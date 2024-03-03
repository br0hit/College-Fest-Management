from flask import Flask
from flask import render_template, request, redirect, url_for, flash, session

from config import Config
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from functools import wraps

from models import db
from models import Admin, student, volunteer, organizer, participant, events

from forms import RegistrationForm

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)


# Define a decorator to check if the user is logged in and has the correct role
def login_required(role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'user_id' not in session or session['role'] != role:
                flash('Please log in with the correct role to access this page.', 'danger')
                return redirect(url_for('notworking'))  # Redirect to the respective login page
            return f(*args, **kwargs)
        return decorated_function
    return decorator

events_data = [
    ("Megalith", "Academic", "5th March", "3pm", "Description 1"),
    ("PalNight", "Cultural", "6th March", "8pm", "Description 2"),
    ("DaVinci", "Art", "6th March", "2pm", "Description 3"),
    ("Google Workshop", "Career", "7th March", "3pm", "Description 4"),
    ("EDMNight", "Cultural", "7th March", "9pm", "Description 5")
]

events = []
for event in events_data:
    event_dict = {
        "Name": event[0],
        "Type": event[1],
        "Date": event[2],
        "Time": event[3],
        "Description":  event[4]
    }
    events.append(event_dict)

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
            
            # Set the user_id and role in the session upon successful login
            session['user_id'] = user.id
            session['role'] = user.user_type
            
            print(session)
            
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
        user_type = request.form['user_type']
        
        # Encrypt the password before storing it in the database
        hashed_password = generate_password_hash(password)

        # Create user
        user = User(username=username, password_hash=hashed_password, user_type=user_type)
        
        # Update the database with the user's information
        db.session.add(user)
        db.session.commit()
        
        flash('User created successfully!', 'success')
        print('User created successfully!')
        print('User added to the database')

        return redirect(url_for('index'))

    return render_template('create_user.html')



@app.route('/testing', methods=['GET', 'POST'])
@login_required('test')
def testing():
    return render_template('testing.html')

@app.route('/afterlogin')
@login_required('admin')
def afterlogin():
    users = User.query.all()
    # Iterating and priting the users
    
    # Retrieve the user ID from the session
    type = session.get('role')
    print(type)
    
    print(users)
    for user in users:
        print(user.username)
        
    return render_template('afterlogin.html', users=users)

        
@app.route('/events')
def events():
    return render_template('events.html', events=events)

@app.route('/events/<event_name>')
def event_details(event_name):
    for event in events_data:
        if event[0] == event_name:
            event_details = {
                "Name": event[0],
                "Type": event[1],
                "Date": event[2],
                "Time": event[3],
                "Description": event[4]
            }
            return render_template('event_details.html', event=event_details)


@app.route('/notworking', methods=['GET', 'POST'])
@login_required('notadmin')
def notworking():
    #getting user id from session
    user_id = session.get('user_type')
    print(user_id)
    return render_template('notworking.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)



# Define routes
@app.route('/waste', methods=['GET', 'POST'])
def waste():
    if request.method == 'POST':
        # Handle login form submission
        username = request.form['username']
        password = request.form['password']

        
        user = User.query.filter_by(username=username).first()
        role = user.user_type
        if user and check_password_hash(user.password_hash, password):
            # Redirect to afterlogin page upon successful login
            
            # Set the user_id and role in the session upon successful login
            session['user_id'] = user.id
            session['role'] = user.user_type
            
            print(session)
            
            return redirect(url_for('afterlogin'))
        else:
            flash('Login unsuccessful. Please check your username and password.', 'danger')
            return redirect(url_for('index'))

    return render_template('index.html')



@app.route('/create_user_old', methods=['GET', 'POST'])
def create_user_old():
    if request.method == 'POST':
        # Handle create user form submission
        username = request.form['username']
        password = request.form['password']
        user_type = request.form['user_type']
        
        # Encrypt the password before storing it in the database
        hashed_password = generate_password_hash(password)

        # Create user
        user = User(username=username, password_hash=hashed_password, user_type=user_type)
        
        # Update the database with the user's information
        db.session.add(user)
        db.session.commit()
        
        flash('User created successfully!', 'success')
        print('User created successfully!')
        print('User added to the database')

        return redirect(url_for('index'))

    return render_template('create_user.html')
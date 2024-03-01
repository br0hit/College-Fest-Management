from flask import render_template, request, redirect, url_for, flash, jsonify
from forms import RegistrationForm
from flask import Flask
from models import db, Admin, KHR_Redddy, User
from config import Config
import time
from flask import request


app = Flask(__name__)
app.config.from_object(Config)
# db.init_app(app)

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

events_data = [
    ("Megalith", "Academic", "5th March", "3pm", "Description 1"),
    ("PalNight", "Cultural", "6th March", "8pm", "Description 2"),
    ("DaVinci", "Art", "6th March", "2pm", "Description 3"),
    ("Google Workshop", "Career", "7th March", "3pm", "Description 4"),
    ("EDMNight", "Cultural", "7th March", "9pm", "Description 5")
]

@app.route('/events')
def events():
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
        

@app.route('/register', methods=['POST'])
def register():
    event_name = request.json['eventName']
    # Perform any registration logic here
    print("Registration successful")
    # You can send the event name to another route if needed
    
    reponse = {}
    response['data'] = 'temp_data'
    repoonse['redirect'] = '/'
    
    return jsonify(response)


if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()
    app.run()

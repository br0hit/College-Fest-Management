from flask import Flask
from flask import render_template, request, redirect, url_for, flash, session
import random

from config import Config
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
import hashlib
from functools import wraps

from models import db
from models import Admin, student, volunteer, organizer, participant, events
from models import User

from forms import CreateEventForm, EventForm, LoginForm

# Create a hash
def create_hash(data):
    hasher = hashlib.sha256()  # You can choose a different algorithm if needed
    hasher.update(data.encode('utf-8'))
    return hasher.hexdigest()[:50]  # Limit the hash length to 100 characters

# Check a hash
def check_hash(data, expected_hash):
    return create_hash(data) == expected_hash

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



# Define routes
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('homepage.html')

@app.route('/login/participant', methods=['GET', 'POST'])
def login_participant():
    if request.method == 'POST':
        # Handle participant login form submission
        email = request.form['email']
        password = request.form['password']
        
        user = participant.query.filter_by(email=email).first()
        print(user)
        print(user.password)
        print(create_hash(password))
        if check_hash(password, user.password):
            # Redirect to afterlogin page upon successful login
            
            # Set the user_id and role in the session upon successful login
            session['user_id'] = user.id
            session['role'] = 'participant'
            
            print(session)
            
            return redirect(url_for('homepagep'))
        else:
            flash('Login unsuccessful. Please check your username and password.', 'danger')
            return redirect(url_for('none'))

    return render_template('participant_login.html')

@app.route('/login/student', methods=['GET', 'POST'])
def login_student():
    
    
    form = LoginForm()
    if form.validate_on_submit():
        
        email = form.email.data
        password = form.password.data
        
        user = student.query.filter_by(email=email).first()
        print(user)
        print(user.password)
        print(create_hash(password))
        
        if check_hash(password, user.password):
            # Redirect to afterlogin page upon successful login
            
            # Set the user_id and role in the session upon successful login
            session['user_id'] = user.id
            session['role'] = 'student'
            
            print(session)
            return redirect(url_for('homepages'))
        else:
            flash('Login unsuccessful. Please check your username and password.', 'danger')
            return redirect(url_for('none'))
        
    return render_template('student_login.html', form=form)

# @app.route('/login/student', methods=['GET', 'POST'])
# def login_student():
#     form = LoginForm()
#     if form.validate_on_submit():
#         email = form.email.data
#         password = form.password.data
        
#         # Dummy authentication, replace with your actual logic
#         user = student.query.filter_by(email=email).first()
#         if user and user.check_password(password):
#             # Set the user_id and role in the session upon successful login
#             session['user_id'] = user.id
#             session['role'] = 'student'
#             flash('Login successful!', 'success')
#             return redirect(url_for('home')) # Assuming 'home' is the name of your homepage route
#         else:
#             flash('Login unsuccessful. Please check your email and password.', 'danger')
#     return render_template('student_login.html', form=form)



@app.route('/login/organiser', methods=['GET', 'POST'])
def login_organiser():
    if request.method == 'POST':
        # Handle participant login form submission
        email = request.form['email']
        password = request.form['password']
        
        user = organizer.query.filter_by(email=email).first()
        print(user)
        print(user.password)
        print(create_hash(password))
        
        if check_hash(password, user.password):
            # Redirect to afterlogin page upon successful login
            
            # Set the user_id and role in the session upon successful login
            session['user_id'] = user.id
            session['role'] = 'organizer'
            
            print(session)
            return redirect(url_for('homepageo'))
        else:
            flash('Login unsuccessful. Please check your username and password.', 'danger')
            return redirect(url_for('none'))
        
    return render_template('organiser_login.html')


@app.route('/create_participant', methods=['GET', 'POST'])
def create_participant():
    if request.method == 'POST':
        
        # Handle create user form submission
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        is_allocated = True if 'is_allocated' in request.form else False
        
        # Encrypt the password before storing it in the database
        hashed_password = create_hash(password)
        
        # participant details should be taken from the participant form
        # if allocate bool is true, then random room number should be allocated
    
        # generate random room number if allocate is true
        # if allocate is false, then room number should be taken from the participant form
        
        if is_allocated:    
            random_number = random.randint(1,15)
            # Format and return the room number
            room_number = f"ROOM#{random_number}"
            user = participant(name=name, email=email, password=hashed_password, is_allocated=is_allocated, room_no=room_number)
        else:
            user = participant(name=name, email=email, password=hashed_password, is_allocated=is_allocated, room_no= "Not Allocated")
            
        db.session.add(user)
        db.session.commit()
        print('User added to the database')
        return redirect(url_for('index'))  # Assuming 'index' is the name of your homepage route
    
    return render_template('create_participant.html')

@app.route('/create_student', methods=['GET', 'POST'])
def create_student():
    if request.method == 'POST':
        
        # Handle create user form submission
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']    
            
        # Encrypt the password before storing it in the database
        hashed_password = create_hash(password)
        user = student(name=name, email=email, password=hashed_password)

        db.session.add(user)
        db.session.commit()
        print('User added to the database')
        return redirect(url_for('index'))  # Assuming 'index' is the name of your homepage route
    
    return render_template('create_student.html')


@app.route('/create_organiser', methods=['GET', 'POST'])
def create_organiser():
    if request.method == 'POST':
        
        # Handle create user form submission
        name = request.form['name']
        email = request.form['email']
        password = request.form['password'] 
        contact = request.form['contact']   
            
        # Encrypt the password before storing it in the database
        hashed_password = create_hash(password)
        user = organizer(name=name, email=email, password=hashed_password, contact=contact)

        db.session.add(user)
        db.session.commit()
        print('Organizer added to the database')
        return redirect(url_for('index'))  # Assuming 'index' is the name of your homepage route
    
    return render_template('create_organiser.html')
        
@app.route('/testing', methods=['GET', 'POST'])
def testing():
    
    # Query and print all the events
    
    with app.app_context():
        all_events = events.query.all()  # Query all events
        for event in all_events:
            print(f"Event ID: {event.event_id}, Name: {event.event_name}, Date: {event.event_date}, Time: {event.event_time}, Venue: {event.event_venue}, Description: {event.event_description}, Winner: {event.event_winner}, Organizer ID: {event.event_organizer}")
    
    return render_template('events.html', events=all_events)

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

        
@app.route('/homepagep', methods=['GET', 'POST'])
def homepagep():
    participant_id = session.get('user_id')
    participant_val = participant.query.get(participant_id)
    # Query and print all the events
    with app.app_context():
        all_events = events.query.all()  # Query all events
        for event in all_events:
            print(f"Event ID: {event.event_id}, Name: {event.event_name}, Date: {event.event_date}, Time: {event.event_time}, Venue: {event.event_venue}, Description: {event.event_description}, Winner: {event.event_winner}, Organizer ID: {event.event_organizer}")

    # Retrieve the flag for displaying the popup
    success = request.args.get('success', default=False, type=bool)
    
    return render_template('participant.html', events=all_events, registration_successful=success, user=participant_val)


# Define the route to handle the event action and redirection
@app.route('/handle_participant/<int:event_id>')
def handle_participant(event_id):
    
    # participant id should be taken from the session
    # event id should be taken from the event form
    # participant_id = 1
    participant_id = session.get('user_id')
    participant_val = participant.query.get(participant_id)
    event_val = events.query.get(event_id)
    participant_val.events.append(event_val)
    db.session.commit()
    print('Participant registered for the event')

    # Redirect to the /participant page with the success flag set to True
    return redirect(url_for('homepagep', success=True))


# Define the route for viewing participant events
@app.route('/participant_events')
def participant_events():
    
    # Get participant ID from the session
    participant_id = session.get('user_id')
    
    # participant id should be taken from the session
    # participant_id = 1
    participant_val = participant.query.get(participant_id)
    print(f"Participant: {participant_val.name}, Email: {participant_val.email}, Events: {participant_val.events}")
    for event in participant_val.events:
        print(f"Event ID: {event.event_id}, Name: {event.event_name}, Date: {event.event_date}, Time: {event.event_time}, Venue: {event.event_venue}, Description: {event.event_description}, Winner: {event.event_winner}, Organizer ID: {event.event_organizer}")
    
    # Print the events in which the participant is there 
    return render_template('participant_events.html', events=participant_val.events, user=participant_val)

@app.route('/homepages', methods=['GET', 'POST'])
def homepages():
    student_id = session.get('user_id')
    student_val = student.query.get(student_id)
    
    # Query and print all the events
    with app.app_context():
        all_events = events.query.all()  # Query all events
        for event in all_events:
            print(f"Event ID: {event.event_id}, Name: {event.event_name}, Date: {event.event_date}, Time: {event.event_time}, Venue: {event.event_venue}, Description: {event.event_description}, Winner: {event.event_winner}, Organizer ID: {event.event_organizer}")

    # Retrieve the flag for displaying the popup
    success = request.args.get('success', default=False, type=bool)
    
    return render_template('student.html', events=all_events, registration_successful=success, user =student_val )

@app.route('/homepages/volunteer', methods=['GET', 'POST'])
def homepages_volunteer():

    
    # student details should be taken from the session id of the student
    student_id = session.get('user_id')
    student_val = student.query.get(student_id)
    # check if student is already registered as a volunteer
    if volunteer.query.filter_by(email=student_val.email).first():
        print("Student is already registered as a volunteer.")
    else:
        # All checks passed, proceed to register the student as a volunteer
        new_volunteer = volunteer(name=student_val.name,email=student_val.email,password=student_val.password)
        db.session.add(new_volunteer)
        try:
            db.session.commit()
            print("Student registered as a volunteer successfully.")
        except Exception as e:
            # Rollback in case of error
            db.session.rollback()
            print(f"An error occurred: {e}")
    
    # Query and print all the events
    with app.app_context():
        all_events = events.query.all()  # Query all events
        for event in all_events:
            print(f"Event ID: {event.event_id}, Name: {event.event_name}, Date: {event.event_date}, Time: {event.event_time}, Venue: {event.event_venue}, Description: {event.event_description}, Winner: {event.event_winner}, Organizer ID: {event.event_organizer}")

    # Retrieve the flag for displaying the popup
    success = request.args.get('success', default=False, type=bool)
    
    return render_template('student_volunteer.html', events=all_events, registration_successful=success, user =student_val)

# Define the route to handle the event action and redirection
@app.route('/handle_student/<int:event_id>')
def handle_student(event_id):
    
    # student id should be taken from the session
    # event id should be taken from the event form
    student_id = session.get('user_id')
    student_val = student.query.get(student_id)
    event = events.query.get(event_id)
    volunteer_val = volunteer.query.filter_by(email=student_val.email).first()
    # volunteer.events.append(event)
 
    if event in volunteer_val.events:
            print("Student is already registered as a volunteer for this event.")
    else:
            # All checks passed, proceed to register the student as a volunteer for the event
            volunteer_val.events.append(event)
            try:
                db.session.commit()
                print("Student registered as a volunteer for the event successfully.")
            except Exception as e:
                # Rollback in case of error
                db.session.rollback()
                print(f"An error occurred: {e}")
    print('Student registered as a volunteer for the event')
    # db.session.commit()
    print('student registered for the event')

    # Redirect to the /student page with the success flag set to True
    return redirect(url_for('homepages_volunteer', success=True))

# Define the route for viewing volunteered events
@app.route('/student_events')
def student_events():
    
    # student id should be taken from the session
    student_id = session.get('user_id')
    student_val = student.query.get(student_id)
    volunteer_val = volunteer.query.filter_by(email=student_val.email).first()
 
    for event in volunteer_val.events:
        print(f"Event ID: {event.event_id}, Name: {event.event_name}, Date: {event.event_date}, Time: {event.event_time}, Venue: {event.event_venue}, Description: {event.event_description}, Winner: {event.event_winner}, Organizer ID: {event.event_organizer}")
    
    # Print the events in which the participant is there 
    return render_template('student_events.html', events=volunteer_val.events, user= student_val)

@app.route('/homepageo', methods=['GET', 'POST'])
def homepageo():
    organiser_id = session.get('user_id')
    organiser_val = organizer.query.get(organiser_id)
    
    # Query and print all the events
    with app.app_context():
        all_events = events.query.all()  # Query all events
        for event in all_events:
            print(f"Event ID: {event.event_id}, Name: {event.event_name}, Date: {event.event_date}, Time: {event.event_time}, Venue: {event.event_venue}, Description: {event.event_description}, Winner: {event.event_winner}, Organizer ID: {event.event_organizer}")

    # Retrieve the flag for displaying the popup
    success = request.args.get('success', default=False, type=bool)
    
    return render_template('organiser.html', events=all_events, registration_successful=success,user= organiser_val)


# Create a route for creating events
@app.route('/create_event', methods=['GET', 'POST'])
def create_event():
    organiser_id = session.get('user_id')
    organiser_val = organizer.query.get(organiser_id)
    
    form = EventForm()
    if form.validate_on_submit():
        event_name = form.event_name.data
        event_date = form.event_date.data
        event_time = form.event_time.data
        event_venue = form.event_venue.data
        event_description = form.event_description.data
        event_winner = form.event_winner.data
        
        # Converting event_date to string format
        event_date = event_date.strftime('%Y-%m-%d')
        
        # Converting event_time to string format
        event_time = event_time.strftime('%H:%M')

        # Create a new event object
        new_event = events(event_name=event_name, event_date=event_date, event_time=event_time,
                          event_venue=event_venue, event_description=event_description, event_winner=event_winner, event_organizer=session.get('user_id'))
        db.session.add(new_event)
        db.session.commit()

        # Redirect to the organizer route after successful event creation
        return redirect(url_for('homepageo'))

    return render_template('create_event.html', form=form, user= organiser_val)

@app.route('/organiser_events')
def organiser_events():
        
    # Get the organizer ID from the session
    organizer_id = session.get('user_id')
    
    # organizer id should be taken from the session
    organizer_val = organizer.query.get(organizer_id)
    for event in organizer_val.events:
        print(f"Event ID: {event.event_id}, Name: {event.event_name}, Date: {event.event_date}, Time: {event.event_time}, Venue: {event.event_venue}, Description: {event.event_description}, Winner: {event.event_winner}, Organizer ID: {event.event_organizer}")
            
    return render_template('organiser_events.html', events=organizer_val.events, user=organizer_val)  
 
@app.route('/organiser_volunteers')
def organiser_volunteers():
            
    # Get the organizer ID from the session
    organizer_id = session.get('user_id')
    organizer_val = organizer.query.get(organizer_id)
    for event in organizer_val.events:
        print(f"Event ID: {event.event_id}, Name: {event.event_name}, Date: {event.event_date}, Time: {event.event_time}, Venue: {event.event_venue}, Description: {event.event_description}, Winner: {event.event_winner}, Organizer ID: {event.event_organizer}")
        for volunteer in event.volunteers:
            print(f"Volunteer ID: {volunteer.id}, Name: {volunteer.name}, Email: {volunteer.email}")
    
    return render_template('organiser_volunteers.html', events= organizer_val.events, user=organizer_val)    


@app.route('/organiser_participants')
def organiser_participants():
    
    # Get the organizer ID from the session
    organizer_id = session.get('user_id')    
    organizer_val = organizer.query.get(organizer_id)
    for event in organizer_val.events:
        print(f"Event ID: {event.event_id}, Name: {event.event_name}, Date: {event.event_date}, Time: {event.event_time}, Venue: {event.event_venue}, Description: {event.event_description}, Winner: {event.event_winner}, Organizer ID: {event.event_organizer}")
        for participant in event.participants:
            print(f"Participant ID: {participant.id}, Name: {participant.name}, Email: {participant.email}, Room No: {participant.room_no}, Is Allocated: {participant.is_allocated}")

    return render_template('organiser_participants.html', events= organizer_val.events, user= organizer_val)
    
    
@app.route('/events/<event_name>')
def event_details(event_name):
    
    

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

from flask import Flask
from flask import render_template, request, redirect, url_for, flash, session
import random

from config import Config
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
import hashlib
from functools import wraps

from models import db
from models import Admin, student, volunteer, organizer, participant, events, room_count
from forms import EventForm, LoginForm

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


def login_required(role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'user_id' not in session or session['role'] != role:
                flash('Please log in with the correct role to access this page.', 'danger')
                # return redirect(url_for('index', popup=False))  # Pass popup=True if not logged in
                return redirect(url_for('index'))  # Pass popup=True if not logged in

            return f(*args, **kwargs)
        return decorated_function
    return decorator



# Define routes

# Defining Admin route
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    # HTML will have a form to admin login
    if request.method == 'POST':
        # Handle admin login form submission
        email = request.form['email']
        password = request.form['password']
        
        # Check if the email and the password are correct
        
        user = Admin.query.filter_by(email=email).first()
        if(user.password == password):
            # Redirect to afterlogin page upon successful login
            
            # Set the user_id and role in the session upon successful login
            session['user_id'] = user.id
            session['role'] = 'admin'
            print(session)
            return redirect(url_for('admin_home'))
        else:
            flash('Login unsuccessful. Please check your username and password.', 'danger')
            return redirect(url_for('admin'))
        
    return render_template('admin.html')

# Define the route for the admin homepage
@app.route('/admin_home')
@login_required('admin')
def admin_home():
    return render_template('admin_home.html')

@app.route('/', methods=['GET', 'POST'])
def index():
    popup = request.args.get('popup', False)  # Check if popup argument is present in the request
    # return render_template('homepage.html', popup=popup)
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
            return redirect(url_for('login_participant'))

    return render_template('participant_login.html')

@app.route('/login/student', methods=['GET', 'POST'])
def login_student():
        
    if request.method == 'POST':
        # Handle participant login form submission
        email = request.form['email']
        password = request.form['password']
        
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
            return redirect(url_for('login_student'))
        
    return render_template('student_login.html')

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
            return redirect(url_for('login_organiser'))
        
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
            
            # getting the first row from the room_count table
            room_count_val = room_count.query.first()
    
            # check if room_count_val has a value greater than 0
            if room_count_val.room_no > 0:
                # allot the room number to the participant
                random_number = room_count_val.room_no                              
                # Format and return the room number
                room_number = f"ROOM#{random_number}"
                # decrement the room number by 1
                room_count_val.room_no = room_count_val.room_no - 1
                # Update the database
                db.session.commit()
                
                user = participant(name=name, email=email, password=hashed_password, is_allocated=is_allocated, room_no=room_number)
            else:
                
                # Display a message to the user that no rooms are available
                flash('No rooms are available.','danger')
                user = participant(name=name, email=email, password=hashed_password, is_allocated=0, room_no="No room available")
        else:
            user = participant(name=name, email=email, password=hashed_password, is_allocated=is_allocated, room_no= "Not Allocated")
            
        db.session.add(user)
        try:
            db.session.commit()
            print("New Participant Created.")
        except Exception as e:
            # Rollback in case of error
            db.session.rollback()
            print(f"An error occurred: {e}")
        print('Participant added to the database')
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
        try:
            db.session.commit()
            print("New Student Created.")
        except Exception as e:
            # Rollback in case of error
            db.session.rollback()
            print(f"An error occurred: {e}")
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
        try:
            db.session.commit()
            print("New Organizer Created.")
        except Exception as e:
            # Rollback in case of error
            db.session.rollback()
            print(f"An error occurred: {e}")
        print('Organizer added to the database')
        return redirect(url_for('index'))  # Assuming 'index' is the name of your homepage route
    
    return render_template('create_organiser.html')
        
@app.route('/testing', methods=['GET', 'POST'])
@login_required('organizer')
def testing():
    
    # Query and print all the events
    
    with app.app_context():
        all_events = events.query.all()  # Query all events
        for event in all_events:
            print(f"Event ID: {event.event_id}, Name: {event.event_name}, Date: {event.event_date}, Time: {event.event_time}, Venue: {event.event_venue}, Description: {event.event_description}, Winner: {event.event_winner}, Organizer ID: {event.event_organizer}")
    
    return render_template('events.html', events=all_events)
        
@app.route('/homepagep', methods=['GET', 'POST'])
@login_required('participant')
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
    
    # Check if the participant is already registered for the event
    if event_val in participant_val.events:
        print("Participant is already registered for the event.")
    else:
        # All checks passed, proceed to register the participant for the event
        participant_val.events.append(event_val)
        try:
            db.session.commit()
            print("Participant registered for the event successfully.")
        except Exception as e:
            # Rollback in case of error
            db.session.rollback()
            print(f"An error occurred: {e}")
    print('Participant registered for the event')

    # Redirect to the /participant page with the success flag set to True
    return redirect(url_for('homepagep', success=True))


# Define the route for viewing participant events
@app.route('/participant_events')
@login_required('participant')
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
@login_required('student')
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
@login_required('student')
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
@login_required('student')
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
@login_required('organizer')
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
@login_required('organizer')
def create_event():
    organiser_id = session.get('user_id')
    organizer_val = organizer.query.get(organiser_id)
    
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
        
        # If the event is created successfully, commit the changes to the database, using try and catch
        db.session.add(new_event)        
        try:
            db.session.commit()
            print("Event Created Sucessfully.")
        except Exception as e:
            # Rollback in case of error
            db.session.rollback()
            print(f"An error occurred: {e}")

        # Redirect to the organizer route after successful event creation
        return redirect(url_for('homepageo'))

    return render_template('create_event.html', form=form, user= organizer_val)

@app.route('/organiser_events')
@login_required('organizer')
def organiser_events():
        
    # Get the organizer ID from the session
    organizer_id = session.get('user_id')
    
    # organizer id should be taken from the session
    organizer_val = organizer.query.get(organizer_id)
    for event in organizer_val.events:
        print(f"Event ID: {event.event_id}, Name: {event.event_name}, Date: {event.event_date}, Time: {event.event_time}, Venue: {event.event_venue}, Description: {event.event_description}, Winner: {event.event_winner}, Organizer ID: {event.event_organizer}")
            
    return render_template('organiser_events.html', events=organizer_val.events, user=organizer_val)  
 
@app.route('/organiser_volunteers')
@login_required('organizer')
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
@login_required('organizer')
def organiser_participants():
    
    # Get the organizer ID from the session
    organizer_id = session.get('user_id')    
    organizer_val = organizer.query.get(organizer_id)
    for event in organizer_val.events:
        print(f"Event ID: {event.event_id}, Name: {event.event_name}, Date: {event.event_date}, Time: {event.event_time}, Venue: {event.event_venue}, Description: {event.event_description}, Winner: {event.event_winner}, Organizer ID: {event.event_organizer}")
        for participant in event.participants:
            print(f"Participant ID: {participant.id}, Name: {participant.name}, Email: {participant.email}, Room No: {participant.room_no}, Is Allocated: {participant.is_allocated}")

    return render_template('organiser_participants.html', events= organizer_val.events, user= organizer_val)

@app.route('/organiser_updatewinner', methods=['GET', 'POST'])
@login_required('organizer')
def organiser_updatewinner():
    
    # Get all the events by query
    
    all_events = events.query.all()
    
    if request.method == 'POST':
        winners = {}
        for event in all_events:
            winner_name = request.form.get('winner_' + event.event_name)
            if winner_name:
                winners[event.event_name] = winner_name
                # Update the event winner in the database
                event = events.query.get(event.event_id)
                # new winner from the form
                event.event_winner = winner_name
                try:
                    db.session.commit()
                    print("Event winner updated successfully.")
                except Exception as e:
                    # Rollback in case of error
                    db.session.rollback()
        # Now winners dictionary contains event names as keys and corresponding winner names as values
        print(winners)  # You can process this data as per your requirement
        return redirect(url_for('homepageo'))

    return render_template('organiser_updatewinner.html', events=all_events) 
  

@app.route('/notworking', methods=['GET', 'POST'])
@login_required('notadmin')
def notworking():
    #getting user id from session
    user_id = session.get('user_type')
    print(user_id)
    return render_template('notworking.html')

@app.route('/logout')
def logout():
    # Clear the session
    session.clear()
    # Redirect to the login page
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

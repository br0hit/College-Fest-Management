# with app.app_context():
#     all_events = events.query.all()  # Query all events
#     for event in all_events:
#         print(f"Event ID: {event.event_id}, Name: {event.event_name}, Date: {event.event_date}, Time: {event.event_time}, Venue: {event.event_venue}, Description: {event.event_description}, Winner: {event.event_winner}, Organizer ID: {event.event_organizer}")


# # adding a new event to the database as the organizer
# with app.app_context():
#     # events details should be taken from the organizer_event form
#     # organizer id should be taken from the session
#     new_event = events(event_name='New Event', event_date='2021-01-01', event_time='00:00:00', event_venue='New Venue', event_description='New Description', event_winner='New Winner', event_organizer=1)
#     db.session.add(new_event)
#     db.session.commit()
#     print('New event added to the database')


# # adding a new participant to the database
# with app.app_context():
#     # participant details should be taken from the participant form
#     # if allocate bool is true, then random room number should be allocated

#     # generate random room number if allocate is true
#     # if allocate is false, then room number should be taken from the participant form

#     # if allocate is true, then is_allocated should be true
#     # if allocate is false, then is_allocated should be false

#     random_number = random.randint(1,15)
#     # Format and return the room number
#     room_number = f"ROOM#{random_number}"
#     # Create a new participant
#     new_participant = participant(name='New Participant',email='newparticipant@gmail.com',password='newpassword',room_no=room_number,is_allocated=True)
#     db.session.add(new_participant)
#     db.session.commit()
#     print('New participant added to the database')


# # participant registers for an event 
# with app.app_context():
#     # participant id should be taken from the session
#     # event id should be taken from the event form
#     participant_id = 1
#     event_id = 3
#     participant = participant.query.get(participant_id)
#     event = events.query.get(event_id)
#     participant.events.append(event)
#     db.session.commit()
#     print('Participant registered for the event')
    

# printing the list of events for a participant
with app.app_context():
    # participant id should be taken from the session
    participant_id = 1
    participant = participant.query.get(participant_id)
    print(f"Participant: {participant.name}, Email: {participant.email}, Events: {participant.events}")
    for event in participant.events:
        print(f"Event ID: {event.event_id}, Name: {event.event_name}, Date: {event.event_date}, Time: {event.event_time}, Venue: {event.event_venue}, Description: {event.event_description}, Winner: {event.event_winner}, Organizer ID: {event.event_organizer}")
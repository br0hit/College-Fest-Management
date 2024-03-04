from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Admin(db.Model):
    _tablename_ = 'admin'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)


class student(db.Model):
    _tablename_ = 'student'
    id= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

    def _repr_(self):
        return f"student('{self.name}', '{self.email}')"
    

volunteer_events = db.Table('volunteer_events',
    db.Column('volunteer_id', db.Integer, db.ForeignKey('volunteer.id',ondelete="CASCADE"), primary_key=True),
    db.Column('event_id', db.Integer, db.ForeignKey('events.event_id',ondelete="CASCADE"), primary_key=True)
)

class volunteer(db.Model):
    _tablename_ = 'volunteer'
    id= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    events= db.relationship('events', secondary=volunteer_events, backref=db.backref('volunteers', lazy='dynamic'))



class organizer(db.Model):
    _tablename_ = 'organizer'
    id= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(100), nullable=False)
    events = db.relationship('events', backref='organizer', lazy=True, cascade="all, delete-orphan")

participants_events = db.Table('participants_events',
    db.Column('participant_id', db.Integer, db.ForeignKey('participant.id', ondelete="CASCADE")),
    db.Column('event_id', db.Integer, db.ForeignKey('events.event_id', ondelete="CASCADE")),
    db.PrimaryKeyConstraint('participant_id', 'event_id')
)


class participant(db.Model):
    _tablename_ = 'participant'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    room_no = db.Column(db.String(100), nullable=True)
    is_allocated = db.Column(db.Boolean, nullable=False, default=False)
    events = db.relationship('events', secondary=participants_events, backref=db.backref('participants', lazy='dynamic'))




# event must have only 1 organizer 
# event may have many participants
class events(db.Model):
    _tablename_ = 'events'
    event_id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(100), nullable=False)
    event_date = db.Column(db.String(100), nullable=False)
    event_time = db.Column(db.String(100), nullable=False)
    event_venue = db.Column(db.String(100), nullable=False)
    event_description = db.Column(db.String(100), nullable=False)
    event_winner = db.Column(db.String(100), nullable=True)
    event_organizer = db.Column(db.Integer, db.ForeignKey('organizer.id'), nullable=False)
    # No need to add anything here for the (participants) many-to-many, it's defined in the participant model
    # No need to add anything here for the (volunteer) many-to-many, it's defined in the volunteer model
from flask import Blueprint, render_template, request
from .models import User, Ticket
from werkzeug.utils import secure_filename
from . import db
main = Blueprint('main', __name__)
UPLOAD_FOLDER = 'static/uploads'  # or wherever you want to store uploaded files



@main.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', user=users)



@main.route('/knowledge')
def knowledge():
    return render_template('knowledge.html')



@main.route('/admin')
def admin():
    tickets = Ticket.query.all()
    return render_template('admin.html', tickets=tickets)



@main.route('/closed')
def closed():
    return render_template('closed.html')



@main.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    department = request.form['department']
    problem = request.form['problem']
    photo = request.files.get('photo')

    photo_filename = None
    if photo and photo.filename:
        photo_filename = secure_filename(photo.filename)
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)
        photo.save(os.path.join(UPLOAD_FOLDER, photo_filename))

    # Create and save the ticket
    ticket = Ticket(
        name=name,
        department=department,
        problem=problem,
        photo_filename=photo_filename
    )
    db.session.add(ticket)
    db.session.commit()

    return render_template('index.html', ticket=ticket)


@main.route('/delete')
def delete_ticket():
    tickets = Ticket.query.all()
    ticket_id = request.args.get('id')
    ticket = Ticket.query.get(ticket_id)

    if ticket:
        db.session.delete(ticket)
        db.session.commit()

    return render_template('admin.html', tickets=tickets)

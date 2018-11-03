from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost/flasknote"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(120), index=True, unique=True)
    user_image_url = db.column(db.String(120), index=True, unique=True)

def __repr__(self):
    return '<User %r>' %self.username

#flask initdb
@app.cli.command('initdb')
def initdb_command():
    db.create_all()

@app.route('/')
def hello_world:
    return 'Hello, World!'

@app.route('/register')
def register():
    newUser = User(username="Rasmus Lerdorf", description="PHP", user_image_url="r6")
    db.session.add(newUser)
    db.session.commit()
    return render_template('result.html', user=newUser)

users = User.query.all()
for user in users:
    print(user.id, user.username, user.description, user.user_image_url)
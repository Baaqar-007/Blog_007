# import necessary libraries
from datetime import datetime
from flask import Flask , render_template , flash, redirect , url_for 
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
# initialize flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = '33754a16e180c8a45c1b1cdf867a2157' # protects against forgery attacks , generated from "secrets"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique =True , nullable = False)
    email = db.Column(db.String(120), unique =True , nullable = False)
    image_file = db.Column(db.String(20), nullable = False, default = 'deafult.jpg')
    password = db.Column(db.String(60),  nullable = False)
    posts = db.relationship('Post', backref='author', lazy=True) # data is not loaded unless actually needed (lazy collection)
    
    def __repr__(self):
        return f"User('{self.username}' , '{self.email}' , '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True) 
    title = db.Column(db.String(100), nullable= False)
    date_posted = db.Column(db.DateTime, nullable= False, default = datetime.utcnow) # no parenthesis cause we need the function not the time right now
    content = db.Column(db.Text, nullable=False) 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"
    



    

# list of sample blog posts
posts = [
    {
        'author' : 'Zain',
        'title' : 'Blog 1',
        'content' : '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec a diam tellus''',
        'date_posted' : 'April 22 , 2023'
    }
    ,
    {
        'author' : 'Zain',
        'title' : 'Blog 2',
        'content' : '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec a diam tellus''',
        'date_posted' : 'April 25 , 2023'
    }
]

# define home route
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

# define about route
@app.route('/about')
def about():
    return render_template('about.html', title = "About")

@app.route('/register', methods =["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for('home'))
    return render_template('register.html', title = "Register", form = form)

@app.route('/login', methods =["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f"You have been logged in!", "success")
            return redirect(url_for('home'))
        else:
            flash("Login failed. Please check username and password.", "danger")
    return render_template('login.html', title = "Login", form = form)



# run the app in debug mode
if __name__ == '__main__' :
    app.run(debug=True)
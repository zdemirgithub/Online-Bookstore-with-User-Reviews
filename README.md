# Online-Bookstore-with-User-Reviews

Project: Online Bookstore with User Reviews
Description:
This project involves building an online bookstore web application where users can browse books, leave reviews, and view average ratings. The application will use MongoDB as the database to store book information and user reviews.

Technologies Used:

Python (Flask framework)
MongoDB (MongoDB Atlas for cloud hosting)
Flask-PyMongo (Python wrapper for MongoDB)
HTML/CSS (for frontend)
Jinja2 (templating engine for Flask)
Bootstrap (CSS framework for styling)
Flask-WTF (for handling forms)
Project Structure:

app.py: Python script for Flask application logic.
templates/: HTML templates for rendering web pages.
static/: Static files (e.g., CSS, JavaScript) for frontend.
models.py: Python script defining MongoDB database models.
forms.py: Python script defining Flask-WTF forms.
config.py: Configuration file for MongoDB connection.



Certainly! Here's a project idea that integrates MongoDB with Python for a web application:

Project: Online Bookstore with User Reviews
Description:
This project involves building an online bookstore web application where users can browse books, leave reviews, and view average ratings. The application will use MongoDB as the database to store book information and user reviews.

Technologies Used:

Python (Flask framework)
MongoDB (MongoDB Atlas for cloud hosting)
Flask-PyMongo (Python wrapper for MongoDB)
HTML/CSS (for frontend)
Jinja2 (templating engine for Flask)
Bootstrap (CSS framework for styling)
Flask-WTF (for handling forms)
Project Structure:

app.py: Python script for Flask application logic.
templates/: HTML templates for rendering web pages.
static/: Static files (e.g., CSS, JavaScript) for frontend.
models.py: Python script defining MongoDB database models.
forms.py: Python script defining Flask-WTF forms.
config.py: Configuration file for MongoDB connection.
Code:

app.py

python
Copy code
from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from forms import ReviewForm

app = Flask(__name__)
app.config['MONGO_URI'] = 'your_mongodb_uri'
mongo = PyMongo(app)

# MongoDB models (defined in models.py)

@app.route('/')
def index():
    books = mongo.db.books.find()
    return render_template('index.html', books=books)

@app.route('/book/<book_id>', methods=['GET', 'POST'])
def book_detail(book_id):
    book = mongo.db.books.find_one_or_404({'_id': book_id})
    form = ReviewForm()

    if form.validate_on_submit():
        # Save review to MongoDB
        review = {
            'username': form.username.data,
            'rating': form.rating.data,
            'comment': form.comment.data
        }
        mongo.db.reviews.insert_one(review)
        return redirect(url_for('book_detail', book_id=book_id))

    return render_template('book_detail.html', book=book, form=form)

if __name__ == '__main__':
    app.run(debug=True)
models.py

python
Copy code
from app import mongo

# MongoDB models
# Example:
# class Book(Document):
#     title = StringField()
#     author = StringField()
#     description = StringField()
#     rating = FloatField()
#     # Add more fields as needed

# class Review(Document):
#     book_id = ObjectIdField()
#     username = StringField()
#     rating = FloatField()
#     comment = StringField()
#     # Add more fields as needed
forms.py

python
Copy code
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class ReviewForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(max=50)])
    rating = FloatField('Rating', validators=[DataRequired()])
    comment = TextAreaField('Comment', validators=[DataRequired(), Length(max=500)])
    submit = SubmitField('Submit Review')
templates/index.html

html
Copy code
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Online Bookstore</title>
    <!-- Add Bootstrap CSS -->
</head>
<body>
    <h1>Online Bookstore</h1>
    <ul>
        {% for book in books %}
            <li><a href="{{ url_for('book_detail', book_id=book._id) }}">{{ book.title }}</a></li>
        {% endfor %}
    </ul>
</body>
</html>
templates/book_detail.html

html
Copy code
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ book.title }} - Online Bookstore</title>
    <!-- Add Bootstrap CSS -->
</head>
<body>
    <h1>{{ book.title }}</h1>
    <p>{{ book.author }}</p>
    <p>{{ book.description }}</p>
    <h2>Reviews</h2>
    <ul>
        {% for review in book.reviews %}
            <li>{{ review.username }} - Rating: {{ review.rating }} - {{ review.comment }}</li>
        {% endfor %}
    </ul>
    <h3>Add Review</h3>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.username.label }} {{ form.username() }}<br>
        {{ form.rating.label }} {{ form.rating() }}<br>
        {{ form.comment.label }} {{ form.comment() }}<br>
        {{ form.submit() }}
    </form>
</body>
</html>
Run the Project:

Install Flask (pip install Flask Flask-PyMongo Flask-WTF).
Set up a MongoDB database and replace 'your_mongodb_uri' in app.py with your MongoDB URI.
Create MongoDB models in models.py.
Create HTML templates in templates/.
Start the Flask server by running python app.py.
Open your web browser and go to http://localhost:5000 to view the online bookstore.
This project provides a simple example of integrating MongoDB with a Python web application using Flask. You can further expand the project by adding authentication, more features (e.g., user accounts, book search), and improving the frontend design.

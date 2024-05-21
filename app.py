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

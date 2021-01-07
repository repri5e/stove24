from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask('__name__')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stove.db'
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String)
    content = db.Column(db.String, nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Post %r>' % self.id

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        post_author = request.form['post_author']
        post_content = request.form['post_content']
        if post_author == '':
            new_post = Post(content=post_content, author='Аноним')
        else:
            new_post = Post(content=post_content, author=post_author)

        try:
            db.session.add(new_post)
            db.session.commit()
            return redirect('/')
        except:
            print('database error')
            return 'Ошибка во время публикации.'

    else:
        posts = Post.query.order_by(Post.date_posted).all()
        return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)

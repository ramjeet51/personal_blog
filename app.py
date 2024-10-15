# app.py
from flask import Flask, render_template, request, redirect, url_for
from models import create_table, add_post, get_posts, get_post, update_post, delete_post

app = Flask(__name__)

# Call create_table() directly when starting the app
create_table()

@app.route('/')
def index():
    posts = get_posts()
    return render_template('index.html', posts=posts)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        tags = request.form['tags']
        add_post(title, content, tags)
        return redirect(url_for('index'))
    return render_template('create_post.html')

@app.route('/edit/<int:post_id>', methods=['GET', 'POST'])
def edit(post_id):
    post = get_post(post_id)
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        tags = request.form['tags']
        update_post(post_id, title, content, tags)
        return redirect(url_for('index'))
    return render_template('edit_post.html', post=post)

@app.route('/delete/<int:post_id>')
def delete(post_id):
    delete_post(post_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

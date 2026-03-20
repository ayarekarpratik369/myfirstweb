from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)


UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        pic = request.files['pic']

        # Save uploaded file
        if pic:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], pic.filename)
            pic.save(filepath)

        # For now, just print the info to console
        print(f"Name: {name}, Password: {password}, Pic saved at: {filepath}")

        return f"Account created for {name}!"

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
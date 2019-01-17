from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)


@app.route('/home')
def HomePage():
    return render_template("index.html")

@app.route('/')
def redirect_to_HomePage():
	return (redirect(url_for('HomePage')))


if __name__ == '__main__':
    app.run(debug=True)
# from flask import Flask, render_template, redirect, url_for
# app = Flask(__name__)


# @app.route('/home')
# def HomePage():
#     return render_template("index.html")

# @app.route('/')
# def redirect_to_HomePage():
# 	return (redirect(url_for('HomePage')))


def is_power_of_2(n):
	if n%2==1:
		return False
	elif n==2:
		return True
	else:
		return is_power_of_2(n/2)


print(is_power_of_2(18))
# if __name__ == '__main__':
#     app.run(debug=True)
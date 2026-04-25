from flask import Flask, render_template, request
import os

picfolder = os.path.join('static')
# Interaction
web = Flask(__name__)

# Mapping
@web.route("/")

# Inputs
def home():
    return "Welcome"


@web.route("/register")
def homepage():
    return render_template('register.html')

@web.route("/confirmation", methods=["POST", "GET"])
def confirmation():
    if request.method == "POST":
        n = request.form.get('name')
        c = request.form.get('city')
        p = request.form.get('phone number')
        return render_template('confirmation.html', name = n, city = c, phonenumber = p)
    
web.config['UPLOAD_FOLDER'] = picfolder
@web.route("/first")
def first():
    pic = os.path.join(web.config['UPLOAD_FOLDER'], 'waterfall.jpg')
    return render_template('home.html', user_image=pic)


if __name__ == "__main__":
    web.run(debug=True)
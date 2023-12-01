from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/restaurant')
def restaurant():
    return render_template('restaurant.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/dolphinarium')
def dolphinarium():
    return render_template('dolphinarium.html')

@app.route('/hotel')
def hotel():
    return render_template('hotel.html')

@app.route('/form', methods=["POST"])
def form():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")
    title = "Thank You!"
    return render_template('form.html', title=title, first_name=first_name, last_name=last_name, email=email)

if __name__ == '__main__':
    app.run(debug=True)
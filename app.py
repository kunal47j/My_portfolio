from flask import Flask,request,render_template,url_for ,flash , redirect
from flask_mail import Mail, Message


app = Flask(__name__ , static_folder='static')

app.secret_key = 'kunal_super_secret_123'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_USERNAME'] = 'janbandhukunal47@gmail.com'
app.config['MAIL_PASSWORD'] = 'lgsjpdfjqetrzzha'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_DEFAULT_SENDER'] = 'janbandhukunal47@gmail.com'

mail = Mail(app)

@app.route("/")
def home():
    return render_template('home.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/resume/')
def resume():
    return render_template('resume.html')

@app.route('/project/')
def project():
    return render_template('project.html')

#@app.route('/contact')
#def contact():
    #return render_template('contact.html')

@app.route('/contact/', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message_body = request.form.get('message')

        try:
            msg = Message(
                subject="New message from portfolio site",
                sender=app.config['MAIL_USERNAME'],
                recipients=['janbandhukunal47@gmail.com']
            )
            msg.body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message_body}"
            mail.send(msg)
            flash('Your message has been sent successfully!', 'success')
            return redirect(url_for('contact'))
        except Exception as e:
            flash(f'Error sending message: {e}', 'danger')

    return render_template('contact.html')

if __name__ =="__main__":
    app.run(debug=True)
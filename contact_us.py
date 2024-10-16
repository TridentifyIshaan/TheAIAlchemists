from flask import Flask, request, render_template

app = Flask(__name__)

class ContactEntry:
    def __init__(self, name, email, message):
        self.name = name
        self.email = email
        self.message = message

class ContactUs:
    def __init__(self):
        self.entries = []

    def add_entry(self, name, email, message):
        entry = ContactEntry(name, email, message)
        self.entries.append(entry)

    def get_entries(self):
        return self.entries

contact_us = ContactUs()

@app.route('/')
def index():
    return render_template('contact_us.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    contact_us.add_entry(name, email, message)
    return "Thank you for your message!"

if __name__ == '__main__':
    app.run(debug=True)
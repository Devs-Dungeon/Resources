#Please create a web app that let's users submit a username and password
#The app checks if the username exists and the password satisfies three conditions as in exercise 81
from flask import Flask, render_template_string, request

app = Flask(__name__)

html = """
  		      <div class="form">
              <form action="{{url_for('sent')}}" method="POST">
  			        <input title="Your email address will be safe with us." placeholder="Enter username" type="text" name="username" required> <br>
  			        <input title="Your email address will be safe with us." placeholder="Enter password" type="text" name="password" required> <br>
                    {{message|safe}}
                <button class="go-button" type="submit"> Submit </button>
  		        </form>
          </div>
"""

@app.route("/")
def index():
    return render_template_string(html)

@app.route("/sent", methods=['GET', 'POST'])
def sent():
    line = None
    if request.method == 'POST':
        while True:
            usr = request.form['username']
            with open("users.txt", "r") as file:
                users = file.readlines()
                users = [i.strip("\n") for i in users]
            if usr in users:
                return render_template_string(html, message="Username exists!"+"<br>")
                continue
            else:
                print("Username is fine!")
                break
        while True:
            notes = []
            psw = request.form['password']
            if not any(i.isdigit() for i in psw):
                notes.append("You need at least one number")
            if not any(i.isupper() for i in psw):
                notes.append("You need at least one uppercase letter")
            if len(psw) < 5:
                notes.append("You need at least 5 characters")
            if len(notes) == 0:
                print("Password is fine"+"<br>")
                break
            else:
                return render_template_string(html, message="Please check password!")
        return render_template_string(html, message="Success"+"<br>")
if __name__ == "__main__":
    app.run(debug=True)

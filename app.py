from flask import Flask, render_template

app = Flask(__name__)

total_students = 200

@app.route('/')
def home():
	return render_template("index.html",ts=total_students)
    
@app.route('/new-student')
def ns():
    return render_template("students/new.html")
    
@app.route('/manage-students')
def ms():
    return render_template("students/manage.html")
    
if __name__ == "__main__":
	app.run(debug=True)
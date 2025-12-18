from flask import Flask, render_template, request, redirect

app = Flask(__name__)

total_students = 200
students = []

@app.route('/')
def home():
	return render_template("index.html",ts=total_students)
    
@app.route('/new-student')
def ns():
    return render_template("students/new.html")
    
@app.route('/manage-students')
def ms():
    return render_template("students/manage.html", students=students)
    
@app.post('/save-student')
def ss():
    if students:
        id=max([s['id'] for s in students])
    else:
        id=1
    name=request.form['name']
    age=request.form['age']
    course=request.form['course']
    new_student={'id':id, 'name':name, 'age':age, 'course':course}
    students.append(new_student)
    return redirect('/')
    
if __name__ == "__main__":
	app.run(debug=True)
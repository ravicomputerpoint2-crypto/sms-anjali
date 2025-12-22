from flask import Flask, render_template, request, redirect

app = Flask(__name__)
students = []



teachers = []

@app.route('/')
def home():
    total_students = len(students)
    total_teachers = len(teachers)
    return render_template("index.html",ts=total_students,tt=total_teachers)
    
@app.route('/new-student')
def ns():
    return render_template("students/new.html")
    
@app.route('/new-teacher')
def nt():
    return render_template("teachers/newt.html")
    
@app.route('/manage-students')
def ms():
    return render_template("students/manage.html", students=students)
    
@app.route('/manage-teachers')
def mt():
    return render_template("teachers/managet.html", teachers=teachers)
    
@app.post('/save-student')
def ss():
    if students:
        id=max([s['id'] for s in students])+1
    else:
        id=1
    name=request.form['name']
    age=request.form['age']
    course=request.form['course']
    new_student={'id':id, 'name':name, 'age':age, 'course':course}
    students.append(new_student)
    return redirect('/manage-students')
    
@app.post('/save-teacher')
def st():
    if teachers:
        id=max([t['id'] for t in teachers])+1
    else:
        id=1
    name=request.form['name']
    age=request.form['age']
    subject=request.form['subject']
    new_teacher={'id':id, 'name':name, 'age':age, 'subject':subject}
    teachers.append(new_teacher)
    return redirect('/manage-teachers')
    
@app.route('/delete-student/<int:id>')
def ds(id):
    global students
    students=[s for s in students if s['id'] != id]
    return redirect('/manage-students')
    
@app.route('/delete-teacher/<int:id>')
def dt(id):
    global teachers
    teachers=[t for t in teachers if t['id'] != id]
    return redirect('/manage-teachers')

@app.route('/print-student/<int:id>')
def ps(id):
    student = [s for s in students if s['id'] == id][0]
    return render_template('students/print.html',student=student)
    
@app.route('/print-teacher/<int:id>')
def pt(id):
    teacher = [t for t in teachers if t['id'] == id][0]
    return render_template('teachers/printt.html',teacher=teacher)
    
    
if __name__ == "__main__":
	app.run(debug=True)
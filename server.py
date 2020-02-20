"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template
import hackbright

app = Flask(__name__)


@app.route('/search')
def search_student():
    """Searches for student with a form in database. """

    return render_template('student_search.html')


@app.route('/add_student', methods=['POST'])
def add_student():

    student_first = request.form.get('first_name')
    student_last = request.form.get('last_name')
    student_github = request.form.get('github')
    hackbright.make_new_student(student_first, student_last, student_github)

    return render_template('confirmation.html')


# @app.route('/get_info', methods=['POST'])
# def gets_info():
#     pass


@app.route('/student')
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    return render_template('student_info.html',
                             first_name=first,
                             last_name=last,
                             github_user=github)




if __name__ == '__main__':
    hackbright.connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')

from flask import Flask, render_template, request
import os

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():

    name = request.form['name']

    minimum_grade = float(request.form['minimum_grade'])
    maximum_grade = float(request.form['maximum_grade'])
    desired_grade = float(request.form['desired_grade'])

    number_of_subjects = int(request.form['number_of_subjects'])

    grades = {}

    for i in range(number_of_subjects):
        subject = request.form[f'subject_{i}']
        grade = float(request.form[f'grade_{i}'])
        grades[subject] = grade

    total = sum(grades.values())
    average = total / len(grades)

    highest_grade = max(grades.values())
    lowest_grade = min(grades.values())

    strongest_subject = max(grades, key=grades.get)
    weakest_subject = min(grades, key=grades.get)

    performance_percentage = (
        (average - minimum_grade)
        / (maximum_grade - minimum_grade)
    ) * 100

    if performance_percentage >= 90:
        performance = 'Excellent'
    elif performance_percentage >= 80:
        performance = 'Very Good'
    elif performance_percentage >= 70:
        performance = 'Good'
    elif performance_percentage >= 60:
        performance = 'Satisfactory'
    else:
        performance = 'Needs Improvement'

    # Calculate the grade needed on the next assessment
    # to reach the desired average.
    next_grade = None

    required_grade = (
        desired_grade * (number_of_subjects + 1)
        - total
    )

    # If the required grade is within the grading scale,
    # it is possible to reach the target with one more grade.
    if required_grade <= maximum_grade:
        if required_grade <= minimum_grade:
            next_grade = minimum_grade
        else:
            next_grade = round(required_grade, 2)

    return render_template(
        'results.html',
        name=name,
        average=average,
        highest_grade=highest_grade,
        lowest_grade=lowest_grade,
        strongest_subject=strongest_subject,
        weakest_subject=weakest_subject,
        performance=performance,
        desired_grade=desired_grade,
        next_grade=next_grade
    )


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port)
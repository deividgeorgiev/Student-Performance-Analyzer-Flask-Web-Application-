from flask import Flask, render_template, request

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

    if average >= desired_grade:
        target_status = 'Target achieved!'
        next_grade = 0
        target_message = 'You have already reached your target.'

    else:
        next_grade = (desired_grade * (len(grades) + 1)) - sum(grades.values())

    if next_grade <= maximum_grade:
        target_status = 'Target not achieved yet.'
        target_message = f'You need a grade of {next_grade:.2f} on your next result to reach your target.'
    else:
        target_status = 'Target not achievable with one more grade.'
        target_message = 'Even the maximum possible grade would not be enough to reach your target with one more result.'
        
    if average >= desired_grade:
        points_difference = average - desired_grade
    else:
        points_difference = desired_grade - average

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
        target_status=target_status,
        points_difference=points_difference,
        next_grade=next_grade,
        target_message=target_message
    )


if __name__ == '__main__':
    app.run(debug=True)
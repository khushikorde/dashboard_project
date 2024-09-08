import csv

def calculate_average_grades(csv_file):
    """Calculates the average grade for each student in a CSV file.

    Args:
        csv_file (str): The path to the CSV file.

    Returns:
        dict: A dictionary containing student names as keys and their average grades as values.
    """

    student_grades = {}
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)  # Skip the header row
        for row in reader:
            name, *grades = row
            grades = [float(grade) for grade in grades]
            average_grade = sum(grades) / len(grades)
            student_grades[name] = average_grade

    return student_grades
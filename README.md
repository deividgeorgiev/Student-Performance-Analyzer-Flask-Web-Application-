# STUDENT PERFORMANCE ANALYZER

A Flask-based web application designed to analyze student academic performance.

This repository contains the web application I developed for my **Student Performance Analyzer** project, which is available as a separate repository on my GitHub profile.

Using **Flask**, I managed to develop a web page that provides a graphical interface for the Student Performance Analyzer, allowing users to enter their information and use the analyzer directly through the website.

## Live Website

To access the deployed web application, copy and paste the link below into your browser:

https://student-performance-analyzer-flask-web-cl5k.onrender.com/

## About the Project

The Student Performance Analyzer (SPA) allows users to enter a student’s grades and receive an automatic analysis of their academic performance. The application calculates the average, highest and lowest grades, strongest and weakest subjects, overall performance, and evaluates progress toward a desired grade.

The application also determines the grade required on the next result to reach the student’s target, or indicates when the target cannot be achieved with one additional grade.

## Features

* Student name input
* Custom number of subjects
* Subject and grade input
* Average grade calculation
* Highest and lowest grade detection
* Strongest and weakest subject detection
* Overall performance evaluation
* Desired grade tracking
* Next-grade calculation
* Target-achievement evaluation
* Simple and colorful web interface

## Technologies Used

* Python
* Flask
* HTML
* CSS
* JavaScript
* Jinja2

## Project Structure

student-performance-analyzer-flask/
│
├── app.py
│
├── templates/
│   ├── index.html
│   └── results.html
│
└── static/
    └── style.css

## How It Works?

1. The user enters their name and grading scale.
2. The user enters their desired grade.
3. The user selects the number of subjects.
4. The application creates the required subject and grade fields.
5. Flask processes the submitted information.
6. The application calculates and displays the performance results.

## How to Run?

To run the program from the previous repository, save the Python file from this repository to a folder on your desktop.

Open the terminal on your computer and navigate to the folder containing the file.

## Then execute the following command:

python spa.py

## On Mac computers, you might need to use:

python3 spa.py

## Purpose

This project was created as an implementation of the Student Performance Analyzer project and as a practical introduction to web development with Python and Flask.

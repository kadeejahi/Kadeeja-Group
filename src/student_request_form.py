"""
CampusConnect - Student Request Form 
(Task: T-01)

This file runs the flash application
for the student request form and submissions. 

Students can: 
- open the form to submit a request for assistance
- assign a category to their request
- provide a description of their request
- preview their request submission

Current limitations: 
- requests are not stored in a database 
- authentication is not implemented
- no input validation is performed
"""

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def student_request_form():
    """
    Display the request form and preview submitted info.
    
    GET: display the blank request form
    POST: recieve entered info and display a preview
    
    Demo purposes only - This request is not permanently stored.
    """

    # no submission preview necessary when page first loads
    preview = None

    # check if form was submitted and retrieve the entered info
    if request.method == "POST":
        preview = {
            "category": request.form.get("category", ""),
            "description": request.form.get("description", ""),
        }

    # preview var passed to template to display submitted info if form was submitted
    return render_template(
        "student_request_form.html",
        preview=preview
    )

# Run the Flask application in debug mode when this file is executed directly
if __name__ == "__main__":
    app.run(debug=True)

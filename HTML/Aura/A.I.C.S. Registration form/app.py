from flask import Flask, redirect, render_template, request, flash
from flask_session import Session
import re  # For data validation

app = Flask(__name__)

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = "your_secret_key"  # Required for flashing messages
Session(app)

# Helper function to validate form inputs
def validate_form_data(form_data):
    errors = []
    # Name validation: allows only alphabets, spaces, and max 50 characters
    name_pattern = re.compile(r"^[A-Za-z\s]{1,50}$")
    if not name_pattern.match(form_data.get("first_name", "")):
        errors.append("Invalid first name.")
    if not name_pattern.match(form_data.get("last_name", "")):
        errors.append("Invalid last name.")
    if not name_pattern.match(form_data.get("parent_first_name", "")):
        errors.append("Invalid parent/guardian first name.")
    if not name_pattern.match(form_data.get("parent_last_name", "")):
        errors.append("Invalid parent/guardian last name.")

    # Contact number validation: exactly 10 digits
    if not re.match(r"^\d{10}$", form_data.get("contact_number", "")):
        errors.append("Invalid primary contact number.")
    if not re.match(r"^\d{10}$", form_data.get("emergency_contact_number", "")):
        errors.append("Invalid emergency contact number.")

    # Email validation: basic pattern matching
    if not re.match(r"[^@]+@[^@]+\.[^@]+", form_data.get("email", "")):
        errors.append("Invalid email address.")

    # Check date fields are not empty
    if not form_data.get("dob"):
        errors.append("Date of birth is required.")
    if not form_data.get("start_date"):
        errors.append("Preferred start date is required.")
    if not form_data.get("date"):
        errors.append("Date is required.")

    # Check other required fields
    if not form_data.get("relationship"):
        errors.append("Relationship to student is required.")
    if not form_data.get("grade"):
        errors.append("Grade applying for is required.")
    if not form_data.get("signature"):
        errors.append("Parent/guardian signature is required.")

    return errors

# Route for the home page
@app.route("/")
def index():
    return render_template("index.html")  # Ensure you have an index.html file

# Route to serve the registration form
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Validate the submitted form data
        errors = validate_form_data(request.form)
        if errors:
            for error in errors:
                flash(error, "error")  # Show error messages to the user
            return render_template("form.html")  # Reload form with error messages
        else:
            # Process the validated form data (e.g., save to database, session, etc.)
            student_info = request.form.to_dict()
            flash("Form submitted successfully!", "success")
            print(student_info)  # Debugging/logging purpose
            return redirect("/")  # Redirect to home or a success page
    
    return render_template("form.html")  # Render the form

if __name__ == "__main__":
    app.run(debug=True)

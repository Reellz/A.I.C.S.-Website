from flask import Flask, redirect, render_template, request, flash
from flask_session import Session
import psycopg2
import re  # For data validation

app = Flask(__name__)

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = "your_secret_key"  # Required for flashing messages
Session(app)

# PostgreSQL Database Configuration
DATABASE_CONFIG = {
    'dbname': 'Register',
    'user': 'postgres',
    'password': 'HillCity.dev',
    'host': 'localhost',
    'port': 5432
}

# Helper function to connect to the database
def get_db_connection():
    conn = psycopg2.connect(**DATABASE_CONFIG)
    return conn

# Helper function to validate form inputs
def validate_form_data(form_data):
    errors = []
    # Validation logic...
    return errors

# Routes for the pages
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/staff")
def staff():
    return render_template("staff.html")


@app.route("/about")
def about():
    return render_template("About us.html")


@app.route("/events")
def events():
    return render_template("events.html")



@app.route("/contact")
def contact():
    return render_template("contact_us.html")

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
            # Process the validated form data (e.g., save to database)
            student_info = request.form.to_dict()

            # Insert into the database
            conn = get_db_connection()
            cursor = conn.cursor()

            query = """
            INSERT INTO registrations (
                id,
                first_name,
                middle_name,
                last_name,
                dob,
                gender,
                grade,
                start_date,
                parent_first_name,
                parent_last_name,
                relationship,
                contact_number,
                email,
                address,
                emergency_contact_name,
                emergency_relationship,
                emergency_contact_number,
                emergency_alternate_number,
                medical_condition,
                medical_details,
                medications,
                medications_details,
                previous_school_name,
                previous_school_address,
                previous_school_contact,
                transportation,
                additional_info,
                signature,
                registration_date
              )
            VALUES (
                id:integer,
                'first_name:character varying',
                'middle_name:character varying',
                'last_name:character varying',
                'dob:date',
                'gender:character varying',
                'grade:character varying',
                'start_date:date',
                'parent_first_name:character varying',
                'parent_last_name:character varying',
                'relationship:character varying',
                'contact_number:character varying',
                'email:character varying',
                'address:text',
                'emergency_contact_name:character varying',
                'emergency_relationship:character varying',
                'emergency_contact_number:character varying',
                'emergency_alternate_number:character varying',
                medical_condition:boolean,
                'medical_details:text',
                medications:boolean,
                'medications_details:text',
                'previous_school_name:character varying',
                'previous_school_address:text',
                'previous_school_contact:character varying',
                transportation:boolean,
                'additional_info:text',
                'signature:text',
                'registration_date:date'
              );
            """
            
            try:
                cursor.execute(query, student_info)
                conn.commit()
                flash("Form submitted successfully!", "success")
            except Exception as e:
                conn.rollback()
                flash(f"An error occurred: {e}", "error")
            finally:
                cursor.close()
                conn.close()

            return redirect("/")  # Redirect to home or a success page

    return render_template("form.html")  # Render the form

if __name__ == "__main__":
    app.run(debug=True)

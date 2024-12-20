<?php
// Database connection
$servername = "localhost";
$username = "Reelly";
$password = "HillCity.dev";
$dbname = "hillcityicaINSERT INTO registrations (
    id,
    student_name,
    email,
    dob,
    gender,
    grade,
    courses,
    comments,
    created_at
  )
VALUES (
    id:int,
    'student_name:varchar',
    'email:varchar',
    'dob:date',
    'gender:enum',
    'grade:varchar',
    'courses:text',
    'comments:text',
    'created_at:timestamp'
  );";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Capture form data
$student_name = $_POST['student-name'];
$student_email = $_POST['student-email'];
$dob = $_POST['dob'];
$gender = $_POST['gender'];
$grade_level = $_POST['grade'];
$courses = implode(", ", $_POST['coures']);
$comments = $_POST['comments'];

// Insert data into database
$sql = "INSERT INTO students (student_name, student_email, dob, gender, grade_level, courses, comments)
        VALUES ('$student_name', '$student_email', '$dob', '$gender', '$grade_level', '$courses', '$comments')";

if ($conn->query($sql) === TRUE) {
    echo "Registration successful!";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>

fetch('nav.html') // Fetch the nav.html file
.then(response => response.text())
.then(data => document.getElementById('navbar').innerHTML = data)
.catch(error => console.error('Error loading the navbar:', error));
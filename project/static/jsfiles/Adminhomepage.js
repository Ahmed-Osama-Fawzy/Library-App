// homepage.js

// Function to handle logout button click
function handleLogout() {
    // You can add logout functionality here
    alert("Logging out..."); // Example: Displaying an alert for demonstration
}

// Function to add event listeners to the links and buttons
function addEventListeners() {
    // Get the logout button
    var logoutButton = document.querySelector('.logout-button');
    // Add click event listener to logout button
    logoutButton.addEventListener('click', handleLogout);
}

// Call the addEventListeners function when the DOM is loaded
document.addEventListener('DOMContentLoaded', function () {
    addEventListeners();
});

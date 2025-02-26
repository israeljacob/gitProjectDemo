/**
 * Fetches usernames and passwords from the server
 * @returns {Promise<Object>} Object containing usernames as keys and passwords as values
 */
async function fetchUsernamesAndPasswords() {
    let usernamesAndPasswords = await fetch('http://localhost:8000/usernames_and_passwords');
    return usernamesAndPasswords.json();
}

/**
 * Handles login form submission, verifies credentials, and redirects if valid
 * @param {Event} event - Form submission event
 */
async function submitDetails(event){
    event.preventDefault();
    let username = document.getElementById('username').value;
    let password = document.getElementById('password').value;
    let usernamesAndPasswords = await fetchUsernamesAndPasswords();
    if (usernamesAndPasswords[username] && usernamesAndPasswords[username] === password) {
        window.location.href = 'MachinesManager.html';
    }
    else {
        document.getElementById('errorMessage').style.display = 'block';
    }
}

/**
 * Initializes the application by hiding the error message on page load
 */
function main() {
    document.getElementById('errorMessage').style.display = 'none';
}

document.addEventListener("DOMContentLoaded", main);
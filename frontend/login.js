async function fetchUsernamesAndPasswords() {
    let usernamesAndPasswords = await fetch('http://localhost:8000/usernames_and_passwords');
    return usernamesAndPasswords.json();
}

async function submitDetails(event){
    event.preventDefault();
    let username = document.getElementById('username').value;
    let password = document.getElementById('password').value;
    let usernamesAndPasswords = await fetchUsernamesAndPasswords();
    if (usernamesAndPasswords[username] && usernamesAndPasswords[username] === password) {
        window.location.href = 'MachinesManager.html'
    }
    else {
        document.getElementById('errorMessage').style.display = 'block';
    }
}


function main() {
    document.getElementById('errorMessage').style.display = 'none';
}

document.addEventListener("DOMContentLoaded", main);

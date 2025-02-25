let key;

async function fetchMachinesList(){
    let list = await fetch('http://localhost:5000/api/list_machines_target_get');
    return list.json().then((data) => data)
}

async function fetchKey(){
    let key = await fetch('http://localhost:8000/key');
    return key.json().then((data) => data);
}

async function fetchUsernamesAndPasswords() {
    let usernamesAndPasswords = await fetch('http://localhost:8000/usernames_and_passwords');
    return usernamesAndPasswords.json().then((data) => data);
}

function decrypt(text, key) {
    let decrypted = [];
    for (let i = 0; i < text.length; i++) {
        let decryptedNum = text.charCodeAt(i) ^ key.charCodeAt(0)
        let decryptedChar = String.fromCharCode(decryptedNum);
        decrypted.push(decryptedChar);
    }
    return decrypted.join('');
}

async function getMachineData(li, button, ownerName) {
    let data = await fetch('http://localhost:5000/api/computer_data/' + ownerName);
    data = await data.json().then((data) => data)
    let p = document.createElement('p');
    p.textContent = JSON.stringify(data, null, 2);
    li.appendChild(p);
}


function addListToElement(machinesList) {
    const listElement = document.getElementById('machine_list_ul');
    machinesList.forEach(machine => {
        const li = document.createElement('li');
        const button = document.createElement('button');
        li.textContent = machine;
        button.textContent = 'get data';
        button.addEventListener('click', () => {getMachineData(li, button, machine)})
        listElement.appendChild(li);
        li.appendChild(button);
    })
    console.log('Adding list to element');
}

function hideAllExceptOne(div){
    document.getElementById('login').style.display = 'none';
    document.getElementById('machinesList').style.display = 'none';
    document.getElementById('machineData').style.display = 'none';
    document.getElementById('errorMessage').style.display = 'none';
    document.getElementById(div).style.display = 'block';
}

function showErrorMassage(){
    const error = document.getElementById('errorMessage')
    const message = document.createElement('p')
    message.textContent = "One of the details are wrong. Please try again.";
    error.appendChild(message)
}

async function goToListPage(){
    let machinesList = await fetchMachinesList();
    machinesList = machinesList.map(machine => decrypt(machine, key));
    addListToElement(machinesList);
    hideAllExceptOne('machinesList')
}

async function submitDetails(event){
    event.preventDefault();
    let username = document.getElementById('username').value;
    let password = document.getElementById('password').value;
    let usernamesAndPasswords = await fetchUsernamesAndPasswords()
    for(let key of Object.keys(usernamesAndPasswords)){
        if (key === username && usernamesAndPasswords[key] !== password){
            document.getElementById('errorMessage').style.display = 'block';
            return;
        }
        else if (key === username){
            await goToListPage()
            return;
        }
    }
    document.getElementById('errorMessage').style.display = 'block';
}

async function main(){
    hideAllExceptOne('login');
    const keyObject = await fetchKey();
    key = keyObject.key;
}

document.addEventListener("DOMContentLoaded", main);
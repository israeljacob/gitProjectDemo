let key;

async function fetchMachinesList(){
    let list = await fetch('http://localhost:5000/api/list_machines_target_get');
    return list.json();
}

async function fetchKey(){
    let key = await fetch('http://localhost:8000/key');
    return key.json();
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

// function extractData(data){
//     const ownerName = Object.keys(data);
//     const fileName = Object.keys(data[ownerName]);
//     const timeStamps = Object.keys(data[ownerName][fileName]);
//     let finalData = [];
//     for (let i = 0; i < timeStamps.length; i++) {
//         finalData.push(data[ownerName][fileName][timeStamps[i]]);
//     }
//     return [fileName, timeStamps, finalData];
// }

async function getMachineData(li, button, ownerName) {

    let data = await fetch('http://localhost:5000/api/computer_data/' + ownerName);
    data = await data.json();

    sessionStorage.setItem('machineData', JSON.stringify(data));
    sessionStorage.setItem('machineOwner', ownerName);
    window.location.href = 'MachineData.html';
}

function addListToElement(machinesList) {
    const listElement = document.getElementById('machine_list_ul');
    while (listElement && listElement.firstChild){
        listElement.removeChild(listElement.firstChild);
    }
    if (listElement){
        machinesList.forEach(machine => {
            const li = document.createElement('li');
            const button = document.createElement('button');
            li.textContent = machine;
            button.textContent = 'get data';
            button.addEventListener('click', () => {getMachineData(li, button, machine)});
            listElement.appendChild(li);
            li.appendChild(button);
        })
    }
}

async function main(){
    const keyObject = await fetchKey();
    key = keyObject.key;
    let machinesList = await fetchMachinesList();
    machinesList = machinesList.map(machine => decrypt(machine, key));
    addListToElement(machinesList);
}

document.addEventListener("DOMContentLoaded", main);

/**
 * Fetches the list of encrypted machine names from the server
 * @returns {Promise<Array>} List of encrypted machine names
 */
async function fetchMachinesList(){
    const list = await fetch('http://localhost:5000/api/list_machines_target_get');
    return list.json();
}

/**
 * Fetches the encryption key from the server
 * @returns {Promise<Object>} Object containing the encryption key
 */
async function fetchKey(){
    const key = await fetch('http://localhost:8000/key');
    return key.json();
}

/**
 * Decrypts a given encrypted string using a provided key
 * @param {string} text - Encrypted text
 * @param {string} key - Encryption key
 * @returns {string} Decrypted text
 */
function decrypt(text, key) {
    let decrypted = [];
    for (let i = 0; i < text.length; i++) {
        const decryptedNum = text.charCodeAt(i) ^ key.charCodeAt(0);
        const decryptedChar = String.fromCharCode(decryptedNum);
        decrypted.push(decryptedChar);
    }
    return decrypted.join('');
}

/**
 * Fetches and stores machine data for a selected owner
 * @param {HTMLElement} li - List item element
 * @param {HTMLElement} button - Button element
 * @param {string} ownerName - Name of the machine owner
 */
async function getMachineData(li, button, ownerName) {
    let data = await fetch('http://localhost:5000/api/computer_data/' + ownerName);
    data = await data.json();

    sessionStorage.setItem('machineData', JSON.stringify(data));
    sessionStorage.setItem('machineOwner', ownerName);
    window.location.href = 'MachineData.html';
}

/**
 * Populates a list element with machine names and buttons
 * @param {Array<string>} machinesList - List of decrypted machine names
 */
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

/**
 * Main function to fetch the key, decrypt machine names, and populate the list
 */
async function main(){
    const keyObject = await fetchKey();
    key = keyObject.key;
    let machinesList = await fetchMachinesList();
    machinesList = machinesList.map(machine => decrypt(machine, key));
    addListToElement(machinesList);
}

document.addEventListener("DOMContentLoaded", main);

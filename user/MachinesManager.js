///**
// * Fetches the list of encrypted machine names from the server
// * @returns {Promise<Array>} List of encrypted machine names
// */
//async function fetchMachinesList(){
//    const list = await fetch('http://localhost:5000/api/list_machines_target_get');
//    return list.json();
//}
//
///**
// * Fetches the encryption key from the server
// * @returns {Promise<Object>} Object containing the encryption key
// */
//async function fetchKey(){
//    const key = await fetch('http://localhost:8000/key');
//    return key.json();
//}
//
///**
// * Decrypts a given encrypted string using a provided key
// * @param {string} text - Encrypted text
// * @param {string} key - Encryption key
// * @returns {string} Decrypted text
// */
//function decrypt(text, key) {
//    let decrypted = [];
//    for (let i = 0; i < text.length; i++) {
//        const decryptedNum = text.charCodeAt(i) ^ key.charCodeAt(0);
//        const decryptedChar = String.fromCharCode(decryptedNum);
//        decrypted.push(decryptedChar);
//    }
//    return decrypted.join('');
//}
//
///**
// * Fetches and stores machine data for a selected owner
// * @param {HTMLElement} li - List item element
// * @param {HTMLElement} button - Button element
// * @param {string} ownerName - Name of the machine owner
// */
//async function getMachineData(li, button, ownerName) {
//    let data = await fetch('http://localhost:5000/api/computer_data/' + ownerName);
//    data = await data.json();
//
//    sessionStorage.setItem('machineData', JSON.stringify(data));
//    sessionStorage.setItem('machineOwner', ownerName);
//    window.location.href = 'MachineData.html';
//}
//
///**
// * Populates a list element with machine names and buttons
// * @param {Array<string>} machinesList - List of decrypted machine names
// */
//function addListToElement(machinesList, ownersList) {
//    const listElement = document.getElementById('machine_list_ul');
//    while (listElement && listElement.firstChild){
//        listElement.removeChild(listElement.firstChild);
//    }
//    if (listElement){
//        for (let j = 0; j < machinesList.length; j++){
//            const li = document.createElement('li');
//            const button = document.createElement('button');
//            li.textContent = machinesList[j] + '    ' + ownersList[j];
//            button.textContent = 'get data';
//            button.addEventListener('click', () => {getMachineData(li, button, machinesList[j])});
//            listElement.appendChild(li);
//            li.appendChild(button);
//        }
//    }
//}
//
///**
// * Main function to fetch the key, decrypt machine names, and populate the list
// */
//async function main(){
//    const keyObject = await fetchKey();
//    key = keyObject.key;
//    let machinesList = await fetchMachinesList();
//    let ownersList = machinesList[1]
//    machinesList = machinesList[0]
//    machinesList = machinesList.map(machine => decrypt(machine, key));
//    ownersList = ownersList.map(machine => decrypt(machine, key));
//    addListToElement(machinesList, ownersList);
//}
//
//document.addEventListener("DOMContentLoaded", main);
/**
 * Fetches the list of encrypted machine names from the server
 * @returns {Promise<Array>} List of encrypted machine names
 */
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
 * @param {HTMLElement} compDiv - Computer div element
 * @param {string} ownerName - Name of the machine owner
 */
async function getMachineData(compDiv, ownerName) {
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
function addListToElement(machinesList, ownersList) {
    const container = document.getElementById("computersList");
    container.innerHTML = ""; // Reset the list before adding new items
    for (let i = 0; i < machinesList.length; i++) {
        const computerDiv = document.createElement("div");
        computerDiv.className = "computer";
        computerDiv.innerHTML = `
            <img src="https://img.icons8.com/ios-filled/100/58a6ff/computer.png" alt="computer icon">
            <div class="computer-info">מחשב ${i + 1}</div>
            <div class="computer-info">בעלים: ${machinesList[i]}</div>
            <div class="computer-info">MAC: ${ownersList[i]}</div>
        `;
        computerDiv.addEventListener('click', () => { getMachineData(computerDiv, machinesList[i]); });
        container.appendChild(computerDiv);
    }
}

/**
 * Main function to fetch the key, decrypt machine names, and populate the list
 */
async function main() {
    const keyObject = await fetchKey();
    const key = keyObject.key;
    let machinesList = await fetchMachinesList();
    let ownersList = machinesList[1];
    machinesList = machinesList[0];
    machinesList = machinesList.map(machine => decrypt(machine, key));
    ownersList = ownersList.map(machine => decrypt(machine, key));
    addListToElement(machinesList, ownersList);
}

document.addEventListener("DOMContentLoaded", main);

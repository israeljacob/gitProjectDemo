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
            <img src="computer.png" alt="computer icon">
            
            <div class="computer-info">machine ${i + 1}</div>
            <div class="computer-info">User: ${machinesList[i]}</div>
            <div class="computer-info">MAC: ${ownersList[i]}</div>
        `;
        computerDiv.addEventListener('click', () => { getMachineData(computerDiv, machinesList[i]); });
        container.appendChild(computerDiv);
    }
}

function applyFilter() {
    const nameFilter = document.getElementById("nameFilter").value.toLowerCase();
    const macFilter = document.getElementById("macFilter").value.toLowerCase();
    const computers = document.querySelectorAll("#computersList .computer");

    computers.forEach(computer => {
        const ownerText = computer.querySelector(".computer-info:nth-child(3)").textContent.toLowerCase();
        const macText = computer.querySelector(".computer-info:nth-child(4)").textContent.toLowerCase();

        if (ownerText.includes(nameFilter) && macText.includes(macFilter)) {
            computer.style.display = "block";
        } else {
            computer.style.display = "none";
        }
    });
}



/**
 * Main function to fetch the key, decrypt machine names, and populate the list
 */
async function main(){
    document.getElementById("nameFilter").addEventListener("input", applyFilter);
    document.getElementById("macFilter").addEventListener("input", applyFilter);
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
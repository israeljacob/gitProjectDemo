/**
 * Extracts relevant data from the given machine data object.
 * @param {Object} data - The machine data object.
 * @returns {Array} An array containing the file name, timestamps, and final data values.
 */
function extractData(data){
    const ownerName = Object.keys(data);
    const fileNames = Object.keys(data[ownerName]);
    result = []
    for(const fileName of fileNames){
        const timeStamps = Object.keys(data[ownerName][fileName]);
        let finalData = [];
        for (let i = 0; i < timeStamps.length; i++) {
            finalData.push(data[ownerName][fileName][timeStamps[i]]);
        }
        result.push([fileName, timeStamps, finalData]);
    }

    return result;
}

/**
 * Retrieves stored machine data and displays it in a table format.
 */
function setData(){
    const data = JSON.parse(sessionStorage.getItem('machineData'));
    const ownerName = sessionStorage.getItem('machineOwner');
    const div = document.getElementById('machineData');
    while (div.children && div.children.length > 0) {
        div.removeChild(div.lastChild);
    }
    const extractedData = extractData(data);
    const p = div.appendChild(document.createElement('p'));
    p.textContent = ownerName;
    for (let organ of extractedData) {
        const fileName = organ[0];
        const timeStamps = organ[1];
        const finalDatas = organ[2];
        const table = div.appendChild(document.createElement('table'));
        const caption = table   .appendChild(document.createElement('caption'));
        caption.textContent = fileName;
        const TrTitle = table.appendChild(document.createElement('tr'));
        const stampTitle = TrTitle.appendChild(document.createElement('th'));
        const dataTitle = TrTitle.appendChild(document.createElement('th'));
        stampTitle.textContent = 'Time stamp';
        dataTitle.textContent = 'Data';
        for (let i = 0; i < timeStamps.length; i++) {
            const tr = table.appendChild(document.createElement('tr'));
            const thTime = tr.appendChild(document.createElement('th'));
            const thData = tr.appendChild(document.createElement('th'));
            thTime.textContent = timeStamps[i];
            thData.textContent = finalDatas[i];
        }
    }
}

/**
 * Redirects the user to the Machines Manager page.
 */
function goToListPage(){
    window.location.href = 'MachinesManager.html';
}

/**
 * Initializes the page by setting the machine data.
 */
function main() {
    setData();
}

document.addEventListener("DOMContentLoaded", main);

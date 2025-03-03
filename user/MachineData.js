/**
 * Extracts relevant data from the given machine data object.
 * @param {Object} data - The machine data object.
 * @returns {Array} An array containing the file name, timestamps, and final data values.
 */
function extractData(data){
    let result = []
    data = data.split('\n\n!@#$%^&*()\n\n');
    let splitData;
    let timeStamp;
    for (const key of data) {
        splitData = key.split('\n');
        timeStamp = splitData[0].replace(/-/g, '');
        let app = splitData[1];
        let finalData = splitData.slice(2).join('\n');
        result.push([timeStamp, app, finalData]);
    }
    return result;
}

function decryptData(text, key) {
    let decrypted = [];
    for (let i = 0; i < text.length; i++) {
        const decryptedNum = text.charCodeAt(i) ^ key.charCodeAt(i % key.length);
        const decryptedChar = String.fromCharCode(decryptedNum);
        decrypted.push(decryptedChar);
    }
    return decrypted.join('');
}

async function fetchKey(){
    const key = await fetch('http://localhost:8000/key');
    return key.json();
}

async function getData(machineName) {
    const keyObject = await fetchKey();
    const key = keyObject.key;
    let myData = await fetch('http://localhost:5000/api/computer_data/' + machineName);
    myData = await myData.json();
    myData = myData.data;
    return decryptData(myData, key);
}

/**
 * Retrieves stored machine data and updates the table without removing applied filters.
 */
async function setData() {
    const ownerName = sessionStorage.getItem('machineOwner');
    const machineName = sessionStorage.getItem('machineName');
    let data = await getData(machineName);

    const div = document.getElementById('machineData');
    div.innerHTML = '';

    const p = div.appendChild(document.createElement('p'));
    p.textContent = ownerName;

    const table = div.appendChild(document.createElement('table'));
    table.id = 'dataTable';

    const headerRow = table.appendChild(document.createElement('tr'));
    const thTimestamp = headerRow.appendChild(document.createElement('th'));
    const thApp = headerRow.appendChild(document.createElement('th'));
    const thData = headerRow.appendChild(document.createElement('th'));
    thTimestamp.textContent = 'Time stamp';
    thApp.textContent = 'App';
    thData.textContent = 'Data';

    const extractedData = extractData(data);

    for (let organ of extractedData) {
        const timeStamps = organ[0];
        const app = organ[1];
        const finalDatas = organ[2];

        const tr = table.appendChild(document.createElement('tr'));
        const tdTime = tr.appendChild(document.createElement('td'));
        const tdApp = tr.appendChild(document.createElement('td'));
        const tdData = tr.appendChild(document.createElement('td'));
        tdTime.textContent = timeStamps;
        tdApp.textContent = app;
        tdData.textContent = finalDatas;
    }

    applyFilterData(); // החלת הסינון מחדש לאחר עדכון הנתונים
}

function applyFilterData() {
    const startDate = document.getElementById('startDate').value;
    const endDate = document.getElementById('endDate').value;
    const appFilter = document.getElementById('appFilter').value.toLowerCase();
    const dataFilter = document.getElementById('dataFilter').value.toLowerCase();

    const trs = document.querySelectorAll('#dataTable tr');

    for (let i = 1; i < trs.length; i++) { // דילוג על שורת הכותרת
        const tds = trs[i].children;
        const timestamp = tds[0].textContent.trim();
        const app = tds[1].textContent.toLowerCase();
        const data = tds[2].textContent.toLowerCase();

        let showRow = true;

        if (startDate && timestamp < startDate.replace(/-/g, '')) {
            showRow = false;
        }

        if (endDate && timestamp > endDate.replace(/-/g, '')) {
            showRow = false;
        }

        if (appFilter && !app.includes(appFilter)) {
            showRow = false;
        }

        if (dataFilter && !data.includes(dataFilter)) {
            showRow = false;
        }

        trs[i].style.display = showRow ? '' : 'none';
    }
}

function goToListPage(){
    window.location.href = 'MachinesManager.html';
}

document.addEventListener('DOMContentLoaded', async () => {
    await setData();

    document.getElementById('startDate').addEventListener('input', applyFilterData);
    document.getElementById('endDate').addEventListener('input', applyFilterData);
    document.getElementById('appFilter').addEventListener('input', applyFilterData);
    document.getElementById('dataFilter').addEventListener('input', applyFilterData);

    await setData()
});

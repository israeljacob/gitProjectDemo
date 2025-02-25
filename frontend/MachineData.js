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

function setData(){
    const data = JSON.parse(sessionStorage.getItem('machineData'));
    const ownerName = sessionStorage.getItem('machineOwner');

    const table = document.getElementById('machine_data_table');
    while (table.children && table.children.length > 1) {
        table.removeChild(table.lastChild);
    }
    let extractedData = extractData(data);
    let fileName = extractedData[0]
    let timeStamps = extractedData[1];
    let finalDatas = extractedData[2];
    for (let i = 0; i < timeStamps.length; i++) {
        const tr = table.appendChild(document.createElement('tr'));
        let thTime = tr.appendChild(document.createElement('th'));
        let thData = tr.appendChild(document.createElement('th'));
        thTime.textContent = timeStamps[i];
        thData.textContent = finalDatas[i];
    }
}

function goToListPage(){
    window.location.href = 'MachinesManager.html';
}

function main() {
    setData()
}




document.addEventListener("DOMContentLoaded", main);

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
        result.push([timeStamps, finalData]);
    }

    return result;
}

/**
 * Retrieves stored machine data and displays it in a table format.
 */
function setData() {
    const data = JSON.parse(sessionStorage.getItem('machineData'));
    const ownerName = sessionStorage.getItem('machineOwner');
    console.log("Raw data from sessionStorage:", data);

    const div = document.getElementById('machineData');

    while (div.children && div.children.length > 0) {
        div.removeChild(div.lastChild);
    }

    const p = div.appendChild(document.createElement('p'));
    p.textContent = ownerName;

    const table = div.appendChild(document.createElement('table'));

    const headerRow = table.appendChild(document.createElement('tr'));
    const thTimestamp = headerRow.appendChild(document.createElement('th'));
    const thData = headerRow.appendChild(document.createElement('th'));
    thTimestamp.textContent = 'Time stamp';
    thData.textContent = 'Data';

    const extractedData = extractData(data);
    console.log("Extracted Data:", extractedData);

    for (let organ of extractedData) {
        const timeStamps = organ[0];
        const finalDatas = organ[1];

        for (let i = 0; i < timeStamps.length; i++) {
            const tr = table.appendChild(document.createElement('tr'));
            const tdTime = tr.appendChild(document.createElement('td'));
            const tdData = tr.appendChild(document.createElement('td'));
            tdTime.textContent = timeStamps[i];
            tdData.textContent = finalDatas[i];
        }
    }
}

function convertDateFormat(dateString) {
    if (dateString.includes("/")) {
        const parts = dateString.split("/");
        return `${parts[2]}-${parts[1]}-${parts[0]}`;
    }
    return dateString;
}


function applyFilterData() {
    const startDate = document.getElementById("startDate").value;
    const endDate = document.getElementById("endDate").value;
    const dataFilter = document.getElementById("dataFilter").value.toLowerCase();

    const trs = document.getElementsByTagName('tr');

    for (let i = 1; i < trs.length; i++) {
        const tds = trs[i].children;
        const timestamp = tds[0].textContent.trim();
        const date = convertDateFormat(timestamp.split(' ')[1]);
        const data = tds[1].textContent.toLowerCase();


        let showRow = true;

        if (startDate && endDate) {
            console.log(date)
            console.log(startDate)
            console.log(endDate)
            if (date < startDate || date > endDate) {
                showRow = false;
            }
        }

        if (dataFilter && !data.includes(dataFilter)) {
            showRow = false;
        }

        trs[i].style.display = showRow ? "" : "none";
    }
}


/**
 * Redirects the user to the Machines Manager page.
 */
function goToListPage(){
    window.location.href = 'MachinesManager.html';
}

document.addEventListener("DOMContentLoaded", () => {
    setData();

    document.getElementById("startDate").addEventListener("input", applyFilterData);
    document.getElementById("endDate").addEventListener("input", applyFilterData);
    document.getElementById("dataFilter").addEventListener("input", applyFilterData);
});


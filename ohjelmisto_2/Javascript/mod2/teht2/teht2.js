let osallistujat = [];
let maara = prompt("Kuinka monta ihmsiä on:");

for (let i = 0; i < maara; i++){
    let nimi = prompt("Anna osallistujan nimi:");
    osallistujat.push(nimi);
}

osallistujat.sort();

let lista = document.getElementById("osallistujat");


for (let i = 0; i < osallistujat.length; i++){
    let kohta = document.createElement("li");
    kohta.textContent = osallistujat[i];
    lista.appendChild(kohta);
}
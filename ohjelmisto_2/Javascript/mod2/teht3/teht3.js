let koirat = [];


for (let i = 0; i < 6; i++){
    let nimi = prompt("Anna koirien nimet:");
    koirat.push(nimi);
}

koirat.sort().reverse();

let lista = document.getElementById("koira");


for (let i = 0; i < koirat.length; i++){
    let kohta = document.createElement("li");
    kohta.textContent = koirat[i];
    lista.appendChild(kohta);
}
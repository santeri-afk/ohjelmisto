let numerot = [];

while (true) {
    let luku = prompt("Anna numero ja 0 lopettaa");
    let intluku = Number(luku);
    if (intluku === 0){
        break
    } else {
        numerot.push(intluku);
    }
}


numerot.sort((a,b) => b-a);

let lista = document.getElementById("numerot");


for (let i = 0; i < numerot.length; i++){
    let kohta = document.createElement("li");
    kohta.textContent = numerot[i];
    lista.appendChild(kohta);
}
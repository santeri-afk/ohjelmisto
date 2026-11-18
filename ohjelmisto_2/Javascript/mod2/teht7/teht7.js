let heitot = [];
let min = 1;
let max = prompt("kuinka monta puolta nopassa on?")
let maxint = Number(max)

function randomint() {
    let x = Math.floor(Math.random() * (maxint - min + 1)) + min;
    return x
}

while (true){
    numero = randomint();
    if (numero === maxint){
        heitot.push(numero);
        break
    }else{
        heitot.push(numero);
    }
}

let lista = document.getElementById("random");

for (let i = 0; i < heitot.length; i++){
    let kohta = document.createElement("li");
    kohta.textContent = heitot[i];
    lista.appendChild(kohta);
}

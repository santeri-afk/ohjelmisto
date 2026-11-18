let heitot = [];
let min = 1;
let max = 6;

function randomint() {
    let x = Math.floor(Math.random() * (max - min + 1)) + min;
    return x
}

while (true){
    numero = randomint();
    if (numero === 6){
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

let numerot = [];

while (true) {
    let luku = prompt("Anna numero ja sama luku kahdesti lopettaa");
    let intluku = Number(luku);
    if (numerot.includes(intluku)){
        alert("tämä numero laitettiin jo")
        break
    } else {
        numerot.push(intluku);
    }
}

numerot.sort((a,b) => a-b);

let lista = document.getElementById("numerot");


for (let i = 0; i < numerot.length; i++){
    console.log(`numero: ${numerot[i]}`);
}
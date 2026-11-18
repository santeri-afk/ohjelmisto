let numerot = [];

alert("Anna viisi lukua")
numerot[0] = prompt("1:")
numerot[1] = prompt("2:")
numerot[2] = prompt("3:")
numerot[3] = prompt("4:")
numerot[4] = prompt("5:")
let temp = new Array(numerot)

for (let i = 0; i < numerot.length; i++) {
    temp[i] = numerot[numerot.length - i - 1];
    
}

for (let i = 0; i < numerot.length; i++) {
    numerot[i] = temp[i];
}

for (let i = 0; i < numerot.length; i++) {
    console.log(`numero: ${numerot[i]}`);
}


// https://www.geeksforgeeks.org/dsa/program-to-reverse-an-array/ käytin tätä sivustoa
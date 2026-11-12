let luku1 = prompt("Anna kolme lukua 1:");
let luku2 = prompt("2:");
let luku3 = prompt("3:");

let luku1int = parseInt(luku1)
let luku2int = parseInt(luku2)
let luku3int = parseInt(luku3)

let summa = luku1int + luku2int + luku3int;
let kerto = luku1int * luku2int * luku3int;
let average = summa / 3;

document.getElementById("luvut").innerHTML =
    "Sum: " + summa + "<br>" +
    "Product: " + kerto + "<br>" +
    "Average: " + average;
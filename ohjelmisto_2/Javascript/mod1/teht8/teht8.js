'use strict';

alert("Anna kaksi vuotta ja printaant kaikki hyppyvuodet niitten väliltä");
let year = parseInt(prompt("ensimmäinen:"));
let year2 =parseInt(prompt("toinen:"));

let current = year
let hyppyvuodet = [];


for (let v = year; v <= year2; v++) {
    if (v % 4 == 0 && v % 100 != 0 || v % 400 == 0){
        hyppyvuodet.push(current);
    } else {
        continue
    }
};

let list = document.getElementById("vuodet");

let yar = year
for (let i = 1; i <= hyppyvuodet.length; i++) {
    let kohta = document.createElement("li");
    kohta.textContent = [yar];
    yar++
    list.appendChild(kohta);
};
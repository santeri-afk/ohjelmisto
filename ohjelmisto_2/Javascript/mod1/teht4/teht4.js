let nimi = prompt("mikä on nimesi?");

let sort = Math.floor(Math.random() * 4);

if(sort === 1){
    document.getElementById("hattu").textContent = nimi + " " + "you are Gryffindor";
} else if (sort ===2){
    document.getElementById("hattu").textContent = nimi + " " + "you are Slytherin";
} else if (sort ===3){
    document.getElementById("hattu").textContent = nimi + " " +"you are Hufflepuff";
} else if (sort ===4){
    document.getElementById("hattu").textContent = nimi + " " + "you are Ravenclaw";
}
    
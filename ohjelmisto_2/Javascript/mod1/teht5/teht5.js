let vuosiluku = parseInt(prompt("Anna vuosiluku: "))

if (vuosiluku % 4 == 0 && vuosiluku % 100 != 0 || vuosiluku % 400 == 0){
    document.getElementById("vuosi").textContent = "vuosiluku on karkausvuosi"
} else {
     document.getElementById("vuosi").textContent = "vuosiluku ei ole karkaus vuosi"
}
    


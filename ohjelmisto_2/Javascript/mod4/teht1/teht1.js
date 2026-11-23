'use strict';


const lomakelem = document.querySelector("#lomake");

const hakuelement = document.querySelector("#query");

lomakelem.addEventListener('sumbit', async function (evt) {
    evt.preventdefault();
    const hakuehto = await hakuelement.json();
    console.log(hakuehto);
}); 
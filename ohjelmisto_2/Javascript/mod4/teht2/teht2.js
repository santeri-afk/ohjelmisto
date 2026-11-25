'use strict';


const form = document.getElementById("lomake");

lomake.addEventListener("submit", async function(event) {

    event.preventDefault();

    const search = document.getElementById("query").value;
    const response = await fetch( `https://api.tvmaze.com/search/shows?q=${search}`);
    const data = await response.json();
    console.log(data);

});

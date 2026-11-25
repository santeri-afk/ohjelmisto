"use strict";
const lomake = document.getElementById("lomake");
const query = document.getElementById("query");
const results = document.getElementById("results");



lomake.addEventListener("submit", async function(event) {
    event.preventDefault();
    const search = document.getElementById("query").value;
    const response = await fetch(`https://api.tvmaze.com/search/shows?q=${encodeURIComponent(search)}`);


    const data = await response.json();
    results.innerHTML = "";

    for(let i = 0; i < data.length; i++){
        const show = data[i].show;
        const article = document.createElement("article")

        const heading = document.createElement("h2");
        heading.textContent = show.name;

        const link = document.createElement("a");
        link.href = show.url;
        link.textContent = "Details";
        link.target = "_blank";

        const image = document.createElement("img");
        image.src = show.image?.medium;
        image.alt = show.name;

        const summary = document.createElement("div");
        summary.innerHTML = show.summary || "";

            
        article.appendChild(heading);
        article.appendChild(link);
        article.appendChild(image);
        article.appendChild(summary);

            
        results.appendChild(article);
        }

});





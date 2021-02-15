window.onload = () => {
document.getElementById("search").addEventListener("click", function () { 
    const userText = document.getElementById('query').value;
    const url = '/search/' + userText; // This should remind you of APIs in Python!
window.fetch(url).then(response => response.json()) // So should JSON conversion!
    .then(data => { // .then will only run the function *once* the data is fetched from the internet
        // See what this logs!
        console.log(data); 
    });
       });
    
}



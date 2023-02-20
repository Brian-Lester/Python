async function test() {
    // The await keyword lets js know that it needs to wait until it gets a response back to continue.
    var response = await fetch("https://api.github.com/users/Brian-Lester");
    // We then need to convert the data into JSON format.
    var coderData = await response.json();
    let div = document.createElement("div");
    let name = document.createElement("p");
    let f = document.createElement('p');
    let img = document.createElement('img');
    name.textContent = coderData.name;
    f.textContent=coderData.followers;
    img.src=coderData.avatar_url;
    div.appendChild(name);
    div.appendChild(img);
    div.appendChild(f)
    let con =document.querySelector('.test');
    con.appendChild(div)
    return con;
}
    
console.log(test());
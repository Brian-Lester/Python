function remove(){
    document.querySelector(".cookie").remove()
}
async function burbank(){
    alert('Loading weather report for Burbank!')
    let response = await fetch("http://api.openweathermap.org/data/2.5/forecast?lat=34.1808&lon=-118.309&units=imperial&appid=5256f9a7488ba0290aae23a7ad6387f7");
    let temp = await response.json();
    document.querySelector('h2').textContent='burbank';
    document.querySelector('p').textContent =temp.list[0].weather[0].description;
    document.querySelector('.test0').textContent = temp.list[0].main.temp_min;
    document.querySelector('.test1').textContent = temp.list[0].main.temp_max;
    console.log(temp.list[0].main.temp_max)
}

async function chicago(){
    alert('Loading weather report for Chicago!')
    let response = await fetch("http://api.openweathermap.org/data/2.5/forecast?lat=41.85&lon=-87.65&units=imperial&appid=5256f9a7488ba0290aae23a7ad6387f7");
    let temp = await response.json();
    document.querySelector('h2').textContent='Chicago';
    document.querySelector('p').textContent =temp.list[0].weather[0].description;
    document.querySelector('.test0').textContent = temp.list[0].main.temp_min;
    document.querySelector('.test1').textContent = temp.list[0].main.temp_max;
    console.log(temp.list[0].main.temp_max)
}

async function dallas(){
    alert('Loading weather report for Dallas!')
    let response = await fetch("http://api.openweathermap.org/data/2.5/forecast?lat=32.7668&lon=-96.7836&units=imperial&appid=5256f9a7488ba0290aae23a7ad6387f7");
    let temp = await response.json();
    document.querySelector('h2').textContent='Dallas';
    document.querySelector('p').textContent =temp.list[0].weather[0].description;
    document.querySelector('.test0').textContent = temp.list[0].main.temp_min;
    document.querySelector('.test1').textContent = temp.list[0].main.temp_max;
    console.log(temp.list[0].main.temp_max)
}

function convert(element){
    var array = document.querySelectorAll('.test');
    for (let i = 0; i < array.length; i++) {
        if(element.value == "f"){
            array[i].innerText = Math.round(array[i].innerText * 9/5 +32);
        } else{
            array[i].innerText = Math.round(array[i].innerText *.32);
        }
    }
}

function apply_style() {
    var p = document.querySelector("table");
    p.classList.add("table");

    var links = document.getElementsByTagName('a');
    for (var i = 0; i < links.length; i++) {
        links[i].setAttribute('target', '_blank');
    }

};

function startTimer(duration, display) {
    var timer = duration, minutes, seconds;
    setInterval(function () {
        minutes = parseInt(timer / 60, 10);
        seconds = parseInt(timer % 60, 10);

        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;

        display.textContent = minutes + ":" + seconds;

        if (--timer < 0) {
            timer = duration;
        }
    }, 1000);
}



const getlocation = () => {
    navigator.geolocation.watchPosition(async (pos) => {
        var lat = pos.coords.latitude;
        var long = pos.coords.longitude;
        var wkey = config.W_KEY;

        const url = 'https://api.openweathermap.org/data/2.5/weather?lat=' + lat + '&lon=' + long + '&APPID=' + wkey + '&units=metric'
        const response = await fetch(url);
        const data = await response.json();

        setWeather(data);

    });
}

function setWeather(data) {

    console.log(data);

    loc = document.querySelector('#place');
    loc.textContent = data.name + ', ' + data.sys.country;

    weather = document.querySelector('#weather');
    weather.textContent = data.weather[0].description;

    temp = document.querySelector('#temp');
    temp.textContent = data.main.temp + ' C°';

    document.getElementById("wimg").src = "http://openweathermap.org/img/wn/" + data.weather[0].icon + '.png';


}

window.onload = function () {
    var fiveMinutes = 60 * 5,
        display = document.querySelector('#time');
    startTimer(fiveMinutes, display);
    getlocation();
};
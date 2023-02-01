//function to display alert when pressing on a city
function alertMessage() {
    alert("Loading weather report...");
}
for (var li of document.querySelectorAll(".topBar li")) {
    li.addEventListener("click", alertMessage);
}

//function to remove cookie message when I accept button is pressed
var cookieMessage = document.querySelector(".footer");
function removeCookie() {
    cookieMessage.remove();
}

//function to switch temperature from celsius to farenheight
function fahrenheit(temperature){
    return(9/5 * temperature + 32).toPrecision(2)
}
function celsius(temperature){
    return(5/9 * (temperature - 32)).toPrecision(3)
}
function changeTemp(id){
    for(let element of document.querySelectorAll(".highTemp,.lowTemp")){
        if(id == 'F'){
            element.innerHTML = fahrenheit(parseFloat(element.innerHTML))
        } else if(id == 'C'){
            element.innerHTML =celsius(parseFloat(element.innerHTML))
        }
    }
}
// // VERSION TWO OF THE SAME FUNCTION
// function changeTemp(id){
//     var myTemperatures = document.querySelectorAll(".highTemp,.lowTemp");
//     for (var i = 0; i < myTemperatures.length; i++) {
//         var element = myTemperatures[i];
//         if (id == "F") {
//             element.innerHTML = fahrenheit(parseFloat(element.innerHTML))
//         } else if (id == "C") {
//             element.innerHTML = celsius(parseFloat(element.innerHTML))
//         }
//     }
// }
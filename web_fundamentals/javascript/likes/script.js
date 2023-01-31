var clicks = [9,12,9]
var likes = [
    document.querySelector(".likesOne"),
    document.querySelector(".likesTwo"),
    document.querySelector(".likesThree")]


function increase(element){
    clicks[element]++;
    likes[element].innerHTML =  clicks[element] + " like(s)";
}

// THIS WAS MY ORIGINAL SET UP, BUT EACH BUTTON HAD THE FUNCTION LABELED AS THE FOLLOWING HERE
// THIS METHOD ALSO WORKS BUT THE NEW WAY IS MUCH CLEANER
// var clicksOne = 9;
// var clicksTwo = 12;
// var clicksThree = 9;
// var likesOne = document.querySelector(".likesOne");
// var likesTwo = document.querySelector(".likesTwo");
// var likesThree = document.querySelector(".likesThree");


// function increaseOne(){
//     clicksOne++;
//     likesOne.innerHTML = clicksOne + " like(s)";
// }
// function increaseTwo(){
//     clicksTwo++;
//     likesTwo.innerHTML = clicksTwo + " like(s)";
// }
// function increaseThree(){
//     clicksThree++;
//     likesThree.innerHTML = clicksThree + " like(s)";
// }
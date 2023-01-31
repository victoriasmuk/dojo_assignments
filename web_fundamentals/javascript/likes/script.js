var clicksOne = 0
var clicksTwo = 0
var clicksThree = 0
var likesOne = document.querySelector(".likesOne");
var likesTwo = document.querySelector(".likesTwo");
var likesThree = document.querySelector(".likesThree");


function increaseOne(){
    clicksOne++;
    likesOne.innerHTML = clicksOne + " like(s)";
}
function increaseTwo(){
    clicksTwo++;
    likesTwo.innerHTML = clicksTwo + " like(s)";
}
function increaseThree(){
    clicksThree++;
    likesThree.innerHTML = clicksThree + " like(s)";
}
// FUNCTION TO EDIT NAME IN PROFILE
var newName = document.querySelector(".user_name");
function editMe(){
    newName.innerText = "Jane Doe"
}
// FUNCTION TO PRESS BUTTON & REMOVE USER
var requests = document.querySelector(".icon2")
var connections = document.querySelector(".icon500")

function removeMe(id){
    var user = document.querySelectorAll("#user1");
    for(var i=0; i < user.length; i++){
        var element = user[i];
        if(id == "action1"){
            element.remove();
            requests.innerHTML--;
            connections.innerHTML++;
        } else if(id == "action2"){
            element.remove();
            requests.innerHTML--;
        }
    }
}
function removeMe2(id){
    var user = document.querySelectorAll("#user2");
    for(var i=0; i < user.length; i++){
        var element = user[i];
        if(id == "action3"){
            element.remove();
            requests.innerHTML--;
            connections.innerHTML++;
        } else if(id == "action4"){
            element.remove();
            requests.innerHTML--;
        }
    }
}


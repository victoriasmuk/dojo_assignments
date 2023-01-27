var a="Fizz"
var b="Buzz"
var c="FizzBuzz"

for(var i=1; i<=100; i++){
    if(i%3 == 0) console.log(a);
    else if(i%5 == 0) console.log(b);
    else if(i%15 == 0) console.log(c);
    else console.log(i)
}


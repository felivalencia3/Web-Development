let num = Math.floor((Math.random()*100)+1);
let guesses=0;
function guessit() {
console.log("Loading...")
let guess = document.getElementById("input1").value;
    console.log(num,guesses,guess);


    guesses++;
    if (guess > num) {
        alert("Lower!")
    }else if(guess < num) {
        alert("Higher!")
    }else {
        let final = "Perfect! My number was " + num +
        " and you guessed it in " + guesses + " guesses."
        alert(final)

}
}

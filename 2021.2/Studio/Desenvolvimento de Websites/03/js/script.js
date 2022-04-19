function RESET(N1,N2){
    N1 = 0
    N2 = 0
}
const Input = [document.getElementsByClassName("input")]
var N1 = Input[0]
var N2 = Input[1]
var N1 = [N1].value
console.log(N1,N2)
var R = document.getElementById("RESET")
if (R>0) {
    RESET(N1,N2)
}
const Output=[N1,N2]
document.getElementsByClassName("input").value = Output
console.log(Input,Output)
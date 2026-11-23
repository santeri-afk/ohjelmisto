let confirmatio = confirm("Should I calculate the square root?")
 
if (confirmatio === true){
    let number = prompt("Anna numero:");
    let numberint = parseInt(number);
    if (numberint > -1){
        let square_root = Math.sqrt(numberint);
        document.getElementById("number").textContent = "numeron square root on = " + square_root
    }else{
        document.getElementById("number").textContent = "The square root of a negative number is not defined"
    }

}else{
    document.getElementById("number").textContent = "The square root is not calculated."
}

function Counter(){
    milliseconds = document.getElementById("milliseconds").innerHTML
    seconds = document.getElementById("seconds").innerHTML
    minutes = document.getElementById("minutes").innerHTML
    hours = document.getElementById("hours").innerHTML
    milliseconds++
    if (milliseconds<10){
        milliseconds = "0"+milliseconds}
    if (milliseconds>99){
        milliseconds=0
        seconds++
        if (seconds<10){
        seconds = "0"+seconds}}
        if (seconds>59){
            seconds=0
            minutes++
            if (minutes<10){
                minutes = "0"+minutes}}
        if (minutes>59){
            minutes=0
            hours++
            if (hours<10){
                hours = "0"+hours}}
    document.getElementById("milliseconds").innerHTML = milliseconds
    document.getElementById("seconds").innerHTML = seconds
    document.getElementById("minutes").innerHTML = minutes
    document.getElementById("hours").innerHTML = hours
    document.getElementById("Pause").onclick = (function(){clearInterval(interval)})
    document.getElementById("Zero").onclick = function(){
        document.getElementById("milliseconds").innerHTML = "00"
        document.getElementById("seconds").innerHTML = "00"
        document.getElementById("minutes").innerHTML = "00"
        document.getElementById("hours").innerHTML = "00"}
    document.getElementById("Stop").onclick = (function(){
        document.getElementById("milliseconds").innerHTML = "00"
        document.getElementById("seconds").innerHTML = "00"
        document.getElementById("minutes").innerHTML = "00"
        document.getElementById("hours").innerHTML = "00"
        clearInterval(interval)})}

var interval
document.getElementById("Start").onclick = (function(){interval = setInterval(Counter, 10)})
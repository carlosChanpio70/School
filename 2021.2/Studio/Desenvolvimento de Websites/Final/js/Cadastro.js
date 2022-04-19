function out_A(Name,Score,Stats){
    const div = document.createElement("div")
    const txt1 = document.createTextNode(Name)
    const p1 = document.createElement("p")
    p1.appendChild(txt1)
    div.appendChild(p1)
    const txt2 = document.createTextNode(Score)
    const p2 = document.createElement("p")
    p2.appendChild(txt2)
    div.appendChild(p2)
    const txt3 = document.createTextNode(Stats)
    const p3 = document.createElement("p")
    p3.appendChild(txt3)
    div.appendChild(p3)
    const out = document.getElementById("A-lines")
    out.appendChild(div)}

function out_R(Name,Score,Stats){
    const div = document.createElement("div")
    const txt1 = document.createTextNode(Name)
    const p1 = document.createElement("p")
    p1.appendChild(txt1)
    div.appendChild(p1)
    const txt2 = document.createTextNode(Score)
    const p2 = document.createElement("p")
    p2.appendChild(txt2)
    div.appendChild(p2)
    const txt3 = document.createTextNode(Stats)
    const p3 = document.createElement("p")
    p3.appendChild(txt3)
    div.appendChild(p3)
    const out = document.getElementById("R-lines")
    out.appendChild(div)}
    
function Save(){
    var Name = document.getElementById("Input1").value
    var Score = Number(document.getElementById("Input2").value)
    var Stats
    if (Score>5){
        Stats = "Aprovado"
    }else{
        Stats = "Reprovado"}
    if (Stats == "Aprovado"){
        out_A(Name,Score,Stats)
    }else{
        out_R(Name,Score,Stats)}}

document.getElementById("Save").onclick = Save
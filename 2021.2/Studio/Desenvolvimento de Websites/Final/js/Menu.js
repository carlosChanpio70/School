function showHome(){
    document.getElementById("Home").style.display = 'none'
    document.getElementById("Cadastrar").style.display = 'none'
    document.getElementById("Approved").style.display = 'none'
    document.getElementById("Non_Approved").style.display = 'none'}

function showCadastro(){
    document.getElementById("Home").style.display = 'none'
    document.getElementById("Cadastrar").style.display = 'block'
    document.getElementById("Approved").style.display = 'none'
    document.getElementById("Non_Approved").style.display = 'none'}

function showApproved(){
    document.getElementById("Home").style.display = 'none'
    document.getElementById("Cadastrar").style.display = 'none'
    document.getElementById("Approved").style.display = 'block'
    document.getElementById("Non_Approved").style.display = 'none'}

function showNon_Approved(){
    document.getElementById("Home").style.display = 'none'
    document.getElementById("Cadastrar").style.display = 'none'
    document.getElementById("Approved").style.display = 'none'
    document.getElementById("Non_Approved").style.display = 'block'}

document.getElementById("HomeB").onclick = function(){showHome()}
document.getElementById("CadastrarB").onclick = function(){showCadastro()}
document.getElementById("ApprovedB").onclick = function(){showApproved()}
document.getElementById("Non_ApprovedB").onclick = function(){showNon_Approved()}
document.getElementById("HomeB2").onclick = function(){showHome()}
document.getElementById("CadastrarB2").onclick = function(){showCadastro()}
document.getElementById("ApprovedB2").onclick = function(){showApproved()}
document.getElementById("Non_ApprovedB2").onclick = function(){showNon_Approved()}
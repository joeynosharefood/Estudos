function start(){
    calculate()
}
function calculate(){
    operatorStr = document.querySelector('input#operator')
    operatorStr = operatorStr.value
    textbox = document.querySelector('select#textbox')
    if (operatorStr.length == 0){
        alert('Erro')
    }else{
        textbox.innerHTML = ''
        for (oper = 0; oper <= 10; oper ++){
            option = document.createElement('option')
            option.text = `${operatorStr}x${oper}=${operatorStr*oper}`
            textbox.appendChild(option)
        }
    }
}
 
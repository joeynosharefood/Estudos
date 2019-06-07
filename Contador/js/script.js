inicioStr = document.querySelector('input#inicio')
fimStr = document.querySelector('input#fim')
passoStr = document.querySelector('input#passo')
divAnswer = document.querySelector('div#answer')
inicioStr = inicioStr.value
fimStr = fimStr.value
passoStr = passoStr.value

function start(){
    generateStructure()
}

function generateStructure(){
    if (inicioStr.length == 0 || fimStr.length == 0 || passoStr.length == 0){
        alert('Erro')
        divAnswer.innerHTML = 'Impossivel contar, tente novamente'
    }else{
        divAnswer.innerHTML = 'Contando<br>'
        inicio = Number(inicioStr.value)
        fim = Number(fimStr.value)
        passo = Number(passoStr.value)
        if (passoStr.value == 0){
            alert('Passo invalido, vou considerar como 1')
            passo = 1
        }
        if (inicio > fim){//Contagem Regressiva
            for (contNeg = inicio; contNeg >= fim; contNeg -= passo){
                divAnswer.innerHTML += contNeg + '&#9755;'
            }
        }else{//Contagem Normal
            for (cont = inicio; cont <= fim; cont += passo){
            divAnswer.innerHTML += cont + '&#9755;'
            }           
        }divAnswer.innerHTML += '&#9983;'
    }
}
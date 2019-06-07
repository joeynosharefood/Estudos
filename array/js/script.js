arraySelect = []
function startEntry(){
    arrayCreator()
}
function startAnalyze(){
    if (arraySelect.length == 0){
        alert('Erro3')
    }else{
        let answer = document.querySelector('div#answer')
        answer.innerHTML = ''
        answer.innerHTML += `Total de Números cadastrados foi de ${arraySelect.length}<br>`
        answer.innerHTML += `O maior valor é ${highestValue()}<br>`
        answer.innerHTML += `O menor valor é ${lowerValue()}<br>`
        answer.innerHTML += `A soma dos valores é ${sumValues()}<br>`
        answer.innerHTML += `A media dos valore é ${arithmeticMean()}`
    }
}
function arrayCreator(){
    if (arraySelect.length > 0){
        let answer = document.querySelector('div#answer')
        answer.innerHTML = ''
    }
    let numberEntry = document.querySelector('input#numbertext')
    if (numberEntry.value.length == 0){
        alert('Erro')
    }else{
        if (arraySelect.indexOf(numberEntry.value) == -1){
            arraySelect.push(numberEntry.value)
            selectStructure(numberEntry.value)
        }else{
            alert('Erro2')
        }
    }
}
function selectStructure(numberData){
    let selectBox = document.querySelector('select#arraybox')
    let opt = document.createElement('option')
    opt.text = `O valor adicionado foi de ${numberData}`
    selectBox.appendChild(opt)
}
function highestValue(){
    var highest = 0 
    for(let pos in arraySelect){
        var highest = arraySelect[pos] > highest ? arraySelect[pos] : highest          
        }
    return highest
}
function lowerValue(){
    var lower = 0
    for(let pos in arraySelect){
        if (lower == 0){
            lower = arraySelect[pos]
        }else{
            lower = arraySelect[pos] < lower ? arraySelect[pos] : lower
        }
    }
    return lower
}
function sumValues(){
    sum = 0
    for(let pos in arraySelect){
        let numberArray = Number(arraySelect[pos])
        sum += numberArray
    }
    return sum
}
function arithmeticMean(){
    return sumValues() / arraySelect.length
}
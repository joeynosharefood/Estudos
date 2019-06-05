function start(){
    idade()
    photoChange()
    info()
}
function idade(){
    returnIdade = document.querySelector('input#idade')
    anoNascimento = Number(returnIdade.value)
    a1 = new Date()
    ano = a1.getFullYear()
    age = ano - anoNascimento
}
function photoChange(){
    returnSexo = document.querySelector('select#sexo')
    rosto = document.querySelector('img#rosto')
    if (age >= 2019){
        alert('Coloque uma data')
    }else if(age < 0){
        alert('Coloque uma data valida')
    }else{
        if (returnSexo.value == 'mas'){//If Masculino
            if (age <= 6){
                rosto.src = 'img/mCria.png'
            }else if(age > 6 && age <= 18){
                rosto.src = 'img/mAdol.png'
            }else if(age > 18 && age <=50){
                rosto.src = 'img/mAdul.png'
            }else if(age > 50){
                rosto.src = 'img/mVeio.png'
        }}else if (returnSexo.value == 'fem'){//Feminino
            if (age <= 6){
                rosto.src = 'img/fCria.png'
            }else if(age > 6 && age <= 18){
                rosto.src = 'img/fAdol.png'
            }else if(age > 18 && age <=50){
                rosto.src = 'img/fAdul.png'
            }else if(age > 50){
                rosto.src = 'img/fVeio.png'
            }
        }
    }
        
}
function info(){
    inf = document.querySelector('p#info')
    if (age >= 2019){
        inf.innerText = 'Coloque uma data'
    }else if(age < 0){
        inf.innerText = 'Coloque uma data valida'
    }else{
        if (returnSexo.value == 'mas'){
        inf.innerText = `Você é um homem de ${age} anos de idade`
        }else if (returnSexo.value == 'fem'){
            inf.innerText = `Você é uma mulher de ${age} amps de idade`
        }
    }

}
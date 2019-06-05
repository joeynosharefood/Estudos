agora = new Date()
hora = agora.getHours()
//hora = 24//debug
cong = document.querySelector('div#bemvindo')
foto = document.querySelector('div#img')

if (hora >= 6 && hora < 12){
    cong.innerHTML = `Bom dia, agora são ${hora} horas`
    foto.innerHTML = '<img src="img/manha.png" alt="fotos">'
    document.body.style.background = '#f9b592'
} else if(hora >= 12 && hora < 18){
    cong.innerHTML = `Boa tarde, agora são ${hora} horas`
    foto.innerHTML = '<img src="img/tarde.png" alt="fotos">'
    document.body.style.background = '#9a7612'
} else if(hora >= 18 && hora < 24){
    cong.innerHTML = `Boa noite, agora são ${hora} horas`
    foto.innerHTML = '<img src="img/noite.png" alt="fotos">'
    document.body.style.background = '#2a3c48'
} else{
    cong.innerHTML = `Boa Madrugada, agora são ${hora}`
    foto.innerHTML = '<img src="img/noite.png" alt="fotos">'
    document.body.style.background = '#2a3c48'
}

url = document.querySelector('#blogimg')

document.querySelector('#submit').addEventListener('click', (event)=> {
    event.preventDefault()
    
    document.querySelector('#imagecontainer').innerHTML = `<img src="${url.value}" alt="" id="photo">`
})
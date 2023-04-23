const tabAgregar = document.querySelector('.tab-agregar')
const tabQuitar = document.querySelector('.tab-quitar')


document.addEventListener('DOMContentLoaded', () => {
    tabAgregar.addEventListener('click', showAgregar)
    tabQuitar.addEventListener('click', showQuitar)
})

const tabContentQuitar = document.querySelector('.tab-content-quitar')
const tabContentAgregar = document.querySelector('.tab-content-agregar')
function showAgregar() {
    tabAgregar.classList.add('activo')
    tabQuitar.classList.remove('activo')
    if(!tabContentAgregar.classList.contains('show')) {
        tabContentAgregar.classList.add('show')
        tabContentQuitar.classList.remove('show')
    }
}

function showQuitar() {
    tabQuitar.classList.add('activo')
    tabAgregar.classList.remove('activo')
    if(!tabContentQuitar.classList.contains('show')) {
        tabContentQuitar.classList.add('show')
        tabContentAgregar.classList.remove('show')
    }
}

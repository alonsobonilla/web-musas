import { objExport } from "./ordenar-producto.js";

function evento () {
    const ordenar_producto = document.querySelectorAll('#ordenar-producto');
    ordenar_producto.forEach( ordenar => {
        
        ordenar.addEventListener("click", (e) => {
            guardarDatos(e);
            console.log(objExport);
            window.location.href = 'producto-comoboduo+-8.html';
        });
    })
}

let nombre_producto, descripcion_producto, precio_producto, img_producto;

function guardarDatos(e) {
    e.preventDefault();
    const elemento_padre = e.target.parentElement.parentElement;
    const hijos = elemento_padre.children;
    
    nombre_producto = hijos.item(0).textContent;
    descripcion_producto = hijos.item(1).textContent;
    precio_producto = hijos.item(2).innerHTML;
    img_producto = elemento_padre.nextElementSibling.firstElementChild.src;
    
    objExport.nombre_producto = nombre_producto;
    objExport.descripcion_producto = descripcion_producto;
    objExport.precio_producto = precio_producto;
    objExport.img_producto = img_producto;
}

export { evento }
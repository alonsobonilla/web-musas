import { agregar_carrito } from "../utils/selectors.js";
import { Producto } from "./Class/Producto.js";
// Eventos
agregar_carrito.addEventListener('submit', () => {
    instanciarProducto(e);
});


function instanciarProducto(e) {
    console.log(e);
    const precio_producto = parseFloat(document.querySelector('.precio_producto-compra').firstElementChild.nextSibling.textContent);
    const nombre_producto = document.querySelector('.nombre_producto-compra').textContent;
    const imagen_producto = document.querySelector('.imagen-producto-precompra').lastElementChild.attributes.src.textContent;

    const productos_personalizar = document.querySelectorAll('.valores');
    let array_agregar = [];
    let array_quitar = [];
    let array_combear = [];
    let array_salsas = [];
    productos_personalizar.forEach(e => {
        if (e.checked) {
            const nombre_producto_personaliza = e.nextElementSibling.nextElementSibling.textContent;
            const precio_producto_personaliza = e.nextElementSibling.nextElementSibling.nextElementSibling.lastChild.textContent;

            const identificador_personaliza = e.parentElement.parentElement.id;
            if (identificador_personaliza == 'agregar') {
                const obj_agregar = {
                    'nombre': nombre_producto_personaliza,
                    'precio': precio_producto_personaliza
                }
                array_agregar.push(obj_agregar);
            } else if (identificador_personaliza == 'quitar') {
                const obj_quitar = {
                    'nombre': nombre_producto_personaliza,
                    'precio': precio_producto_personaliza
                }
                array_quitar.push(obj_quitar);
            } else if (identificador_personaliza == 'combear') {
                const obj_combear = {
                    'nombre': nombre_producto_personaliza,
                    'precio': precio_producto_personaliza
                }
                array_combear.push(obj_combear);
            } else {
                const obj_salsas = {
                    'nombre': nombre_producto_personaliza,
                }
                array_salsas.push(obj_salsas);
            }
        }
    });

    const producto = new Producto(nombre_producto,precio_producto,imagen_producto,array_agregar,array_combear,array_quitar,array_salsas);
    producto.guardarDatos();
}
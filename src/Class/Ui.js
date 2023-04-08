import { img_producto, nombre_producto, precio_producto, descripcion_producto } from "../utils/selectors.js";

class Ui {

    static renderizarProducto(nombre, descripcion, precio, img) {
        img_producto.src = img;
        img_producto.alt = nombre;
        nombre_producto.textContent = nombre;
        precio_producto.innerHTML = precio;
        descripcion_producto.textContent = descripcion;
    }
}

export { Ui };
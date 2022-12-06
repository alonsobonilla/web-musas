//Carrito de compras 

document.addEventListener('DOMContentLoaded', () => {
    const datosCarrito = () => window.innerWidth <= 1024;
    const table_datos = document.querySelector('.productos-table')
    if (datosCarrito()) {
        mostrarDatosCarrito('movil');
        mostrarAgregados();
    } else {
        mostrarDatosCarrito('pc');
        if (table_datos != null) {
            if (localStorage.length != 0) {
                table_datos.classList.add('d-block');
            }
        }
    }
} )
agregarCarrito();
function agregarCarrito() {
    const agregar = document.getElementById('agregar-carrito');
    const precio_producto = parseFloat(document.querySelector('.precio_producto-compra').firstElementChild.nextSibling.textContent);
    agregar.addEventListener('click', (e) => {
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
                        'nombre_agregar': nombre_producto_personaliza,
                        'precio_agregar': precio_producto_personaliza
                    }
                    array_agregar.push(obj_agregar);
                } else if (identificador_personaliza == 'quitar') {
                    const obj_quitar = {
                        'nombre_quitar': nombre_producto_personaliza,
                        'precio_quitar': precio_producto_personaliza
                    }
                    array_quitar.push(obj_quitar);
                } else if (identificador_personaliza == 'combear') {
                    const obj_combear = {
                        'nombre_combo': nombre_producto_personaliza,
                        'precio_combo': precio_producto_personaliza
                    }
                    array_combear.push(obj_combear);
                } else {
                    const obj_salsas = {
                        'nombre_salsa': nombre_producto_personaliza,
                    }
                    array_salsas.push(obj_salsas);
                }
            }
        });
        guardarDatos(nombre_producto, precio_producto, imagen_producto, array_agregar, array_quitar, array_combear, array_salsas);
    })
    
}

function guardarDatos(nombre_p, precio_p, imagen_producto, agregar, quitar, combear, salsas) {
    if(localStorage.getItem(nombre_p) == null) {
        localStorage.setItem(nombre_p, JSON.stringify(
            {
                'precioProducto': precio_p,
                'precioVenta': Math.round((precio_p + precioCombos(combear) + precioAgregar(agregar))*100)/100,
                'cantidad': 1,
                'img': imagen_producto,
                'personaliza': {
                    'agregar': agregar,
                    'quitar': quitar,
                    'combear': combear,
                    'salsas': salsas
                }
            }
        ));
    } else {
        //Faltaria actualizar si agrega personalización 
        actualizarDatosCarrito(nombre_p);
    }
}
function actualizarDatosCarrito(nombre_p) {
    const productos = JSON.parse(localStorage.getItem(nombre_p));
    productos.cantidad++;
    productos.precioVenta = (productos.precioProducto + precioCombos(productos.personaliza.combear) + precioAgregar(productos.personaliza.agregar)) * productos.cantidad;
    localStorage.setItem(nombre_p, JSON.stringify(productos));
}

function mostrarDatosCarrito(dispositivo) {
    let productos_carrito;
    dispositivo == 'movil' ? productos_carrito = document.querySelector('.productos-carrito') : productos_carrito = document.querySelector('.productos-carrito-table');
    const precio_total = document.getElementById('precio-total');
    const carrito_vacio = document.querySelector('.carrito-vacio');
    let content = '';
    let content_vacio = '';
    if(localStorage.length == 0) {
        content_vacio = `<p class="fs-3 text-center text-uppercase">Tu carrito esta vacio</p>`;
        carrito_vacio.innerHTML = content_vacio;
    } else {
        content = contentCarrito(dispositivo);
    }
    if(productos_carrito != null && content != '') productos_carrito.innerHTML = content;
    if(sumaCarrito() != 0) precio_total.innerHTML = `<p class="fs-4 text-end"><span class="fw-bold fs-4">Total a pagar:</span> S/.${sumaCarrito()}</p>`;

    eliminarProducto();
    disminuirCantidad();
    aumentarCantidad();
    vaciarCarrito();
}
function contentCarrito(dispositivo) {
    let content = '';
    switch(dispositivo) {
        case 'movil':
            for(let i=0; i<localStorage.length; i++) {
                const key = localStorage.key(i);
                const producto = JSON.parse(localStorage.getItem(key));
                content += `<div class="mb-2">
                    <div class="d-flex justify-content-between align-items-center">
                        <div class="info-img-nombre-precio d-flex align-items-center gap-2">
                            <div class="product-img">
                                <img src=${producto.img} alt="Hamburguesa">
                            </div>
                            
                            <div>
                                <p>${producto.cantidad} x ${key}</p>
                                <p>${producto.precioVenta}</p>
                            </div>
                            
                        </div>
                        <div class="otros">
                            <div class="d-flex align-items-center justify-content-around">
                                <button type="button" name="${key}" class="eliminar-producto boton-eliminar">
                                    <a href="" class="icon-trash d-flex align-items-center">
                                        <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-trash" width="36"
                                            height="36" viewBox="0 0 24 24" stroke-width="1.5" stroke="#DB4200" fill="none"
                                            stroke-linecap="round" stroke-linejoin="round">
                                            <path stroke="none" d="M0 0h24v24H0z" fill="none" />
                                            <line x1="4" y1="7" x2="20" y2="7" />
                                            <line x1="10" y1="11" x2="10" y2="17" />
                                            <line x1="14" y1="11" x2="14" y2="17" />
                                            <path d="M5 7l1 12a2 2 0 0 0 2 2h8a2 2 0 0 0 2 -2l1 -12" />
                                            <path d="M9 7v-3a1 1 0 0 1 1 -1h4a1 1 0 0 1 1 1v3" />
                                        </svg>
                                    </a>
                                </button>
                                <div class="icon-more">
                                    <i class="fa-solid fa-caret-down"></i>
                                </div>
                            </div>
                            
                            <div class="d-flex justify-content-center align-items-center gap-2 mt-2">
                                <button name="${key}" class="botones-carrito btn border-0 w-auto disminuir-cantidad">-</button>
                                    <p>${producto.cantidad}</p>
                                <button name="${key}" class="botones-carrito btn border-0 w-auto aumentar-cantidad">+</button>
                            </div>
        
                        </div>
                    </div>
                    <div class="info-producto">
                        <p class="fw-bold text-uppercase text-start">Se agregó</p>
                        <ul class="lista-agregados">
                        ${contentProductosPersonalizacion(producto,'agregar')}
                        </ul>
                        <p class="fw-bold text-uppercase text-start">Se quitó</p>
                        <ul class="lista-agregados">
                        ${contentProductosPersonalizacion(producto,'quitar')}
                        </ul>
                        <p class="fw-bold text-uppercase text-start">Combos agregados</p>
                        <ul class="lista-agregados">
                        ${contentProductosPersonalizacion(producto,'combear')}
                        </ul>
                        <p class="fw-bold text-uppercase text-start">Salsas</p>
                        <ul class="lista-agregados">
                        ${contentProductosPersonalizacion(producto,"salsas")}
                        </ul>
                    </div>
                </div>`
            }
        break;
        case 'pc':
            for(let i=0; i<localStorage.length; i++) {
                const key = localStorage.key(i);
                const producto = JSON.parse(localStorage.getItem(key));
                content += `
                    <tr>
                        <td class="d-flex gap-2 justify-content-center">
                            <div>
                                <img src="${producto.img}" alt="Hamburguesa">
                            </div>
                            <div>
                                <h3 class="fs-6">${key}</h3>
                                <div class="text-center"> 
                                    <p class="fw-bold text-uppercase text-start">Se agregó</p>
                                    <ul class="lista-agregados">
                                    ${contentProductosPersonalizacion(producto,'agregar')}
                                    </ul>
                                    <p class="fw-bold text-uppercase text-start">Se quitó</p>
                                    <ul class="lista-agregados">
                                    ${contentProductosPersonalizacion(producto,'quitar')}
                                    </ul>
                                    <p class="fw-bold text-uppercase text-start">Combos agregados</p>
                                    <ul class="lista-agregados">
                                    ${contentProductosPersonalizacion(producto,'combear')}
                                    </ul>
                                    <p class="fw-bold text-uppercase text-start">Salsas</p>
                                    <ul class="lista-agregados">
                                    ${contentProductosPersonalizacion(producto,"salsas")}
                                    </ul>
                                </div>
                            </div>
                            <button type="button" name="${key}" class="eliminar-producto boton-eliminar">
                                    <a href="" class="icon-trash d-flex align-items-center">
                                        <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-trash" width="36"
                                            height="36" viewBox="0 0 24 24" stroke-width="1.5" stroke="#DB4200" fill="none"
                                            stroke-linecap="round" stroke-linejoin="round">
                                            <path stroke="none" d="M0 0h24v24H0z" fill="none" />
                                            <line x1="4" y1="7" x2="20" y2="7" />
                                            <line x1="10" y1="11" x2="10" y2="17" />
                                            <line x1="14" y1="11" x2="14" y2="17" />
                                            <path d="M5 7l1 12a2 2 0 0 0 2 2h8a2 2 0 0 0 2 -2l1 -12" />
                                            <path d="M9 7v-3a1 1 0 0 1 1 -1h4a1 1 0 0 1 1 1v3" />
                                        </svg>
                                    </a>
                            </button>
                        </td>
                        <td>
                            <p class="d-flex align-items-center justify-content-center" style="height: 100px;">S/. ${producto.precioProducto}</p>
                        </td>
                        <td>
                            <div class="d-flex justify-content-center align-items-center gap-2" style="height: 100px;">
                                <button name="${key}" class="botones-carrito btn border-0 w-auto disminuir-cantidad">-</button>
                                    <p>${producto.cantidad}</p>
                                <button name="${key}" class="botones-carrito btn border-0 w-auto aumentar-cantidad">+</button>
                            </div>
                        </td>
                        <td>
                            <p class="d-flex justify-content-center align-items-center" style="height: 100px;">S/. ${producto.precioVenta}</p>
                        </td>
                    </tr>`
            }
        break;
    }   
    return content;
}
function sumaCarrito() {
    let suma = 0;
    if(localStorage.length != 0) {
        for(let i=0; i<localStorage.length; i++) {
            const key = localStorage.key(i);
            suma += JSON.parse(localStorage.getItem(key)).precioVenta;
        }
    }
    return suma;
}
function contentProductosPersonalizacion(producto, personalizacion) {
    let productos_quitados;
    let content = '';
    switch(personalizacion) {
        case 'agregar': 
            productos_quitados = producto.personaliza.agregar;
            for(let i=0; i<productos_quitados.length; i++) {
                content += `<li><p>${productos_quitados[i].nombre_agregar} - S/.${productos_quitados[i].precio_agregar}</p></li>`;
            }
            break;
        case 'quitar': 
            productos_quitados = producto.personaliza.quitar;
            for(let i=0; i<productos_quitados.length; i++) {
                content += `<li><p>${productos_quitados[i].nombre_quitar} - S/.${productos_quitados[i].precio_quitar}</p></li>`;
            }
            break;
        case 'combear': 
            productos_quitados = producto.personaliza.combear;
            for(let i=0; i<productos_quitados.length; i++) {
                content += `<li><p>${productos_quitados[i].nombre_combo} - S/.${productos_quitados[i].precio_combo}</p></li>`;
            }
            break;
        default:
            productos_quitados = producto.personaliza.salsas;
            for(let i=0; i<productos_quitados.length; i++) {
                content += `<li><p>${productos_quitados[i].nombre_salsa}</p></li>`;
            }
        break;
    }
    return content;
}

/**Validamos la sesión del cliente */
function eliminarProducto() {
    const eliminarProducto = document.querySelectorAll('.eliminar-producto');
    eliminarProducto.forEach(e => {
        e.addEventListener('click', () => {
            const nombreProducto = e.attributes.name.nodeValue;
            localStorage.removeItem(nombreProducto);
            location.reload();
        });
    });
}

function disminuirCantidad() {
    const elemento = document.querySelectorAll('.disminuir-cantidad');
    elemento.forEach(elemento => {
        elemento.addEventListener('click', () => {
            const nombreProducto = elemento.attributes.name.value;
            const obj = JSON.parse(localStorage.getItem(nombreProducto));
            if(obj.cantidad > 1) {
                obj.cantidad--;
                obj.precioVenta = Math.round((obj.precioProducto + precioCombos(obj.personaliza.combear) + precioAgregar(obj.personaliza.agregar))*100)/100 * obj.cantidad;
                localStorage.setItem(nombreProducto, JSON.stringify(obj));
                mostrarDatosCarrito();
                location.reload();
            }
        })
    });
}

function aumentarCantidad() {
    const elemento = document.querySelectorAll('.aumentar-cantidad');
    elemento.forEach(elemento => {
        elemento.addEventListener('click', () => {
            const nombreProducto = elemento.attributes.name.value;
            const obj = JSON.parse(localStorage.getItem(nombreProducto));
            obj.cantidad++;
            obj.precioVenta = Math.round((obj.precioProducto + precioCombos(obj.personaliza.combear) + precioAgregar(obj.personaliza.agregar))*100)/100 * obj.cantidad;
            localStorage.setItem(nombreProducto, JSON.stringify(obj));
            mostrarDatosCarrito();
            location.reload();
        })
    });
}

function vaciarCarrito() {
    const vaciarCarrito = document.querySelector('.btn-vaciar-carrito');
    vaciarCarrito.addEventListener('click', () => {
        localStorage.clear();
        mostrarDatosCarrito();
        location.reload();
    });
}
function mostrarAgregados() {
    const icon_more = document.querySelectorAll('.icon-more');
    if(icon_more != null) {
        icon_more.forEach(ele => {
            ele.addEventListener('click', () => {
                const clase_ele = ele.parentElement.parentElement.parentElement.nextElementSibling.classList[0];
                console.log(clase_ele);
                const info_producto = document.querySelector('.'+clase_ele);
                if(ele.classList.contains('active')) {
                    ele.classList.remove('active');
                    info_producto.classList.remove('d-block');
                } else {
                    ele.classList.add('active');
                    info_producto.classList.add('d-block');
                }
            })
        })
    }
}

function precioCombos(combear) {
    let suma=0;
    for(let i=0; i<combear.length; i++) {
        suma += Math.round(parseFloat(combear[i].precio_combo)*100)/100;
    }
    return suma;
}
function precioAgregar(agregar) {
    let suma=0;
    for(let i=0; i <agregar.length; i++) {
        suma += Math.round(parseFloat(agregar[i].precio_agregar)*100)/100;
    }
    return suma;
}

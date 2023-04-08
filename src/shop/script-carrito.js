//Carrito de compras 
import { table_data_carrito } from "../utils/selectors.js";
import { scripting } from "./functions.js";


document.addEventListener('DOMContentLoaded', () => {
    const datosCarrito = window.innerWidth <= 1024;
    if (datosCarrito) {
        mostrarDatosCarrito('movil');
    } else {
        mostrarDatosCarrito('pc');
        if (table_data_carrito != null) {
            if (localStorage.length != 0) {
                table_data_carrito.classList.add('d-block');
            }
        }
    }
} )

//Insertar 
const main_productos_carrito = document.querySelector('main');
const btn_vaciar_carrito = document.querySelector('main .btn-vaciar-carrito');


function actualizarDatosCarrito(nombre_p) {
    const productos = JSON.parse(localStorage.getItem(nombre_p));
    productos.cantidad++;
    productos.precioVenta = (productos.precioProducto + precioCombos(productos.personaliza.combear) + precioAgregar(productos.personaliza.agregar)) * productos.cantidad;
    localStorage.setItem(nombre_p, JSON.stringify(productos));
}

function mostrarDatosCarrito(dispositivo) {
    const precio_total = document.getElementById('#precio-total');

    if(localStorage.length == 0) {
        const div_carrito_vacio = scripting('DIV');
        const parrafo_carrito_vacio = scripting('P',['fs-3','text-center','text-uppercase'],'Tu carrito esta vacio');

        div_carrito_vacio.appendChild(parrafo_carrito_vacio);

        main_productos_carrito.insertBefore(div_carrito_vacio, btn_vaciar_carrito);
    } else {
        const p_precio_total = scripting('P',['fs-4','text-end','fw-bold'], 'Total a pagar: ');
        const span_precio_total = scripting('SPAN',['fs-4','fw-light'],`S/. ${sumaCarrito()}`);

        p_precio_total.appendChild(span_precio_total);
        precio_total.appendChild(p_precio_total);

        const div_main = contentCarrito(dispositivo);
        main_productos_carrito.insertBefore(div_main, btn_vaciar_carrito);
    }

}
function contentCarrito(dispositivo) {
    console.log(dispositivo);
    switch(dispositivo) {
        case 'movil':
            const div_main = scripting('DIV',['mb-2']);
            for(let i=0; i<localStorage.length; i++) {
                const key = localStorage.key(i);
                const producto = JSON.parse(localStorage.getItem(key));

                const { img, nombre, precio_venta, cantidad, personaliza } = producto;
                
                //Informacion del producto principal y 
                const div_producto = scripting('DIV',['d-flex','justify-content-between','align-items-center']);

                    //Información principal
                const div_info = scripting('DIV',['info-img-nombre-precio','d-flex','align-items-center','gap-2']);
                        //Imagen
                const div_info_img = scripting('DIV',['product-img']);
                const info_img = scripting('IMG');
                info_img.src = `${img}`;
                info_img.alt = `${nombre}`;

                div_info_img.appendChild(info_img);
                        //Cantidad y precio
                const div_info_cant_precio = scripting('DIV');
                const info_cantidad = scripting('P',[],`${cantidad} x ${key}`);
                const info_precio = scripting('P',[],`${precio_venta}`);

                div_info_cant_precio.appendChild(info_cantidad);
                div_info_cant_precio.appendChild(info_precio);   

                div_info.appendChild(div_info_img);
                div_info.appendChild(div_info_cant_precio);


                             //Actividades
                const div_actividades = scripting('DIV',['otros']);
                        //Div para los botones de más informacion y el boton de eliminar
                const div_info_eliminar = scripting('DIV',['d-flex','align-items-center','justify-content-around']);

                const button_eliminar = scripting('BUTTON',['eliminar-producto','boton-eliminar']);
                button_eliminar.type = "button";
                button_eliminar.name = `${key}`;

                button_eliminar.onclick = function() {
                    //Agregar funcionaldiad
                }


                const icono_eliminar = scripting('DIV',['icon-trash','d-flex','align-items-center']);
                icono_eliminar.innerHTML = 
                `<svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-trash" width="36"
                height="36" viewBox="0 0 24 24" stroke-width="1.5" stroke="#DB4200" fill="none"
                stroke-linecap="round" stroke-linejoin="round">
                <path stroke="none" d="M0 0h24v24H0z" fill="none" />
                    <line x1="4" y1="7" x2="20" y2="7" />
                    <line x1="10" y1="11" x2="10" y2="17" />
                    <line x1="14" y1="11" x2="14" y2="17" />
                    <path d="M5 7l1 12a2 2 0 0 0 2 2h8a2 2 0 0 0 2 -2l1 -12" />
                    <path d="M9 7v-3a1 1 0 0 1 1 -1h4a1 1 0 0 1 1 1v3" />
                </svg>`

                const icon_more = scripting('DIV',['icon-more']);
                const icon = scripting('i',['fa-solid','fa-caret-down']);
                icon_more.appendChild(icon);
                icon_more.onclick = mostrarAgregados;

                button_eliminar.appendChild(icono_eliminar);
                div_info_eliminar.appendChild(button_eliminar);
                div_info_eliminar.appendChild(icon_more);

                    //Botones para el manejo de las cantidades
                
                const div_cantidades = scripting('DIV',['d-flex','justify-content-center','align-items-center','gap-2','mt-2']);
                const button_disminuir = scripting('BUTTON',['botones-carrito','btn','border-0','w-auto'],'-');
                button_disminuir.onclick = function() {
                    //agregar funcionalidad
                }
                const botones_info_cantidad = scripting('P',[],`${cantidad}`)
                const button_aumentar = scripting('BUTTON',['botones-carrito','btn','border-0','w-auto'],'+');

                button_aumentar.onclick = function() {
                    //Agregar funcionalidad
                }
                div_cantidades.appendChild(button_disminuir);
                div_cantidades.appendChild(botones_info_cantidad);
                div_cantidades.appendChild(button_aumentar);


                //Agregamos los dos div de las actividades
                div_actividades.appendChild(div_info_eliminar);
                div_actividades.appendChild(div_cantidades);
                //Información del producto
                div_producto.appendChild(div_info);
                div_producto.appendChild(div_actividades);


                //Productos personalizacion

                const { agregar, combear, quitar, salsas} = personaliza;

                const div_productos_personalizacion = scripting('DIV',['info-producto']);
            
                const titulo_agregados = scripting('P',['fw-bold','text-uppercase','text-start'],'Se agregó');

                const titulo_quitados = scripting('P',['fw-bold','text-uppercase','text-start'],'Se quitó');
                
                const titulo_combos = scripting('P',['fw-bold','text-uppercase','text-start'],'Combos agregados');

                const titulo_salsas = scripting('P',['fw-bold','text-uppercase','text-start'],'Salsas');
                
                div_productos_personalizacion.appendChild(titulo_agregados);
                div_productos_personalizacion.appendChild(
                    productosPersonalizacion(agregar)
                )

                div_productos_personalizacion.appendChild(titulo_quitados);
                div_productos_personalizacion.appendChild(
                    productosPersonalizacion(quitar)
                )
                div_productos_personalizacion.appendChild(titulo_combos);
                div_productos_personalizacion.appendChild(
                    productosPersonalizacion(combear)
                )
                div_productos_personalizacion.appendChild(titulo_salsas);
                div_productos_personalizacion.appendChild(
                    productosPersonalizacion(salsas)
                )

                //Agregamos los dos div al main
                div_main.appendChild(div_producto);
                div_main.appendChild(div_productos_personalizacion);

                // content += 
                // `<div class="mb-2">
                //     <div class="d-flex justify-content-between align-items-center">
                //         <div class="info-img-nombre-precio d-flex align-items-center gap-2">
                //             <div class="product-img">
                //                 <img src=${producto.img} alt="Hamburguesa">
                //             </div>
                            
                //             <div>
                //                 <p>${producto.cantidad} x ${key}</p>
                //                 <p>${producto.precioVenta}</p>
                //             </div>
                            
                //         </div>
                //         <div class="otros">
                //             <div class="d-flex align-items-center justify-content-around">
                //                 <button type="button" name="${key}" class="eliminar-producto boton-eliminar">
                //                     <a href="" class="icon-trash d-flex align-items-center">
                //                         <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-trash" width="36"
                //                             height="36" viewBox="0 0 24 24" stroke-width="1.5" stroke="#DB4200" fill="none"
                //                             stroke-linecap="round" stroke-linejoin="round">
                //                             <path stroke="none" d="M0 0h24v24H0z" fill="none" />
                //                             <line x1="4" y1="7" x2="20" y2="7" />
                //                             <line x1="10" y1="11" x2="10" y2="17" />
                //                             <line x1="14" y1="11" x2="14" y2="17" />
                //                             <path d="M5 7l1 12a2 2 0 0 0 2 2h8a2 2 0 0 0 2 -2l1 -12" />
                //                             <path d="M9 7v-3a1 1 0 0 1 1 -1h4a1 1 0 0 1 1 1v3" />
                //                         </svg>
                //                     </a>
                //                 </button>
                //                 <div class="icon-more">
                //                     <i class="fa-solid fa-caret-down"></i>
                //                 </div>
                //             </div>
                            
                //             <div class="d-flex justify-content-center align-items-center gap-2 mt-2">
                //                 <button name="${key}" class="botones-carrito btn border-0 w-auto disminuir-cantidad">-</button>
                //                 <p>${producto.cantidad}</p>
                //                 <button name="${key}" class="botones-carrito btn border-0 w-auto aumentar-cantidad">+</button>
                //             </div>
        
                //         </div>
                //     </div>
                //     <div class="info-producto">
                //         <p class="fw-bold text-uppercase text-start">Se agregó</p>
                //         <ul class="lista-agregados">
                //         ${contentProductosPersonalizacion(producto,'agregar')}
                //         </ul>
                //         <p class="fw-bold text-uppercase text-start">Se quitó</p>
                //         <ul class="lista-agregados">
                //         ${contentProductosPersonalizacion(producto,'quitar')}
                //         </ul>
                //         <p class="fw-bold text-uppercase text-start">Combos agregados</p>
                //         <ul class="lista-agregados">
                //         ${contentProductosPersonalizacion(producto,'combear')}
                //         </ul>
                //         <p class="fw-bold text-uppercase text-start">Salsas</p>
                //         <ul class="lista-agregados">
                //         ${contentProductosPersonalizacion(producto,"salsas")}
                //         </ul>
                //     </div>
                // </div>`
            }
            
            return div_main;
        case 'pc':
            //Armamos la tabla base
            const table = scripting('TABLE',['productos-table','table','mt-2']);
            const thead = scripting('THEAD');
            const tr = scripting('TR');
            const td_productos = scripting('TD',['text-center','productos-carrito'],'Productos');
            const td_precio = scripting('TD',['text-center','productos-carrito'],'Precio por unidad');
            const td_cantidad = scripting('TD',['text-center','productos-carrito'],'Cantidad');
            const td_subtotal = scripting('TD',['text-center','productos-carrito'],'Subtotal');

            tr.appendChild(td_productos);
            tr.appendChild(td_precio);
            tr.appendChild(td_cantidad);
            tr.appendChild(td_subtotal);

            thead.appendChild(tr);
            table.appendChild(thead);

            const tbody = scripting('TBODY',['productos-carrito-table']);

            table.appendChild(tbody);

            for(let i=0; i<localStorage.length; i++) {
                const key = localStorage.key(i);
                const producto = JSON.parse(localStorage.getItem(key));

                const { nombre, precio_producto, img, personaliza } = producto;
                const { agregar, combear, quitar, salsas} = personaliza;
                content += `
                    <tr>
                        <td class="d-flex gap-2 justify-content-center">
                            <div>
                                <img src="${img}" alt="Hamburguesa">
                            </div>
                            <div>
                                <h3 class="fs-6">${key}</h3>
                                <div class="text-center"> 
                                    <p class="fw-bold text-uppercase text-start">Se agregó</p>
                                    ${productosPersonalizacion(agregar)}
                                    <p class="fw-bold text-uppercase text-start">Se quitó</p>
                                    ${productosPersonalizacion(quitar)}
                                    <p class="fw-bold text-uppercase text-start">Combos agregados</p>
                                    ${productosPersonalizacion(combear)}
                                    <p class="fw-bold text-uppercase text-start">Salsas</p>
                                    ${productosPersonalizacion(salsas)}
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
                            <p class="d-flex align-items-center justify-content-center" style="height: 100px;">S/. ${precio_producto}</p>
                        </td>
                        <td>
                            <div class="d-flex justify-content-center align-items-center gap-2" style="height: 100px;">
                                <button name="${key}" class="botones-carrito btn border-0 w-auto disminuir-cantidad">-</button>
                                    <p>${cantidad}</p>
                                <button name="${key}" class="botones-carrito btn border-0 w-auto aumentar-cantidad">+</button>
                            </div>
                        </td>
                        <td>
                            <p class="d-flex justify-content-center align-items-center" style="height: 100px;">S/. ${precio_venta}</p>
                        </td>
                    </tr>`

                tbody.innerHTML += content;
            }

            

            main_productos_carrito.insertBefore(table, btn_vaciar_carrito);
        break;
    } 
}
function sumaCarrito() {
    let suma = 0;
    for(let i=0; i<localStorage.length; i++) {
        const key = localStorage.key(i);
        suma += JSON.parse(localStorage.getItem(key)).precioVenta;
    }
    return suma;
}

function productosPersonalizacion(tipo_personalizacion) {
    const lista_quitados = scripting('UL',['lista-agregados']);

    tipo_personalizacion.forEach( producto => {
        const { nombre, precio } = producto;
        
        const li = scripting('LI');
        const p = scripting('P');

        p.textContent = precio !== null ? `${nombre} - S/. ${precio}` :`${nombre}`; 
        
        li.appendChild(p);
        lista_quitados.appendChild(li);
    })

    return lista_quitados;
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



mostrarDatos();
mostrarProductosFinalizar();
finalizarCompra();

function mostrarDatos() {
    const info = JSON.parse(sessionStorage.getItem(0));
    const tipo_entrega = info.tipoEntrega;
    const info_compra = document.querySelector('.info-compra');
    let content = '';
    if(tipo_entrega == 'Delivery') {
        content = `
            <p class="fw-bold fs-6">Forma de entrega: <span class="fs-6 fw-normal">${tipo_entrega}</span></p>
            <p class="fw-bold fs-6">Dirección de entrega: <span class="fs-6 fw-normal">${info.direccion}</span></p>
        `;
    } else {
        content = `
        <p class="fw-bold fs-6">Forma de entrega: <span class="fs-6 fw-normal">${tipo_entrega}</span></p>
        <p class="fw-bold fs-6">Tienda para tu pedido:</p>
        <ul>
            <li><p class="fs-6 fw-bold ms-4">Distrito: <span class="fs-6 fw-normal">${info.distrito}</span></p></li>
            <li><p class="fs-6 fw-bold ms-4">Dirección: <span class="fs-6 fw-normal">${info.direccion}</span></p></li>
        </ul>
    `;
    }
    info_compra.innerHTML = content;
}

function mostrarProductosFinalizar() {
    const productos_fin = document.querySelector('.productos-pag-compra');
    const resumen = document.querySelector('.resumen-costos-fin');
    const subtotal = sumaCarrito();
    const igv = Math.round((subtotal * 0.18)*100)/100;
    const total = subtotal + igv;
    let content = '';
    for(let i=0; i<localStorage.length; i++) {
        const key = localStorage.key(i);
        const producto = JSON.parse(localStorage.getItem(key));
        content += `
        <div class="mb-2 p-2">
            <div class="d-flex justify-content-between align-items-center">
                <div class="info-img-nombre-precio d-flex align-items-center gap-2">
                    <div class="product-img">
                        <img src=${producto.img} alt="Hamburguesa">
                    </div>
                    
                    <div>
                        <h4>${key}</h4>
                        <div>
                            <div class="row">
                                <div class="col-6">
                                    <p class="fw-bold text-uppercase text-start">Se agregó</p>
                                    <ul class="lista-agregados">
                                    ${contentProductosPersonalizacion(producto,'agregar')}
                                    </ul>
                                </div>
                                <div class="col-6">
                                    <p class="fw-bold text-uppercase text-start">Se quitó</p>
                                    <ul class="lista-agregados">
                                    ${contentProductosPersonalizacion(producto,'quitar')}
                                    </ul>
                                </div>
                            </div>
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
                </div>
                <p>Cant. ${producto.cantidad}</p>
                <p>S/. ${producto.precioVenta}</p>
            </div> 
        </div>`
    }
    productos_fin.innerHTML = content;
    resumen.innerHTML = `
    <h4 class="text-start fs-5 mb-2">SubTotal: <span class="fs-5">S/. ${subtotal}</span></pan></h4>
    <h4 class="text-start fs-5 mb-2">IGV: <span class="fs-5">S/. ${igv}</span></h4>
    <h4 class="text-start fs-5">Total: <span class="fs-5">S/. ${total}</span></h4>
    `
}
function finalizarCompra() {
    const finalizar = document.getElementById('btn-finalizar-compra');
    finalizar.addEventListener('click', e => {
        const tarjeta = document.getElementById('tarjeta').checked;
        const aplicativo = document.getElementById('aplicativo').checked;
        if(tarjeta == false && aplicativo == false) {
            e.preventDefault();
            const m_pago = document.querySelector('.metodo-pago');
            m_pago.innerHTML += `<p class="elija-uno text-uppercase fw-bold fs-5">Elija un método de pago</p>`;
        } else {
            const obj = JSON.parse(sessionStorage.getItem(0));
            const modal = document.querySelector('.modal-fin-compra');
            e.preventDefault();
            tarjeta == true ? obj.metodo_pago = 'Tarjeta' : obj.metodo_pago = 'Aplicativo móvil';
            let content = `<div class="modal fade modal-fin-compra" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                    <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                        <h5 class="modal-title" id="exampleModalLabel">FINALICE SU COMPRA</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div class="modal-body">
                        <p>Método de pago: ${obj.metodo_pago}</p>
                        <p>Total: ${sumaCarrito() + Math.round(sumaCarrito()*0.18*100)/100}</p>
                        </div>
                        <div class="modal-footer">
                        <button type="button" class="btn btn-primary border-0 compra-finalizada-pagada"><a href="index.html">Comprar</a></button>
                        </div>
                    </div>
                    </div>
                </div>`; 
            modal.innerHTML = content;
            sessionStorage.setItem(0,JSON.stringify(obj));
        }
        compraFinalizada();
    })
}

function compraFinalizada() {
    const button_fin = document.querySelector('.compra-finalizada-pagada');
    button_fin.addEventListener('click', () => {
        localStorage.clear();
        sessionStorage.clear();
    })
}
let objInfo;
const delivery = document.getElementById('delivery');
const recojo = document.getElementById('recojo-tienda');

if (delivery != null) {
    delivery.addEventListener('click', e => {
        const direccion = document.getElementById('direccion').value;
        sessionStorage.setItem(0, JSON.stringify(
            {
                'tipoEntrega': 'Delivery',
                'direccion': direccion,
                'metodo_pago': null
            }
        ))
    });

}
if (recojo != null) {
    recojo.addEventListener('click', e => {
        const distrito = document.querySelector('.distrito-recojo').textContent;
        const direccion = document.querySelector('.direccion-recojo').textContent;
        sessionStorage.setItem(0, JSON.stringify(
            {
                'tipoEntrega': 'Recojo en tienda',
                'distrito': distrito,
                'direccion': direccion,
                'metodo_pago': null
            }
        ))
    })
}
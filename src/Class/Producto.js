class Producto {

    constructor(nombre,precio_producto,img,agregar,combear,quitar,salsas,)  {
        nombre = this.nombre;
        precio_producto = this.precio_producto;
        precio_venta = 0;
        cantidad = 1;
        img = this.img;
        personaliza = {
            agregar: agregar,
            combear: combear,
            quitar: quitar,
            salsas: salsas
        }
    }

    guardarDatos() {
        if(localStorage.getItem(this.nombre) == null) {
            this.precio_venta = this.precioVenta();
            console.log(this.precio_venta);
            localStorage.setItem(this.nombre, JSON.stringify(this
                // {
                //     'precioProducto': precio_p,
                //     'precioVenta': Math.round((precio_p + precioCombos(combear) + precioAgregar(agregar))*100)/100,
                //     'cantidad': 1,
                //     'img': imagen_producto,
                //     'personaliza': {
                //         'agregar': agregar,
                //         'quitar': quitar,
                //         'combear': combear,
                //         'salsas': salsas
                //     }
                // }
            ));

        }
    }

    precioVenta() {
        return Math.round((this.precio_producto + this.precioCombos() + this.precioAgregar())*100)/100
    }

    precioCombos() {
        const { combear } = this.personaliza;
        let suma=0;
        for(let i=0; i<combear.length; i++) {
            suma += Math.round(parseFloat(combear[i].precio)*100)/100;
        }
        return suma;
    }

    precioAgregar() {
        const { agregar } = this.personaliza;
        let suma=0;
        for(let i=0; i <agregar.length; i++) {
            suma += Math.round(parseFloat(agregar[i].precio)*100)/100;
        }
        return suma;
    }
}

export { Producto }
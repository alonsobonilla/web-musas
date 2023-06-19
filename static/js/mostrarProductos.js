const productos = document.querySelector(".productos-carrito");
let mapCremas = new Map();

window.addEventListener("DOMContentLoaded", async () => {
  await obtenerCremas();
  mostrarProductos();
});

async function mostrarProductos() {
  limpiarHijos();

  for (let i = 0; i < localStorage.length; i++) {
    const key = localStorage.key(i);
    const producto = JSON.parse(localStorage.getItem(key));

    const div = document.createElement("div");
    const divInformacion = document.createElement("div");
    const divModificaciones = document.createElement("div");
    const divCremas = document.createElement("div");
    const listaCremas = document.createElement("ul");
    const precio = document.createElement("p");
    const nombre = document.createElement("p");
    const cantidad = document.createElement("p");
    const precioTotal = document.createElement("p");
    const divCantidades = document.createElement("div");
    const botonEliminar = document.createElement("button");
    const botonSuma = document.createElement("button");
    const botonResta = document.createElement("button");

    const idCremas = producto.cremas;
    listaCremas.classList.add("d-flex", "gap-2");
    const p = document.createElement("p");
    p.textContent = "Cremas: ";
    p.classList.add("fw-bold");
    idCremas.forEach((id) => {
      const li = document.createElement("li");
      const p = document.createElement("p");
      p.textContent = mapCremas.get(id);
      li.appendChild(p);
      listaCremas.appendChild(li);
    });
    divCremas.appendChild(p);
    divCremas.appendChild(listaCremas);

    precio.textContent = `Precio unidad: ${producto.precio}`;
    nombre.textContent = producto.nombre;
    cantidad.textContent = producto.cantidad;
    precioTotal.textContent = `Precio total: ${producto.precioTotal}`;
    botonEliminar.textContent = "Eliminar";
    botonSuma.textContent = "+";
    botonResta.textContent = "-";

    botonEliminar.classList.add("btn", "btn-danger");
    botonEliminar.onclick = () => {
      localStorage.removeItem(key);
      mostrarProductos();
    };
    botonSuma.classList.add("btn", "btn-success");
    botonSuma.onclick = () => {
      producto.cantidad += 1;
      producto.precioTotal = producto.precio * producto.cantidad;
      localStorage.setItem(key, JSON.stringify(producto));
      mostrarProductos();
    };
    botonResta.classList.add("btn", "btn-success");
    botonResta.onclick = () => {
      producto.cantidad -= 1 ? producto.cantidad > 1 : 1;
      producto.precioTotal = producto.precio * producto.cantidad;
      localStorage.setItem(key, JSON.stringify(producto));
      mostrarProductos();
    };

    divCantidades.classList.add("d-flex", "align-items-center", "gap-2");
    div.classList.add(
      "d-flex",
      "gap-2",
      "align-items-center",
      "justify-content-around",
      `producto-carrito-${key}`
    );

    precio.classList.add("precio");
    nombre.classList.add("nombre");
    cantidad.classList.add("cantidad");
    precioTotal.classList.add("precioTotal");

    divInformacion.appendChild(nombre);
    divInformacion.appendChild(precio);
    divInformacion.appendChild(precioTotal);
    divInformacion.appendChild(divCremas);

    divCantidades.appendChild(botonResta);
    divCantidades.appendChild(cantidad);
    divCantidades.appendChild(botonSuma);

    divInformacion.appendChild(divCantidades);
    divModificaciones.appendChild(botonEliminar);

    div.appendChild(divInformacion);
    div.appendChild(divModificaciones);
    productos.appendChild(div);
  }
}

function limpiarHijos() {
  while (productos.firstChild) {
    productos.removeChild(productos.firstChild);
  }
}

async function obtenerCremas() {
  const url = "http://127.0.0.1:5000/get_productos_categoria/3";

  try {
    const accesToken = await fetch("http://127.0.0.1:5000/auth", {
      method: "POST",
      body: JSON.stringify(autorizacion),
      headers: {
        "Content-Type": "application/json",
      },
    });
    const token = await accesToken.json();

    const response = await fetch(url, {
      headers: {
        Authorization: `JWT ${token.access_token}`,
      },
    });
    const data = await response.json();

    data.productos.forEach((crema) => {
      mapCremas.set(crema.idProducto, crema.nombre);
    });
  } catch (error) {
    console.log(error);
  }
}

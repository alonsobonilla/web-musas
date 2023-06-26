import { obtenerCremas } from "./fetchApis.js";
import { IDCATEGORIACREMAS, SERVER, mapCremas } from "./variables.js";
const productos = document.querySelector(".productos-carrito");
const vaciar = document.querySelector("#vaciar-carrito");

window.addEventListener("DOMContentLoaded", async () => {
  await obtenerCremas(SERVER, IDCATEGORIACREMAS, mapCremas);
  mostrarProductos();
});

vaciar.addEventListener("click", () => {
  localStorage.clear();
  mostrarProductos();
});

async function mostrarProductos() {
  limpiarHijos();

  for (let i = 0; i < localStorage.length; i++) {
    const key = localStorage.key(i);
    const producto = JSON.parse(localStorage.getItem(key));

    const div = document.createElement("div");
    const divImagen = document.createElement("div");
    const img = document.createElement("img");
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
    listaCremas.classList.add("d-flex", "gap-2", "justify-content-center");
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

    divCantidades.classList.add(
      "d-flex",
      "align-items-center",
      "gap-2",
      "justify-content-center",
      "mb-3"
    );
    div.classList.add(
      "row",
      "align-items-center",
      "justify-content-around",
      `producto-carrito-${key}`
    );
    divInformacion.classList.add("col-md-4", "text-center");
    divModificaciones.classList.add("col-md-4", "text-center");
    divImagen.classList.add("col-md-4", "text-center");
    img.src = "/static/img/hamburguesas/h-2.jpg";
    img.alt = "Imagen de la hamburguesa";
    img.style.width = "200px";

    precio.classList.add("precio");
    nombre.classList.add("nombre", "fw-bold", "fs-6");
    cantidad.classList.add("cantidad");
    precioTotal.classList.add("precioTotal");

    divInformacion.appendChild(nombre);
    divInformacion.appendChild(precio);
    divInformacion.appendChild(precioTotal);
    divInformacion.appendChild(divCremas);
    divImagen.appendChild(img);

    divCantidades.appendChild(botonResta);
    divCantidades.appendChild(cantidad);
    divCantidades.appendChild(botonSuma);

    divInformacion.appendChild(divCantidades);
    divModificaciones.appendChild(botonEliminar);

    div.appendChild(divImagen);
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

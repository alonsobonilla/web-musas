import { IDCATEGORIACREMAS, SERVER, mapCremas } from "./config.js";
import { obtenerCremas } from "./fetchApis.js";
const containerProductos = document.querySelector(".productos-comprar");

document.addEventListener("DOMContentLoaded", async () => {
  await obtenerCremas(SERVER, IDCATEGORIACREMAS, mapCremas);
  showProductos();
});

function showProductos() {
  for (let i = 0; i < localStorage.length; i++) {
    const key = localStorage.key(i);
    const producto = JSON.parse(localStorage.getItem(key));

    const div = document.createElement("div");
    const divImagen = document.createElement("div");
    const img = document.createElement("img");
    const divInformacion = document.createElement("div");
    const divCremas = document.createElement("div");
    const listaCremas = document.createElement("ul");
    const precio = document.createElement("p");
    const nombre = document.createElement("p");
    const cantidad = document.createElement("p");
    const precioTotal = document.createElement("p");

    listaCremas.classList.add("d-flex", "gap-2");
    const p = document.createElement("p");
    p.textContent = "Cremas: ";
    p.classList.add("fw-bold");
    const idCremas = producto.cremas;

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
    cantidad.textContent = `Cantidad: ${producto.cantidad}`;
    precioTotal.textContent = `Precio total: ${producto.precioTotal}`;

    div.classList.add(
      "d-flex",
      "gap-2",
      "align-items-center",
      "justify-content-center",
      `producto-carrito-${key}`,
      "mb-3"
    );

    precio.classList.add("precio");
    nombre.classList.add("nombre", "fw-bold", "fs-6", "text-center");
    cantidad.classList.add("cantidad");
    precioTotal.classList.add("precioTotal");

    divImagen.classList.add("w-50", "text-center");
    img.src = "/static/img/hamburguesas/h-2.jpg";
    img.alt = "Imagen de la hamburguesa";
    img.style.width = "200px";

    divInformacion.appendChild(nombre);
    divInformacion.appendChild(precio);
    divInformacion.appendChild(cantidad);
    divInformacion.appendChild(precioTotal);
    divInformacion.appendChild(divCremas);
    divImagen.appendChild(img);

    div.appendChild(divImagen);
    div.appendChild(divInformacion);
    containerProductos.appendChild(div);
  }
}

import { SERVER } from "./config.js";
import { transaccionCompra } from "./fetchApis.js";
const btnComprar = document.querySelector("#comprar-producto");
btnComprar.addEventListener("click", comprarProductos);

async function comprarProductos(e) {
  e.preventDefault();
  const dni = document.querySelector("#dni").value;
  const nombres = document.querySelector("#nombres").value;
  const telefono = document.querySelector("#telefono").value;
  const horaRecojo = document.querySelector("#hora-recojo").value;
  const checkboxes = document.querySelectorAll("input[type=checkbox]");
  const boleta = checkboxes[0].checked;
  const billeteraDigital = checkboxes[1].checked;
  let id = document.querySelector("#idUsuario");
  if (id) {
    id = id.value;
  }
  const datosPedido = {
    idUsuario: id ? id : "",
    dniNoRegistrado: dni,
    nombres,
    telefono,
    horaRecojo,
    estadoBoleta: boleta,
    billeteraDigital,
  };
  const productos = arregloProductos();
  const objetoTransaccion = {
    datosPedido,
    productos,
  };
  console.log(objetoTransaccion);
  const rpta = await transaccionCompra(objetoTransaccion);
  console.log(rpta);
  if (rpta.status == "1") {
    guardarPedidos();
    localStorage.clear();
    alert("Compra realizada con éxito");
    window.location.href = `${SERVER}/`;
  }
}
function guardarPedidos() {
  const listaPedidos = [];
  for (let i = 0; i < localStorage.length; i++) {
    const key = localStorage.key(i);
    const pedido = localStorage.getItem(key);

    listaPedidos.push(pedido);
  }
  localStorage.setItem("mis_pedidos", JSON.stringify(listaPedidos));
  console.log(listaPedidos);
}
function arregloProductos() {
  const productos = [];

  for (let i = 0; i < localStorage.length; i++) {
    const key = localStorage.key(i);
    const producto = JSON.parse(localStorage.getItem(key));
    productos.push(producto);
  }

  return productos;
}

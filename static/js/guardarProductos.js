const agregarCarrito = document.querySelector("#agregar-carrito");
const cremas = document.querySelectorAll("input[type=checkbox]");
const autorizacion = {
  username: "grupo5",
  password: "grupo5",
};

let id;
let url;
let cremasElegidas = [];
if (agregarCarrito) {
  agregarCarrito.addEventListener("click", (e) => {
    id = window.location.href.split("/").pop();
    url = `http://dawgrupo5.pythonanywhere.com/get_producto/${id}`;

    //obtengo las cremas elegidas
    cremas.forEach((crema) => {
      if (crema.checked) {
        cremasElegidas.push(parseInt(crema.value));
      }
    });
    obtener_data_producto();
  });
}

async function obtener_data_producto() {
  try {
    const accesToken = await fetch("http://dawgrupo5.pythonanywhere.com/auth", {
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
    guardar_data_carrito(data);
  } catch (error) {
    console.log(error);
  }
}

function guardar_data_carrito(data) {
  const id = localStorage.length + 1;

  const { idProducto, idCategoria, nombre, descripcion, precio, existencias } =
    data.producto;

  const obj = {
    idProducto: idProducto,
    idCategoria: idCategoria,
    nombre: nombre,
    descripcion: descripcion,
    precio: precio,
    existencias: existencias,
    imagen: "",
    cantidad: 1,
    precioTotal: precio,
    cremas: cremasElegidas,
  };

  localStorage.setItem(id, JSON.stringify(obj));
  cremasElegidas = [];
}

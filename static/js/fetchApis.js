const datosAutorizacion = {
  username: "grupo5",
  password: "grupo5",
};

let token;

async function obtenerCremas(SERVER, IDCATEGORIACREMAS, mapCremas) {
  const url = `${SERVER}/get_productos_categoria/${IDCATEGORIACREMAS}`;

  try {
    await autorizacion(SERVER);
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

async function transaccionCompra(SERVER, datosTransaccion) {
  const url = `${SERVER}/transaccion_compra`;

  try {
    await autorizacion(SERVER);
    const response = await fetch(url, {
      method: "POST",
      body: JSON.stringify(datosTransaccion),
      headers: {
        "Content-Type": "application/json",
        Authorization: `JWT ${token.access_token}`,
      },
    });
    return response.json();
  } catch (error) {
    console.log(error);
  }
}

async function autorizacion(SERVER) {
  try {
    const accesToken = await fetch(`${SERVER}/auth`, {
      method: "POST",
      body: JSON.stringify(datosAutorizacion),
      headers: {
        "Content-Type": "application/json",
      },
    });
    token = accesToken.json();
  } catch (error) {
    console.log(error);
  }
}
export { obtenerCremas, transaccionCompra };

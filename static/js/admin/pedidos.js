import { transaccionComprobante } from "../fetchApis.js";
const btnpedido = document.querySelectorAll("#btn-recogido");

if (btnpedido) {
  btnpedido.forEach((btn) => {
    btn.addEventListener("click", async (e) => {
      e.preventDefault();
      const id = document.querySelector("#idPedido").value;
      const key = document.querySelector("#keyPedido").value;

      const datosTransaccion = {
        idPedido: id,
        keyPedido: key,
      };

      const response = await transaccionComprobante(datosTransaccion);
      if (response.status == "1") {
        alert("Pedido confirmado");
        window.location.href = `/admin/pedidos`;
      } else {
        alert("Error al confirmar pedido");
      }
    });
  });
}

document.addEventListener("DOMContentLoaded", () => {
  categoriasFija();
});

function categoriasFija() {
  const breakPoint = document.querySelector(".categorias-content");

  const categorias_lista = document.querySelector(".categorias");

  window.addEventListener("scroll", () => {
    // console.log(breakPoint.getBoundingClientRect());
    const aviso = breakPoint.getBoundingClientRect().y;

    if (aviso < 30) {
      categorias_lista.classList.add("fijo");
    } else {
      categorias_lista.classList.remove("fijo");
    }
  });
}

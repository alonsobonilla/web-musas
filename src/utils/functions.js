function scripting(etiqueta, clases = [], mensaje,) {
    const crearEtiqueta = document.createElement(etiqueta);
    if(clases.length != 0) {
        clases.forEach( clase => {
            crearEtiqueta.classList.add(clase);
        });
    }
    if(mensaje)
        crearEtiqueta.textContent = mensaje;
    return crearEtiqueta;
}

export { scripting }
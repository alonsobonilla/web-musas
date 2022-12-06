
/**
 * Navegación movil
 */
const esDispositivoMovil = () => window.innerWidth <= 768;


if(esDispositivoMovil()) {
    const enlaces_nav = document.querySelector('.contenedor-nav');
    enlaces_nav.innerHTML = `${enlaces_nav.innerHTML} <div class="contenedor-nav contenedor-nav-hijo hidden-menu header-higth">
    <div class="contenedor-nav-top"><div class="nav-menu"><svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-x icon-close" width="40" height="40" viewBox="0 0 24 24" stroke-width="1.5" stroke="#FBD357" fill="none" stroke-linecap="round" stroke-linejoin="round">
    <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
    <line x1="18" y1="6" x2="6" y2="18" />
    <line x1="6" y1="6" x2="18" y2="18" />
    </svg><a href="index.html"><img src="img/logo.jpg" alt="Logo"></a></div><div class="nav-top-login"><a href="pag-inicio-sesion.html"><svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-user-circle" width="40" height="40" viewBox="0 0 24 24" stroke-width="1.5" stroke="#FBD357" fill="none" stroke-linecap="round" stroke-linejoin="round"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><circle cx="12" cy="12" r="9" /><circle cx="12" cy="10" r="3" /><path d="M6.168 18.849a4 4 0 0 1 3.832 -2.849h4a4 4 0 0 1 3.834 2.855" /></svg></a><p>Inicia sesión o crea tu cuenta</p></div>
    </div><button><a href="pag-carrito-compras.html"><svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-shopping-cart" width="40" height="40" viewBox="0 0 24 24" stroke-width="1.5" stroke="#FBD357" fill="none" stroke-linecap="round" stroke-linejoin="round"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><circle cx="6" cy="19" r="2" /><circle cx="17" cy="19" r="2" /><path d="M17 17h-11v-14h-2" /><path d="M6 5l14 1l-1 7h-13" /></svg></a>
    </button>
    </div>`;
    const header_nav = document.querySelector('.contenedor-nav-hijo');
    const menu_despegable = document.querySelector('.nav-menu-despegable');
    const icon_close = document.querySelector('.icon-close');
    const icon_open = document.querySelector('.icon-open');

    icon_close.addEventListener('click', () => {

        //Removemos animaciones
        header_nav.classList.remove('animate__fadeInRight');
        menu_despegable.classList.remove('animate__fadeInRight');

        //Ocultamos el menu con transform:translate al 100%
        header_nav.classList.add('hidden-menu');
        menu_despegable.classList.add('hidden-menu');
        //Añadimos clases de animación para el cierre del menu
        header_nav.classList.add('animate__animated','animate__fadeOutRight');
        menu_despegable.classList.add('animate__animated','animate__fadeOutRight');
        //Barra de navegación visible
        document.querySelector('body').style.overflow = 'visible';
    });

    icon_open.addEventListener('click', () => {
        
        //Removemos clases de animación de salida 
        if(header_nav.classList.contains('animate__fadeOutRight','animate__fadeOutRight')) {
            header_nav.classList.remove('animate__fadeOutRight');
            menu_despegable.classList.remove('animate__fadeOutRight');
        } 
        //Mostramos el menu con transform: translate 0
        header_nav.classList.add('activo');
        menu_despegable.classList.add('activo');
        //Añadimos clases de anmiación de entrada
        header_nav.classList.add('animate__animated','animate__fadeInRight');
        menu_despegable.classList.add('animate__animated','animate__fadeInRight');
        //Barra de navegación oculta
        document.querySelector('body').style.overflow = 'hidden';
    });

    /**
     * Footer mobile
     */
    const atencion_cliente = document.querySelector('.atencion-cliente');

    atencion_cliente.addEventListener('click', () => {
        if(atencion_cliente.classList.contains('active')) {
            atencion_cliente.classList.remove('active');
        } else {
            atencion_cliente.classList.add('active');
        }
    }); 


} else {
    const nav_main = document.querySelector('.nav-main');
    
    nav_main.innerHTML = `${nav_main.innerHTML} 
    <a href="pag-carrito-compras.html">
    <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-shopping-cart" width="36" height="36" viewBox="0 0 24 24" stroke-width="1.5" stroke="#DB4200" fill="none" stroke-linecap="round" stroke-linejoin="round">
    <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
    <circle cx="6" cy="19" r="2" />
    <circle cx="17" cy="19" r="2" />
    <path d="M17 17h-11v-14h-2" />
    <path d="M6 5l14 1l-1 7h-13" /></svg>
    </a>`;
    nav_main.classList.add('d-flex'); 
}

const btn_vaciar_carrito = document.querySelector('.btn-vaciar-carrito');
const btn_sec_carrito = document.querySelector('.botones-sec-carrito');
if( btn_vaciar_carrito != null && btn_sec_carrito != null && localStorage.length != 0) {
    btn_vaciar_carrito.classList.add('d-block');
    btn_sec_carrito.classList.add('mostrar');
}


// function quitarEfectos(widtPag) {
//     if(widtPag > 768) {  
//         header_nav.classList.remove('animate__animated','animate__fadeOutRight');
//         menu_despegable.classList.remove('animate__animated','animate__fadeOutRight');

//         header_nav.classList.add('hidden-menu');
//         menu_despegable.classList.add('hidden-menu');
//     }else {
        
//     }
// }

// window.onload = () => {
//     window.onresize = () => {
//         console.log(window.innerWidth);
//         quitarEfectos(window.innerWidth);
//     }
// }

const triggerTabList = document.querySelectorAll('#myTab a')
const agregar = triggerTabList[0];
const quitar = triggerTabList[1];
triggerTabList.forEach(triggerEl => {
    const tabTrigger = new bootstrap.Tab(triggerEl);
    triggerEl.addEventListener('click', event => {
        event.preventDefault();
        const enlace = event.target.parentElement.attributes[0].textContent;
        console.log(enlace);
        
        if(enlace == agregar.attributes[0].textContent) {
            agregar.classList.add('border-bottom-personalizar');
            quitar.classList.remove('border-bottom-personalizar');
        } else {
            agregar.classList.remove('border-bottom-personalizar');
            quitar.classList.add('border-bottom-personalizar');
        }
        tabTrigger.show()
    })
})
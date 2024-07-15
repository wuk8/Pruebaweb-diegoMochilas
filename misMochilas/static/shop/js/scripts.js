document.addEventListener('DOMContentLoaded', () => {
    // Selecciona el formulario y el botón "Enviar"
    const form = document.getElementById('formularioContacto');

    // Añade un event listener al formulario para manejar el envío
    form.addEventListener('submit', (event) => {
        event.preventDefault(); // Previene el envío del formulario
        if (validarFormulario()) { // Valida el formulario
            form.submit(); // Envía el formulario si es válido
        }
    });

    // Función para validar el formulario
    function validarFormulario() {
        // Obtiene los valores de los campos del formulario
        const rut = document.getElementById('rut').value.trim();
        const nombre = document.getElementById('nombre').value.trim();
        const direccion = document.getElementById('direccion').value.trim();
        const puesto = document.getElementById('puesto').value.trim();
        const sexo = document.getElementById('sexo').value;
        const telefono = document.getElementById('telefono').value.trim();
        const ocupacion = document.getElementById('ocupacion').value.trim();

        // Expresión regular para validar RUT
        const rutValido = /^\d{9,10}$/; // RUT debe tener entre 9 y 10 dígitos

        // Validaciones de cada campo
        if (!rutValido.test(rut)) {
            alert('RUT inválido. Debe tener entre 9 y 10 dígitos y solo números.');
            return false;
        }
        if (!nombre.match(/^[a-zA-Z\s]+$/) || nombre.length < 3 || nombre.length > 20) {
            alert('El nombre debe tener entre 3 y 20 caracteres y solo debe contener letras.');
            return false;
        }
        if (!direccion.match(/^[a-zA-Z\s]+$/) || direccion.length < 3 || direccion.length > 40) {
            alert('Dirección inválida. Debe tener entre 3 y 40 caracteres y solo debe contener letras.');
            return false;
        }
        if (!puesto.match(/^[a-zA-Z\s]+$/) || puesto.length < 3 || puesto.length > 20) {
            alert('Puesto inválido. Debe tener entre 3 y 20 caracteres y solo debe contener letras.');
            return false;
        }
        if (!sexo) {
            alert('Debe seleccionar un género.');
            return false;
        }
        if (!telefono.match(/^\d+$/) || telefono.length < 9 || telefono.length > 12) {
            alert('El teléfono debe tener entre 9 y 12 caracteres y solo debe contener números.');
            return false;
        }
        if (!ocupacion.match(/^[a-zA-Z\s]+$/)) {
            alert('Ocupación inválida. Solo debe contener letras.');
            return false;
        }

        // Si todo pasa, retorna true
        return true;
    }
});


// mochila

document.addEventListener('DOMContentLoaded', function() {
    // Escuchar clic en el botón "Agregar al Carrito" dentro del modal
    const addToCartButtons = document.querySelectorAll('.btn-confirm-purchase');
    
    addToCartButtons.forEach(button => {
        button.addEventListener('click', function() {
            const productId = this.getAttribute('data-product-id');
            const cantidadInput = document.getElementById(`cantidad${productId}`);
            const cantidad = cantidadInput.value;
            
            // Realizar la solicitud Ajax
            fetch('/comprar/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify({
                    producto_id: productId,
                    cantidad: cantidad
                })
            })
            .then(response => {
                if (!response.ok) {
                    throw Error(response.statusText);
                }
                return response.json();
            })
            .then(data => {
                // Manejar la respuesta del servidor (opcional)
                console.log('Compra realizada con éxito:', data);
                alert('Mochila agregada al carrito correctamente.');
            })
            .catch(error => {
                console.error('Error al realizar la compra:', error);
                alert('Hubo un problema al agregar la mochila al carrito.');
            });
        });
    });

    // Función para obtener el valor del token CSRF
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});

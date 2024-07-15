# diegoMochilas

## Descripción del Proyecto

diegoMochilas es una aplicación web desarrollada como parte de un proyecto académico para la creación de una tienda en línea de mochilas. El proyecto sigue el patrón de diseño MVC (Modelo-Vista-Controlador) y utiliza Django como framework backend y Bootstrap para el frontend.

## Funcionalidades Principales

. **Catálogo de Productos**: Listado de mochilas disponibles para la venta.
. **Carrito de Compras**: Permite a los usuarios agregar compras
. **Formulario de Contacto**: Formulario para que los usuarios puedan contactarse con la tienda.
. **Formulario de Consulta de Servicios**: Formulario para consultar los servicios ofrecidos.
. **Validaciones de Formularios**: Validaciones en el frontend usando JavaScript y en el backend con Django.
. **Componentes UI**: Uso de componentes Bootstrap como carousel, navbar, modal, card, e imágenes.

1.
C:\>Pruebaweb 
Crear y activar un entorno virtual:  python -m venv env //// En Windows: env\Scripts\activate
Instalar Django y las dependencias del proyecto:

    
    pip install django
    

2. Realizar las migraciones de la base de datos:

    python manage.py makemigrate
    python manage.py migrate
    

3. Crear un superusuario para acceder al panel de administración:

    
    python manage.py createsuperuser
    

4. Ejecutar el servidor de desarrollo:

    
    python manage.py runserver
    

5. Acceder a la aplicación en el navegador:

    
    http://127.0.0.1:8000/


## Estructura del Proyecto

- `aplicaciones/`: Contiene las aplicaciones Django del proyecto.
    - `nuevos_servicios/`: Aplicación que maneja los formularios de contacto y consulta de servicios.
- `static/`: Archivos estáticos (CSS, JavaScript, imágenes).
- `templates/`: Plantillas HTML del proyecto.
- `manage.py`: Archivo de gestión del proyecto Django.

- **Realizado**:
    - 5 vistas terminadas.
    - Al menos un formulario web terminado con validaciones.
    - Al menos 2 funciones en JavaScript.
    - Validaciones de reglas de negocio con JavaScript.
    - Componentes extras no propuestos anteriormente.
    - Diseño corporativo (tipografía, colores de la empresa, logos).
    - Matriz de seguimiento.
    - Versionamiento con GitHub.

  **Desarrollo de Funcionalidades**:
    - Mantenedores dentro de la aplicación web.
    - Funciones necesarias para el correcto funcionamiento.
    - Reglas de negocio según el caso planteado.
    - Autenticación y autenticación.
    - Carrito de compras.
 
  ## Autor

Diego Norambuena

# Primer Entrega - Matias Vera
### Descripcion

 Proyecto simulando una web de Comercio Online, donde existen 3 modelos:
- Vendedor( nombre(char), DNI(int), email(email), contrasenia(char))
- Comprador( nombre(char), DNI(int), email(email), contrasenia(char), direccion_de_envio(char))
- Producto( titulo(char), descripcion(char), precio(int))

### Funcionamiento

Para ingresar al inicio se debe ingresar a   [localhost/ComercioOnline/inicio/][PlDb].
En la navbar encontramos 7 botones los caules se detallan a continuacion: 
| Boton | URL | Descripcion |
| ------ | ------ | ------ |
| Compra en San Juab | [localhost/ComercioOnline/inicio/][PlDb] | Nos lleva a la pagina de inicio.
| Buscar | [localhost/ComercioOnline/buscarproducto/][PlGh] | Sirve para  buscar productos segun el titulo.
| Crear Producto | [localhost/ComercioOnline/crearproducto/][PlGd] | Sirve para poder crear un producto determinado.
| Crear Comprador | [localhost/ComercioOnline/crearcomprador/][PlOd] | Sirve para poder crear un comprador.
| Crear Vendedor | [localhost/ComercioOnline/crearvendedor/][PlMe] | Sirve para poder crear un vendedor.
| Comprador | --- | Boton diseñado para usar mas adelante mediante sistema de autenticacion. No tiene funcionamiento.
| Vendedor | --- | Boton diseñado para usar mas adelante mediante sistema de autenticacion. No tiene funcionamiento.

### Detalles
A continuacion, se detallan algunos productos que pueden buscarse:
- Samsung - Devuelve 3 resultados
- Iphone - Devuelve 2 resultados
- Motorola - Devuelve 1 reesultado.
- En caso de no encontrar coincidencias, la pagina notifica esto.
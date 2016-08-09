Odoo - Generic Webservices Container
====================================

Este es un módulo técnico que provee servicios de consumisión y testeo para casi cualquier clase de
webservice.
Utilizado en conjunto con tu módulo, puede proveer una buena base que permita contener tus servidores externos. 
Por ejemplo:
Servidores o servicios de Factura Electrónica.
Actualización de monedas.
Servicios Freemium que usen APIs(Toggle, Todoist, etc)
SugarCRM o SuiteCRM
..o inclusive, otras instancias de Odoo.

##Características
Provee conectividad a interfaces RESTFUL
Puede leer JSON, y está preparado (aunque no implementado aún) para leer resultados en XML or HTML.
Es posible configurar diferentes tipos de métodos de autenticación (API, User/Password).
Puedes compartir tus claves API o usuario / contraseña con otros usuarios, o configurarlos en base
a cada usuario del sistema.

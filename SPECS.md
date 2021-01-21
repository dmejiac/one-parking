La Oficina Nacional de Estadística nos ha requerido el desarrollo de un sistema para gestionar la asignación de parqueos de la institución.

Principalmente nos solicitan los siguientes requerimientos funcionales:

1 - Mantenimiento de estacionamientos
    - Consulta disponibilidad de estacionamientos
2 - Mantenimiento de parqueos
3 - Mantenimiento de solicitudes
    - Asignación de estacionamientos
4 - Reporte de solicitudes pendientes
5 - Reporte de estacionamientos asignados por área organizacional

Además debemos seguir estos requerimientos no-funcionales:

1 - Los valores ingresados por el usuario deben validarse
2 - Evitar duplicidad de datos
3 - Gestionar las excepciones a la hora de capturar datos

Solución:

Atributos/Datos de Estacionamiento:

    - EstacionamientoID (int)
    - Numero (int)
    - UbicacionID (FK Parqueo - int)
    - Reservado (bool)
    - Disponibilidad (bool)

Atributos/Datos de Parqueo:

    - ParqueoID (int)
    - Descripcion (varchar(50))
    - Ubicacion (varchar(100))
    - TotalEstacionamientos (int)

Atributos/Datos de Solicitud:

    - SolicitudID (int)
    - Beneficiario (varchar(100))
        - Nombres
        - Apellidos
    - Identifiacion (long(11))
        - RNC
        - Cedula
    - Codigo (int)
    - Departamento (varchar(100))
    - TipoSolicitud (varchar(13))
        - Institucional
        - Personal
    - FechaSolicitud (date)
    - FechaAprobacion (date)
    - Estado (varchar(9))
        - Aprobada
        - Pendiente

Atributos/Datos de Vehiculo:

    - VehiculoID (int)
    - SolicitudID (FK Solicitud - int)
    - EstacionamientoID (FK Estacionamiento - int)
    - Marca (varchar(15))
    - Modelo (varchar(50))
    - Color (varchar(20))
    - Placa (varchar(6))
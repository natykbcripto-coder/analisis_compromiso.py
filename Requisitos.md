Requerimiento	Descripción	Entrada	Resultado
R1 - Datos iniciales	Crear matriz con datos de sesiones de clientes	Matriz de listas	Matriz con mínimo 5 registros (ID, Duración, Clics)
R2 – Módulos de clasificación	función que clasifique el nivel de compromiso de cada sesión	Duración (seg) y cantidad de clics	Retornar alto – medio – bajo según reglas definidas
R3 – Regla de compromiso alto	Clasificar como "Alto"	Duración y Clics	"Alto" si Duración > 180 Y Clics > 8
R4 – Regla de compromiso medio	Clasificar como "Alto"	Duración y Clics	"Medio" en todos los casos que no cumplan Alto ni Bajo
R5 – Regla de compromiso bajo	Clasificar como "Alto"	Duración y Clics	"Bajo" si Duración < 60 O Clics < 3
R6 - Generación de Informe	Mostrar un reporte final con la clasificación de cada cliente	Matriz completa de sesiones	Tabla en pantalla con: ID Cliente, Duración, Clics y Clasificación

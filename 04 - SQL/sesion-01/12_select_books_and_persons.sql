SELECT nombre_libro, nombre_persona
FROM "Libro" as Libro
INNER JOIN "Prestamo" as Prestamo ON Prestamo.id_libro = Libro.id_libro

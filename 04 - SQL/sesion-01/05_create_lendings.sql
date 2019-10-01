CREATE TABLE "Prestamo"
(
    id_prestamo integer NOT NULL,
    id_libro integer,
    nombre_persona varchar(256),
    fecha_inicio date,
    fecha_termino date,
    CONSTRAINT "Prestamo_pkey" PRIMARY KEY (id_prestamo),
    CONSTRAINT "Prestamo_id_libro_fkey" FOREIGN KEY (id_libro) REFERENCES "Libro" (id_libro)
);


CREATE TABLE "Libro"
(
    id_libro integer NOT NULL,
    nombre_libro varchar(256),
    autor varchar(256),
    genero varchar(256),
    CONSTRAINT "Libro_pkey" PRIMARY KEY (id_libro)
);

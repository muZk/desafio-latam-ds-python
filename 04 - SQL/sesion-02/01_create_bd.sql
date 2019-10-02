DROP DATABASE IF EXISTS Music;
DROP TABLE IF EXISTS Artista;
DROP TABLE IF EXISTS Cancion;
DROP TABLE IF EXISTS Album;

CREATE DATABASE Music ENCODING = 'UTF8';

CREATE TABLE Artista
(
    nombre_artista varchar(256),
    fecha_de_nacimiento date,
    nacionalidad varchar(256)
);

CREATE TABLE Cancion
(
    titulo_cancion varchar(256),
    artista varchar(256),
    album varchar(256),
    numero_del_track int
);

CREATE TABLE Album
(
    titulo_album varchar(256),
    artista varchar(256),
    anio int
);

COPY Album(titulo_album, artista, anio) FROM 'Album.csv' CSV DELIMITER ',' HEADER  ENCODING 'UTF8';
COPY Artista(nombre_artista, fecha_de_nacimiento, nacionalidad) FROM 'Artista.csv' CSV DELIMITER ',' HEADER  ENCODING 'UTF8';
COPY Cancion(titulo_cancion, artista, album, numero_del_track) FROM 'Cancion.csv' CSV DELIMITER ',' HEADER ENCODING 'UTF8';

SELECT titulo_cancion, Cancion.artista
FROM Cancion
LEFT JOIN Album ON titulo_album = album 
WHERE anio = 2018;

SELECT titulo_album, nacionalidad
FROM Album
INNER JOIN Artista ON artista = nombre_artista;

SELECT numero_del_track, titulo_cancion, titulo_album, anio, Cancion.artista
FROM Cancion
LEFT JOIN Album ON titulo_album = album
ORDER BY anio, album, artista;

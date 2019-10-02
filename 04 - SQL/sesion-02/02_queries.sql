SELECT titulo_cancion, Cancion.artista
FROM Cancion
LEFT JOIN Album ON titulo_album = album 
WHERE anio = 2018;

SELECT titulo_album, nacionalidad
FROM Album
LEFT JOIN Artista ON artista = nombre_artista 
WHERE anio = 2018;

SELECT numero_del_track, titulo_cancion, titulo_album, anio, Cancion.artista
FROM Cancion
LEFT JOIN Album ON titulo_album = album
ORDER BY anio, album, artista;

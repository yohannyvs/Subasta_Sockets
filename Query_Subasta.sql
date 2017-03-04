--Usuarios
insert into Usuarios values('Yohanny','Senryu','12345')

--Articulos
insert into Articulos values(1,'Computadora Personal',130000, 5, 'dsc dskc');
insert into Articulos values(1,'XBOX 360',150000, 5, 'dsc dskc');

--Selects
select * from Usuarios
select * from Articulos
SELECT Detalle, Precio, Tiempo, Imagen FROM Articulos
SELECT Detalle, Precio, Tiempo, Imagen FROM Articulos where Detalle Like '%o%'
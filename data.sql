create sequence  routeDetruitSeq START WITH 1 INCREMENT BY 1;
create sequence  materielSeq START WITH 1 INCREMENT BY 1;

create table typeRoad(
    id integer Primary key,
    value varchar(10)
);


CREATE VIEW RoadCoordinate AS
SELECT roadno, ST_X(ST_StartPoint(geom)) as latitude, ST_Y(ST_StartPoint(geom)) as longitude, ST_AsGeoJSON(geom) as geoJSON 
FROM route;

create table affaire(
    id integer default nextval('routeDetruitSeq'::regclass) NOT NULL PRIMARY KEY,
    puMetreCube DOUBLE PRECISION,
    dureeMetreCube bigint,
    typeRoad int,
    foreign key (typeRoad) references typeRoad(id)
);

create table PartieDetruit(
    id integer default nextval('routeDetruitSeq'::regclass) NOT NULL PRIMARY KEY,
    idRoute int,
    idAffaire int,
    pkDebut float8,
    pkEnd float8,
    niveau int,
    foreign key (idRoute) references madagascar_roads(gid),
    foreign key (idAffaire) references affaire(id)
);


insert into typeRoad values ( 1, 'goudron');
insert into typeRoad values ( 2, 'pave');
insert into typeRoad values ( 3, 'tany');
insert into typeRoad values ( 4, 'vato');

insert into affaire values ( default, 15000, 3000, 1);
insert into affaire values ( default, 10000, 2300, 2);
insert into affaire values ( default, 2000, 400, 3);
insert into affaire values ( default, 5000, 1000, 4);

insert into PartieDetruit values (default, 3, 8, 32, 34, 2);
insert into PartieDetruit values (default, 5, 9, 2, 54, 5);
insert into PartieDetruit values (default, 7, 10, 42, 54, 3);
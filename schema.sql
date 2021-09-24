create table if not exists modulos (
  id_modulo varchar(6) primary key not null,
  modulo varchar(200) not null,
  url varchar(250) not null
) engine = InnoDB;
create table if not exists unidades (
  id_modulo varchar(6) not null,
  unidad tinyint not null,
  titulo varchar(255) not null,
  url varchar(255) not null,
  primary key (id_modulo, unidad),
  constraint fk_unidades_modulos foreign key(id_modulo) references modulos(id_modulo) on delete restrict on update cascade
) engine = InnoDB;
create table if not exists tareas (
  id_modulo varchar(50) not null,
  unidad tinyint not null,
  tipo enum('cuestionario', 'tarea') not null,
  fecha_limite date not null,
  fecha_terminado date,
  primary key (id_modulo, unidad, tipo),
  constraint fk_tareas_unidades foreign key(id_modulo, unidad) references unidades(id_modulo, unidad) on delete restrict on update cascade
) engine = InnoDB;
/*  **** Dummy data **** */
insert into
  modulos
values(
    "ASO",
    "Administración de Sistemas Operativos",
    "#"
  ),
  (
    "ASGBD",
    "Administración de Sistemas Gestores de Base de Datos",
    "#"
  ),
  (
    "SRI",
    "Servicios de Red e Internet",
    "#"
  ),
  (
    "IAW",
    "Implantación de Aplicaciones Web",
    "#"
  ),
  (
    "SAD",
    "Seguridad y Alta Disponibilidad",
    "#"
  ),
  (
    "EIE",
    "Empresa e Iniciativa Emprendedora",
    "#"
  );
insert into
  unidades
values
  (
    "ASO",
    1,
    "Servicios de acceso y administración remota",
    "#"
  ),
  (
    "ASO",
    2,
    "Administración de servidores de impresión",
    "#"
  ),
  (
    "ASO",
    3,
    "Administración de servicios de directorio",
    "#"
  ),
  (
    "IAW",
    1,
    "Instalación de servidores de aplicaciones web",
    "#"
  ),
  (
    "IAW",
    2,
    "Programación de documentos web utilizando lenguajes de script de servidor",
    "#"
  ),
  (
    "IAW",
    3,
    "Acceso a bases de datos desde lenguajes de script de servidor",
    "#"
  );
insert into
  tareas (id_modulo, unidad, tipo, fecha_limite)
values
  ("IAW", 1, "Tarea", "2021-09-29"),
  ("IAW", 2, "Tarea", "2021-09-29"),
  ("IAW", 2, "Cuestionario", "2021-10-15"),
  ("ASO", 1, "Tarea", "2021-09-29"),
  ("ASO", 2, "Tarea", "2021-10-19"),
  ("ASO", 3, "Cuestionario", "2021-11-02");
  /* **** Consultas **** */
  create view view_tareas as
select
  t.id_modulo,
  m.modulo,
  t.unidad,
  u.titulo,
  t.tipo,
  t.fecha_limite,
  t.fecha_terminado
from
  tareas t
  join unidades u using(id_modulo, unidad)
  join modulos m using (id_modulo)
order by
  t.fecha_limite;
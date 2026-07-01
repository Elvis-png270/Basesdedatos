# diccionario de datos de la base de datos de control escolar 

1. informacion general

| elemento | valor |
| :--- | :--- |
| proyecto  | control escolar |
| version | 1.0 |
| elaboro | elvis |
| SGBD | SQLSERVER |

2. descripcion de la base de datos

la base de datos administra

-carrera
-alumno
-profesor
-materia
-grpo
-inscripcion
permite controlar la oferta academica y la inscripcion de estudiantes 

3. catalogo de restricciones utilizadas

| catalogo | significado |
| :--- | :--- |
| pk | primary key |
| fk | foreign key |
| nn | not null |
| uq | unique |
| ai | autoincrement o identity |
| ck | check |
| df | default |

4. diccionario de datos

**tabla:** _carrera_
**descripcion**
almacena las carreras ofertadas por la universidad
| Campo | tipo | longitud | restricciones | descripcion |
| :--- | :--- | :--- | :--- | :--- |
| id_carrera | int | - | pk,ai,nn | identificador de la carrera |
| nombre | varchar | 100 | uq,nn | nombre de la carrera| 
| duracion_cuatrimestre | int | - | nn,ck (>0) | duracion en cuaatrimestres |

---
**tabla:** _alumno_
**tabla:** _carrera_
**descripcion**
almacena la informacion de los estudiantes
almacena las carreras ofertadas por la universidad
| campo | tipo | longitud | restricciones | descripcion |
| :--- | :--- | :--- | :--- | :--- |
| id_alumno | int | - | pk,ai,nn | identificador de la carrera |
| matricula | varchar | 10 | uq,nn | matricula de la carrera | 
| nombre | varchar | int | 50 | nn | nombre del alumno |
| apellido_paterno | varchar | 50 | null | apellido paterno |
| apellido_materno | varchar | 50 | null | apellido materno |
| correo | varchar | 100 | uq,null | correo institucional |
| fecha_nacimietno | date | uq,nn | fecha nacimiento |
| id_carrera | int | - | fk,nn | carrera a la que pertenece |

TODO: documentar las siguientes tablas

5.Relaciones de la base de datos
| relacion | cardinalidad | edscripcion |
| :--- | :--- | :--- |
| carrera->alumno | 1:n | una carrera tiene muchos alumnos |
| carrera->materia | 1:n | una carrera tiene muchas materias |
| Profesor->grupo | 1:n | un profesor puede impartir a varios grupos |
| materia->grupo | 1:n | una materia puede abrirse en varios grupos |
| alumno->inscripcion | 1:n | un alumno puede tener varias inscripciones |
| grupo->inscripcion | 1:n | un grupo puede tener varios alumnos |

6. mtriz de claves foraneas
**tabla:** _carrera_
**descripcion**
almacena la informacion de los estudiantes
almacena las carreras ofertadas por la universidad
| tabla | campofk | referencia |
| :--- | :--- | :--- | :--- |
| id_alumno | id_carrera | carrera(id_carrera) | 
| materia | id_carrera | carrera(id_carrera) |
| grupo | id_profesor | profesor(id_profesor) |
| grupo | idmateria | materia(id_materia) |
| inscripcion | id_alumno | Alumno(id_alumno) |
| inscripcion | id_grupo | grupo(id_grupo) |  
| nombre | varchar | int | 

7. Reglas del negocio
| clave | regla | 
| :--- | :--- | 
| rn-01 | un alumno pertenece a una sola carrera |
| matricula | varchar |  
| nombre | varchar | int |
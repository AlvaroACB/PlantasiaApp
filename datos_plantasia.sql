DROP TABLE DETALLE_COMPRA;
DROP TABLE COMPRA;
DROP TABLE PRODUCTO;
DROP TABLE CATEGORIA;

CREATE TABLE CATEGORIA(
categoria_id NUMBER (3) NOT NULL,
nombre_categ VARCHAR2 (25) NOT NULl,
img_categ VARCHAR2 (100) NULL
);
ALTER TABLE CATEGORIA ADD CONSTRAINT PK_CAT PRIMARY KEY (categoria_id);

CREATE TABLE PRODUCTO(
producto_id NUMBER (3) NOT NULL,
nombre_prod VARCHAR2 (25) NOT NULl,
descripcion_prod VARCHAR2 (300) NOT NULl,
valor_prod NUMBER (7) NOT NULl,
categoria_id NUMBER (3) NOT NULL,
stock NUMBER(3) NOT NULL,
img_prod VARCHAR2 (100) NULL
);
ALTER TABLE PRODUCTO ADD CONSTRAINT PK_PRO PRIMARY KEY (producto_id);
ALTER TABLE PRODUCTO ADD CONSTRAINT FK_PRO_CAT FOREIGN KEY (categoria_id) REFERENCES CATEGORIA (categoria_id);

CREATE TABLE COMPRA(
compra_id NUMBER (6) NOT NULL,
usuario_id NUMBER (11) NOT NULL,
estado_compra VARCHAR2 (25) NOT NULL
);
ALTER TABLE COMPRA ADD CONSTRAINT PK_COM PRIMARY KEY (compra_id);
ALTER TABLE COMPRA ADD CONSTRAINT FK_COM_ID FOREIGN KEY (usuario_id) REFERENCES AUTH_USER (id);

CREATE TABLE DETALLE_COMPRA(
compra_id NUMBER (6) NOT NULL,
producto_id NUMBER (3) NOT NULL,
cantidad NUMBER (3) NOT NULL
);
ALTER TABLE DETALLE_COMPRA ADD CONSTRAINT FK_DET_COM FOREIGN KEY (compra_id) REFERENCES COMPRA (compra_id);
ALTER TABLE DETALLE_COMPRA ADD CONSTRAINT FK_DET_PRO FOREIGN KEY (producto_id) REFERENCES PRODUCTO (producto_id);

DROP SEQUENCE SEQ_PRO;
DROP SEQUENCE SEQ_COM;

CREATE SEQUENCE SEQ_PRO
START WITH 1
INCREMENT BY 1;

CREATE SEQUENCE SEQ_COM
START WITH 1
INCREMENT BY 1;

INSERT INTO CATEGORIA VALUES(100, 'Plantas de interior', 'categorias/img_plantas_interior.png');
INSERT INTO CATEGORIA VALUES(200, 'Plantas de exterior', 'categorias/img_plantas_exterior.png');
INSERT INTO CATEGORIA VALUES(300, 'Suculentas', 'categorias/img_suculenta.png');
INSERT INTO CATEGORIA VALUES(400, 'Plantas carnivoras', 'categorias/img_carnivora.png');
INSERT INTO CATEGORIA VALUES(500, 'Huerto', 'categorias/img_huerto.png');
INSERT INTO CATEGORIA VALUES(600, 'Insumos de jardineria', 'categorias/img_insumos.png');

INSERT INTO PRODUCTO VALUES(SEQ_PRO.NEXTVAL, 'Ficus benjamina', 'Higuera nativa del sur y sureste de Asia, y sur y norte de Australia.', 20000, 100, 50,  'productos/img_ficus_benjamina.png');
INSERT INTO PRODUCTO VALUES(SEQ_PRO.NEXTVAL, 'Peperomia cucharita', 'La Cucharita peperomia prefiere la luz indirecta y se desarrolla mejor en lugares con iluminación media.', 10000, 100, 50, 'productos/img_peperomia_cucharita.png');
INSERT INTO PRODUCTO VALUES(SEQ_PRO.NEXTVAL, 'Monstera deliciosa', 'Especie de planta trepadora de la familia Araceae, endémica de selvas tropicales.', 15000, 100, 50, 'productos/img_monstera_deliciosa.png');
INSERT INTO PRODUCTO VALUES(SEQ_PRO.NEXTVAL, 'Mandarino', 'Citrus reticulata es una especie del género Citrus, nativa del sudeste asiático y Filipinas', 50000, 200, 50, 'productos/img_mandarino.png');
INSERT INTO PRODUCTO VALUES(SEQ_PRO.NEXTVAL, 'Limonero', 'Pequeño árbol frutal perenne. Su fruto es el limón ? o citrón.', 45000, 200, 50, 'productos/img_limonero.png');
INSERT INTO PRODUCTO VALUES(SEQ_PRO.NEXTVAL, 'Pino', 'Género de plantas vasculares, comúnmente llamadas pinos.', 30000, 200, 50, 'productos/img_pino.png');
INSERT INTO PRODUCTO VALUES(SEQ_PRO.NEXTVAL, 'Echeveria', 'Echeveria es un género polifilético de plantas de la familia Crassulaceae.', 5000, 300, 50, 'productos/img_echeveria.png');
INSERT INTO PRODUCTO VALUES(SEQ_PRO.NEXTVAL, 'Kalamchoe', 'De la familia de las crasuláceas, nativas de África tropical, especialmente de Madagascar', 3000, 300, 50, 'productos/img_kalamchoe.png');
INSERT INTO PRODUCTO VALUES(SEQ_PRO.NEXTVAL, 'Sedum burrito', 'Planta suculenta, nativa del sur de México.', 6000, 300, 50, 'productos/img_sedum_burrito.png');
INSERT INTO PRODUCTO VALUES(SEQ_PRO.NEXTVAL, 'Venus atrapamoscas', 'Su hábito alimenticio es atrapar presas vivas, principalmente insectos y arácnidos. Es nativa del sureste de Estados Unidos.', 25000, 400, 50, 'productos/img_venus_atrapamoscas.png');
INSERT INTO PRODUCTO VALUES(SEQ_PRO.NEXTVAL, 'Rocio del sol', 'Drosera, conocido también como rocío del sol, ?? es uno de los géneros más numerosos de plantas carnívoras.', 30000, 400, 50, 'productos/img_rocio_del_sol.png');
INSERT INTO PRODUCTO VALUES(SEQ_PRO.NEXTVAL, 'Lirio de cobra', 'Nativo del norte de California y Oregón, que crece en pantanos y agua corriente.', 20000, 400, 50, 'productos/img_lirio_de_cobra.png');
INSERT INTO PRODUCTO VALUES(SEQ_PRO.NEXTVAL, 'Tomate cherry', 'Su hábito alimenticio es atrapar presas vivas, principalmente insectos y arácnidos. Es nativa del sureste de Estados Unidos.', 5000, 500, 50, 'productos/img_tomate_cherry.png');
INSERT INTO PRODUCTO VALUES(SEQ_PRO.NEXTVAL, 'Menta', 'Drosera, conocido también como rocío del sol, ?? es uno de los géneros más numerosos de plantas carnívoras.', 4000, 500, 50, 'productos/img_menta.png');
INSERT INTO PRODUCTO VALUES(SEQ_PRO.NEXTVAL, 'Albahaca', 'Nativo del norte de California y Oregón, que crece en pantanos y agua corriente.', 5000, 500, 50, 'productos/img_albahaca.png');
INSERT INTO PRODUCTO VALUES(SEQ_PRO.NEXTVAL, 'Tierra de hoja', 'Tierra de hoja de alta calidad, rica en nutrientes como nitrogeno.', 10000, 600, 50, 'productos/img_tierra_de_hoja.png');
INSERT INTO PRODUCTO VALUES(SEQ_PRO.NEXTVAL, 'Macetero', 'Maceretro de 15x15x45, rinde 5 litros.', 3000, 600, 50, 'productos/img_macetero.png');
INSERT INTO PRODUCTO VALUES(SEQ_PRO.NEXTVAL, 'Regadora', 'Regadora que permite una distribución homogenea del agua, con capacidad de 5 litros.', 5000, 600, 50, 'productos/img_regadera.png');

commit;
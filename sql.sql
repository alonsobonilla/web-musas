CREATE TABLE categoriaProducto (
  idCategoria     smallint(6) NOT NULL, 
  nombreCategoria varchar(50) NOT NULL, 
  descripcion     varchar(255), 
  PRIMARY KEY (idCategoria));
CREATE TABLE comprobante (
  idComprobante     int(11) NOT NULL, 
  idPedido          int(11) NOT NULL, 
  dniUsuario        char(8), 
  dniNoRegistrado   int(11) NOT NULL, 
  fechaComprobante  date NOT NULL, 
  horaComprobante   time NOT NULL, 
  subTotal          float NOT NULL, 
  montoTotal        float NOT NULL, 
  igv               float NOT NULL, 
  numeroComprobante varchar(25) NOT NULL, 
  PRIMARY KEY (idComprobante));
CREATE TABLE detalleComprobante (
  idComprobante  int(11) NOT NULL, 
  idProducto     int(11) NOT NULL, 
  nombreProducto varchar(100) NOT NULL, 
  precioUnidad   float NOT NULL, 
  cantidad       smallint(6) NOT NULL, 
  precioTotal    float NOT NULL, 
  PRIMARY KEY (idComprobante, 
  idProducto));
CREATE TABLE detalleCremas (
  idPedido   int(11) NOT NULL, 
  idProducto int(11) NOT NULL, 
  idCrema    int(11) NOT NULL, 
  PRIMARY KEY (idPedido, 
  idProducto, 
  idCrema));
CREATE TABLE detalleOrden (
  idProducto     int(11) NOT NULL, 
  idPedido       int(11) NOT NULL, 
  nombreProducto varchar(100) NOT NULL, 
  precioUnidad   float NOT NULL, 
  cantidad       smallint(6) NOT NULL, 
  precioTotal    float NOT NULL, 
  PRIMARY KEY (idProducto, 
  idPedido));
CREATE TABLE producto (
  idProducto  int(11) NOT NULL, 
  idCategoria smallint(6) NOT NULL, 
  nombre      varchar(100) NOT NULL, 
  descripcion varchar(255) NOT NULL, 
  precio      float, 
  existencias smallint(6), 
  PRIMARY KEY (idProducto));
CREATE TABLE registroPedido (
  idPedido         int(11) NOT NULL, 
  dniUsuario       char(8), 
  dniNoRegistrado  char(8) NOT NULL, 
  numeroTelefono   char(9) NOT NULL, 
  estadoRecojo     bit(1) DEFAULT false NOT NULL, 
  horaRecojo       time NOT NULL, 
  fechaPedido      date DEFAULT (CURRENT_DATE) NOT NULL, 
  estadoBoleta     bit(1) NOT NULL, 
  billeteraDigital bit(1) NOT NULL, 
  keyPedido        smallint(6) NOT NULL, 
  PRIMARY KEY (idPedido));
CREATE TABLE usuario (
  dni             char(8) NOT NULL, 
  nombres         varchar(100) NOT NULL, 
  apellidos       varchar(100) NOT NULL, 
  correo          varchar(200) NOT NULL, 
  numTel          char(9) NOT NULL, 
  fechaNacimiento date NOT NULL, 
  contraseña      varchar(250) NOT NULL, 
  PRIMARY KEY (dni));
CREATE TABLE usuarioAdmin (
  idAdmin    smallint(6) NOT NULL, 
  usuario    varchar(50) NOT NULL, 
  contraseña varchar(250) NOT NULL, 
  PRIMARY KEY (idAdmin));
ALTER TABLE detalleComprobante ADD CONSTRAINT FKdetalleCom998263 FOREIGN KEY (idComprobante) REFERENCES comprobante (idComprobante);
ALTER TABLE detalleOrden ADD CONSTRAINT FKdetalleOrd26951 FOREIGN KEY (idProducto) REFERENCES producto (idProducto);
ALTER TABLE detalleCremas ADD CONSTRAINT FKdetalleCre204471 FOREIGN KEY (idProducto, idPedido) REFERENCES detalleOrden (idProducto, idPedido);
ALTER TABLE producto ADD CONSTRAINT FKproducto802442 FOREIGN KEY (idCategoria) REFERENCES categoriaProducto (idCategoria);
ALTER TABLE registroPedido ADD CONSTRAINT FKregistroPe480639 FOREIGN KEY (dniUsuario) REFERENCES usuario (dni);
ALTER TABLE detalleOrden ADD CONSTRAINT FKdetalleOrd726046 FOREIGN KEY (idPedido) REFERENCES registroPedido (idPedido);
ALTER TABLE comprobante ADD CONSTRAINT FKcomprobant592336 FOREIGN KEY (dniUsuario) REFERENCES usuario (dni);
ALTER TABLE detalleComprobante ADD CONSTRAINT FKdetalleCom611488 FOREIGN KEY (idProducto) REFERENCES producto (idProducto);
ALTER TABLE comprobante ADD CONSTRAINT FKcomprobant506863 FOREIGN KEY (idPedido) REFERENCES registroPedido (idPedido);
ALTER TABLE detalleCremas ADD CONSTRAINT FKdetalleCre352772 FOREIGN KEY (idCrema) REFERENCES producto (idProducto);

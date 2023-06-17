CREATE TABLE categoriaProducto (
  idCategoria     smallint(6) NOT NULL AUTO_INCREMENT, 
  nombreCategoria varchar(50) NOT NULL, 
  descripcion     varchar(255), 
  PRIMARY KEY (idCategoria));
CREATE TABLE comprobante (
  idComprobante     int(11) NOT NULL AUTO_INCREMENT, 
  idPedido          int(11) NOT NULL, 
  idUsuario         int(11), 
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
  idProducto  int(11) NOT NULL AUTO_INCREMENT, 
  idCategoria smallint(6) NOT NULL, 
  nombre      varchar(100) NOT NULL, 
  descripcion varchar(255) NOT NULL, 
  precio      float, 
  existencias smallint(6), 
  PRIMARY KEY (idProducto));
CREATE TABLE registroPedido (
  idPedido         int(11) NOT NULL AUTO_INCREMENT, 
  idUsuario        int(11) NOT NULL, 
  dniNoRegistrado  char(8) NOT NULL, 
  numeroTelefono   char(9) NOT NULL, 
  estadoRecojo     tinyint(1) DEFAULT false NOT NULL, 
  horaRecojo       time NOT NULL, 
  fechaPedido      date DEFAULT (CURRENT_DATE) NOT NULL, 
  estadoBoleta     tinyint(1) NOT NULL, 
  billeteraDigital tinyint(1) NOT NULL, 
  keyPedido        smallint(6) NOT NULL, 
  PRIMARY KEY (idPedido));
CREATE TABLE usuario (
  idUsuario   int(11) NOT NULL AUTO_INCREMENT, 
  dni         char(8) NOT NULL, 
  nombres     varchar(100) NOT NULL, 
  apellidos   varchar(100) NOT NULL, 
  correo      varchar(200) NOT NULL, 
  numTelf     char(9) NOT NULL, 
  contraseña  varchar(100) NOT NULL, 
  tipoUsuario tinyint(1) NOT NULL, 
  PRIMARY KEY (idUsuario));
ALTER TABLE detalleComprobante ADD CONSTRAINT FKdetalleCom998263 FOREIGN KEY (idComprobante) REFERENCES comprobante (idComprobante);
ALTER TABLE detalleOrden ADD CONSTRAINT FKdetalleOrd26951 FOREIGN KEY (idProducto) REFERENCES producto (idProducto);
ALTER TABLE detalleCremas ADD CONSTRAINT FKdetalleCre204471 FOREIGN KEY (idProducto, idPedido) REFERENCES detalleOrden (idProducto, idPedido);
ALTER TABLE producto ADD CONSTRAINT FKproducto802442 FOREIGN KEY (idCategoria) REFERENCES categoriaProducto (idCategoria);
ALTER TABLE registroPedido ADD CONSTRAINT FKregistroPe851289 FOREIGN KEY (idUsuario) REFERENCES usuario (idUsuario);
ALTER TABLE detalleOrden ADD CONSTRAINT FKdetalleOrd726046 FOREIGN KEY (idPedido) REFERENCES registroPedido (idPedido);
ALTER TABLE comprobante ADD CONSTRAINT FKcomprobant749904 FOREIGN KEY (idUsuario) REFERENCES usuario (idUsuario);
ALTER TABLE detalleComprobante ADD CONSTRAINT FKdetalleCom611488 FOREIGN KEY (idProducto) REFERENCES producto (idProducto);
ALTER TABLE comprobante ADD CONSTRAINT FKcomprobant506863 FOREIGN KEY (idPedido) REFERENCES registroPedido (idPedido);
ALTER TABLE detalleCremas ADD CONSTRAINT FKdetalleCre352772 FOREIGN KEY (idCrema) REFERENCES producto (idProducto);

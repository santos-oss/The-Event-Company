CREATE DATABASE GerenciamentoEventos;
USE GerenciamentoEventos;
CREATE TABLE Usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Eventos (
    id_evento INT AUTO_INCREMENT PRIMARY KEY,
    nome_evento VARCHAR(100) NOT NULL,
    descricao TEXT,
    data_evento DATE NOT NULL,
    localizacao VARCHAR(150),
    organizador_id INT,
    FOREIGN KEY (organizador_id) REFERENCES Usuarios(id_usuario)
);

CREATE TABLE Inscricoes (
    id_inscricao INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    evento_id INT,
    data_inscricao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES Usuarios(id_usuario),
    FOREIGN KEY (evento_id) REFERENCES Eventos(id_evento)
);
SHOW TABLES;
INSERT INTO Usuarios (nome, email, senha) VALUES
('João Silva', 'joao@email.com', 'senha123'),
('Maria Oliveira', 'maria@email.com', 'senha456');
INSERT INTO Eventos (nome_evento, descricao, data_evento, localizacao, organizador_id) VALUES
('Curso de MySQL', 'Curso básico de MySQL para iniciantes', '2024-12-05', 'Online', 1),
('Palestra sobre Segurança', 'Palestra sobre segurança em TI', '2024-12-10', 'Auditório Central', 2);
INSERT INTO Inscricoes (usuario_id, evento_id) VALUES
(1, 1), -- João no Curso de MySQL
(2, 2); -- Maria na Palestra de Segurança
SELECT * FROM Usuarios;
SELECT * FROM Eventos;
SELECT * FROM Inscricoes;

INSERT INTO Usuarios (nome, email, senha) VALUES
('Carlos Souza', 'carlos@email.com', 'senha789');
INSERT INTO Eventos (nome_evento, descricao, data_evento, localizacao, organizador_id) VALUES
('Workshop de Python', 'Workshop sobre programação em Python', '2024-12-15', 'Centro de Convenções', 1);
INSERT INTO Inscricoes (usuario_id, evento_id) VALUES
(1, 3); -- Carlos se inscreve no Workshop de Python
SELECT * FROM Usuarios;
SELECT e.nome_evento, e.data_evento
FROM Eventos e
JOIN Inscricoes i ON e.id_evento = i.evento_id
WHERE i.usuario_id = 1;
SELECT * FROM Eventos;
UPDATE Usuarios
SET nome = 'Carlos Alberto Souza'
WHERE id_usuario = 3;
UPDATE Eventos
SET data_evento = '2024-12-20'
WHERE id_evento = 3;
UPDATE Eventos
SET descricao = 'Novo workshop de Python com foco em dados.'
WHERE id_evento = 3;
DELETE FROM Usuarios
WHERE id_usuario = 3;
DELETE FROM Eventos
WHERE id_evento = 3;
DELETE FROM Inscricoes
WHERE id_inscricao = 2
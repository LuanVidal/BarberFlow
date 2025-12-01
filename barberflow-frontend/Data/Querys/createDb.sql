CREATE TABLE IF NOT EXISTS clientes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    telefone TEXT NOT NULL,
    data_cadastro DATETIME
);
CREATE TABLE IF NOT EXISTS funcionario(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    telefone TEXT NOT NULL,
    ativo BOOLEAN
);
CREATE TABLE servicos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nome TEXT NOT NULL,
  preco REAL NOT NULL,
  duracao_min INTEGER
);

CREATE TABLE agendamentos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  cliente_id INTEGER,
  servico_id INTEGER,
  funcionario_id INTEGER,
  data_hora DATETIME,
  status TEXT,
  FOREIGN KEY (cliente_id) REFERENCES clientes(id),
  FOREIGN KEY (servico_id) REFERENCES servicos(id),
  FOREIGN KEY (funcionario_id) REFERENCES funcionario(id)
);
CREATE TABLE caixa (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  valor DECIMAL,
  data_hora DATETIME,
  tipo TEXT NOT NULL
);

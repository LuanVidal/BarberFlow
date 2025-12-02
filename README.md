# 💈 BarberFlow - Sistema de Gestão para Barbearias

![Status do Projeto](https://img.shields.io/badge/Status-Concluído-brightgreen)

## 📋 Sobre o Projeto

O **BarberFlow** é uma solução completa desenvolvida para modernizar a gestão de barbearias, integrando a experiência do cliente (agendamento inteligente) com uma visão administrativa completa (financeiro, configurações e gerenciamento de serviços).

Este sistema foi desenvolvido como parte da avaliação prática da disciplina de **Gestão e Qualidade de Software**, aplicando metodologias ágeis, boas práticas de arquitetura e processos de garantia de qualidade.

---

## 🚀 Principais Features Entregues

### 🔐 Autenticação Unificada
* Login único para **Clientes** e **Barbeiros**, com redirecionamento automático para sua área correta (`/home` ou `/admin`).

### 📅 Agendamento Inteligente
* Bloqueio automático de horários já marcados.
* Filtragem de horários disponíveis, excluindo automaticamente o período de almoço (12:00–13:00).
* Interface de agendamento simples e rápida para o cliente.

### 🧑‍🔧 Dashboard Administrativo (Barbeiro / Admin)
* Gerenciamento de horários.
* Gerenciamento de serviços e preços.
* Controle de operação diária.

### 💸 Painel Financeiro
* Cálculo automático da **Receita Bruta Total**.
* Gráfico de Desempenho Diário usando **Chart.js**.
* Visualização clara do faturamento e tendência.

### ⚙️ Configurações Dinâmicas
* Definição dos horários de funcionamento.
* Criação e edição de serviços (preço + duração).

### 🎨 Qualidade UX
* Interface moderna em **Azul Marinho**.
* Responsiva, com animações e feedbacks utilizando **SweetAlert2**.

---

## 👥 Equipe de Desenvolvimento

| Nome | Matrícula | Função |
| :--- | :--- | :--- |
| **Thiago Mendes Borges** | 323125240 | Desenvolvedor / QA |
| **Wanderson Matheus Pontes Lima** | 323119778 | Desenvolvedor / QA |
| **Márcio Alves Pereira Neto** | 323129278 | Desenvolvedor / QA |
| **Luan Gabriel Vidal da Silva** | 323125685 | Desenvolvedor / QA |
| **Mayumi Moreira Leão** | 323130501 | Desenvolvedor / QA |

---

## 🎯 Metodologia e Qualidade de Software

O projeto adotou práticas consolidadas de qualidade e engenharia:

### 🧪 TDD – Test Driven Development
* Regras críticas como Agendamento, Conflito de Horário e Login foram desenvolvidas seguindo o ciclo **Red → Green → Refactor**, garantindo confiabilidade.

### 🔄 Integração Contínua (CI)
* GitHub Actions configurado para rodar a suíte de testes automaticamente e validar cada *push* ou *pull request*.

### 🧱 Arquitetura Modular
* **Backend:** Application Factory com Flask + SQLAlchemy.
* **Frontend:** Angular com Standalone Components.
* Separação clara de camadas e responsabilidades.

---

## 🛠️ Tecnologias Utilizadas

| Módulo | Tecnologia | Descrição |
| :--- | :--- | :--- |
| **Backend** | Python (Flask) | API REST, SQLAlchemy (SQLite), segurança com Werkzeug |
| **Frontend** | Angular 21 | Components standalone, HttpClient, FormsModule |
| **Testes** | PyTest | Validação das regras de negócio |
| **Gráficos** | Chart.js | Dashboards financeiros |
| **Ferramentas** | CI/CD, Jira, GitHub Actions | Gestão e qualidade |

---

## 📅 Cronograma e Entregas

- [x] **Fase 1 (06/11):** Setup inicial (Jira, GitHub, CI).
- [x] **Fase 2 (13/11):** Desenvolvimento inicial e apresentação.
- [x] **Fase 3 (27/11):** Gestão de configuração, branches e code review.
- [x] **Fase 4 (04/12):** Sistema finalizado e entrega do pitch.

---

# 🚀 Execução do Projeto

O projeto é dividido em dois módulos:

📦 `barberflow-backend` (API Flask)  
💻 `barberflow-frontend` (Angular)

---

## ▶️ 1. Rodando o Backend (Flask)

### Entrar na pasta:
```bash
cd barberflow-backend
```

### Instalar dependências:
```bash
pip install -r requirements.txt
```

### Iniciar servidor:
```bash
python run.py
```
#### 🟢 Servidor ativo: http://127.0.0.1:5000 | O sistema cria automaticamente o banco de dados e os usuários padrão ao iniciar.


## ▶️ 1. Rodando o Frontend (Angular)

### Entrar na pasta:
```bash
cd ../barberflow-frontend
```

### Instalar dependências:
```bash
npm install
```

### Iniciar servidor:
```bash
ng serve
```

#### 🟢 Aplicação ativa em: http://localhost:4200 | A cada alteração no código, a página recarrega automaticamente.


# ✔️ Cenários de Teste (Fluxos Principais)

Abra o navegador em **http://localhost:4200** e valide os seguintes comportamentos:

---

## 🔹 Credenciais e Acessos Padrão

| Usuário   | E-mail               | Senha | Acesso   |
|----------|-----------------------|-------|----------|
| BARBEIRO | barbeiro@teste.com    | 123   | /admin   |
| CLIENTE  | novo cadastro         | definida ao registrar | /home |

---

## 🔹 Testes Funcionais Importantes

### **Cliente**
- Deve conseguir visualizar somente **horários disponíveis**.
- O **horário de almoço (12:00–13:00)** é automaticamente bloqueado.
- **Horários já agendados** não aparecem.
- Após agendar, deve ser **redirecionado com mensagem de sucesso**.

### **Barbeiro/Admin**
- Consegue **ajustar horário de funcionamento**.
- Pode **criar/editar/remover serviços** (nome, preço e duração).
- Visualiza **receita bruta** no dashboard financeiro.
- **Gráficos** funcionam corretamente (Chart.js).

---

# 🧪 Rodando os Testes Automatizados (PyTest)

No terminal do backend (**barberflow-backend**), execute:

```bash
pytest -v
```

## 🔎 Resultado Esperado


#### Todos os testes devem retornar: PASSED 100%

### Os testes cobrem:
- Login e autenticação  
- Conflitos de horário  
- Criação de agendamentos  
- Regras de bloqueio de horário  
- Cálculo financeiro  

---

## 🗂️ Principais Telas do Sistema

### 🏠 Cliente
- Home com **horários disponíveis**
- **Agendamento rápido**
- **Confirmação de agendamento** (popup SweetAlert2)

### 🧔 Barbeiro/Admin
- **Dashboard completo**
- Gráfico de **desempenho diário**
- **Configuração de horários**
- Área de **serviços (CRUD)**

---

## 🧩 Arquitetura e Padrões

### Backend (Flask)
- Padrão **Application Factory**
- **SQLAlchemy ORM**
- **Blueprints** para modularização
- **Validações centralizadas**
- Testes **PyTest** organizados por contexto

### Frontend (Angular 21)
- **Components Standalone**
- **Services** para consumo da API
- **Reactive Forms**
- **Router** separado por perfis (cliente/admin)

---

## 📈 Resultado Final

O projeto foi concluído com sucesso, entregando:

✔ Sistema funcional de ponta a ponta  
✔ Testes automatizados garantindo robustez  
✔ CI ativo no GitHub Actions  
✔ Interface moderna e responsiva  
✔ Arquitetura organizada e escalável  
✔ Documentação completa  
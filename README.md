# 💈 BarberFlow - Sistema de Gestão para Barbearias

![Status do Projeto](https://img.shields.io/badge/Status-Em_Desenvolvimento-yellow)

## 📋 Sobre o Projeto

O **BarberFlow** é uma solução completa desenvolvida para modernizar a gestão de barbearias. O sistema integra o agendamento de clientes com um painel financeiro robusto, permitindo não apenas o controle de horários, mas também a projeção de recebimentos e gestão de comissões.

Este projeto foi desenvolvido como parte da avaliação prática da disciplina de **Gestão e Qualidade de Software**, com foco na aplicação de metodologias ágeis, garantia de qualidade e automação de processos.

## 👥 Equipe de Desenvolvimento

| Nome | Matrícula | Função |
| :--- | :--- | :--- |
| **Thiago Mendes Borges** | 323125240 | Desenvolvedor / QA |
| **Wanderson Matheus Pontes Lima** | 323119778 | Desenvolvedor / QA |
| **Márcio Alves Pereira Neto** | 323129278 | Desenvolvedor / QA |
| **Luan Gabriel Vidal da Silva** | 323125685 | Desenvolvedor / QA |
| **Mayumi Moreira Leão** | 323130501 | Desenvolvedor / QA |

---

## 🎯 Objetivos Acadêmicos e Metodologia

O principal objetivo deste projeto é aplicar na prática os conceitos de Qualidade de Software. Para garantir a robustez e a manutenibilidade do código, adotamos as seguintes práticas:

* **TDD (Test Driven Development):** Todo o desenvolvimento é orientado a testes. Primeiro escrevemos o teste (que falha), depois o código (para passar) e por fim a refatoração.
* **Integração Contínua (CI):** Utilizamos **GitHub Actions** para rodar automaticamente a suíte de testes a cada *push* ou *pull request*, garantindo que nada quebre a *build*.
* **Gestão de Configuração:** Utilizamos o fluxo de branches (GitFlow simplificado) e Code Reviews obrigatórios para manter a integridade da branch `main`.
* **Gestão Ágil:** O acompanhamento do projeto, requisitos e histórias de usuário é feito através do **Jira Software**.

---

## 🚀 Funcionalidades Principais

### 🧑‍💻 Gestão de Contas
* Cadastro e Login (Clientes e Barbeiros).
* Gestão de Perfis e Permissões.

### 🗓️ Agendamento (Core)
* Visualização de disponibilidade por barbeiro.
* Agendamento de serviços.
* Cancelamento e reagendamento.
* Bloqueio de agenda (para folgas/almoço).

### 💸 Painel Financeiro
* Registro de pagamentos e formas de pagamento.
* Dashboard de faturamento (Diário/Semanal/Mensal).
* **Projeção de Recebimentos** futuros baseada na agenda.
* Relatórios de comissão por barbeiro.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** [Python / JavaScript]
* **Framework Backend:** [ Django ]
* **Frontend:** [ Vue ]
* **Banco de Dados:** [ MySQL ]
* **Testes:** [ PyTest ]
* **Ferramentas:** Jira, GitHub Actions, Docker.

---

## 📅 Cronograma e Entregas

- [x] **Fase 1 (06/11):** Configuração do Projeto (Jira, GitHub, CI Setup).
- [ ] **Fase 2 (13/11):** Desenvolvimento Inicial e Apresentação de Gestão.
- [ ] **Fase 3 (27/11):** Gestão de Configuração, Branches e Code Review.
- [ ] **Fase 4 (04/12):** Sistema Finalizado e Pitch do Projeto.

---

# Projeto

This project was generated using [Angular CLI](https://github.com/angular/angular-cli) version 21.0.1.

## Development server

To start a local development server, run:

```bash
ng serve
```

Once the server is running, open your browser and navigate to `http://localhost:4200/`. The application will automatically reload whenever you modify any of the source files.

## Code scaffolding

Angular CLI includes powerful code scaffolding tools. To generate a new component, run:

```bash
ng generate component component-name
```

For a complete list of available schematics (such as `components`, `directives`, or `pipes`), run:

```bash
ng generate --help
```

## Building

To build the project run:

```bash
ng build
```

This will compile your project and store the build artifacts in the `dist/` directory. By default, the production build optimizes your application for performance and speed.

## Running unit tests

To execute unit tests with the [Vitest](https://vitest.dev/) test runner, use the following command:

```bash
ng test
```

## Running end-to-end tests

For end-to-end (e2e) testing, run:

```bash
ng e2e
```

Angular CLI does not come with an end-to-end testing framework by default. You can choose one that suits your needs.

## Additional Resources

For more information on using the Angular CLI, including detailed command references, visit the [Angular CLI Overview and Command Reference](https://angular.dev/tools/cli) page.

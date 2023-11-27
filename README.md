# Job Insights - Análise de Dados de Empregos

Este projeto consiste na análise de um conjunto de dados sobre empregos, extraídos do site Glassdoor através do Kaggle. O objetivo é realizar análises e extrair insights desses dados para auxiliar em tomadas de decisão.

## 🚵 Habilidades Desenvolvidas

- Utilização do terminal interativo do Python.
- Uso de estruturas condicionais e de repetição.
- Manipulação de arquivos.
- Utilização de funções built-in do Python.
- Tratamento de exceções.
- Escrita de funções reutilizáveis.
- Desenvolvimento de testes utilizando Pytest.
- Criação e importação de módulos próprios.

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para o desenvolvimento do projeto.
- **Pytest**: Framework de testes utilizado para garantir a qualidade das implementações.
- **Flake8**: Linter utilizado para manter a consistência e boas práticas no código.

## 🧱 Estrutura do Projeto

```
  Legenda:
  🔸Arquivos usados para testar o desenvolvimento do projeto
  🔹Arquivos do projeto que atendem os testes (Principal)
  .
  ├── data
  │   └──🔹jobs.csv
  ├── src
  │   ├── insights
  │   │   ├──🔹industries.py
  │   │   ├──🔹jobs.py
  │   │   └──🔹salaries.py
  │   ├── pre_built
  │   │   ├──🔸brazilian_jobs.py
  │   │   ├──🔹counter.py
  ├── tests
  │   ├──🔸__init__.py
  │   ├──🔸conftest.py
  │   ├──🔸marker.py
  │   ├── brazilian
  │   │   ├──🔸__init__.py
  │   │   ├──🔸conftest.py
  │   │   ├──🔸mocks.py
  │   │   ├──🔹test_brazilian_jobs.py
  │   ├── counter
  │   │   ├──🔸__init__.py
  │   │   ├──🔸conftest.py
  │   │   ├──🔸mocks.py
  │   │   ├──🔹test_counter.py
  │   ├── mocks
  │   │   ├──🔸job_1.html
  │   │   ├──🔸jobs.csv
  │   │   ├──🔸jobs_with_industries.csv
  │   │   ├──🔸jobs_with_salaries.csv
  │   │   └──🔸jobs_with_types.csv
  │   ├──🔸test_industries.py
  │   ├──🔸test_jobs.py
  │   ├──🔸test_salaries.py
  ```

## ⚙️ Funcionalidades Principais

### Manipulação de Dados de Empregos

- **Leitura de Dados**: O módulo `jobs.py` oferece funcionalidades para ler dados de um arquivo CSV contendo informações de empregos.
- **Análises de Dados**: Os módulos `industries.py`, `salaries.py` fornecem métodos para extrair informações únicas sobre indústrias, informações salariais máximas/mínimas e filtragens com base em critérios.

### Testes

- **Testes de Funcionalidades**: Os arquivos de teste `test_brazilian_jobs.py` e `test_counter.py` validam a correta implementação das funcionalidades principais.

## 🏁 Execução dos Testes

Para executar os testes, siga as instruções abaixo:

```bash
python3 -m pytest
```

## 🧹 Linter
Para garantir a qualidade do código, utilizei o linter Flake8:

```bash
Copy code
python3 -m flake8
```

# Python Algoritmos

> Coleção de exercícios práticos e exemplos para desenvolvimento e estudo de lógica de programação utilizando Python.

---

## Tecnologias e Pré-requisitos

Para executar e testar os scripts deste repositório, você precisará de:

- [Python 3.x](https://www.python.org/downloads/) instalado na sua máquina.
- Git (opcional, caso queira clonar o repositório via terminal).
- Um editor de código ou IDE (como VS Code ou PyCharm).

### Como verificar se o Python está instalado:
Abra o seu terminal (Prompt de Comando, PowerShell ou Terminal do Linux/macOS) e digite:

```bash
python --version
```
> Caso o comando acima não funcione no Windows, tente `py --version` ou `python3 --version`.

---

## Estrutura do Repositório

O repositório é dividido entre os arquivos de exemplo na raiz e os exercícios de lógica na pasta `algoritmos/`:

```text
Python-Algoritmos/
│
├── algoritmos/                    # Lista de exercícios de lógica
│   ├── algoritmos.md              # Enunciado de cada exercício
│   ├── media.py                   # 1. Média de três números
│   ├── conversor.py               # 2. Conversão de Celsius para Fahrenheit
│   ├── condicional.py             # 3. Identificação de número par ou ímpar
│   ├── fatorial.py                # 4. Cálculo de fatorial de um número
│   ├── bissexto.py                # 5. Verificação de ano bissexto
│   ├── sinais.py                  # 6. Número positivo, negativo ou zero
│   ├── comparacao.py              # 7. Comparação de dois números
│   ├── idade.py                   # 8. Verificação de maioridade
│   └── triangulos.py              # 9. Classificação de triângulos
│
├── condicional.py                 # Exemplo de estrutura condicional (par ou ímpar)
├── for.py                         # Exemplo de laço de repetição for (1 a 100)
├── soma.py                        # Exemplo de entrada, soma e saída
└── README.md                      # Documentação do projeto
```

---

## Como Executar e Testar Localmente

### 1. Clonar ou Baixar o Repositório
Se tiver o Git instalado, execute no terminal:
```bash
git clone https://github.com/EnzoToniato567/Python-Algoritmos.git
```
Em seguida, acesse a pasta do projeto:
```bash
cd Python-Algoritmos
```

---

### 2. Executando os Arquivos de Exemplo (Raiz)

Os arquivos `.py` localizados na raiz do projeto são exemplos de demonstração de conceitos básicos:

```bash
# Exemplo de soma de dois números inteiros
python soma.py

# Exemplo de laço for com contagem de 1 a 100
python for.py

# Exemplo de condicional para par ou ímpar
python condicional.py
```

---

### 3. Executando os Exercícios (Pasta algoritmos/)

Você pode executar os exercícios de duas maneiras:

#### Opção 1: Entrando na pasta de exercícios (Recomendado)

Navegue até a pasta `algoritmos`:
```bash
cd algoritmos
```

E execute diretamente o exercício desejado:
```bash
python media.py
python fatorial.py
python triangulos.py
```

Para retornar à raiz do projeto quando terminar:
```bash
cd ..
```

#### Opção 2: A partir da raiz do projeto

Caso prefira continuar na raiz do repositório, informe o caminho do arquivo:

No Windows (PowerShell / CMD):
```powershell
python algoritmos\media.py
python algoritmos\fatorial.py
python algoritmos\triangulos.py
```

No Linux / macOS / Git Bash:
```bash
python algoritmos/media.py
python algoritmos/fatorial.py
python algoritmos/triangulos.py
```

---

## Testes e Entradas/Saídas Esperadas

Abaixo estão alguns testes com valores de entrada e o resultado esperado para validar as execuções:

### Exemplos da raiz:
- **`soma.py`**
  - Entradas: `4` e `6`
  - Saída esperada: `A soma destes números é  10`
- **`condicional.py`**
  - Entrada: `7`
  - Saída esperada: `O número  7  é ímpar`

### Exercícios da pasta `algoritmos/`:
- **`algoritmos/media.py`**
  - Entradas: `10`, `8`, `6`
  - Saída esperada: `A média dos números é:  8.0`
- **`algoritmos/fatorial.py`**
  - Entrada: `5`
  - Saída esperada: `O fatorial de 5 é: 120`
- **`algoritmos/triangulos.py`**
  - Entradas: `5`, `5`, `5` -> `O triângulo é equilátero. Possue todos os lados iguais.`
  - Entradas: `5`, `5`, `3` -> `O triângulo é isósceles. Possue dois lados iguais.`
  - Entradas: `3`, `4`, `5` -> `O triângulo é escaleno. Possue todos os lados diferentes.`

---

## Dicas Úteis

- Interromper a execução: Caso o script esteja aguardando uma entrada e você queira encerrá-lo, pressione `Ctrl + C` no terminal.
- Terminal Integrado: Você pode abrir o terminal diretamente no editor (no VS Code: `Ctrl + '` ou `Ctrl + J`) e rodar os comandos sem sair da interface.
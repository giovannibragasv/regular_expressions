# Validador de Placas de Veículos - Documentação

## 1. Descrição do Projeto

Este projeto implementa um validador de placas de veículos brasileiros utilizando expressões regulares. O programa valida placas nos dois formatos oficiais:
- **Formato Antigo**: AAA-9999 (três letras, hífen, quatro números)
- **Formato Mercosul**: AAA9A99 (três letras, um número, uma letra, dois números)

O sistema funciona via linha de comando (terminal), oferecendo uma interface textual simples e eficiente para validação de placas.

## 2. Expressões Regulares Implementadas

### 2.1 Notação Algébrica das Expressões Regulares

#### Placa Formato Antigo (AAA-9999)
Em notação algébrica: `[A-Z][A-Z][A-Z]-[0-9][0-9][0-9][0-9]`

Pode ser simplificada para: `[A-Z]³-[0-9]⁴`

#### Placa Formato Mercosul (AAA9A99)
Em notação algébrica: `[A-Z][A-Z][A-Z][0-9][A-Z][0-9][0-9]`

Pode ser simplificada para: `[A-Z]³[0-9][A-Z][0-9]²`

### 2.2 Sintaxe Implementada no Programa

#### Placa Formato Antigo
```python
r'^[A-Z]{3}-\d{4}$'
```

Onde:
- `^` indica o início da string
- `[A-Z]{3}` representa exatamente 3 letras maiúsculas
- `-` representa o hífen literal
- `\d{4}` representa exatamente 4 dígitos
- `$` indica o fim da string

#### Placa Formato Mercosul
```python
r'^[A-Z]{3}\d[A-Z]\d{2}$'
```

Onde:
- `^` indica o início da string
- `[A-Z]{3}` representa exatamente 3 letras maiúsculas
- `\d` representa 1 dígito
- `[A-Z]` representa 1 letra maiúscula
- `\d{2}` representa exatamente 2 dígitos
- `$` indica o fim da string

## 3. Implementação do Programa

### 3.1 Estrutura do Código

O programa está estruturado da seguinte forma:

1. **Classe ValidadorPlacas**: Contém a lógica de validação usando expressões regulares
2. **Funções de interface**: Implementam a interação com o usuário via terminal
   - `exibir_menu()`: Mostra o menu de opções
   - `exibir_info_regex()`: Exibe informações sobre as expressões regulares usadas
   - `main()`: Função principal que coordena o fluxo do programa

### 3.2 Funcionalidades

- Validação de placas no formato antigo (AAA-9999)
- Validação de placas no formato Mercosul (AAA9A99)
- Detecção automática do formato da placa
- Interface de terminal intuitiva com menu de opções
- Normalização da entrada (remoção de espaços, conversão para maiúsculas)
- Exibição de informações sobre as expressões regulares utilizadas

### 3.3 Requisitos

- Python 3.6 ou superior
- Biblioteca padrão: re, sys

### 3.4 Como Executar

1. Certifique-se de ter o Python instalado
2. Execute o arquivo principal: `python validador_placas_terminal.py`
3. Siga as instruções no terminal

## 4. Exemplo de Uso

### 4.1 Menu Principal

```
===== VALIDADOR DE PLACAS DE VEÍCULOS =====
1. Validar placa (detecção automática de formato)
2. Validar placa no formato antigo (AAA-9999)
3. Validar placa no formato Mercosul (AAA9A99)
4. Exibir informações sobre as expressões regulares
5. Sair
============================================
```

### 4.2 Validação de Placas

Exemplos de entrada e saída:

#### Placa válida no formato antigo
```
Digite a placa a ser validada: ABC-1234

Resultado da validação:
✅ Placa válida no formato antigo (AAA-9999)
```

#### Placa válida no formato Mercosul
```
Digite a placa a ser validada: ABC1D23

Resultado da validação:
✅ Placa válida no formato Mercosul (AAA9A99)
```

#### Placa inválida
```
Digite a placa a ser validada: ABC1234

Resultado da validação:
❌ Placa inválida. Formatos aceitos: AAA-9999 ou AAA9A99
```

## 6. Conclusão

Este projeto demonstra a aplicação prática de expressões regulares e autômatos finitos não-determinísticos na validação de dados estruturados. A implementação mostra como conceitos teóricos de Linguagens Formais e Autômatos podem ser aplicados para resolver problemas do mundo real, como a validação de placas de veículos.

## 7. Autores

- Giovanni B. S. Vasconcelos
- Cauã M. S. Nara
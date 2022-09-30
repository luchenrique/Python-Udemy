# [Curso de Python do Básico ao Avançado - Udemy](https://www.udemy.com/course/python-3-do-zero-ao-avancado/)

👋🏽 Olá, estou aperfeiçoando meus conhecimento na linguagem Python. <br>
Esse é um repositório onde irei colocar alguns projetos e taferas aprendidos no curso a cima. 

## Projetos
✔️ Calculadora de IMC

_____________________

## Módulos
**[1- Lógica de Programação (Python Básico)](https://github.com/luchenrique/Python-Udemy#1-m%C3%B3dulo---l%C3%B3gica-de-programa%C3%A7%C3%A3o)**

_____________________

## 1° Módulo - Lógica de Programação

Tipos de Dados:
- [x] str - string 
- [x] int- inteiros 
- [x] float - real
- [x] bool - booleano/lógico

_____________________

Operadores Aritméticos:

```python
print('Adição:', 10 + 10)
print('Subtração:', 10 - 5)
print('Multiplicação:', 10 * 10)
print('Divisão: ', 10 / 2)
print('Divisão inteira', 10 // 3)
print('Potenciação', 2 ** 10)
print('Módulo', 10 % 3)
```
_____________________

Operadores Lógicos(IF/ELSE):
<br>
- [x] Validação de Login

```python
user = input('Nome do usuário: ')
password = input('Senha do usuário: ')

user_bd = 'Lucas'
password_bd = '123456'

if user_bd == user and password_bd == password:
    print ('Acesso liberado')
else:
    print ('Acesso Negado! Usuário ou senha inválidos')
```

_____________________

Função Length:

```python
usuario = input('Digite seu nome: ')
qtde_caracteres = len(usuario)
print(f'{usuario} sou nome tem {qtde_caracteres} caracteres')
```
ou
```python
usuario = input('Digite seu nome: ')
print(f'{usuario} sou nome tem {len (usuario)} caracteres')
```
## Instrutor

- [Luis Guimaraes](https://www.linkedin.com/in/luisguima/)
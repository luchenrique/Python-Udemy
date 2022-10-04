# [Curso de Python do Básico ao Avançado - Udemy](https://www.udemy.com/course/python-3-do-zero-ao-avancado/)

👋🏽 Olá, estou aperfeiçoando meus conhecimento na linguagem Python.🐍 <br>
Esse é um repositório onde irei colocar alguns projetos e taferas aprendidos no curso a cima. 📚

## Projetos
✔️ Calculadora de IMC
<br>
⌛️ Validação de CPF

_____________________

## Módulos
**[1- Lógica de Programação (Python Básico)](https://github.com/luchenrique/Python-Udemy#1-m%C3%B3dulo---l%C3%B3gica-de-programa%C3%A7%C3%A3o)**
- [x] Tipos de Dados
- [x] Operadores Aritméticos
- [x] Operadores Lógicos (IF/ELSE)
- [x] Função Length
- [x] Função While
- [x] Estrutura de Repetição (For in)

**[2- Programação Procedural (Python Intermediário)](https://github.com/luchenrique/Python-Udemy#2-m%C3%B3dulo---programa%C3%A7%C3%A3o-procedural)**

**[3- Introdução à Programação Orientada a Objetos | POO)](https://github.com/luchenrique/Python-Udemy#3-m%C3%B3dulo---introdu%C3%A7%C3%A3o-%C3%A0-programa%C3%A7%C3%A3o-orientada-a-objetos)**

**[4- os, datetime, sys, json, csv, selenium, pillow etc](https://github.com/luchenrique/Python-Udemy#4-m%C3%B3dulo---os-datetime-sys-json-csv-selenium-pillow-etc)**

**[5- PyQT5 - Interface gráfica no Python - GUI para Desktop](https://github.com/luchenrique/Python-Udemy#5-m%C3%B3dulo---pyqt5---interface-gr%C3%A1fica-no-python---gui-para-desktop)**

**[6- Bases de dados com Python - SQLite, MySQL e MariaDB](https://github.com/luchenrique/Python-Udemy#6-m%C3%B3dulo---bases-de-dados-com-python---sqlite-mysql-e-mariadb)**

**[7- Django no Python - Básico](https://github.com/luchenrique/Python-Udemy#7-m%C3%B3dulo---django-no-python---b%C3%A1sico)**

**[8- Django no Python - Projeto Agenda](https://github.com/luchenrique/Python-Udemy#8-m%C3%B3dulo---django-no-python---projeto-agenda)**

**[9- Django com Python - Primeiro Deploy (Linux)](https://github.com/luchenrique/Python-Udemy#9-m%C3%B3dulo---django-com-python---primeiro-deploy-linux)**

**[10- Django com Python - Projeto Blog](https://github.com/luchenrique/Python-Udemy#10-m%C3%B3dulo---django-com-python---projeto-blog)**


_____________________

## 1° Módulo - Lógica de Programação

#### Tipos de Dados:
- Datatypes que são aceitos no Python.
<br>

- [x] str - string 
- [x] int- inteiros 
- [x] float - real
- [x] bool - booleano/lógico

_____________________

#### Operadores Aritméticos:

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

#### Operadores Lógicos (IF/ELSE):
- Função que só será aceita caso a condição for verdadeira. Como no exemplo abaixo, o usuário será liberado somente se o 'user' e a 'password' fornecida forem iguais as que estão salvas no banco de dados -> 'user_bd' & 'password_bd', caso ontrário o usuário irá receber a mensagem 'Acesso Negado! Usuário ou senha inválidos'.
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

#### Função Length:
- Função que mostra quantos caracteres tem uma respectiva variável.

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

_____________________

#### Função While:
- Uma estrutura de repetição que assim como, a função IF, necessiva de uma condição verdadeira que ela possa ser aceita.
No exemplo abaixo para que a calculadora se inicie é necessável que o usuário forneça o valor 1, assim, o sistema irá ser iniciado, possibilitando que o usuário possa fazer suas operações.

```python
print('\n'*2)
x1 = int(input('Digite 1 para iniciar a calculadora! '))

while x1 == 1:
    n1 = int(input('Digite um número: '))
    op = input('Digite um operador (+, -, * ou /): ')
    n2 = int(input('Digite outro número: '))

    if op == '+':
        print(f'O valor da soma é de {n1 + n2}')
    elif op == '-':
        print(f'O valor da subtração é de {n1 - n2}')
    elif op == '*':
        print(f'O valor da multiplicação é de {n1 * n2}')
    elif op == '/':
        print(f'O valor da divisão é de {n1 / n2:.2f}')
    else:
        print('Operador inválido')

    x1 = int(input('\nDigite 1 para continuar ou 0 para parar! '))

    if x1 != 1:
        print('\n\nO programa será encerrado! \n\nPrograma Encerrado!!')
    else:
        print('Valor inválido')
```

_____________________

#### Estrutura de Repetição (For in):
- Outra estrutura de repetição porém mais prática que a função while. O exemplo abaixo é de uma contagem regressiva de 10 minutos, os valores são definicos na função 'range' e vão caindo de 1 em 1.

```python
# Função range(start=0, stop, step=1)

seg = 59
min = 9
print('10:00')
for min in range (9, -1, -1):
    for seg in range (59, -1, -1):
        print(f'{min:02d}:{seg:02d}')
```

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"> 

## 2° Módulo - Programação Procedural

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"> 

## 3° Módulo - Introdução à Programação Orientada a Objetos

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"> 

## 4° Módulo - os, datetime, sys, json, csv, selenium, pillow etc

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"> 

## 5° Módulo - PyQT5 - Interface gráfica no Python - GUI para Desktop

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"> 

## 6° Módulo - Bases de dados com Python - SQLite, MySQL e MariaDB

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"> 

## 7° Módulo - Django no Python - Básico

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"> 

## 8° Módulo - Django no Python - Projeto Agenda

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"> 

## 9° Módulo - Django com Python - Primeiro Deploy (Linux)

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"> 

## 10° Módulo - Django com Python - Projeto Blog

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"> 

## Instrutor

- [Luis Guimaraes](https://www.linkedin.com/in/luisguima/)

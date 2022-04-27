import PySimpleGUI as sg
import mysql.connector
from mysql.connector import Error



class Criar_Conexao:
    def __init__(self, host, user, password, banco_dados=None):
        self.host = host
        self.user = user
        self.password = password
        self.banco_dados = banco_dados
    
    def criar_conexao(self):
        try:
            banco = mysql.connector.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                database = self.banco_dados,
            )
        except mysql.connector.errors.InterfaceError:
            font = ("Helvica, 16")
            sg.popup(f'{"Servidor Offline!":^48}\nInicie o servidor e tente novamente!', title='Erro', font=font, )
            quit()
        return banco
    
    def criar_Banco(nome_banco):
        conexao = Criar_Conexao('localhost', 'root', '')
        banco = conexao.criar_conexao()
        cursor = banco.cursor()

        try:
            sql = f'CREATE DATABASE IF NOT EXISTS {nome_banco}'
            cursor.execute(sql)
            cursor.execute(f'use {nome_banco}')
            sql2 = 'CREATE TABLE IF NOT EXISTS cadastros (id INT PRIMARY KEY AUTO_INCREMENT NOT NULL, usuario VARCHAR(200) NOT NULL UNIQUE, senha VARCHAR(200) NOT NULL)'
            cursor.execute(sql2)
            sql3 = 'CREATE TABLE IF NOT EXISTS senhas (id INT PRIMARY KEY AUTO_INCREMENT NOT NULL, login VARCHAR(200) NOT NULL, senha VARCHAR(200) NOT NULL, site VARCHAR(200) NOT NULL, proprietario VARCHAR(200) NOT NULL)'
            cursor.execute(sql3)
            # sql4 = 'CREATE TABLE IF NO EXISTS cotacoes ()'
            # cursor.execute(sql4)
            # sql5 = ''
            # cursor.execute(sql5)       
        except Error as error:
            sg.popup(f'{error}', title='Erro')
            return False
        else:
            if banco.is_connected():
                sg.popup(f'Conexão estabelecida com sucesso!', title='Sucesso')
                return True 
            else:
                sg.popup(f'Não foi possível estabelecer conexão!', title='Erro')


class Funcoes:
    def MOSTRAR_GERENCIADOR_SENHAS(janela):
        janela['-GERENCIADOR_SENHA-'].update(visible=True)
        janela['-GERADOR_COTACAO-'].update(visible=False)
        janela['-GERENCIADOR_CARTAO-'].update(visible=False)
        janela['-ADICIONAR_SALDO-'].update(visible=False)
        janela['-DETALHAMENTO-'].update(visible=False)
        
        
    def MOSTRAR_GERADOR_COTACOES(janela):
        janela['-GERADOR_COTACAO-'].update(visible=True)
        janela['-GERENCIADOR_SENHA-'].update(visible=False)
        janela['-GERENCIADOR_CARTAO-'].update(visible=False)
        janela['-ADICIONAR_SALDO-'].update(visible=False)
        janela['-DETALHAMENTO-'].update(visible=False)
        
        
    def MOSTRAR_GERENCIADOR_CARTOES(janela):
        janela['-GERENCIADOR_CARTAO-'].update(visible=True)
        janela['-GERENCIADOR_SENHA-'].update(visible=False)
        janela['-GERADOR_COTACAO-'].update(visible=False)
        janela['-ADICIONAR_SALDO-'].update(visible=False)
        janela['-DETALHAMENTO-'].update(visible=False)
        
        
    def MOSTRAR_ADICIONAR_SALDO(janela):
        janela['-ADICIONAR_SALDO-'].update(visible=True)
        janela['-GERENCIADOR_SENHA-'].update(visible=False)
        janela['-GERADOR_COTACAO-'].update(visible=False)
        janela['-GERENCIADOR_CARTAO-'].update(visible=False)
        janela['-DETALHAMENTO-'].update(visible=False)
    
    
    def MOSTRAR_DETALHES(janela):
        janela['-DETALHAMENTO-'].update(visible=True)
        janela['-ADICIONAR_SALDO-'].update(visible=False)
        janela['-GERENCIADOR_SENHA-'].update(visible=False)
        janela['-GERADOR_COTACAO-'].update(visible=False)
        janela['-GERENCIADOR_CARTAO-'].update(visible=False)
    
    
    def MOSTRAR_VER_SENHAS(janela):
        janela['-INCLUIR_SENHA-'].update(visible=False)
        janela['-VER_SENHAS-'].update(visible=True)
        janela['-ALTERAR_SENHA-'].update(visible=False)
        janela['-APAGAR_SENHA-'].update(visible=False)
    
    def MOSTRAR_INCLUIR_SENHA(janela):
        janela['-INCLUIR_SENHA-'].update(visible=True)
        janela['-VER_SENHAS-'].update(visible=False)
        janela['-ALTERAR_SENHA-'].update(visible=False)
        janela['-APAGAR_SENHA-'].update(visible=False)
    
    def MOSTRAR_ALTERAR_SENHA(janela):
        janela['-INCLUIR_SENHA-'].update(visible=False)
        janela['-VER_SENHAS-'].update(visible=False)
        janela['-ALTERAR_SENHA-'].update(visible=True)
        janela['-APAGAR_SENHA-'].update(visible=False)
    
    def MOSTRAR_APAGAR_SENHA(janela):
        janela['-INCLUIR_SENHA-'].update(visible=False)
        janela['-VER_SENHAS-'].update(visible=False)
        janela['-ALTERAR_SENHA-'].update(visible=False)
        janela['-APAGAR_SENHA-'].update(visible=True)
    
    
    
    
    
    
    
    
    
    
    
    
    
     
    def cadastrar_usuarios(valor):
        conexao = Criar_Conexao('localhost', 'root', '')
        banco = conexao.criar_conexao()
        cursor = banco.cursor()
        cursor.execute('use dados')
        
        user = valor['-USUARIO-'].strip()
        password = valor['-SENHA-'].strip()
        
        if len(user) == 0 or len(password) == 0:
            sg.popup('Preencha todos os campos!', title='Erro')
        else:   
            cadastrar = f'INSERT INTO cadastros VALUES (null, "{user}", "{password}")'
            try:
                cursor.execute(cadastrar)
                banco.commit()
                sg.popup('Usuario cadastrado com sucesso!')
                return True
            except mysql.connector.errors.IntegrityError:
                sg.popup(f'Usuario já cadastrado!\n Tente outro Usuario ou faça login com ele', title='Erro')
            except Error as error:
                sg.popup(f'Erro inesperado: {error}', title='Erro Inesperado', )
            
    
    def get_id(usuario):
        conexao = Criar_Conexao('localhost', 'root', '')
        banco = conexao.criar_conexao()
        cursor = banco.cursor()
        cursor.execute('use dados')

        
        
        sql_id = f'SELECT id FROM cadastros WHERE usuario = "{usuario}"'
        cursor.execute(sql_id)
        id = cursor.fetchone()[0]
        return id
        
        
    def cadastrar_senha_gerenciador(valor, usuario):
            conexao = Criar_Conexao('localhost', 'root', '')
            banco = conexao.criar_conexao()
            cursor = banco.cursor()
            cursor.execute('USE dados')
            
            id_proprietario = Funcoes.get_id(usuario)
            login = valor['-LOGIN_INCLUIR-']
            senha = valor['-SENHA_INCLUIR-']
            site = valor['-SITE_INCLUIR-']
            
            if len(login) == 0 or len(site) == 0 or len(senha) == 0:
                sg.popup('Preencha todos os campos!')
            else:
                try:
                    sql = f'INSERT INTO senhas VALUES(null, "{login}", "{senha}", "{site}", "{id_proprietario}")'
                    cursor.execute(sql)
                    banco.commit()
                except Error as error:
                    sg.popup(f'Erro inesperado: {error}', title='Erro Inesperado', )
                else:
                    sg.popup(f'Senha cadastrada com sucesso!', title='Sucesso')
            pass     
        
        
    def autenticar_login(valor):
        conexao = Criar_Conexao('localhost', 'root', '')
        banco = conexao.criar_conexao()
        cursor = banco.cursor()
        cursor.execute('use dados')
        
        usuario = valor['-USUARIO-'].strip()
        senha = valor['-SENHA-'].strip()
        if len(usuario) == 0 or len(senha) == 0:
            sg.popup('Preencha todos os campos!', title='Campos Incompletos')
        else:
            try:
                sql_usuario = f'SELECT usuario FROM cadastros WHERE id = "{Funcoes.get_id(usuario)}"'
                cursor.execute(sql_usuario)
                usuario_recuperado = cursor.fetchone()[0]
                
                sql_senha = f'SELECT senha FROM cadastros WHERE id = "{Funcoes.get_id(usuario)}"'
                cursor.execute(sql_senha)
                senha_recuperada = cursor.fetchone()[0]
                
                if usuario == usuario_recuperado and senha == senha_recuperada:
                    sg.popup(f'Login efetuado com Sucesso!', title='Sucesso')
                    return True
                else:
                    sg.popup(f'Usuario ou senha incorretos!\nVerifique e tente novamente!', title='Usuario ou senha incorretos')
                    return False
            except Error as error:
                sg.popup(f'{error}')
            except TypeError:
                sg.popup(f'Usuario ou senha incorretos!\nVerifique e tente novamente!', title='Usuario ou senha incorretos')
            
    
    
    def retornar_senhas_bd(valor):
        conexao = Criar_Conexao('localhost', 'root', '')
        banco = conexao.criar_conexao()
        cursor = banco.cursor()
        cursor.execute('use dados')
        
        try:
            usuario_atual = valor['-USUARIO-']
        except KeyError:
            usuario_atual = valor['-USUARIO_ATUAL-']
        
        id_proprietario = Funcoes.get_id(usuario_atual)
        cursor.execute(f'SELECT id, login, senha, site FROM senhas WHERE proprietario = "{id_proprietario}"')
        dados = cursor.fetchall()
        return dados
    
            
class Conta_Corrente:
    pass
import PySimpleGUI as sg
from sistemas.funcoes import Criar_Conexao as CC
from sistemas.telas import Telas as t
from sistemas.funcoes import Funcoes as f
from sistemas.icones import icone_autenticar

autenticacao = False
criar_banco = CC.criar_Banco('dados')
conexao = CC('localhost', 'root', '',)
banco = conexao.criar_conexao()
tela_login, tela_cadastro, tela_principal = None, None, None


if criar_banco:
    tela_login = t.autenticar()
    tela_login.SetIcon(pngbase64=icone_autenticar)
else:
    quit()


while True:
    janela, evento, valor = sg.read_all_windows()
    
    if evento == sg.WIN_CLOSED:
        if sg.popup('Deseja mesmo fechar o app ?', title='Confirmação', custom_text=('Sim', 'Não'), font=("Helvica, 14")) == 'Sim':  
            break
        else:
            pass
    elif janela == tela_login and evento == '-FECHAR-':
        if sg.popup('Deseja mesmo fechar o app  ?', title='Confirmação', custom_text=('Sim', 'Não'), font=("Helvica, 14")) == 'Sim':
            break
        else:
            pass
    
    elif janela == tela_cadastro and evento == '-VOLTAR-':
        tela_cadastro.close()
        tela_login = t.autenticar()
    
    elif janela == tela_login and evento == '-ENTRAR-':
        autenticacao = f.autenticar_login(valor)
        if autenticacao:
            tela_login.close()
            tela_principal = t.tela_principal(valor) 
        
    elif janela == tela_login and evento == '-CADASTRAR_USUARIO-':
        tela_login.close()
        tela_cadastro = t.cadastrar_login()
    
    elif janela == tela_cadastro and evento == '-CADASTRAR_USUARIO-':
        cadastro = f.cadastrar_usuarios(valor)
        if cadastro:
            tela_cadastro.close()
            tela_login = t.autenticar()
            
    elif janela == tela_principal and evento == '-BTN_GERENCIADOR_SENHA-':
        f.MOSTRAR_GERENCIADOR_SENHAS(janela)

    elif janela == tela_principal and evento == '-BTN_GERADOR_COTACAO-':
        f.MOSTRAR_GERADOR_COTACOES(janela)
    
    elif janela == tela_principal and evento == '-BTN_GERENCIADOR_CARTAO-':
        f.MOSTRAR_GERENCIADOR_CARTOES(janela)
        
    elif janela == tela_principal and evento == '-BTN_ADICIONAR_SALDO-':
        f.MOSTRAR_ADICIONAR_SALDO(janela)
    
    elif janela == tela_principal and evento == '-BTN_DETALHAMENTO-':
        f.MOSTRAR_DETALHES(janela)
        
    elif janela == tela_principal and evento == '-BTN_VER_SENHAS-':
        f.MOSTRAR_VER_SENHAS(janela)
    
    elif janela == tela_principal and evento == '-ATUALIZAR_SENHAS-':
        janela['-SENHAS_ATUAIS-'].update(f.retornar_senhas_bd(valor))
    
    elif janela == tela_principal and evento == '-BTN_ADICIONAR_SENHA-':
        f.MOSTRAR_INCLUIR_SENHA(janela)
        
    elif janela == tela_principal and evento == '-SALVAR-':
        usuario = valor['-USUARIO_ATUAL-']
        f.cadastrar_senha_gerenciador(valor, usuario)
        
    elif janela == tela_principal and evento == '-BTN_ALTERAR_SENHA-':
        f.MOSTRAR_ALTERAR_SENHA(janela)
        
    elif janela == tela_principal and evento == '-BTN_APAGAR_SENHA-':
        f.MOSTRAR_APAGAR_SENHA(janela)
        
    elif janela == tela_principal and evento == '-SALVAR-':
        pass
        
    elif janela == tela_principal and evento == '-SAIR-':
        if sg.popup('Deseja se desconectar ?', title='Confirmação', custom_text=('Sim', 'Não'), font=("Helvica, 14")) == 'Sim':
            tela_principal.close()
            tela_login = t.autenticar()
        else:
            pass
        
    
    
    
    



    
    
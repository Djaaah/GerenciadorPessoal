import PySimpleGUI as sg
from sistemas.funcoes import Criar_Conexao as CC
from sistemas.funcoes import Funcoes as f
import sistemas.icones as si

class Telas:
    def tela_principal(valor):
        usuario = valor['-USUARIO-']
        usuario = usuario.title()
        font = ("Helvica, 13")
        
        layout_btn = [
            [sg.Button('',image_data=(si.icone_gerenciador_senha), key='-BTN_GERENCIADOR_SENHA-', border_width=0, button_color=(sg.theme_background_color(), sg.theme_background_color()), tooltip='Gerenciador de Senhas'), 
             sg.Button('',image_data=(si.icone_gerador_cotacao), key='-BTN_GERADOR_COTACAO-', border_width=0, button_color=(sg.theme_background_color(), sg.theme_background_color()), tooltip='Gerador de Cotações'), 
             sg.Button('',image_data=(si.icone_gerenciador_cartao), key='-BTN_GERENCIADOR_CARTAO-', border_width=0, button_color=(sg.theme_background_color(), sg.theme_background_color()), tooltip='Gerenciador de Cartão de crédito'),
             sg.Button('',image_data=(si.icone_adicionar_saldo), key='-BTN_ADICIONAR_SALDO-', border_width=0, button_color=(sg.theme_background_color(), sg.theme_background_color()), tooltip='Adicionar Saldo')],
        ]
        
        layout_infos = [
            [sg.Text("Olá,", font=font), sg.Input(f'{usuario}', key='-USUARIO_ATUAL-', tooltip="Usuario", font=font, readonly=True, border_width=0, disabled_readonly_background_color=sg.theme_background_color())],
            [sg.Text(f'Saldo Atual {"R$ 0,00"}', font=font, key='-SALDO-')],
            [sg.Button(f'Detalhamentos', font=font, key='-BTN_DETALHAMENTO-', size=(16,1), border_width=0, button_color=('White', 'Blue'), mouseover_colors='Green', )],
            [sg.Button('Sair', key='-SAIR-', border_width=0, size=(16,1), button_color=('White', 'Red'), font=font,  mouseover_colors='Red')],
        ]
        
        layout = [
            [sg.Text(f'{"---"*1000}')],
            [sg.Text(' '*3),
             sg.Column(layout_btn), 
             sg.Column(layout_infos)],
            [sg.Text(f'{"---"*1000}')],
            [sg.Frame('Gerenciador de Senhas', Telas.app_gerenciar_senha(valor), visible=False, key='-GERENCIADOR_SENHA-', size=(680,700), border_width=0, element_justification='center', title_location='n', font=("Futura, 16"), ), 
             sg.Frame('Gerador de Cotações', Telas.app_gerar_cotacao(), visible=False, key='-GERADOR_COTACAO-', size=(680,700), border_width=0, element_justification='center', title_location='n', font=("Futura, 16")), 
             sg.Frame('Gerenciador de Cartão de Crédto', Telas.app_gerenciar_cartao(), visible=False, key='-GERENCIADOR_CARTAO-', border_width=0, size=(680,700), element_justification='center', title_location='n', font=("Futura, 16")),
             sg.Frame('Adicionar Saldo', Telas.app_adicionar_saldo(), visible=False, key='-ADICIONAR_SALDO-', size=(680,700), border_width=0, element_justification='center', title_location='n', font=("Futura, 16")),
             sg.Frame('Detalhamento das Contas', Telas.app_detalhamentos(), visible=False, key='-DETALHAMENTO-', size=(680,700), border_width=0, element_justification='center', title_location='n', font=("Futura, 16"))],
        ]
        
        return sg.Window('Gerenciador Pessoal', layout=layout, finalize=True, size=(680,700))

    
    def autenticar():
        sg.theme('Dark')
        
        layout = [
            [sg.Text('Usuario', size=(7,1)), sg.Input(key='-USUARIO-', border_width=0)],
            [sg.Text('Senha', size=(7,1)), sg.Input(key='-SENHA-', password_char='*', border_width=0)],
            [sg.Text(' '*23), sg.Button('Entrar', key='-ENTRAR-', border_width=0, mouseover_colors='Green', button_color=('Black', '#FFD700'), size=(10,1)), sg.Button('Fechar', key='-FECHAR-', border_width=0, mouseover_colors='Red', button_color=('Black', '#FFD700'), size=(10,1))],
            [sg.Text(' '*23), sg.Button('Cadastrar Usuario', key='-CADASTRAR_USUARIO-', border_width=0, size=(22,1), button_color=('White', '#4169E1')),],
        ]

        return sg.Window('Login', layout=layout, finalize=True)
    
    
    def cadastrar_login():
        sg.theme('Dark')
        
        layout = [
            [sg.Text('Usuario', size=(7,1)), sg.Input(key='-USUARIO-', border_width=0)],
            [sg.Text('Senha', size=(7,1)), sg.Input(key='-SENHA-', password_char='*', border_width=0)],
            [sg.Text(' '*14), sg.Button('Cadastrar Usuario', key='-CADASTRAR_USUARIO-', border_width=0, size=(22,1), button_color=('White', '#4169E1'), mouseover_colors='Green'),sg.Button('Voltar', key='-VOLTAR-', border_width=0, mouseover_colors='Red', button_color=('Black', '#FFD700'), size=(15,1))],
        ]

        return sg.Window('Cadastro', layout=layout, finalize=True)
    
    
    def app_gerenciar_senha(valor):
        
        layout = [
            [sg.Button('Ver Senhas', key='-BTN_VER_SENHAS-'), sg.Button('Adicionar Senha', key='-BTN_ADICIONAR_SENHA-'),
            sg.Button('Alterar Senha', key='-BTN_ALTERAR_SENHA-'), sg.Button('Apagar Senha', key='-BTN_APAGAR_SENHA-')],
            [sg.Frame('Ver Senhas', Telas.ver_senhas(valor), size=(680,700), element_justification='center', title_location='n', visible=False, key='-VER_SENHAS-', ),
             sg.Frame('Adicionar Senha', Telas.incluir_senha(), size=(700,150), element_justification='center', title_location='n', visible=False, key='-INCLUIR_SENHA-'),
             sg.Frame('Alterar Senha', Telas.alterar_senha(), size=(700,200), element_justification='center', title_location='n', visible=False, key='-ALTERAR_SENHA-'),
             sg.Frame('Apagar Senha', Telas.apagar_senha(), size=(700,200), element_justification='center', title_location='n', visible=False, key='-APAGAR_SENHA-')]
            
        ]

        return layout
    
    def ver_senhas(valor):
        cabecalho = ['ID', 'Login', 'Senha', 'Site']
        layout = [
            [sg.Table(headings=cabecalho, values=f.retornar_senhas_bd(valor),
                      justification='center',
                      num_rows=10,
                      auto_size_columns=True,
                      key = '-SENHAS_ATUAIS-',
            )],
            [sg.Button('Atualizar', key='-ATUALIZAR_SENHAS-')]
        ]
        
        return layout
    
    def incluir_senha():
        layout = [
            [sg.Text('Login', size=(8,1)), sg.Input('', do_not_clear=False, key='-LOGIN_INCLUIR-', size=(40,1), border_width=0)],
            [sg.Text('Senha', size=(8,1)), sg.Input('', do_not_clear=False, key='-SENHA_INCLUIR-', size=(40,1), border_width=0)],
            [sg.Text('Site', size=(8,1)), sg.Input('', do_not_clear=False, key='-SITE_INCLUIR-', size=(40,1), border_width=0)],
            [sg.Text(' '*15), sg.Button('Salvar', key='-SALVAR-', size=(20,1), border_width=0, button_color=('Black', '#FFD700'), tooltip='Salvar')]
        ]
        
        return layout
    
    def alterar_senha():
        layout = [
            [sg.Text('ID', size=(8,1)), sg.Input('', do_not_clear=False, key='-ID-', size=(10,1), border_width=0), sg.Button('Pesquisar', key='-PESQUISAR_SENHA-', border_width=0, button_color=('Black', '#FFD700'), tooltip='Pesquisar')],
            [sg.Text('Login', size=(8,1), visible=False), sg.Input('', do_not_clear=False, key='-LOGIN_ALTERAR-', size=(40,1), border_width=0, visible=False)],
            [sg.Text('Senha', size=(8,1), visible=False), sg.Input('', do_not_clear=False, key='-SENHA_ALTERAR-', size=(40,1), border_width=0, visible=False)],
            [sg.Text('Site', size=(8,1), visible=False), sg.Input('', do_not_clear=False, key='-SITE_ALTERAR-', size=(40,1), border_width=0, visible=False)],
            [sg.Text(' '*15), sg.Button('Salvar', visible=False, key='-ALTERAR-', size=(20,1), border_width=0, button_color=('Black', '#FFD700'), tooltip='Salvar')]
        ]
        
        return layout
    
    def apagar_senha():
        layout = [
            [sg.Text('ID', size=(8,1)), sg.Input('', do_not_clear=False, key='-ID-', size=(10,1), border_width=0), sg.Button('Pesquisar', key='-PESQUISAR_SENHA-', border_width=0, button_color=('Black', '#FFD700'), tooltip='Pesquisar')],
            [sg.Text('Login', size=(8,1), visible=False), sg.Input('', do_not_clear=False, key='-LOGIN_APAGAR-', size=(40,1), border_width=0, visible=False)],
            [sg.Text('Senha', size=(8,1), visible=False), sg.Input('', do_not_clear=False, key='-SENHA_APAGAR-', size=(40,1), border_width=0, visible=False)],
            [sg.Text('Site', size=(8,1), visible=False), sg.Input('', do_not_clear=False, key='-SITE_APAGAR-', size=(40,1), border_width=0, visible=False)],
            [sg.Text(' '*15), sg.Button('Apagar', key='-APAGAR-', size=(20,1), visible=False, border_width=0, button_color=('Black', '#FFD700'), tooltip='Salvar', )]
        ]
        
        return layout
    
    
    
    
    
    
    
    
    
    def app_gerenciar_cartao():

        layout = [
            [sg.Text('Gerenciador de Cartões')]
        ]

        return layout
    
    def app_gerar_cotacao():

        layout = [
            [sg.Text('Gerador de Cotações')]
        ]

        return layout
    
    def app_adicionar_saldo():
        
        layout = [
            [sg.Text('Adicionar Saldo')]
        ]

        return layout
    
    def app_detalhamentos():
        
        layout = [
            
        ]
        return layout
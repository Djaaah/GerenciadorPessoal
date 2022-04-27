import PySimpleGUI as sg
from sistemas.funcoes import Criar_Conexao as CC
from sistemas.funcoes import Funcoes as f
import sistemas.icones as si


criar_banco = CC.criar_Banco('')
conexao = CC('localhost', 'root', '',)
banco = conexao.criar_conexao()
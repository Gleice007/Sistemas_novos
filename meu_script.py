from pywinauto.application import Application
from pywinauto.timings import TimeoutError
import time

# Inicia o Bloco de Notas utilizando o backend 'uia'
app = Application(backend="uia").start("notepad.exe")

time.sleep(3)
# Seleciona a janela principal do Bloco de Notas
dlg = app.window(title_re=".*Bloco de Notas")

# Digita algum texto
dlg.Edit.type_keys("Este é um teste com pywinauto!", with_spaces=True)
time.sleep(3)
# Clica no menu Arquivo e escolhe Sair
dlg.menu_select("Arquivo -> Sair")

# Aguarda pela janela de confirmação
confirmation_dialog = app.window(title_re=".*Bloco de Notas")

try:
    # Localiza o botão "Não Salvar" utilizando propriedades da API UI Automation
    nao_salvar_button = confirmation_dialog.child_window(
        title="Não Salvar",
        control_type="Button",
        auto_id="CommandButton_7"
    )
    nao_salvar_button.wait('enabled', timeout=10)
    nao_salvar_button.click()
except TimeoutError:
    print("O botão 'Não Salvar' não foi encontrado ou não ficou disponível a tempo.")



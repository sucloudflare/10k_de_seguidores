import PySimpleGUI as sg
import webbrowser

sg.theme('Black')  # Set the theme to 'Black'

def create_login_window():
    layout = [
        [sg.Text('Ganhe 10k de seguidores', font=('Arial', 16), text_color='white')],
        [sg.Text('Faça o login do Instagram', font=('Arial', 12), text_color='white')],
        [sg.Text('Usuário', font=('Arial', 12), text_color='white'), sg.Input(key='usuario')],
        [sg.Text('Senha', font=('Arial', 12), text_color='white'), sg.Input(key='senha', password_char='*')],
        [sg.Checkbox('Salva o login', font=('Arial', 12), text_color='white')],
        [sg.Button('Entrar', size=(10, 1))]
    ]
    return sg.Window('Tela de login', layout, background_color='black')

def create_welcome_window():
    layout = [
        [sg.Text('Eai Cidadão', font=('Arial', 20), text_color='white')],
        [sg.Text('Vc foi Hackeado', font=('Arial', 16), text_color='white')],
        [sg.Text("Clica aqui", font=('Arial', 12), text_color='white')],
        [sg.Button('DeepWeb', size=(10, 1))]
    ]
    return sg.Window('Entrar', layout, background_color='black')

def main():
    login_window = create_login_window()

    while True:
        login_event, login_values = login_window.read()

        if login_event == sg.WIN_CLOSED:
            break
        elif login_event == 'Entrar':
            # You can add authentication logic here
            login_window.close()

            welcome_window = create_welcome_window()

            while True:
                welcome_event, _ = welcome_window.read()

                if welcome_event == sg.WIN_CLOSED or welcome_event == 'Fechar':
                    welcome_window.close()
                    break

                if welcome_event == 'DeepWeb':
                    webbrowser.open('https://github.com/sucloudflare')

if __name__ == "__main__":
    main()

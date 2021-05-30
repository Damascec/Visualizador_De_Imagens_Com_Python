import PySimpleGUI as sg
import os.path

# Janela com o layout de duas colunas

file_list_column = [
    [

    sg.Text('Image Folder'),
    sg.In(size=(25,1), enable_events=True, key='-FOLDER-'),
    sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40,20),
            key='-FILE LIST-'
        )

    ],

]

# Tela que vai aparecer a imagem escolhida
image_viewer_column = [
    
        [sg.Text('Escolha uma imagem da lista para aparecer ao lado')],
        [sg.Text(size=(40,1), key='-TOUT-')],
        [sg.Image(key='-IMAGE-')],
]

layout = [
    [
        sg.Column(file_list_column),
        sg.VSeparator(),
        sg.Column(image_viewer_column),
    ]
]

window = sg.Window('Image Viewer', layout)

# event loop

while True:
    event, values = window.read()
    if event == 'EXIT' or event == sg.WIN_CLOSED:
        break
    # nome da pasta selecionada na lista de arquivos
    if event == '-FOLDER-':
        folder = values['-FOLDER-']
        try:
            # pega a lista de arquivos na pasta
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            # Filtrando os arquivos pela extensão
            f 
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith(('.png', '.gif', '.jpg'))
        ]
        
        window['-FILE LIST-'].update(fnames)
    elif event == '-FILE LIST-': # arquivo escolhido da lista
        try:
            filename = os.path.join(
                values['-FOLDER-'], values['-FILE LIST-'] [0]
            )
            window['-TOUT-'].update(filename)
            window['-IMAGE-'].update(filename=filename)
        except:
            pass
window.close()
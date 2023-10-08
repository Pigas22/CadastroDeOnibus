def Popup_Padrao(titulo, texto):
    import PySimpleGUI as sg
    from main import detalhes

    sg.theme(detalhes['tema'])

    
    return sg.popup(titulo, texto, background_color= detalhes['corFundo'], any_key_closes= True, text_color= 'White', font= f'{detalhes["fonte"]} {detalhes["tamanhoFonte"]}')

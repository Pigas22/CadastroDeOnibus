def Popup_Save():
    import PySimpleGUI as sg
    from interface.Detalhes import detalhes

    sg.theme(detalhes['tema'])
    
    return sg.popup_yes_no('Salvar as alterações?', background_color= detalhes['corFundo'], text_color= 'White', font= f'{detalhes["fonte"]} {detalhes["tamanhoFonte"]}')

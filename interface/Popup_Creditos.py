def Popup_Creditos(): # a ser feito
    from interface.Detalhes import detalhes
    import PySimpleGUI as sg
    
    sg.theme(detalhes["tema"])
    
    return sg.popup('Grupo de Projeto: ', '| Samuel Paiva Paizante \n| Vinícius Rocha Aleixo \n| Thiago Holz Coutinho', background_color= detalhes["corFundo"], text_color= 'White', font= f'{detalhes["fonte"]} {detalhes["tamanhoFonte"]}', any_key_closes= True, keep_on_top= True)

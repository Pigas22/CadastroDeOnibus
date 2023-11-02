def PopupCreditosImagens():
    from interface.Detalhes import detalhes
    import PySimpleGUI as sg
    
    sg.theme(detalhes["tema"])

    texto = ("| Creatype" + 
             "\n| Imagens PNG" + 
             "\n| Kiranshastry" +
             "\n " +
             "\nMais detalhes no arquivo 'creditos.txt' nos arquivos do App.")
    
    return sg.popup('Crédito das Imagens: ', texto, background_color= detalhes["corFundo"], text_color= 'White', font= f'{detalhes["fonte"]} {detalhes["tamanhoFonte"]}', any_key_closes= True, keep_on_top= True)

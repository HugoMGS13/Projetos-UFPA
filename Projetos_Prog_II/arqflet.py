import flet as ft

def main(pagina): #função pra criar a página como se fosse tk.page() no tkinter
    def save_login(evento): #função do botão
        if not nome.value:
            nome.error_text = "Digite algo, por favor" #Setar uma mensagem de erro caso a condição for atendida
            pagina.update() #Para atualizar a página e mostrar o erro
        else:
            name = nome.value #Name recebe o valor colocado na variável nome
            print(f'Nome: {name}')

            pagina.clean() #tirar todos os elementos da página

            pagina.add(
                ft.Text(f'Olá, {name} \nSeja bem-vindo!', size=50)
            )
    ola = ft.Text(value="Olá, mundo!", size=30) #função flet que mostra um texto na tela (igual o label no tkinter)

    nome = ft.TextField(label='Digite seu nome') #Caixa de texto que recebe textos do usuário (Label siginfica a mensagem da caixa)

    pagina.add( #adicionar coisas na página
        ola,
        nome,
        ft.ElevatedButton('Pronto', on_click=save_login) #criar botão # o 'on_click' mostra qual função vai ser executada no click do botão
    )

    pagina.update() #pra atualizar as páginas com as novas atualizações feitas acima

ft.app(target=main) #função que roda a página como se fosse o mainloop() do tkinter
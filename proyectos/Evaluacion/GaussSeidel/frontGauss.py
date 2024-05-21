import flet as ft

def main(page: ft.Page):

    inputsA = [] #Los Inputs de A
    inputsB = [] #Los Inputs de A    
    A = [] #Matriz A donde seran almacenados los valores de los inputs
    B = [] #Matriz A donde seran almacenados los valores de los inputs


    fila = []
    columna = []

    page.bgcolor = ft.colors.INDIGO_900
    page.update()




    def btn_crearInputs(e):
        if not txt_name.value:
            txt_name.error_text = "Please enter your name"
            page.update()
        else:
            tamañoMatriz = int(txt_name.value)
            txt_name.value = ""

            page.add(ft.Text(f"Se ha creado su matriz de {tamañoMatriz} x {tamañoMatriz} , Ingrese las {tamañoMatriz} que desea encontrar del SEL"))


            textoEsIgual = ft.Text("=")

            for x in range(tamañoMatriz):
                inputsA.append(ft.TextField(label=f"Ingrese sus incognitas en el input separandolas por comas (x{x+1})", border_color=ft.colors.WHITE, fill_color=ft.colors.WHITE))

            for x in range(tamañoMatriz):
                inputsB.append(ft.TextField(label=f"Inputs de B (x{x+1})", border_color=ft.colors.WHITE,fill_color=ft.colors.WHITE, height=50, width=200,))
            
            for x in range(tamañoMatriz):
                fila.append(ft.Row(spacing=10))
                fila[x].controls.append(inputsA[x])
                fila[x].controls.append(textoEsIgual)
                fila[x].controls.append(inputsB[x])

                columna.append(ft.Column(spacing=10))
                columna[x].controls.append(fila[x])
                page.add(columna[x])

            page.add(ft.ElevatedButton("Ver lo ingresado en los inputsA", on_click=btn_mostrarValues))


    def btn_mostrarValues(e):

        for i in inputsA:
            A.append(list(map(int, i.value.split(','))))
        
        page.add(ft.Text(f"Se ha creado su matriz que desea encontrar del SEL: {A}"))


    titulo = ft.Text(f"Gauss-Seidel", color=ft.colors.WHITE ,size=30)

    txt_name = ft.TextField(label="Ingrese el tamaño de su matriz", border_color=ft.colors.WHITE,
    fill_color=ft.colors.WHITE, height=50, width=200,)

    page.add(
        ft.Container(
        content=titulo,
        margin=10,
        padding=10,
        alignment=ft.alignment.center,
        bgcolor=ft.colors.BLUE_900,
        width=1400,
        height=70,
        border_radius=10,
        )
    )

    page.add(txt_name, ft.ElevatedButton("Confirmar", on_click=btn_crearInputs))

ft.app(main)
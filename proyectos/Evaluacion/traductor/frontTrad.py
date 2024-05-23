import flet as ft
from traductor.traductorFun import dec_bin, dec_ter, dec_cua, dec_oct, dec_hex
from traductor.traductorFun import bin_dec, bin_ter, bin_cua, bin_oct, bin_hex
from traductor.traductorFun import ter_dec, ter_bin, ter_cua, ter_oct, ter_hex
from traductor.traductorFun import cua_dec, cua_bin, cua_ter, cua_oct, cua_hex
from traductor.traductorFun import oct_dec, oct_bin, oct_ter, oct_cua, oct_hex
from traductor.traductorFun import hex_dec, hex_bin, hex_ter, hex_cua, hex_oct



def frontTraductor(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.START

    #Funcion Limpiar
    def limpiar(e):
        inputNumero.value = ""
        inputResultado.value = ""
        opcion1.value = ""
        opcion2.value = ""
        page.update()


    def transformar(e):
        inputValue = int(inputNumero.value)
        inputResultadoValue = inputResultado.value 
        opcion1Value = opcion1.value
        opcion2Value = opcion2.value
        listaNumeros = []

        for i in str(inputValue):
            listaNumeros += i


        if opcion1Value == None:
            page.add(ft.Text(f"{opcion1Value}", color=ft.colors.WHITE ,size=30))
        
        if opcion2Value == None:
            page.add(ft.Text("Escoger opcion random", color=ft.colors.WHITE ,size=30))

        #Casos a hacer

        if(opcion1Value == "Decimal" and opcion2Value == "Binario"):
            resultado = dec_bin(inputValue)
            inputResultado.value = resultado
            page.update()
        elif (opcion1Value == "Decimal" and opcion2Value == "Ternario"):
            resultado = dec_ter(inputValue)
            inputResultado.value = resultado
            page.update()
        elif (opcion1Value == "Decimal" and opcion2Value == "Quaternario"):
            resultado = dec_cua(inputValue)
            inputResultado.value = resultado
            page.update()
        elif (opcion1Value == "Decimal" and opcion2Value == "Octal"):
            resultado = dec_oct(inputValue)
            inputResultado.value = resultado
            page.update()
        elif (opcion1Value == "Decimal" and opcion2Value == "Hexadecimal"):
            resultado = dec_hex(inputValue)
            inputResultado.value = resultado
            page.update()
        elif (opcion1Value == "Binario" and opcion2Value == "Decimal"):
            for i in listaNumeros:
                if "23456789":
                    inputNumero.value = "Error"
                    page.update()
                else:
                    resultado = bin_dec(inputValue)
                    inputResultado.value = resultado
                    page.update()
        elif (opcion1Value == "Binario" and opcion2Value == "Ternario"):
            for i in listaNumeros:
                if "23456789":
                    inputNumero.value = "Error"
                    page.update()
                else:
                    resultado = bin_ter(inputValue)
                    inputResultado.value = resultado
                    page.update()
        elif (opcion1Value == "Binario" and opcion2Value == "Quaternario"):
            for i in listaNumeros:
                if "23456789":
                    inputNumero.value = "Error"
                    page.update()
                else:            
                    resultado = bin_cua(inputValue)
                    inputResultado.value = resultado
                    page.update()
        elif (opcion1Value == "Binario" and opcion2Value == "Octal"):
            for i in listaNumeros:
                if "23456789":
                    inputNumero.value = "Error"
                    page.update()
                else:
                    resultado = bin_oct(inputValue)
                    inputResultado.value = resultado
                    page.update()
        elif (opcion1Value == "Binario" and opcion2Value == "Hexadecimal"):
            for i in listaNumeros:
                if "23456789":
                    inputNumero.value = "Error"
                    page.update()
                else:
                    resultado = bin_hex(inputValue)
                    inputResultado.value = resultado
                    page.update()
        elif (opcion1Value == "Ternario" and opcion2Value == "Decimal"):
            for i in listaNumeros:
                if "3456789":
                    inputNumero.value = "Error"
                    page.update()
                else:            
                    resultado = ter_dec(inputValue)
                    inputResultado.value = resultado
                    page.update()
        elif (opcion1Value == "Ternario" and opcion2Value == "Binario"):
            for i in listaNumeros:
                if "3456789":
                    inputNumero.value = "Error"
                    page.update()
                else:      
                    resultado = ter_bin(inputValue)
                    inputResultado.value = resultado
                    page.update()
        elif (opcion1Value == "Ternario" and opcion2Value == "Quaternario"):
            for i in listaNumeros:
                if "3456789":
                    inputNumero.value = "Error"
                    page.update()
                else:      
                    resultado = ter_cua(inputValue)
                    inputResultado.value = resultado
                    page.update()
        elif (opcion1Value == "Ternario" and opcion2Value == "Octal"):
            for i in listaNumeros:
                if "3456789":
                    inputNumero.value = "Error"
                    page.update()
                else:      
                    resultado = ter_oct(inputValue)
                    inputResultado.value = resultado
                    page.update()
        elif (opcion1Value == "Ternario" and opcion2Value == "Hexadecimal"):
            for i in listaNumeros:
                if "3456789":
                    inputNumero.value = "Error"
                    page.update()
                else:      
                    resultado = ter_hex(inputValue)
                    inputResultado.value = resultado
                    page.update()            
        elif (opcion1Value == "Quaternario" and opcion2Value == "Decimal"):
            for i in listaNumeros:
                if "456789":
                    inputNumero.value = "Error"
                    page.update()
                else:      
                    resultado = cua_dec(inputValue)
                    inputResultado.value = resultado
                    page.update() 
        elif (opcion1Value == "Quaternario" and opcion2Value == "Binario"):
            for i in listaNumeros:
                if "456789":
                    inputNumero.value = "Error"
                    page.update()
                else:      
                    resultado = cua_bin(inputValue)
                    inputResultado.value = resultado
                    page.update() 
        elif (opcion1Value == "Quaternario" and opcion2Value == "Ternario"):
            for i in listaNumeros:
                if "456789":
                    inputNumero.value = "Error"
                    page.update()
                else:      
                    resultado = cua_ter(inputValue)
                    inputResultado.value = resultado
                    page.update() 
        elif (opcion1Value == "Quaternario" and opcion2Value == "Octal"):
            for i in listaNumeros:
                if "456789":
                    inputNumero.value = "Error"
                    page.update()
                else:      
                    resultado = cua_oct(inputValue)
                    inputResultado.value = resultado
                    page.update() 
        elif (opcion1Value == "Quaternario" and opcion2Value == "Hexadecimal"):
            for i in listaNumeros:
                if "456789":
                    inputNumero.value = "Error"
                    page.update()
                else:      
                    resultado = cua_hex(inputValue)
                    inputResultado.value = resultado
                    page.update() 
        elif (opcion1Value == "Octal" and opcion2Value == "Decimal"):
            for i in listaNumeros:
                if "89":
                    inputNumero.value = "Error"
                    page.update()
                else:      
                    resultado = oct_dec(inputValue)
                    inputResultado.value = resultado
                    page.update() 
        elif (opcion1Value == "Octal" and opcion2Value == "Binario"):
            resultado = oct_bin(inputValue)
            inputResultado.value = resultado
            page.update() 
        elif (opcion1Value == "Octal" and opcion2Value == "Ternario"):
            resultado = oct_ter(inputValue)
            inputResultado.value = resultado
            page.update() 
        elif (opcion1Value == "Octal" and opcion2Value == "Cuaternario"):
            resultado = oct_cua(inputValue)
            inputResultado.value = resultado
            page.update() 
        elif (opcion1Value == "Octal" and opcion2Value == "Hexadecimal"):
            resultado = oct_hex(inputValue)
            inputResultado.value = resultado
            page.update() 
        elif (opcion1Value == "Hexadecimal" and opcion2Value == "Decimal"):
            resultado = hex_dec(inputValue)
            inputResultado.value = resultado
            page.update() 
        elif (opcion1Value == "Hexadecimal" and opcion2Value == "Binario"):
            resultado = hex_bin(inputValue)
            inputResultado.value = resultado
            page.update() 
        elif (opcion1Value == "Hexadecimal" and opcion2Value == "Ternario"):
            resultado = hex_ter(inputValue)
            inputResultado.value = resultado
            page.update() 
        elif (opcion1Value == "Hexadecimal" and opcion2Value == "Quaternario"):
            resultado = dec_bin(inputValue)
            inputResultado.value = resultado
            page.update() 
        elif (opcion1Value == "Hexadecimal" and opcion2Value == "Octal"):
            resultado = dec_bin(inputValue)
            inputResultado.value = resultado
            page.update() 
        else:
            inputResultado.value = "Su operacion no puede ser posible"
            page.update()


    #Agregando todo a la pagina    
    page.bgcolor = ft.colors.INDIGO_900
    page.update()

    titulo = ft.Text("Traductor Numerico", color=ft.colors.WHITE ,size=30)
    esIgual = ft.Text("=", color=ft.colors.WHITE ,size=30)


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

    inputNumero = ft.TextField(label="Ingrese un numero", border_color=ft.colors.WHITE,
    fill_color=ft.colors.WHITE, height=70, width=500,)

    inputResultado = ft.TextField(label="Ingrese un numero", border_color=ft.colors.WHITE,
    fill_color=ft.colors.WHITE, height=70, width=500,)

    #Lista
    opcion1 = ft.Dropdown(
                hint_text="Desde",
                options=[
                    ft.dropdown.Option("Decimal"),
                    ft.dropdown.Option("Binario"),
                    ft.dropdown.Option("Ternario"),
                    ft.dropdown.Option("Quaternario"),
                    ft.dropdown.Option("Octal"),
                    ft.dropdown.Option("Hexadecimal")
                ],
                autofocus=True,
                bgcolor=ft.colors.WHITE,
                fill_color=ft.colors.WHITE, 
                width=300, 
                border_color=ft.colors.WHITE, 
                border_width=0,
    )

    opcion2 = ft.Dropdown(
                hint_text="A",
                options=[
                    ft.dropdown.Option("Decimal"),
                    ft.dropdown.Option("Binario"),
                    ft.dropdown.Option("Ternario"),
                    ft.dropdown.Option("Quaternario"),
                    ft.dropdown.Option("Octal"),
                    ft.dropdown.Option("Hexadecimal")
                ],
                autofocus=True,
                bgcolor=ft.colors.WHITE,
                fill_color=ft.colors.WHITE, 
                width=300, 
                border_color=ft.colors.WHITE, 
                border_width=0,
    )


    page.add(

        ft.Row(
            [
                inputNumero,
                esIgual
                ,inputResultado
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),

        ft.Row(
            [ 
                opcion1,
                opcion2
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        
        ft.Row(
            [ 
                ft.FilledButton(
                    "Transformar Numero",
                    style=ft.ButtonStyle(padding=20),
                    on_click= transformar
                ),
                ft.FilledButton(
                    "Limpiar",
                    style=ft.ButtonStyle(padding=20),
                    on_click= limpiar
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )


    )


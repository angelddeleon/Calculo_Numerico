import flet as ft
from GaussSeidel.GaussSeidelFun import gauss_seidel
import numpy as np

def gauss(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.START


    inputsA = [] #Los Inputs de A
    inputsB = [] #Los Inputs de A    
    A = [] #Matriz A donde seran almacenados los valores de los inputs
    B = [] #Matriz A donde seran almacenados los valores de los inputs

    def btn_Resultado(e):
        arrayA = np.array(A)
        arrayB = np.array(B)
        tamañoListaB = len(B)
        x = np.zeros(tamañoListaB)
        solution = gauss_seidel(arrayA, arrayB, x)
        page.add(ft.Row(ft.Text(f"La solucion es: {solution}", color=ft.colors.WHITE)))


    fila = []
    columna = []

    page.bgcolor = ft.colors.INDIGO_900
    page.update()


    def obtener_datos():
        matriz_datos = []
        for fila in filas: 
            fila_datos = []
            for control in fila.controls:
                if isinstance(control, ft.TextField): 
                    fila_datos.append(float(control.value))
            matriz_datos.append(fila_datos)
        page.add(ft.Row(ft.Text(f"{matriz_datos}", color=ft.colors.WHITE)))
        return matriz_datos




    def btn_crearInputs(e):
        if not tamañoDelaMatrizInput.value and tamañoDelaMatrizInput.value <= 0 :
            tamañoDelaMatrizInput.value = "Ingrese Un dato correcto"
            page.update()
        else:
            tamañoMatriz = int(tamañoDelaMatrizInput.value)
            tamañoDelaMatrizInput.value = ""

            page.add(ft.Text(f"Se ha creado su matriz de {tamañoMatriz} x {tamañoMatriz} , Ingrese las {tamañoMatriz} que desea encontrar del SEL", color=ft.colors.WHITE))


            textoEsIgual = ft.Text("=")

            for x in range(tamañoMatriz):
                inputsA.append(ft.TextField(label="", border_color=ft.colors.WHITE, fill_color=ft.colors.WHITE))

            for x in range(tamañoMatriz):
                inputsB.append(ft.TextField(label="", border_color=ft.colors.WHITE,fill_color=ft.colors.WHITE, height=50, width=200,))
            
            for x in range(tamañoMatriz):
                fila.append(ft.Row(spacing=10))
                fila[x].controls.append(inputsA[x])
                fila[x].controls.append(textoEsIgual)
                fila[x].controls.append(inputsB[x])

                columna.append(ft.Column(spacing=10))
                columna[x].controls.append(fila[x])
                page.add(columna[x])


            page.add(ft.ElevatedButton("Ver lo ingresado en los inputsA", on_click=btn_mostrarValues))

            page.add(ft.ElevatedButton("Resultado", on_click=btn_Resultado))


    def btn_mostrarValues(e):
        for i in inputsA:
            A.append(list(map(int, i.value.split(','))))
        for i in inputsB:
            B.append(list(map(int, i.value)))
        
        page.add(ft.Text(f"Se ha creado su matriz que desea encontrar del SEL: {A}", color=ft.colors.WHITE))
        page.add(ft.Text(f" {B}", color=ft.colors.WHITE))


    titulo = ft.Text(f"Gauss-Seidel", color=ft.colors.WHITE ,size=30)

    tamañoDelaMatrizInput = ft.TextField(label="Ingrese el tamaño de su matriz", border_color=ft.colors.WHITE,
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

    page.add(tamañoDelaMatrizInput, ft.ElevatedButton("Confirmar", on_click=btn_crearInputs))

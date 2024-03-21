import typer
import subprocess
import sys
from PyInquirer import prompt, print_json, Separator
from rich import print as rprint
from rich.console import Console
from rich.table import Table
from time import sleep
from rich.progress import track

console = Console()
app = typer.Typer()

def process_data():
    sleep(0.02)

def print_configuration(equis1, equis2, dobleu1, dobleu2):
    console.clear()
    table = Table(title="Configuracion Actual de RELU", title_style="green")
    table.add_column("Variable", style="green")
    table.add_column("Valor", style="green")

    table.add_row("Entrada X1", str(equis1))
    table.add_row("Entrada X2", str(equis2))

    console.print(table)

@app.command("run")
def sample_func():
    equis1 = 1 
    equis2 = 0
    dobleu1 = 1 #no se ocupa esta enduro en la funcion nomas pero existe la opcion futura de habilitar la funcion para cambiarlo
    dobleu2 = 1 #no se ocupa esta enduro en la funcion nomas pero existe la opcion futura de habilitar la funcion para cambiarlo
    bias = 0 #no se ocupa esta enduro en la funcion nomas pero existe la opcion futura de habilitar la funcion para cambiarlo
 

    module_list_question = questions = [
        {
            'type': 'list',
            'name': 'opcion',
            'message': 'Elige una opcion: ',
            'choices': [
                        {
                            'name': 'Calcular Relu',
                        },
                        {
                            'name': 'Salir()',
                        } 
            ],
        }
    ]

    relu_options_list_question = questions = [
        {
            'type': 'list',
            'name': 'opcion',
            'message': 'Elige una opcion: ',
            'choices': [
                        {
                            'name': 'Cambiar valor X1',
                        },
                        {
                            'name': 'Cambiar valor X2',
                        },
                        {
                            'name': 'Calcular Relu',
                        },
                        {
                            'name': 'Salir()'
                        }
            ],
        }
    ]

    processing_art = r''' ____            ___                  ___         __     
/\  _`\         /\_ \               /'___`\     /'__`\   
\ \ \L\ \     __\//\ \    __  __   /\_\ /\ \   /\ \/\ \  
 \ \ ,  /   /'__`\\ \ \  /\ \/\ \  \/_/// /__  \ \ \ \ \ 
  \ \ \\ \ /\  __/ \_\ \_\ \ \_\ \__  // /_\ \__\ \ \_\ \
   \ \_\ \_\ \____\/\____\\ \____/\_\/\______/\_\\ \____/
    \/_/\/ /\/____/\/____/ \/___/\/_/\/_____/\/_/ \/___/ 
                                                         
                                                          '''
    rprint(processing_art)
    for _ in track(range(100),description= f'[green]Setting Up',transient=True):
        process_data()

    opcion = prompt(module_list_question)
    if(opcion['opcion']=="Calcular Relu"):
        rprint("")
        pass
    else:
        sys.exit()
    

    #rprint(f"[red]{opcion['opcion']}[red]")
    #folder_name = input()
    while True:
        print_configuration(equis1, equis2, dobleu1, dobleu2)

        opcion2 = prompt(relu_options_list_question)

        if opcion2['opcion'] == "Cambiar valor X1":
            equis1 = 1 if equis1 == 0 else 0
        elif opcion2['opcion'] == "Cambiar valor X2":
            equis2 = 1 if equis2 == 0 else 0
        elif opcion2['opcion'] == "Salir()":
            break  # Exit
        elif opcion2['opcion'] == "Calcular Relu":
            # Relu formula
            X1 = equis1
            X2 = equis2

            S1 = max(0,(X1 * 1)+(X2 * 1) + 0)
            S2 = max(0,(X1 * 1)+(X2 * 1) + -1)
            Y = max(0,(S1 * 1)+(S2 * -2) + 0)
            
            #console.print(f"\n\tValor calculado: {Y}")
            print_configuration(equis1, equis2, dobleu1, dobleu2)
            console.print(f"\n\t[magenta2]Valor calculado: {Y}[magenta2]")
            input("Presiona Enter para continuar...")  # Esperar para limpiar consola
            console.clear()


if __name__ == "__main__":
    app()  

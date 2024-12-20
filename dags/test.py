from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Función que escribe en un archivo
def write_hello_to_file():
    # Obtiene la hora y fecha actuales
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"Hola desde Python\nFecha y hora: {current_time}\n"

    # Ruta y nombre del archivo
    file_path = "/tmp/hola_python.txt"

    # Escribir el mensaje en el archivo
    with open(file_path, "w") as file:
        file.write(message)

    print(f"Archivo escrito en: {file_path}")

# Configuración del DAG
with DAG(
    dag_id="hello_world_dag",  # Nombre del DAG
    start_date=datetime(2024, 12, 19),  # Fecha inicial del DAG
    schedule_interval="0 * * * *",  # Se ejecuta cada hora
    catchup=False,  # Evita ejecutar tareas pasadas
) as dag:

    # Tarea que llama a la función
    write_hello_task = PythonOperator(
        task_id="write_hello_task",  # Nombre de la tarea
        python_callable=write_hello_to_file,  # Función a ejecutar
    )

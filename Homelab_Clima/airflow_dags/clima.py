from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import requests
import mysql.connector
import pandas as pd


def ConsultarAPI():
    url = "https://api.open-meteo.com/v1/forecast?latitude=-22.9&longitude=-43.2&daily=temperature_2m_max,temperature_2m_min&timezone=America%2FSao_Paulo"
    resposta = requests.get(url)
    dados = resposta.json()
    return dados

def ArmazenandoDados(ti):
    conexao = mysql.connector.connect(
            host="192.168.0.124",
            port=3306,
            user="root",
            password="********",
            database="Clima_RJ"
        )
    cursor = conexao.cursor()
    dados = ti.xcom_pull(task_ids="API_clima")

    df = pd.DataFrame(dados["daily"])
    df = df.rename(columns={"time":"data", "temperature_2m_max":"temperatura_maxima", "temperature_2m_min":"temperatura_minima"})
    for i, linha in df.iterrows():
        cursor.execute(
            """
            INSERT INTO Clima (data, temperatura_max, temperatura_min)
            VALUES (%s, %s, %s)
            ON DUPLICATE KEY UPDATE
                temperatura_max = VALUES(temperatura_max),
                temperatura_min = VALUES(temperatura_min)
        """,
            (linha["data"], linha["temperatura_maxima"], linha["temperatura_minima"]),
        )

    conexao.commit()
    cursor.close()
    conexao.close()


with DAG(
    dag_id="Clima_semanal",
    start_date=datetime(2026, 11, 16),
    schedule="0 21 * * *",
    catchup=False
):
    API_clima = PythonOperator(task_id="API_clima", python_callable=ConsultarAPI)
    dados_armazenar = PythonOperator(task_id="dados_armazenar", python_callable=ArmazenandoDados)
    


    API_clima >> dados_armazenar    
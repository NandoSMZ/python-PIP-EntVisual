import utils
import read_csv
import charts
import pandas as pd

def run():
    df = pd.read_csv('data.csv')  # Lectura del archivo con pandas
    df = df[df['Continent'] == 'South America']  # Seleccion de datos con Pandas
    
    countries = df['Country/Territory'].values 
    porcentage = df['World Population Percentage'].values
    charts.generate_pie_chart('South America',countries, porcentage)

if __name__ == '__main__':
    run()
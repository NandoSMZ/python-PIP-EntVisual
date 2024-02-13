import utils
import read_csv
import charts


def run():
    data = read_csv.read_csv('data.csv')
    user_select = int(input('1) para Chart, 2) para Pie, 3) para segunda forma pie==>'))
    if user_select == 1:
        population_by_country_chart(data)
    elif user_select == 2:
        population_by_country_pie(data)
    elif user_select == 3:
        population_by_country_pie_two_way(data)


def population_by_country_chart(data):
    country = input('Type Country ==> ')
    result = utils.population_by_country(data, country)  # Usamos la funcion de retornar o filtar diccionario selecionado por el pais

    if len(result) > 0:
        country_dict_selected = result[0]  # Tomo la posicion 0, ya que result es una lsita de diccionarios,
#        print(country_dict_selected)       # y requiero que quede como un solo diccionario y en esta lista solo hay un diccionario que estan la posicion 0
        labels, values = utils.get_population(country_dict_selected)  # Ejecuto la funcion para construir un nuevo dict apartir del actual
        charts.generate_bar_chart(country, labels, values)  # Genero grafica con valores tomaods


def population_by_country_pie(data):
    user_continent = input('Indica el Continente para filtrar ==>')
    data_filter = list(filter(lambda item: item['Continent'] == user_continent, data))
    new_list_world_pocentage = []
    new_list_world_name = []
    for item in data_filter:
        new_list_world_name.append(item['Country/Territory'])
        new_list_world_pocentage.append(item['World Population Percentage'])
    charts.generate_pie_chart(user_continent, new_list_world_name, new_list_world_pocentage)


def population_by_country_pie_two_way(data):
    user_continent = input('Indica el Continente para filtrar ==>')
    data_filter = list(filter(lambda item: item['Continent'] == user_continent, data))
    countries = list(map(lambda x: x['Country/Territory'], data_filter))
    porcentages = list(map(lambda x: x['World Population Percentage'], data_filter))
    charts.generate_pie_chart(user_continent, countries, porcentages)


# para que se pueda ejecutar como un script se debe agregar el main
if __name__ == '__main__':
    run()

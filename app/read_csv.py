import csv


def read_csv(path):
    with open(path, 'r') as csvfile:  # Nombro el archivo como csvfile
        reader = csv.reader(csvfile, delimiter = ',')  # Pasamos el archivo y el delimitor a la funcion reader, reader es un iterable
        header = next(reader)  # Se extrae el nombre de las columnas, la primera fila
        data = []
        count = 0
        for row in reader:  # pasamos fila a fila
            iterable = zip(header, row)  # Une el Header y el Row, los pone en un array de tuplas
#            print(list(iterable))
            country_dict = {key: value for key, value in iterable}
#            print(country_dict)
            data.append(country_dict)
#            print('**********' * 5)
#            print(row)
            count += 1
        print(f'Este archivo contiene {count} filas')
        return data


if __name__ == '__main__':
    data_dict = read_csv('/Users/fernando.salazar/proyectos/Ruta Backend Python/pythonCursoPlatzi/app/data.csv')
    print(data_dict[0])

    # Filter para traer a Colombia
    new_list = list(filter(lambda item: item['Country/Territory'] == 'Colombia', data_dict))
    print(new_list)

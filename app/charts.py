import matplotlib.pyplot as plt


def generate_bar_chart(name, labels, values):
    fig, ax = plt.subplots()  # matplotlib me da dos variables, la figura y cordenadas
    ax.bar(labels, values)  # Creo diagrama de barras de acuerdo a las cordenadas se ingresa labels y valores
    plt.savefig(f'./img/{name}_bar.png')
    plt.close()


def generate_pie_chart(continent, labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)  # Creo una torta
    plt.savefig(f'./img/{continent}_pie.png')
    plt.close()


if __name__ == '__main__':
    type_chart = int(input('Ingrese el tipo de grafica, 1 -> Bar o 2 -> Pie => '))
    num_values = int(input('Ingrese el numero de datos a graficar => '))

    labels_init = []
    values_init = []
    for i in range(1, num_values + 1):
        user_label = input(f'Ingrese el nombre del dato {i} => ')
        user_value = int(input(f'Ingrese el valor del dato {i} => '))
        labels_init.append(user_label)
        values_init.append(user_value)

    if type_chart == 1:
        generate_bar_chart(labels_init, values_init)
    else:
        generate_pie_chart(labels_init, values_init)

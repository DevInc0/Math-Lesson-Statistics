import pandas as pd
import matplotlib.pyplot as plt

def draw_pie(values: list, labels: list):
    plt.figure()
    plt.pie(values, labels = labels)
    plt.title('Круговая диаграмма')

def draw_bars(values: list, labels: list):
    plt.figure()
    plt.bar(values, labels)
    plt.grid(True)
    plt.title('Столбчатая диаграмма')

def draw_plot(values: list, labels: list):
    plt.figure()
    plt.plot(values, labels)
    plt.grid(True)
    plt.title('Кривая')

def main():
    data = pd.read_csv('data.csv', sep=';')
    data['Value'] = data['Sex'] + ' - ' + data['Result']
    data_values = data['Value'].tolist()

    counters = {result:data_values.count(result) for result in sorted(set(data_values))}

    values = counters.values()
    labels = counters.keys()

    draw_pie(values, labels)
    draw_bars(labels, values)    
    draw_plot(labels, values)

    plt.show()

if __name__ == '__main__': main()

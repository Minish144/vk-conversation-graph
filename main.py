from parse import *
import json
import matplotlib.pyplot as plt

def main():
    with open("date.json") as file:
        dates = json.load(file)['dates']
    data = extremum(dates)

    plt.plot(data['X_Axis'], data['Y_Axis'])
    plt.ylabel('Date')
    plt.ylabel('Activity')
    plt.xticks(rotation=45) 
    plt.show()

if __name__ == "__main__":
    main()
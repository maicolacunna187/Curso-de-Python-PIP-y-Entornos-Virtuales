import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ["Melissa", "Norma", "'La Jesuu'"]
    values = [57, 22, 19]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig("pie.png")
    plt.close()
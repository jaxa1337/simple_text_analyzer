import actions
import matplotlib.pyplot as plt

def draw_bar_chart(dictionary):
    v = sorted(dictionary.values(), reverse= True)

    sort_dict = {}
    for j in v:
        for i in dictionary:
            if dictionary[i] == j:
                sort_dict[i] = j

    fig, ax = plt.subplots()

    fig.set_figwidth(7)
    fig.set_figheight(7)
    # fig.tight_layout()
    fig.subplots_adjust(top = 0.979, bottom = 0.067, left=0.076, right = 0.976)

    ax.barh(list(sort_dict.keys()), list(sort_dict.values()), edgecolor = 'black', color = ['cornflowerblue','mediumblue'])
    ax.set_axisbelow(True)
    ax.grid()

    ax.xaxis.set_tick_params(pad = 5)
    ax.yaxis.set_tick_params(pad = 5)

    for i in ax.patches:
        plt.text(i.get_width()+0.2, i.get_y()+0.5,
                str(round((i.get_width()), 2)),
                fontsize = 10, fontweight ='bold',
                color ='black', va = 'center_baseline')

    plt.xlabel('Amount')
    plt.ylabel('Letters')
    plt.show()

def draw_pie_chart(values, labels):

    fig, ax = plt.subplots()
    ax.pie(values, labels = labels,autopct='%1.2f%%')
    ax.axis('equal')
    plt.show()
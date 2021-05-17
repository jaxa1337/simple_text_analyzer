import actions
import matplotlib.pyplot as plt

def draw_bar_chart(dictionary):
    v = sorted(dictionary.values())
    v.reverse()
    
    sort_dict = {}
    for j in v:
        for i in dictionary:
            if dictionary[i] == j:
                sort_dict[i] = j

    fig, ax = plt.subplots()
    ax.bar(sort_dict.keys(),sort_dict.values())
    ax.set_axisbelow(True)
    ax.grid()
    plt.show()

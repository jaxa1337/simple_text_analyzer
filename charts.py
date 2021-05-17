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

    plt.grid(True)
    plt.bar(sort_dict.keys(),sort_dict.values())
    plt.ylabel('Quantity')
    plt.xlabel('Letter')
    plt.title('The number of occurrences of letters')
    plt.show()

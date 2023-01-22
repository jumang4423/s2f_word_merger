import json
import sys
import networkx as nx
import matplotlib.pyplot as plt

def main():
    # get args
    word_dict_filepath = sys.argv[1]

    # var
    word_dict = {}

    # load word dict
    with open(word_dict_filepath, 'r') as f:
        word_dict = json.load(f)

    graph = nx.Graph()

    for key in word_dict.keys():
        for word in word_dict[key]:
            graph.add_edge(key, word)

    colormap = []
    fontcolor = []
    for node in graph:
        # if node connected to more than 5 nodes, color it red, else color it blue
        if len(list(graph.neighbors(node))) > 2:
            colormap.append('red')
            fontcolor.append('black')

        else:
            colormap.append('lightgray')
            fontcolor.append('white')


    plt.title("ninjumango word graph")
    # top rank 5 nodes
    top_rank = sorted(graph.degree, key=lambda x: x[1], reverse=True)[:5]
    top_rank = [x[0] for x in top_rank]
    # low rank 5 nodes
    low_rank = sorted(graph.degree, key=lambda x: x[1], reverse=False)[:5]
    low_rank = [x[0] for x in low_rank]
    # show rank words in plt
    print("[1;32m top rank words: ", top_rank)
    print("[1;32m low rank words: ", low_rank)
    print("here is the graph:")
    # draw graph
    nx.draw(graph, with_labels=True, node_color=colormap, node_size=100, font_size=12, font_color="black", alpha=0.5, linewidths=40, node_shape='s', width=2)
    plt.show()

if __name__ == '__main__':
    main()

# from the text book
def trim_edges(g, weight=1):
    g2 = nx.Graph()
    for f, to, edata in g.edges(data=True):
        if edata['weight'] > weight:
            #print(edata['weight'])
            g2.add_edge(f, to, weight=edata['weight'])
    return g2



# As an experiment, use the weighted_project_graph function
# This will have edges with weights: [1..9]
projected_states = bipartite.weighted_projected_graph(divorce, list(states))

# show the result
nx.draw_networkx_edge_labels(projected_states, pos=nx.nx_pydot.graphviz_layout(projected_states))

# Now trim all edges with weights < 6
trimmed = trim_edges(projected_states, 6)

# show our islands
nx.draw(trimmed,        
        font_size=9,
        font_weight="bold",
        font_color="black",
        node_size=1500, 
        edge_color="grey",
        node_shape="o", 
        alpha=0.5, 
        linewidths=4, 
        width=2,
        with_labels=True,
        pos=nx.nx_pydot.graphviz_layout(trimmed))

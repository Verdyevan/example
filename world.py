import pydot

asia = [
    {
        "Japan": [],
        "Korea": [],
        "India": [],
        "Indonesia": [],
    }
]

europe = [
    {
        "France": [],
        "Germany": [],
        "Italy": [],
        "Netherlands": [],
    }
]

africa = [
    {
        "Kenya": [],
        "South Africa": [],
        "Uganda": [],
        "Rwanda": [],
    }
]

america = [
    {
        "Canada": [],
        "Brazil": [],
        "Chile": [],
        "United States": [],
    }
]

australia = [
    {
    "Australia": [],
    }
]

continent = [{
    "Continent": [{
        "Asia": asia,
        "Europe": europe,
        "Africa": africa,
        "America": america,
        "Australia": australia,
    }],
}]


def iterate(course_list, parent=None, filename=None):
    for c in course_list:
        for key, val in c.items():
            if parent is not None:
                graph.add_edge(pydot.Edge(parent, key))
            if val is not None or len(val) > 0:
                iterate(val, parent=key)



graph = pydot.Dot(graph_type='digraph', rankdir='LR')
iterate(continent, parent=None, filename='world_continent.png')





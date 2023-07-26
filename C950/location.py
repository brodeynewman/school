class Location:
  def __init__(self, name, address):
    self.name = name
    self.address = address

class LocationGraph:
  def __init__(self):
      self.adjacency_list = {}
      self.location_weights = {}
      
  def add_vertex(self, new_vertex):
      self.adjacency_list[new_vertex] = []
      
  def add_directed_edge(self, from_vertex, to_vertex, weight = 1.0):
      self.location_weights[(from_vertex, to_vertex)] = weight
      self.adjacency_list[from_vertex].append(to_vertex)
      
  def add_undirected_edge(self, vertex_a, vertex_b, weight = 1.0):
      self.add_directed_edge(vertex_a, vertex_b, weight)
      self.add_directed_edge(vertex_b, vertex_a, weight)
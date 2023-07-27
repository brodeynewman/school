class Manager:
  def __init__(self, trucks, packages, map):
    self.trucks = trucks
    self.packages = packages
    self.map = map

  def distribute_packages(self):
    for truck in self.trucks:
      print("TRUCK", truck, self.packages)

  def sort_packages(self):
    print("sorting...")

  def start(self):
    for key in self.map.vertices:
      if key.address == "1060 Dalton Ave S":
        print("bingo:", key.name)

        for route, value in key.routes.items():
          print("route:::", route.address)

          if route.address == "3595 Main St":
            print("DURATION:::", value)
    

class Manager:
  def __init__(self, trucks, packages, locations = []):
    self.trucks = trucks
    self.packages = packages
    self.locations = locations

  def distribute_packages(self):
    for truck in self.trucks:
      print("TRUCK", truck, self.packages)

  def sort_packages(self):
    print("sorting...")

  def start(self):
    self.distribute_packages()
    

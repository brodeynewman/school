class Manager:
  def __init__(self, trucks, packages):
    self.trucks = trucks
    self.packages = packages

  def distribute_packages(self):
    for truck in self.trucks:
      print("TRUCK", truck)

  def start(self):
    self.distribute_packages()

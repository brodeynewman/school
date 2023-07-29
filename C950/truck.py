class Truck:
  def __init__(self):
    self.packages = []
    self.miles_traveled = 0
    self.status = 'stationed'

  def load(self, packages = []):
    print("Loading truck with packages: ", len(packages))

    if len(packages) > 16:
      raise Exception("Truck can not carry more than 16 packages")

    self.packages = packages

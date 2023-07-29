from datetime import datetime

MANAGER_TIME_FORMAT = "%m/%d/%Y %I:%M:%S %p"

class Manager:
  def __init__(self, trucks, packages, map):
    self.trucks = trucks
    self.packages = packages
    self.sorted_packages = self.sort_packages(packages)
    self.map = map

  def distribute_packages(self):
    for truck in self.trucks:
      print("TRUCK", truck, self.packages)

  def sort_packages(self, packages):
    print("sorting packages...")

    def parse_time_string(package):
      if not package.has_deadline():
        return datetime.now()

      return datetime.strptime(package.get_deadline(), MANAGER_TIME_FORMAT)

    # Sort datetime objects
    sort = sorted(packages, key=parse_time_string)

    return sort

  def start(self):
    for key in self.map.vertices:
      if key.address == "6351 South 900 East":
        print("bingo:", key.name)

        for route, value in key.routes.items():
          if route.address == "4001 South 700 East":
            print("DURATION:::", value)
    

from datetime import datetime

MANAGER_TIME_FORMAT = "%m/%d/%Y %I:%M:%S %p"
MAX_PACKAGE_LIMIT = 16

class Manager:
  def __init__(self, trucks, packages, map):
    self.trucks = trucks
    self.packages = packages
    self.sorted_packages = self.sort_packages(packages)
    self.map = map

  def sort_packages(self, packages):
    print("sorting packages...")

    def parse_time_string(package):
      if not package.has_deadline():
        return datetime.now()

      return datetime.strptime(package.get_deadline(), MANAGER_TIME_FORMAT)

    # Sort datetime objects
    sort = sorted(packages, key=parse_time_string)

    return sort
  
  def distribute_packages(self):
    print("Loading trucks with packages of length: ", len(self.sorted_packages))
    
    # it shouldn't matter which truck gets the deadlined packages
    chunked = []

    i = 0
    truck = 0
    chunkedAmt = 0

    while chunkedAmt < len(self.sorted_packages) -  1:
      if i < MAX_PACKAGE_LIMIT:
        chunked.append(self.sorted_packages[i])
        i += 1
        chunkedAmt += 1
      else:
        i = 0
        self.trucks[truck].load(chunked)
        chunked = []

    # set our sorted packages in our state so that we can re-distribute once the trucks tell us they can
    self.sorted_packages = chunked

  def start(self):
    self.distribute_packages()

    # for key in self.map.vertices:
    #   if key.address == "6351 South 900 East":
    #     print("bingo:", key.name)

    #     for route, value in key.routes.items():
    #       if route.address == "4001 South 700 East":
    #         print("DURATION:::", value)
    

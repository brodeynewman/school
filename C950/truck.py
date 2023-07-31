from hmap import HashMap
from datetime import timedelta

MAX_PACKAGE_SIZE = 16
# we could DI this eventually but whatever
TRUCK_SPEED = 18
HUB_ADDRESS = '4001 South 700 East'

class Truck:
  def __init__(self, id, map, packages, min_start_time = None):
    self.id = id
    self.pmap = HashMap(MAX_PACKAGE_SIZE)
    self.pcache = []

    self.packages = None
    self.total_packages = 0
    self.miles_traveled = 0
    self.package_index = 0

    self.map = map

    self.start_time = None
    self.current_time = min_start_time
    self.min_start_time = min_start_time
    
    hub = self.map.find_node(HUB_ADDRESS)

    if hub == None:
      raise Exception("Hub location not found.")

    # best first search
    self.current_location = hub
    self.load(packages)

  def get_package(self, pid):
    return self.pmap.get(pid)

  def maybe_depart(self, time = None):
    if self.start_time != None:
      return
    # starts our truck timer
    elif time == None:
      self.start_time = self.min_start_time
    elif time > self.min_start_time:
      self.start_time = time

  def load(self, payload = []):
    print("Loading truck with packages: ", len(payload))

    # validate that we aren't loading too many packages
    if len(payload) > MAX_PACKAGE_SIZE:
      # i'm too lazy to format this constant within the error
      raise Exception("Truck can not carry more than 16 packages")

    packages = []

    # set our packages in our package hashmap
    for package in payload:
      self.pmap.set(package.id, package)

      p = self.pmap.get(package.id)

      # once we load our packages, we set the departure time to be the
      # time the truck should leave the lot
      p.set_departure_time(self.min_start_time)
      # keep a cache of all of the packages we hit
      self.pcache.append(p)
      packages.append(p)

    self.packages = packages
    self.total_packages = len(packages)

  def __find_target(self):
    lowest_target_location = None
    lowest_weight = None
    target_package = None

    print(f'Analyzing current address: {self.current_location.address}', end='\n')

    # We loop through each undelivered package and find the closest one to the current address
    # This entire process is O(n^2)
    for package in self.packages:
      # we're already at the target location; we can deliver the packages instantly
      if package.address == self.current_location.address:
        lowest_target_location = self.current_location
        lowest_weight = 0
        target_package = package

        break

      # do a lookup in our graph to find the package address
      location = self.map.find_node(package.address)
      # grab the weight of the next potential location
      weight = self.current_location.routes[location]
      
      if lowest_weight == None or weight < lowest_weight:
        lowest_weight = weight
        target_package = package
        lowest_target_location = location

    return {
      "weight": lowest_weight,
      "package": target_package,
      "location": lowest_target_location
    }

  def is_complete(self):
    return len(self.packages) == 0

  def __remove_package(self, id):
    self.packages = list(filter(lambda p: p.id != id, self.packages))

  def deliver_latest(self):
    print(f'Delivering package: {self.package_index} of {self.total_packages}', end='\n')

    # this is the nearest neighbor logic
    target = self.__find_target()

    new_loc = target.get('location')
    new_weight = target.get('weight')
    package = target.get('package')

    print(f'Truck {self.id}: new target found [{new_loc.address}] with lowest distance of [{new_weight}]', end='\n')
    
    # increase time by doing math based on how quick the truck moves (e.g. 18mph)
    self.current_time += timedelta(hours=(new_weight / TRUCK_SPEED))

    # increment our truck's delivery index
    self.package_index += 1

    # set our package's delivery time
    package.set_delivered_time(self.current_time)

    # increase miles traveled after we take our new weight
    self.miles_traveled += new_weight
    # swap the current location
    self.current_location = new_loc
    # remove the package from our unordered queue
    self.__remove_package(package.id)

from functools import reduce 

MANAGER_TIME_FORMAT = "%m/%d/%Y %I:%M:%S %p"
MAX_PACKAGE_LIMIT = 16

class Manager:
  def __init__(self, trucks):
    self.trucks = trucks

  def show_total_mileage(self):
    for truck in self.trucks:
      log = f'Distance traveled for truck [{truck.id}]:  {truck.miles_traveled}'

      print(log)

  def __get_package_status(self, truck, package, time):
    # if the time inputted by the user was before the truck even left, then it's obviously still at the hub
    if truck.start_time >= time:
      status = "At Hub"
    else:
      status = package.get_status_by_time(time)

    return status

  def show_status_of_all(self, time):
    for truck in self.trucks:
      for package in truck.pcache:
        status = self.__get_package_status(truck, package, time)

        print(f'Package id: [{package.id}] delivery status: [{status}]', end='\n')

  def show_status_of_package_id(self, pid, time):
    for truck in self.trucks:
      package = truck.get_package(pid)

      if package != None:
        status = self.__get_package_status(truck, package, time)

        # print our package information
        print(f'Package id: [{package.id}] delivery status: [{status}]', end='\n')
        print(package)
        exit()
      
    raise Exception("Package not found")
        

  def __show_results(self):
    print(' ')
    print('All trucks complete.')
    print(' ')

    for truck in self.trucks:
      log = f'''

        Distance traveled:  {truck.miles_traveled}
        Packages delivered: {truck.package_index}
        Start time:         {truck.start_time}
        End time:           {truck.current_time}

      '''

      print(f'Summary of truck {truck.id}:', end='\n')
      print(log)

    combined_mileage = reduce(lambda x, y: x + y.miles_traveled, self.trucks, 0)
    combined_packages = reduce(lambda x, y: x + y.package_index, self.trucks, 0)

    totals = f'''

      Total mileage:            {combined_mileage}
      Total packages delivered: {combined_packages}

    '''

    print(totals)
  
  def deliver(self):
    latest_complete_time = None

    while not all(truck.is_complete() for truck in self.trucks):
      print("Not all trucks are complete. Routing...")

      incomplete_trucks = list(filter(lambda truck: not truck.is_complete(), self.trucks))

      # only run two trucks at a time
      for truck in incomplete_trucks[:2]:
         # set the latest departed time if one exists
         truck.maybe_depart(latest_complete_time)
         truck.deliver_latest()

         if truck.is_complete():
           latest_complete_time = truck.current_time
    
    self.__show_results()

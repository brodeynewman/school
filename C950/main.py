# Brodey Newman, ID: 009462905

# Constraints:
# 1. All 40 packages must be delivered on time.
# 2. There are 3 trucks
# 3. There are 2 drivers
# 4. Both trucks must not travel over a combined total of 140 miles

# Assumptions:
# 1. Each truck can carry a maximum of 16 packages, and the ID number of each package is unique.
# 2. The trucks travel at an average speed of 18 miles per hour and have an infinite amount of gas with no need to stop.
# 3. There are no collisions.
# 4. Three trucks and two drivers are available for deliveries. Each driver stays with the same truck as long as that truck is in service.
# 5. Drivers leave the hub no earlier than 8:00 a.m., with the truck loaded, and can return to the hub for packages if needed. 
# 6. The delivery and loading times are instantaneous, i.e., no time passes while at a delivery or when moving packages to a truck at the hub (that time is factored into the calculation of the average speed of the trucks).
# 7. There is up to one special note associated with a package.
# 8. The delivery address for package #9, Third District Juvenile Court, is wrong and will be corrected at 10:20 a.m.
#   a. WGUPS is aware that the address is incorrect and will be updated at 10:20 a.m.
#   b. WGUPS does not know the correct address (410 S State St., Salt Lake City, UT 84111) until 10:20 a.m.
# 9. The distances provided in the WGUPS Distance Table are equal regardless of the direction traveled.
# 10. The day ends when all 40 packages have been delivered.

# Algorithms:
# I'll be using nearest neighbord alg. I plan to convert each delivery location to a vertex in the graph.
# The graph will be a weighted graph and will include distances between points as the weights.

from package import Package
from truck import Truck
from manager import Manager
from map import createMap
from datetime import timedelta
from utils import get_manager_start_time, convert_to_datetime

ALL = "all"

def print_mileage(manager):
  manager.show_total_mileage()

def show_statuses(manager):
  time = input("Please enter a valid time following the format HH:MM:SS: ")

  (h, m, s) = time.split(":")
  converted = timedelta(hours=int(h), minutes=int(m), seconds=int(s))
  combined = convert_to_datetime(converted)
  
  p_input = input('Enter a package ID. Enter "all" to see every package for the given time: ')

  if p_input == ALL:
    manager.show_status_of_all(combined)
  else:
    # we assume this was a package ID
    manager.show_status_of_package_id(int(p_input), combined)

option_map = {
  "mileage": print_mileage,
  "statuses": show_statuses
}

def init_prompt(manager):
  option = input("Choose an option: [mileage, statuses]: ")

  func = option_map.get(option)

  if func is None:
    raise Exception("Option not found in allowed list of options")
  
  # call our manager function for whatever it is we want to view
  func(manager)

def main():
  map = createMap()

  # initialize 3 trucks that will be used by our manager to coordinate package deliveries
  trucks = [
    Truck(1, map, [
      Package(1, "195 W Oakland Ave", "Salt Lake City", "84115", "12/31/1899 10:30:00 AM", 21, ""),
      Package(5, "410 S State St", "Salt Lake City", "84115", "12/31/1899 10:30:00 AM", 21, ""),
      Package(35, "1060 Dalton Ave S", "Salt Lake City", "84104", "12/31/1899 10:30:00 AM", 88, ""),
      Package(37, "410 S State St", "Salt Lake City", "84111", "12/31/1899 10:30:00 AM", 88, ""),
      Package(34, "4580 S 2300 E", "Holladay", "84117", "12/31/1899 10:30:00 AM", 2, ""),
      Package(40, "380 W 2880 S", "Salt Lake City", "84115", "12/31/1899 10:30:00 AM", 45, ""),
      Package(13, "2010 W 500 S", "Salt Lake City", "84104", "12/31/1899 10:30:00 AM", 2, ""),
      Package(14, "4300 S 1300 E", "Millcreek", "84117", "12/31/1899 10:30:00 AM", 88, "Must be delivered with 15, 19"),
      Package(15, "4580 S 2300 E", "Holladay", "84117", "12/31/1899 9:00:00 AM", 4, ""),
      Package(16, "4580 S 2300 E", "Holladay", "84117", "12/31/1899 10:30:00 AM", 88, "Must be delivered with 13, 19"),
      Package(19, "177 W Price Ave", "Salt Lake City", "84115", "EOD", 37, ""),
      Package(20, "3595 Main St", "Salt Lake City", "84115", "12/31/1899 10:30:00 AM", 37, "Must be delivered with 13, 15"),
      Package(29, "1330 2100 S", "Salt Lake City", "84106", "12/31/1899 10:30:00 AM", 2, ""),
      Package(30, "300 State St", "Salt Lake City", "84103", "12/31/1899 10:30:00 AM", 1, ""),
      # 8am start
    ], get_manager_start_time()),
    Truck(2, map, [
      Package(31, "3365 S 900 W", "Salt Lake City", "84119", "12/31/1899 10:30:00 AM", 1, ""),
      Package(2, "2530 S 500 E", "Salt Lake City", "84106", "EOD", 44, ""),
      Package(3, "233 Canyon Rd", "Salt Lake City", "84103", "EOD", 2, "Can only be on truck 2"),
      Package(18, "1488 4800 S", "Salt Lake City", "84123", "EOD", 6, "Can only be on truck 2"),
      Package(36, "2300 Parkway Blvd", "West Valley City", "84119", "EOD", 88, "Can only be on truck 2"),
      Package(38, "410 S State St", "Salt Lake City", "84111", "EOD", 9, "Can only be on truck 2"),
      Package(33, "2530 S 500 E", "Salt Lake City", "84106", "EOD", 1, ""),
      Package(4, "380 W 2880 S", "Salt Lake City", "84115", "EOD", 4, ""),
      Package(6, "3060 Lester St", "West Valley City", "84119", "12/31/1899 10:30:00 AM", 88, "Delayed on flight---will not arrive to depot until 9:05 am"),
      Package(25, "5383 S 900 East #104", "Salt Lake City", "84117", "12/31/1899 10:30:00 AM", 7, "Delayed on flight---will not arrive to depot until 9:05 am"),
      Package(28, "2835 Main St", "Salt Lake City", "84115", "EOD", 7, "Delayed on flight---will not arrive to depot until 9:05 am"),
      Package(32, "3365 S 900 W", "Salt Lake City", "84119", "EOD", 1, "Delayed on flight---will not arrive to depot until 9:05 am"),
      # 9:05am start time
    ], get_manager_start_time() + timedelta(hours=1, minutes=5)),
    Truck(3, map, [
      Package(7, "1330 2100 S", "Salt Lake City", "84106", "EOD", 8, ""),
      Package(8, "300 State St", "Salt Lake City", "84103", "EOD", 9, ""),
      Package(9, "410 S State St", "Salt Lake City", "84111", "EOD", 2, ""),
      Package(10, "600 E 900 South", "Salt Lake City", "84105", "EOD", 1, ""),
      Package(11, "2600 Taylorsville Blvd", "Salt Lake City", "84118", "EOD", 1, ""),
      Package(17, "3148 S 1100 W", "Salt Lake City", "84119", "EOD", 2, ""),
      Package(21, "3595 Main St", "Salt Lake City", "84115", "EOD", 3, ""),
      Package(22, "6351 South 900 East", "Murray", "84121", "EOD", 2, ""),
      Package(23, "5100 South 2700 West", "Salt Lake City", "84118", "EOD", 5, ""),
      Package(24, "5025 State St", "Murray", "84107", "EOD", 7, ""),
      Package(26, "5383 S 900 East #104", "Salt Lake City", "84117", "EOD", 25, ""),
      Package(27, "1060 Dalton Ave S", "Salt Lake City", "84104", "EOD", 5, ""),
      Package(12, "3575 W Valley Central Station bus Loop", "West Valley City", "84119", "EOD", 1, ""),
      Package(39, "2010 W 500 S", "Salt Lake City", "84104", "EOD", 9, ""),
      # 10:20am start
    ], get_manager_start_time() + timedelta(hours=2, minutes=20)),
  ]

  # tell our manager about the trucks, packages & locations available
  manager = Manager(trucks)
  manager.deliver()

  init_prompt(manager)

main()

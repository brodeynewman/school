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
# I'll be using A* as the finding algorithm. I plan to convert each delivery location to a vertex in the graph.
# The graph will be a weighted graph and will include distances between points as the weights.

from package import Package
from truck import Truck
from manager import Manager
from location import Location, LocationGraph

packages = [
  Package(1, "195 W Oakland Ave", "Salt Lake City", "UT", "84115", "12/31/1899 10:30:00 AM", 21, ""),
  Package(2, "2530 S 500 E", "Salt Lake City", "UT", "84106", "EOD", 44, ""),
  Package(3, "233 Canyon Rd", "Salt Lake City", "UT", "84103", "EOD", 2, "Can only be on truck 2"),
  Package(4, "380 W 2880 S", "Salt Lake City", "UT", "84115", "EOD", 4, ""),
  Package(5, "410 S State St", "Salt Lake City", "UT", "84115", "12/31/1899 10:30:00 AM", 21, ""),
  Package(6, "3060 Lester St", "West Valley City", "UT", "84119", "12/31/1899 10:30:00 AM", 88, "Delayed on flight---will not arrive to depot until 9:05 am"),
  Package(7, "1330 2100 S", "Salt Lake City", "UT", "84106", "EOD", 8, ""),
  Package(8, "300 State St", "Salt Lake City", "UT", "84103", "EOD", 9, ""),
  Package(9, "300 State St", "Salt Lake City", "UT", "84103", "EOD", 2, ""),
  Package(10, "600 E 900 South", "Salt Lake City", "UT", "84105", "EOD", 1, ""),
  Package(11, "2600 Taylorsville Blvd", "Salt Lake City", "UT", "84118", "EOD", 1, ""),
  Package(12, "3575 W Valley Central Station bus Loop", "West Valley City", "UT", "84119", "EOD", 1, ""),
  Package(13, "2010 W 500 S", "Salt Lake City", "UT", "84104", "12/31/1899 10:30:00 AM", 2, ""),
  Package(14, "4300 S 1300 E", "Millcreek", "UT", "84117", "12/31/1899 10:30:00 AM", 88, "Must be delivered with 15, 19"),
  Package(15, "4580 S 2300 E", "Holladay", "UT", "84117", "12/31/1899 9:00:00 AM", 4, ""),
  Package(16, "4580 S 2300 E", "Holladay", "UT", "84117", "12/31/1899 10:30:00 AM", 88, "Must be delivered with 13, 19"),
  Package(17, "3148 S 1100 W", "Salt Lake City", "UT", "84119", "EOD", 2, ""),
  Package(18, "1488 4800 S", "Salt Lake City", "UT", "84123", "EOD", 6, "Can only be on truck 2"),
  Package(19, "177 W Price Ave", "Salt Lake City", "UT", "84115", "EOD", 37, ""),
  Package(20, "3595 Main St", "Salt Lake City", "UT", "84115", "12/31/1899 10:30:00 AM", 37, "Must be delivered with 13, 15"),
  Package(21, "3595 Main St", "Salt Lake City", "UT", "84115", "EOD", 3, ""),
  Package(22, "6351 South 900 East", "Murray", "UT", "84121", "EOD", 2, ""),
  Package(23, "5100 South 2700 West", "Salt Lake City", "UT", "84118", "EOD", 5, ""),
  Package(24, "5025 State St", "Murray", "UT", "84107", "EOD", 7, ""),
  Package(25, "5383 South 900 East #104", "Salt Lake City", "UT", "84117", "12/31/1899 10:30:00 AM", 7, "Delayed on flight---will not arrive to depot until 9:05 am"), 
  Package(26, "5383 South 900 East #104", "Salt Lake City", "UT", "84117", "EOD", 25, ""),
  Package(27, "1060 Dalton Ave S", "Salt Lake City", "UT", "84104", "EOD", 5, ""),
  Package(28, "2835 Main St", "Salt Lake City", "UT", "84115", "EOD", 7, "Delayed on flight---will not arrive to depot until 9:05 am"),
  Package(29, "1330 2100 S", "Salt Lake City", "UT", "84106", "12/31/1899 10:30:00 AM", 2, ""),
  Package(30, "300 State St", "Salt Lake City", "UT", "84103", "12/31/1899 10:30:00 AM", 1, ""),
  Package(31, "3365 S 900 W", "Salt Lake City", "UT", "84119", "12/31/1899 10:30:00 AM", 1, ""),
  Package(32, "3365 S 900 W", "Salt Lake City", "UT", "84119", "EOD", 1, "Delayed on flight---will not arrive to depot until 9:05 am"),
  Package(33, "2530 S 500 E", "Salt Lake City", "UT", "84106", "EOD", 1, ""),
  Package(34, "4580 S 2300 E", "Holladay", "UT", "84117", "12/31/1899 10:30:00 AM", 2, ""),
  Package(35, "1060 Dalton Ave S", "Salt Lake City", "UT", "84104", "12/31/1899 10:30:00 AM", 88, ""),
  Package(36, "2300 Parkway Blvd", "West Valley City", "UT", "84119", "EOD", 88, "Can only be on truck 2"),
  Package(37, "410 S State St", "Salt Lake City", "UT", "84111", "12/31/1899 10:30:00 AM", 88, ""),
  Package(38, "410 S State St", "Salt Lake City", "UT", "84111", "EOD", 9, "Can only be on truck 2"),
  Package(39, "2010 W 500 S", "Salt Lake City", "UT", "84104", "EOD", 9, ""),
  Package(40, "380 W 2880 S", "Salt Lake City", "UT", "84115", "12/31/1899 10:30:00 AM", 45, ""),
]

# hub location, aka start
hub = Location("Western Governors University", "4001 South 700 East")
peaceGarden = Location("International Peace Gardens", "1060 Dalton Ave S")
sugarHouse = Location("Sugar House Park", " 1060 Dalton Ave S")
hertigageCityGov = Location("Taylorsville-Bennion Heritage City Gov Off", "1488 4800 S")
healthServices = Location("Salt Lake City Division of Health Services", "177 W Price Ave")
publicWorks = Location("South Salt Lake Public Works", "195 W Oakland Ave")
streetsAndSanitation = Location("Salt Lake City Streets and Sanitation", "2010 W 500 S")
dekerLake = Location("Deker Lake", "2300 Parkway Blvd")
ottingerHall = Location("Salt Lake City Ottinger Hall", "233 Canyon Rd")
columbusLibrary = Location("Columbus Library", "2530 S 500 E")
taylorsvilleCityHall = Location("Taylorsville City Hall", "2600 Taylorsville Blvd")
southSaltPolice = Location("South Salt Lake Police", "2835 Main St")
councilHall = Location("Council Hall", "300 State St")
redwoodPark = Location("Redwood Park", "3060 Lester St")
slcMentalHealth = Location("Salt Lake County Mental Health", "3148 S 1100 W")
slcPolice = Location("Salt Lake County/United Police Dept", "3365 S 900 W")
westValleyProsecutor = Location("West Valley Prosecutor", " 3575 W Valley Central Station bus Loop")
slcHousingAuth = Location("Housing Auth. of Salt Lake County", "3595 Main St")
dmv = Location("Utah DMV Administrative Office", "380 W 2880 S")
juvenileCourt = Location("Third District Juvenile Court", "410 S State St")
cottonwoodSoftball = Location("Cottonwood Regional Softball Complex", "4300 S 1300 E")
holidayCityOffice = Location("Holiday City Office", "4580 S 2300 E")
murrayMuseum = Location("Murray City Museum", "5025 State St")
vrSoftball = Location("Valley Regional Softball Complex", " 5100 South 2700 West")
rockSprings = Location("City Center of Rock Springs", "5383 S 900 East #104")
rtPaviliionPark = Location("Rice Terrace Pavilion Park", "600 E 900 South")
historicalFarm = Location("Wheeler Historic Farm", "6351 South 900 East")

def createMap():
  map = LocationGraph()

  # add all of our map vertexes (locations)
  map.add_vertex(hub)
  map.add_vertex(peaceGarden)
  map.add_vertex(sugarHouse)

  return map

def main():
  print("hello")

  # initialize 3 trucks that will be used by our manager to coordinate package deliveries
  trucks = [
    Truck([]),
    Truck([]),
    Truck([]),
  ]

  map = createMap()

  # tell our manager about the trucks, packages & locations available
  manager = Manager(trucks, packages, map)
  manager.start()

main()

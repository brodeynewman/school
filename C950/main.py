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
hub = Location("hub", "4001 South 700 East")
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
rtPavillionPark = Location("Rice Terrace Pavilion Park", "600 E 900 South")
historicFarm = Location("Wheeler Historic Farm", "6351 South 900 East")

def createMap():
  map = LocationGraph()

  # add all of our map vertexes (locations)
  map.add_vertex(hub)
  map.add_edge(hub, peaceGarden, 7.2)

  map.add_vertex(peaceGarden)
  map.add_edge(peaceGarden, hub, 7.2)

  map.add_vertex(sugarHouse)
  map.add_edge(sugarHouse, hub, 3.8)
  map.add_edge(sugarHouse, peaceGarden, 7.1)

  map.add_vertex(hertigageCityGov)
  map.add_edge(hertigageCityGov, hub, 11.0)
  map.add_edge(hertigageCityGov, peaceGarden, 6.4)
  map.add_edge(hertigageCityGov, peaceGarden, 9.2)

  map.add_vertex(healthServices)
  map.add_edge(healthServices, hub, 2.2)
  map.add_edge(healthServices, peaceGarden, 6.0)
  map.add_edge(healthServices, sugarHouse, 4.4)
  map.add_edge(healthServices, sugarHouse, 5.6)

  map.add_vertex(publicWorks)
  map.add_edge(publicWorks, hub, 3.5)
  map.add_edge(publicWorks, peaceGarden, 4.8)
  map.add_edge(publicWorks, sugarHouse, 2.8)
  map.add_edge(publicWorks, sugarHouse, 6.9)
  map.add_edge(publicWorks, healthServices, 1.9)

  map.add_vertex(streetsAndSanitation)
  map.add_edge(streetsAndSanitation, hub, 10.9)
  map.add_edge(streetsAndSanitation, peaceGarden, 1.6)
  map.add_edge(streetsAndSanitation, sugarHouse, 8.6)
  map.add_edge(streetsAndSanitation, sugarHouse, 8.6)
  map.add_edge(streetsAndSanitation, healthServices, 7.9)
  map.add_edge(streetsAndSanitation, publicWorks, 6.3)

  map.add_vertex(dekerLake)
  map.add_edge(dekerLake, hub, 8.6)
  map.add_edge(dekerLake, peaceGarden, 2.8)
  map.add_edge(dekerLake, sugarHouse, 6.3)
  map.add_edge(dekerLake, sugarHouse, 4.0)
  map.add_edge(dekerLake, healthServices, 5.1)
  map.add_edge(dekerLake, publicWorks, 4.3)
  map.add_edge(dekerLake, streetsAndSanitation, 4.0)

  map.add_vertex(ottingerHall)
  map.add_edge(ottingerHall, hub, 7.6)
  map.add_edge(ottingerHall, peaceGarden, 4.8)
  map.add_edge(ottingerHall, sugarHouse, 5.3)
  map.add_edge(ottingerHall, sugarHouse, 11.1)
  map.add_edge(ottingerHall, healthServices, 7.5)
  map.add_edge(ottingerHall, publicWorks, 4.5)
  map.add_edge(ottingerHall, streetsAndSanitation, 4.2)
  map.add_edge(ottingerHall, dekerLake, 7.7)

  map.add_vertex(columbusLibrary)
  map.add_edge(columbusLibrary, hub, 2.8)
  map.add_edge(columbusLibrary, peaceGarden, 6.3)
  map.add_edge(columbusLibrary, sugarHouse, 1.6)
  map.add_edge(columbusLibrary, sugarHouse, 7.3)
  map.add_edge(columbusLibrary, healthServices, 2.6)
  map.add_edge(columbusLibrary, publicWorks, 1.5)
  map.add_edge(columbusLibrary, streetsAndSanitation, 8.0)
  map.add_edge(columbusLibrary, dekerLake, 9.3)
  map.add_edge(columbusLibrary, ottingerHall, 4.8)

  map.add_vertex(taylorsvilleCityHall)
  map.add_edge(taylorsvilleCityHall, hub, 6.4)
  map.add_edge(taylorsvilleCityHall, peaceGarden, 7.3)
  map.add_edge(taylorsvilleCityHall, sugarHouse, 10.4)
  map.add_edge(taylorsvilleCityHall, sugarHouse, 1.0)
  map.add_edge(taylorsvilleCityHall, healthServices, 6.5)
  map.add_edge(taylorsvilleCityHall, publicWorks, 8.7)
  map.add_edge(taylorsvilleCityHall, streetsAndSanitation, 8.6)
  map.add_edge(taylorsvilleCityHall, dekerLake, 4.6)
  map.add_edge(taylorsvilleCityHall, ottingerHall, 11.9)
  map.add_edge(taylorsvilleCityHall, columbusLibrary, 9.4)

  map.add_vertex(southSaltPolice)
  map.add_edge(southSaltPolice, hub, 3.2)
  map.add_edge(southSaltPolice, peaceGarden, 5.3)
  map.add_edge(southSaltPolice, sugarHouse, 3.0)
  map.add_edge(southSaltPolice, sugarHouse, 6.4)
  map.add_edge(southSaltPolice, healthServices, 1.5)
  map.add_edge(southSaltPolice, publicWorks, 0.8)
  map.add_edge(southSaltPolice, streetsAndSanitation, 6.9)
  map.add_edge(southSaltPolice, dekerLake, 4.8)
  map.add_edge(southSaltPolice, ottingerHall, 4.7)
  map.add_edge(southSaltPolice, columbusLibrary, 1.1)
  map.add_edge(southSaltPolice, taylorsvilleCityHall, 7.3)

  map.add_vertex(councilHall)
  map.add_edge(councilHall, hub, 7.6)
  map.add_edge(councilHall, peaceGarden, 4.8)
  map.add_edge(councilHall, sugarHouse, 5.3)
  map.add_edge(councilHall, sugarHouse, 11.1)
  map.add_edge(councilHall, healthServices, 7.5)
  map.add_edge(councilHall, publicWorks, 4.5)
  map.add_edge(councilHall, streetsAndSanitation, 4.2)
  map.add_edge(councilHall, dekerLake, 7.7)
  map.add_edge(councilHall, ottingerHall, 0.6)
  map.add_edge(councilHall, columbusLibrary, 5.1)
  map.add_edge(councilHall, taylorsvilleCityHall, 12.0)
  map.add_edge(councilHall, southSaltPolice, 4.7)

  map.add_vertex(redwoodPark)
  map.add_edge(redwoodPark, hub, 5.2)
  map.add_edge(redwoodPark, peaceGarden, 3.0)
  map.add_edge(redwoodPark, sugarHouse, 6.5)
  map.add_edge(redwoodPark, sugarHouse, 3.9)
  map.add_edge(redwoodPark, healthServices, 3.2)
  map.add_edge(redwoodPark, publicWorks, 3.9)
  map.add_edge(redwoodPark, streetsAndSanitation, 4.2)
  map.add_edge(redwoodPark, dekerLake, 1.6)
  map.add_edge(redwoodPark, ottingerHall, 7.6)
  map.add_edge(redwoodPark, columbusLibrary, 4.6)
  map.add_edge(redwoodPark, taylorsvilleCityHall, 4.9)
  map.add_edge(redwoodPark, southSaltPolice, 3.5)
  map.add_edge(redwoodPark, councilHall, 7.3)

  map.add_vertex(slcMentalHealth)
  map.add_edge(slcMentalHealth, hub, 4.4)
  map.add_edge(slcMentalHealth, peaceGarden, 4.6)
  map.add_edge(slcMentalHealth, sugarHouse, 5.6)
  map.add_edge(slcMentalHealth, sugarHouse, 4.3)
  map.add_edge(slcMentalHealth, healthServices, 2.4)
  map.add_edge(slcMentalHealth, publicWorks, 3.0)
  map.add_edge(slcMentalHealth, streetsAndSanitation, 8.0)
  map.add_edge(slcMentalHealth, dekerLake, 3.3)
  map.add_edge(slcMentalHealth, ottingerHall, 7.8)
  map.add_edge(slcMentalHealth, columbusLibrary, 3.7)
  map.add_edge(slcMentalHealth, taylorsvilleCityHall, 5.2)
  map.add_edge(slcMentalHealth, southSaltPolice, 2.6)
  map.add_edge(slcMentalHealth, councilHall, 7.8)
  map.add_edge(slcMentalHealth, redwoodPark, 1.3)

  map.add_vertex(slcPolice)
  map.add_edge(slcPolice, hub, 3.7)
  map.add_edge(slcPolice, peaceGarden, 4.5)
  map.add_edge(slcPolice, sugarHouse, 5.8)
  map.add_edge(slcPolice, sugarHouse, 4.4)
  map.add_edge(slcPolice, healthServices, 2.7)
  map.add_edge(slcPolice, publicWorks, 3.8)
  map.add_edge(slcPolice, streetsAndSanitation, 5.8)
  map.add_edge(slcPolice, dekerLake, 3.4)
  map.add_edge(slcPolice, ottingerHall, 6.6)
  map.add_edge(slcPolice, columbusLibrary, 4.0)
  map.add_edge(slcPolice, taylorsvilleCityHall, 5.4)
  map.add_edge(slcPolice, southSaltPolice, 2.9)
  map.add_edge(slcPolice, councilHall, 6.6)
  map.add_edge(slcPolice, redwoodPark, 1.5)
  map.add_edge(slcPolice, slcMentalHealth, 1.5)

  map.add_vertex(westValleyProsecutor)
  map.add_edge(westValleyProsecutor, hub, 7.6)
  map.add_edge(westValleyProsecutor, peaceGarden, 7.4)
  map.add_edge(westValleyProsecutor, sugarHouse, 5.7)
  map.add_edge(westValleyProsecutor, sugarHouse, 7.2)
  map.add_edge(westValleyProsecutor, healthServices, 1.4)
  map.add_edge(westValleyProsecutor, publicWorks, 5.7)
  map.add_edge(westValleyProsecutor, streetsAndSanitation, 7.2)
  map.add_edge(westValleyProsecutor, dekerLake, 3.1)
  map.add_edge(westValleyProsecutor, ottingerHall, 7.2)
  map.add_edge(westValleyProsecutor, columbusLibrary, 6.7)
  map.add_edge(westValleyProsecutor, taylorsvilleCityHall, 8.1)
  map.add_edge(westValleyProsecutor, southSaltPolice, 6.3)
  map.add_edge(westValleyProsecutor, councilHall, 7.2)
  map.add_edge(westValleyProsecutor, redwoodPark, 4.0)
  map.add_edge(westValleyProsecutor, slcMentalHealth, 6.4)
  map.add_edge(westValleyProsecutor, slcPolice, 5.6)

  map.add_vertex(slcHousingAuth)
  map.add_edge(slcHousingAuth, hub, 2.0)
  map.add_edge(slcHousingAuth, peaceGarden, 6.0)
  map.add_edge(slcHousingAuth, sugarHouse, 4.1)
  map.add_edge(slcHousingAuth, sugarHouse, 5.3)
  map.add_edge(slcHousingAuth, healthServices, 0.5)
  map.add_edge(slcHousingAuth, publicWorks, 1.9)
  map.add_edge(slcHousingAuth, streetsAndSanitation, 7.7)
  map.add_edge(slcHousingAuth, dekerLake, 5.1)
  map.add_edge(slcHousingAuth, ottingerHall, 5.9)
  map.add_edge(slcHousingAuth, columbusLibrary, 2.3)
  map.add_edge(slcHousingAuth, taylorsvilleCityHall, 6.2)
  map.add_edge(slcHousingAuth, southSaltPolice, 1.2)
  map.add_edge(slcHousingAuth, councilHall, 5.9)
  map.add_edge(slcHousingAuth, redwoodPark, 3.2)
  map.add_edge(slcHousingAuth, slcMentalHealth, 2.4)
  map.add_edge(slcHousingAuth, slcPolice, 1.6)
  map.add_edge(slcHousingAuth, westValleyProsecutor, 7.1)

  map.add_vertex(dmv)
  map.add_edge(dmv, hub, 3.6)
  map.add_edge(dmv, peaceGarden, 5.0)
  map.add_edge(dmv, sugarHouse, 3.6)
  map.add_edge(dmv, sugarHouse, 6.0)
  map.add_edge(dmv, healthServices, 1.7)
  map.add_edge(dmv, publicWorks, 1.1)
  map.add_edge(dmv, streetsAndSanitation, 6.6)
  map.add_edge(dmv, dekerLake, 4.6)
  map.add_edge(dmv, ottingerHall, 5.4)
  map.add_edge(dmv, columbusLibrary, 1.8)
  map.add_edge(dmv, taylorsvilleCityHall, 6.9)
  map.add_edge(dmv, southSaltPolice, 1.0)
  map.add_edge(dmv, councilHall, 5.4)
  map.add_edge(dmv, redwoodPark, 3.0)
  map.add_edge(dmv, slcMentalHealth, 2.2)
  map.add_edge(dmv, slcPolice, 1.7)
  map.add_edge(dmv, westValleyProsecutor, 6.1)
  map.add_edge(dmv, slcHousingAuth, 1.6)

  map.add_vertex(juvenileCourt)
  map.add_edge(juvenileCourt, hub, 6.5)
  map.add_edge(juvenileCourt, peaceGarden, 4.8)
  map.add_edge(juvenileCourt, sugarHouse, 4.3)
  map.add_edge(juvenileCourt, sugarHouse, 10.6)
  map.add_edge(juvenileCourt, healthServices, 6.5)
  map.add_edge(juvenileCourt, publicWorks, 3.5)
  map.add_edge(juvenileCourt, streetsAndSanitation, 3.2)
  map.add_edge(juvenileCourt, dekerLake, 6.7)
  map.add_edge(juvenileCourt, ottingerHall, 1.0)
  map.add_edge(juvenileCourt, columbusLibrary, 4.1)
  map.add_edge(juvenileCourt, taylorsvilleCityHall, 11.5)
  map.add_edge(juvenileCourt, southSaltPolice, 3.7)
  map.add_edge(juvenileCourt, councilHall, 1.0)
  map.add_edge(juvenileCourt, redwoodPark, 6.9)
  map.add_edge(juvenileCourt, slcMentalHealth, 6.8)
  map.add_edge(juvenileCourt, slcPolice, 6.4)
  map.add_edge(juvenileCourt, westValleyProsecutor, 7.2)
  map.add_edge(juvenileCourt, slcHousingAuth, 4.9)
  map.add_edge(juvenileCourt, dmv, 4.4)

  map.add_vertex(cottonwoodSoftball)
  map.add_edge(cottonwoodSoftball, hub, 1.9)
  map.add_edge(cottonwoodSoftball, peaceGarden, 9.5)
  map.add_edge(cottonwoodSoftball, sugarHouse, 3.3)
  map.add_edge(cottonwoodSoftball, sugarHouse, 5.9)
  map.add_edge(cottonwoodSoftball, healthServices, 3.2)
  map.add_edge(cottonwoodSoftball, publicWorks, 4.9)
  map.add_edge(cottonwoodSoftball, streetsAndSanitation, 11.2)
  map.add_edge(cottonwoodSoftball, dekerLake, 8.1)
  map.add_edge(cottonwoodSoftball, ottingerHall, 8.5)
  map.add_edge(cottonwoodSoftball, columbusLibrary, 3.8)
  map.add_edge(cottonwoodSoftball, taylorsvilleCityHall, 6.9)
  map.add_edge(cottonwoodSoftball, southSaltPolice, 4.1)
  map.add_edge(cottonwoodSoftball, councilHall, 8.5)
  map.add_edge(cottonwoodSoftball, redwoodPark, 6.2)
  map.add_edge(cottonwoodSoftball, slcMentalHealth, 5.3)
  map.add_edge(cottonwoodSoftball, slcPolice, 4.9)
  map.add_edge(cottonwoodSoftball, westValleyProsecutor, 10.6)
  map.add_edge(cottonwoodSoftball, slcHousingAuth, 3.0)
  map.add_edge(cottonwoodSoftball, dmv, 4.6)
  map.add_edge(cottonwoodSoftball, juvenileCourt, 7.5)

  map.add_vertex(holidayCityOffice)
  map.add_edge(holidayCityOffice, hub, 3.4)
  map.add_edge(holidayCityOffice, peaceGarden, 10.9)
  map.add_edge(holidayCityOffice, sugarHouse, 5.0)
  map.add_edge(holidayCityOffice, sugarHouse, 7.4)
  map.add_edge(holidayCityOffice, healthServices, 5.2)
  map.add_edge(holidayCityOffice, publicWorks, 6.9)
  map.add_edge(holidayCityOffice, streetsAndSanitation, 12.7)
  map.add_edge(holidayCityOffice, dekerLake, 10.4)
  map.add_edge(holidayCityOffice, ottingerHall, 10.3)
  map.add_edge(holidayCityOffice, columbusLibrary, 5.8)
  map.add_edge(holidayCityOffice, taylorsvilleCityHall, 8.3)
  map.add_edge(holidayCityOffice, southSaltPolice, 6.2)
  map.add_edge(holidayCityOffice, councilHall, 10.3)
  map.add_edge(holidayCityOffice, redwoodPark, 8.2)
  map.add_edge(holidayCityOffice, slcMentalHealth, 7.4)
  map.add_edge(holidayCityOffice, slcPolice, 6.9)
  map.add_edge(holidayCityOffice, westValleyProsecutor, 12.0)
  map.add_edge(holidayCityOffice, slcHousingAuth, 5.0)
  map.add_edge(holidayCityOffice, dmv, 6.6)
  map.add_edge(holidayCityOffice, juvenileCourt, 9.3)
  map.add_edge(holidayCityOffice, cottonwoodSoftball, 2.0)

  map.add_vertex(murrayMuseum)
  map.add_edge(murrayMuseum, hub, 2.4)
  map.add_edge(murrayMuseum, peaceGarden, 8.3)
  map.add_edge(murrayMuseum, sugarHouse, 6.1)
  map.add_edge(murrayMuseum, sugarHouse, 4.7)
  map.add_edge(murrayMuseum, healthServices, 2.5)
  map.add_edge(murrayMuseum, publicWorks, 4.2)
  map.add_edge(murrayMuseum, streetsAndSanitation, 10.0)
  map.add_edge(murrayMuseum, dekerLake, 7.8)
  map.add_edge(murrayMuseum, ottingerHall, 7.8)
  map.add_edge(murrayMuseum, columbusLibrary, 4.3)
  map.add_edge(murrayMuseum, taylorsvilleCityHall, 4.1)
  map.add_edge(murrayMuseum, southSaltPolice, 3.4)
  map.add_edge(murrayMuseum, councilHall, 7.8)
  map.add_edge(murrayMuseum, redwoodPark, 5.5)
  map.add_edge(murrayMuseum, slcMentalHealth, 4.6)
  map.add_edge(murrayMuseum, slcPolice, 4.2)
  map.add_edge(murrayMuseum, westValleyProsecutor, 9.4)
  map.add_edge(murrayMuseum, slcHousingAuth, 2.3)
  map.add_edge(murrayMuseum, dmv, 3.9)
  map.add_edge(murrayMuseum, juvenileCourt, 6.8)
  map.add_edge(murrayMuseum, cottonwoodSoftball, 2.9)
  map.add_edge(murrayMuseum, holidayCityOffice, 4.4)

  map.add_vertex(vrSoftball)
  map.add_edge(vrSoftball, hub, 6.4)
  map.add_edge(vrSoftball, peaceGarden, 6.9)
  map.add_edge(vrSoftball, sugarHouse, 9.7)
  map.add_edge(vrSoftball, sugarHouse, 0.6)
  map.add_edge(vrSoftball, healthServices, 6.0)
  map.add_edge(vrSoftball, publicWorks, 9.0)
  map.add_edge(vrSoftball, streetsAndSanitation, 8.2)
  map.add_edge(vrSoftball, dekerLake, 4.2)
  map.add_edge(vrSoftball, ottingerHall, 11.5)
  map.add_edge(vrSoftball, columbusLibrary, 7.8)
  map.add_edge(vrSoftball, taylorsvilleCityHall, 0.4)
  map.add_edge(vrSoftball, southSaltPolice, 6.9)
  map.add_edge(vrSoftball, councilHall, 11.5)
  map.add_edge(vrSoftball, redwoodPark, 4.4)
  map.add_edge(vrSoftball, slcMentalHealth, 4.8)
  map.add_edge(vrSoftball, slcPolice, 5.6)
  map.add_edge(vrSoftball, westValleyProsecutor, 7.5)
  map.add_edge(vrSoftball, slcHousingAuth, 5.5)
  map.add_edge(vrSoftball, dmv, 6.5)
  map.add_edge(vrSoftball, juvenileCourt, 11.4)
  map.add_edge(vrSoftball, cottonwoodSoftball, 6.4)
  map.add_edge(vrSoftball, holidayCityOffice, 7.9)
  map.add_edge(vrSoftball, murrayMuseum, 4.5)

  map.add_vertex(rockSprings)
  map.add_edge(rockSprings, hub, 2.4)
  map.add_edge(rockSprings, peaceGarden, 10.0)
  map.add_edge(rockSprings, sugarHouse, 6.1)
  map.add_edge(rockSprings, sugarHouse, 6.4)
  map.add_edge(rockSprings, healthServices, 4.2)
  map.add_edge(rockSprings, publicWorks, 5.9)
  map.add_edge(rockSprings, streetsAndSanitation, 11.7)
  map.add_edge(rockSprings, dekerLake, 9.5)
  map.add_edge(rockSprings, ottingerHall, 9.5)
  map.add_edge(rockSprings, columbusLibrary, 4.8)
  map.add_edge(rockSprings, taylorsvilleCityHall, 4.9)
  map.add_edge(rockSprings, southSaltPolice, 5.2)
  map.add_edge(rockSprings, councilHall, 9.5)
  map.add_edge(rockSprings, redwoodPark, 7.2)
  map.add_edge(rockSprings, slcMentalHealth, 6.3)
  map.add_edge(rockSprings, slcPolice, 5.9)
  map.add_edge(rockSprings, westValleyProsecutor, 11.1)
  map.add_edge(rockSprings, slcHousingAuth, 4.0)
  map.add_edge(rockSprings, dmv, 5.6)
  map.add_edge(rockSprings, juvenileCourt, 8.5)
  map.add_edge(rockSprings, cottonwoodSoftball, 2.8)
  map.add_edge(rockSprings, holidayCityOffice, 3.4)
  map.add_edge(rockSprings, murrayMuseum, 1.7)
  map.add_edge(rockSprings, vrSoftball, 5.4)

  map.add_vertex(rtPavillionPark)
  map.add_edge(rtPavillionPark, hub, 5.0)
  map.add_edge(rtPavillionPark, peaceGarden, 4.4)
  map.add_edge(rtPavillionPark, sugarHouse, 2.8)
  map.add_edge(rtPavillionPark, sugarHouse, 10.1)
  map.add_edge(rtPavillionPark, healthServices, 5.4)
  map.add_edge(rtPavillionPark, publicWorks, 3.5)
  map.add_edge(rtPavillionPark, streetsAndSanitation, 5.1)
  map.add_edge(rtPavillionPark, dekerLake, 6.2)
  map.add_edge(rtPavillionPark, ottingerHall, 2.8)
  map.add_edge(rtPavillionPark, columbusLibrary, 3.2)
  map.add_edge(rtPavillionPark, taylorsvilleCityHall, 11.0)
  map.add_edge(rtPavillionPark, southSaltPolice, 3.7)
  map.add_edge(rtPavillionPark, councilHall, 2.8)
  map.add_edge(rtPavillionPark, redwoodPark, 6.4)
  map.add_edge(rtPavillionPark, slcMentalHealth, 6.5)
  map.add_edge(rtPavillionPark, slcPolice, 5.7)
  map.add_edge(rtPavillionPark, westValleyProsecutor, 6.2)
  map.add_edge(rtPavillionPark, slcHousingAuth, 5.1)
  map.add_edge(rtPavillionPark, dmv, 4.3)
  map.add_edge(rtPavillionPark, juvenileCourt, 1.8)
  map.add_edge(rtPavillionPark, cottonwoodSoftball, 6.0)
  map.add_edge(rtPavillionPark, holidayCityOffice, 7.9)
  map.add_edge(rtPavillionPark, murrayMuseum, 6.8)
  map.add_edge(rtPavillionPark, vrSoftball, 10.6)
  map.add_edge(rtPavillionPark, rockSprings, 7.0)

  map.add_vertex(historicFarm)
  map.add_edge(historicFarm, hub, 3.6)
  map.add_edge(historicFarm, peaceGarden, 13.0)
  map.add_edge(historicFarm, sugarHouse, 7.4)
  map.add_edge(historicFarm, sugarHouse, 10.1)
  map.add_edge(historicFarm, healthServices, 5.5)
  map.add_edge(historicFarm, publicWorks, 7.2)
  map.add_edge(historicFarm, streetsAndSanitation, 14.2)
  map.add_edge(historicFarm, dekerLake, 10.7)
  map.add_edge(historicFarm, ottingerHall, 14.1)
  map.add_edge(historicFarm, columbusLibrary, 6.0)
  map.add_edge(historicFarm, taylorsvilleCityHall, 6.8)
  map.add_edge(historicFarm, southSaltPolice, 6.4)
  map.add_edge(historicFarm, councilHall, 14.1)
  map.add_edge(historicFarm, redwoodPark, 10.5)
  map.add_edge(historicFarm, slcMentalHealth, 8.8)
  map.add_edge(historicFarm, slcPolice, 8.4)
  map.add_edge(historicFarm, westValleyProsecutor, 13.6)
  map.add_edge(historicFarm, slcHousingAuth, 5.2)
  map.add_edge(historicFarm, dmv, 6.9)
  map.add_edge(historicFarm, juvenileCourt, 13.1)
  map.add_edge(historicFarm, cottonwoodSoftball, 4.1)
  map.add_edge(historicFarm, holidayCityOffice, 4.7)
  map.add_edge(historicFarm, murrayMuseum, 3.1)
  map.add_edge(historicFarm, vrSoftball, 7.8)
  map.add_edge(historicFarm, rockSprings, 1.3)
  map.add_edge(historicFarm, rtPavillionPark, 8.3)

  return map

def main():
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

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
]

def main():
  print("hello")

main()

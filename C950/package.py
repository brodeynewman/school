class Package:
  def __init__(self, id, address, city, zip, delivery_deadline, weight, notes):
    self.id = id
    self.address = address
    self.city = city
    self.zip = zip
    self.delivery_deadline = delivery_deadline
    self.weight = weight
    self.notes = notes
    self.delivery_time = None
    self.departure_time = None

  def set_departure_time(self, depart_time):
    self.departure_time = depart_time

  def set_delivered_time(self, delivery_time):
    self.delivery_time = delivery_time

  def get_status_by_time(self, time):
    if self.delivery_time < time:
      return "Delivered"
    elif time < self.departure_time:
      return "At Hub"

    return "En Route"
  
  def print(self, time):
    log = f'''
      Package Information:

        ID: {self.id}
        Address: {self.address}
        City: {self.city}
        Zip: {self.zip}
        Weight: {self.weight}
        Delivery Deadline: {self.delivery_deadline}
        Delivery Time: {self.delivery_time}
        Status: {self.get_status_by_time(time)}
    '''

    print(log)


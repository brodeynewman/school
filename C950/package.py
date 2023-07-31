END_OF_DAY = "EOD"
STATUS_EN_ROUTE = 'en_route'
STATUS_DELIVERED = 'delivered'

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

  def set_delivered_time(self, delivery_time):
    self.status = STATUS_DELIVERED
    self.delivery_time = delivery_time

  def get_status_by_time(self, time):
    if self.delivery_time < time:
      return "Delivered"

    return "En Route"
  
  def __str__(self):
    return "%s, %s, %s, %s, %s, %s, %s" % (self.id, self.address, self.city, self.zip, self.delivery_deadline, self.weight, self.delivery_time)


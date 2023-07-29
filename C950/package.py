END_OF_DAY = "EOD"
STATUS_AT_HUB = "at_hub"

class Package:
  def __init__(self, id, address, city, zip, delivery_deadline, weight, notes, status = STATUS_AT_HUB):
    self.id = id
    self.address = address
    self.city = city
    self.zip = zip
    self.delivery_deadline = delivery_deadline
    self.weight = weight
    self.notes = notes
    self.status = status

  def has_deadline(self):
    return self.delivery_deadline != END_OF_DAY

  def get_deadline(self):
    return self.delivery_deadline

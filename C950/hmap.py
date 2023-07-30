class HashMap(object):
  def __init__(self, size = 16):
    self.count = 0
    self.keys = [None] * size
    self.items = [None] * size
    self.size = size

  def hash(self, key):
    return key.__hash__() % self.size

  def rehash(self, prev_hash):
    return (prev_hash + 1) % self.size
  
  def size(self):
    return self.count
  
  def set(self, key, value):
    hash = self.hash(key)

    if self.keys[hash] is None: 
      self.keys[hash] = key
      self.items[hash] = value
      self.count += 1

      return True
    else:
      if self.keys[hash] == key:
        self.items[hash] = value

        return True
      else:
        rehash = self.rehash(hash)

        # keep trying...
        while (not self.keys[rehash] is None) and (rehash != hash):
          rehash = self.rehash(rehash)
        # Double check if we found an empty spot.
        if self.keys[rehash] is None: 
          self.keys[rehash] = key
          self.items[rehash] = value
          self.count += 1

          return True
        else:
          return False

  def get(self, key):
    initial = self.hash(key)
    current = initial
  
    while (not self.keys[current] is None):
      if self.keys[current] == key:
        return self.items[current]
      else:
        # we rehash, which creates a new value
        # for us to continue to iterate, since rehash probes + 1
        current = self.rehash(current)

        if current == initial: 
          break

    return None

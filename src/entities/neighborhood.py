from entities.vector import Vector

class Neighborhood():
  name: str
  scores: Vector

  def __init__(self, name: str, scores: Vector):
    self.name = name
    self.scores = scores

  def __str__(self):
    return f'Neighborhood(scores:{self.scores})'
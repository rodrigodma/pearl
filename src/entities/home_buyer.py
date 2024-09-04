from entities.vector import Vector

class Home_Buyers():
  name: str
  goals: Vector
  preferences: [] # type: ignore
  current_preference: int
  setted = bool

  def __init__(self, name: str, goals: Vector, preferences: list):
    self.name = name
    self.goals = goals
    self.preferences = preferences
    self.setted = False

  def fit(self, score: Vector):
    return self.goals.energy_efficiency * score.energy_efficiency + self.goals.water * score.water + self.goals.resilience * score.resilience

  def change_preferences(self):
    if self.current_preference < len(self.preferences) - 1:
      self.current_preference += 1

  def __str__(self):
    return f'Home_Buyers(goals:{self.goals},preferences:{self.preferences})'
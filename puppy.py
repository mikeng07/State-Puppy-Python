import state_asleep
class Puppy:
  """Represents a puppy object"""
  def __init__(self):
    self._state = state_asleep.StateAsleep()
    self.reset()

  def plays(self):
    """Access number of times the puppy has played in a row."""
    return self._plays
    
  def feeds(self):
    """Access number of times the puppy has eaten in a row."""
    return self._feeds
    
  def change_state(self, new_state):
    """Updates the puppy's state"""
    self._state = new_state

  def throw_ball(self):
    """Plays with the puppy."""
    return self._state.play(self)

  def give_food(self):
    """Feeds the puppy."""
    return self._state.feed(self)

  def inc_feeds(self):
    """Increments the number of times the puppy has been fed."""
    self._feeds += 1
    
  def inc_plays(self):
    """Increments the number of time the puppy has bee played with."""
    self._plays += 1
    
  def reset(self):
    """Resets the number of times that the puppy has been fed or played with."""
    self._plays = 0
    self._feeds = 0
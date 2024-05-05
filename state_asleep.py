import puppy_state
import state_eat
class StateAsleep(puppy_state.PuppyState):
  """Puppy is in the Asleep state."""
  def play(self, puppy):
    """Plays with the puppy."""
    return "The puppy is asleep.  It doesn't want to play right now."
    
  def feed(self, puppy):
    """Feeds the puppy."""
    puppy.change_state(state_eat.StateEat())
    puppy.inc_feeds()
    return "The puppy wakes up and comes running to eat."
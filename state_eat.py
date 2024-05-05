import puppy_state
import state_play
import state_asleep
class StateEat(puppy_state.PuppyState):
  """Puppy is in the Eating state."""
  def play(self, puppy):
    """Plays with the puppy."""
    puppy.change_state(state_play.StatePlay())
    puppy.inc_plays()
    return "The puppy looks up from its food and chases the ball you threw."
    
  def feed(self, puppy):
    """Feeds the puppy."""
    s = "The puppy continues to eat as you add another scoop of kibble to its bowl."
    puppy.inc_feeds()
    if puppy.feeds() > 2:
      puppy.change_state(state_asleep.StateAsleep())
      s += "\nThe puppy at so much it fell asleep!"
      puppy.reset()
    return s
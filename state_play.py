import puppy_state
import state_asleep


class StatePlay(puppy_state.PuppyState):
    """Puppy is in the Playing state."""

    def play(self, puppy):
        """Plays with the puppy."""
        s = "You throw the ball again and the puppy excitedly chases it."
        puppy.inc_plays()
        if puppy.plays() > 2:
            puppy.change_state(state_asleep.StateAsleep())
            s += "\nThe puppy played so much it fell asleep!"
            puppy.reset()
        return s

    def feed(self, puppy):
        """Feeds the puppy."""
        return "The puppy is too busy playing with the ball to eat right now."

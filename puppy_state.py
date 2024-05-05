import abc
class PuppyState(abc.ABC):
  """Represents the states of the puppy."""
  @abc.abstractmethod
  def play(self, puppy):
    """Plays with the puppy."""
    pass

  @abc.abstractmethod
  def feed(self, puppy):
    """Feeds the puppy."""
    pass
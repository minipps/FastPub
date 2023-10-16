from schemas import Object, Collection, Link
from pydantic import ForwardRef, Optional


class Actor(Object):
    inbox : Collection # should be OrderedCollection
    outbox : Collection
    following : Optional[Link]
    followers : Optional[Link]
    liked : Optional[Link]
    
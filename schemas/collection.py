
from schemas.object import Object
from schemas.link import Link
from schemas.collection_page import CollectionPage
from typing import Annotated
from annotated_types import Ge


class Collection(Object):
    totalItems : Annotated[int, Ge(0)]
    current : CollectionPage
    first : CollectionPage
    last : CollectionPage
    items : [Object | Link]
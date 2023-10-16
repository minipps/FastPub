from annotated_types import Union
from pydantic import ForwardRef
from schemas.object import Object
from schemas.collection import Collection
from schemas.link import Link


CollectionPage = ForwardRef('CollectionPage')
class CollectionPage(Object):
    partOf : Union[Link, Collection]
    prev : Union[Link, CollectionPage]
    next : Union[Link, CollectionPage]
    
CollectionPage.resolve_model()

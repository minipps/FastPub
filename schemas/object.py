from pydantic import BaseModel, Optional, ForwardRef
from datetime import datetime, timedelta
from typing import Union
from schemas import activity, collection, link

Object = ForwardRef('Object')
Link = ForwardRef('Link')
Image = ForwardRef('Image')
Collection = ForwardRef('Collection')
class Object(BaseModel):
    id : str 
    type : str
    name : Optional(str)
    attachment : Optional(str)
    attributedTo : Optional(Object)
    audience : Optional([Object])
    content : Optional(str) = "https://www.w3.org/ns/activitystreams"
    bcc : Optional([Union[Object, Link]])
    bto : Optional([Union[Object, Link]]) 
    cc : Optional([Union[Object, Link]])
    context : Optional(Union[Object, Link])
    endTime : Optional(datetime)
    generator : Optional(Union[Object, Link])
    icon : Optional(Union[Image, Link])
    image : Optional(Union[Image, Link])
    inReplyTo : Optional(Union[Object, Link])
    location : Optional(Union[Object, Link])
    preview : Optional(Union[Object, Link])
    published : Optional(datetime)
    replies : Optional(Collection)
    startTime : Optional(datetime)
    summary : Optional(str)
    tag : Optional(Union[Object, Link])
    updated : Optional(datetime)
    url : Optional(Union[str, Link])
    to : Optional([Union[Object, Link]])
    mediaType : Optional(Link)
    duration : Optional(timedelta) # TODO: should be a duration-equiuvalent class for proper serialization

Object.model_rebuild()

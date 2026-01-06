from enum import Enum
from pydantic import BaseModel


class EventType(str,Enum):
    EXACT = "exact"
    OVER ="over"
    UNDER ="under"

class Event(BaseModel):
    occurred: bool
    value: int = 0
    eventType: EventType  # count, overUnder

class Stat(BaseModel):
    name: str
    description: str
    isComputed : bool = False

class PlayerEvent(Event):
    player: str
    stat : Stat
    #really just a integer but float for consistency
    #ex over 8.5 points == >= 9 points

class TeamEvent(Event):
    team: str
    stat : Stat
    #really just a integer but float for consistency
    #ex over 8.5 points == >= 9 points
    


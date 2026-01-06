from models import Stat,PlayerEvent,EventType

def test_player_event_model():
    stat = Stat(name="points", description="Total points scored", isComputed=False)
    event = PlayerEvent(occurred=True, player="John Doe", stat=stat, value=12, eventType=EventType.OVER)

    print(event)

if __name__ == "__main__":
    test_player_event_model()
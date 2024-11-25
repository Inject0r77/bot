class MusicQueue:
    def __init__(self):
        self.queue = []

    def add_track(self, track: str) -> None:
        self.queue.append(track)

    def get_next_track(self) -> str | None:
        return self.queue.pop(0) if self.queue else None

    def clear(self) -> None:
        self.queue.clear()

    def list_tracks(self) -> list[str]:
        return self.queue

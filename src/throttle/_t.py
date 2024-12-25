import time


class Throttle:

    def __init__(self, interval: float):
        self._interval = interval
        self._last_time = 0

    def __bool__(self) -> bool:
        now = time.time()
        if now - self._last_time > self._interval:
            self._last_time = now
            return True
        return False

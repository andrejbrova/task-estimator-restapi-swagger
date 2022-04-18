class RunningMode:
    DEBUG = "debug"
    NO_LOGS = "no-logs"

    def __init__(self, mode: str) -> None:
        self.mode = mode

    def is_loggable(self) -> bool:
        return self.mode != self.NO_LOGS

class Timer:
    """
    The class responsible for the logical representation of the timer.
    """
    def __init__(self, seconds: int, bonus: int) -> None:
        self.seconds = seconds
        self.bonus = bonus
        self.running = False

    def tick(self) -> bool:
        if self.seconds > 0:
            self.seconds -= 1
            return True
        return False

    def add_bonus(self) -> None:
        self.seconds += self.bonus

    def format_time(self) -> str:
        mins = self.seconds // 60
        secs = self.seconds % 60
        return f"{mins:02}:{secs:02}"

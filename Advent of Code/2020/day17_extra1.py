class ConwayCube:
    def __init__(self, active = False):
        self._active = active


    def activate(self) -> None:
        self._active = True


    def deactivate(self) -> None:
        self._active = False


    def is_active(self) -> bool:
        return self._active


    def display(self) -> str:
        if self._active:
            return '#'
        else:
            return '.'

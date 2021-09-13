from uuid import UUID


class EntityNotFoundException(Exception):
    def __init__(self, name: str, value: UUID):
        self.name = name
        self.value = value

from pydantic import BaseModel

class Name(BaseModel):
    name:str

class Names(BaseModel):
    names: list[Name]


class StoredNames:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.names = []
        return cls._instance

    def add_names(self, name: Name):
        self.names.append(name)

    def get_names(self):
        return self.names
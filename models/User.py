class User:
    def __init__(self, id, name, age):
        super().__init__()
        self.id = id
        self.name = name
        self.age = age

    @property
    def serialize(self):
        return {"id": self.id, "name": self.name, "age": self.age}

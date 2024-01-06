from uuid import uuid4
from datetime import datetime
class BaseModel:
    id = str(uuid4())
    create_at = datetime.now()
    update_at = datetime.now()

    def __str__(self):
        classname = type(self).__name__
        return "[{}] ({}) {}".format(classname, self.id, self.__dict__)
    
    def save(self):
        self.update_at = datetime.now()

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["create_at"] = self.create_at.isoformat()
        obj_dict["update_at"] = self.update_at.isoformat()
        return obj_dict

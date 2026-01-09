from abc import ABC, abstractmethod
from pickle import loads as pickle_load
from pickle import dumps as pickle_dump
from json import loads as json_load
from json import dumps as json_dump


class SerializedFileHandler(ABC):

    def __init__(self, file_name):
        self.file_name = file_name

    @abstractmethod
    def serialize(self, data):
        pass

    @abstractmethod
    def deserialize(self, data):
        pass

    def write(self, data):
        with open(self.file_name, "wb") as file:
            file.write(self.serialize(data))


    def read(self):
        with open(self.file_name, "rb") as file:
            return self.deserialize(file.read())



class PickleHandler(SerializedFileHandler):
    def serialize(self, data):
        return pickle_dump(data)

    def deserialize(self, data):
        return pickle_load(data)


class JSONHandler(SerializedFileHandler):

    def serialize(self, data):
        # json_str =
        return json_dump(data).encode("utf-8")

    def deserialize(self, data):
        # json_str =
        return json_load(data.decode("utf-8"))


if __name__ == '__main__':
    data = {"name":"Aditya" , "age" : "21"}
    pickle_writer = PickleHandler("data.pkl")
    pickle_writer.write(data)
    print(pickle_writer.read())

    json_writer = JSONHandler("json_data.json")
    json_writer.write(data)
    print(json_writer.read())


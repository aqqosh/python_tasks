from __future__ import annotations
from abc import ABC, abstractmethod

class DataCreator(ABC):

    @abstractmethod
    def factory_method(self):
        pass

    def some_data_opeartion(self):
        pass


class ImageDataCreator(DataCreator):
    def factory_method(self) -> Data:
        return Image()


class TableDataCreator(DataCreator):
    def factory_method(self) -> Data:
        return Table()


class Data(ABC):

    @abstractmethod
    def operation(self):
        pass


class Image(Data):

    def operation(self):
        pass


class Table(Data):

    def operation(self):
        pass


def client_code(creator: DataCreator) -> None:
    pass
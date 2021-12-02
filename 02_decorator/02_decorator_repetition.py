class Data():
    
    def show(self):
        pass
    

class Video(Data):
    
    def show(self):
        pass
    

class Decorator():
    _data: Data = None
    
    def __init__(self, data: Data) -> None:
        self._data = data
        
    @property
    def data(self) -> str:
        return self._component
    
    def show(self) -> None:
        return self._component.operation()


class VideoProcessing(Decorator):
    
    def show(self):
        pass
    

def client_code(data: Data):
    pass
class Component():
    
    def operation(self) -> str:
        pass


class ConcreteComponent(Component):
    
    def operation(self) -> str:
        pass


class Decorator(Component):
    _component: Component = None
    
    def __init__(self, component: Component) -> None:
        self._component = component
        
    @property
    def component(self) -> str:
        return self._component
    
    def operation(self) -> str:
        return self._component.operation()
    

class ConcreteDecoratorA(Decorator):
    
    def operation(self) -> str:
        pass

    
class ConcreteDecoratorB(Decorator):
    
    def operation(self) -> str:
        pass


def client_code(component: Component) -> None:
    # do something with component
    pass
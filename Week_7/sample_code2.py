from abc import ABC, abstractmethod

# 1) Abstract Product
class Shape(ABC):
    @abstractmethod
    def draw(self) -> str:
        """Render the shape and return a description."""
        pass


# 2) Concrete Products
class Circle(Shape):
    def draw(self) -> str:
        return "Drawing a Circle"


class Square(Shape):
    def draw(self) -> str:
        return "Drawing a Square"


# 3) Factory
class ShapeFactory:
    _registry = {
        "circle": Circle,
        "square": Square,
    }


    @classmethod
    def create(cls, shape_type: str) -> Shape:
        shape_cls = cls._registry.get(shape_type.lower())
        if shape_cls is None:
            raise ValueError(f"Unknown shape type: {shape_type!r}. "
                             f"Available: {', '.join(cls._registry)}")
        return shape_cls()
    
    def register_shape(self, shape_type: str, shape_cls: type) -> None:
        if not issubclass(shape_cls, Shape):
            raise ValueError("shape_cls must be a subclass of Shape")
        self._registry[shape_type.lower()] = shape_cls


# 4) Client code (examples)
if __name__ == "__main__":
    factory = ShapeFactory

    circle = factory.create("circle")
    print(circle.draw())  

    square = factory.create("square")
    print(square.draw())  

    try:
        unknown = factory.create("triangle")
    except ValueError as e:
        print(e)

    # Dynamically add a new shape
    class Triangle(Shape):
        def draw(self) -> str:
            return "Drawing a Triangle"
        
    factory.register_shape("triangle", Triangle)
    triangle = factory.create("triangle")
    print(triangle.draw())
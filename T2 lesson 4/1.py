class Box(ABC):
    @abstractmethod
    def add(self, items: list|tuple):
        pass

    @abstractmethod
    def empty(self): # return list/tuple of items in the box
        pass

    @abstractmethod
    def count(self):
        pass


class Item():
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"{self.__class__.__name__}({ self.name !r}, { self.value !r})"

class ListBox(Box):
    def __init__(self):
        self.box_items = list()

    def add(self, *args: Item) -> None:
        for i in args:
            self.box_items.append(i)

    def empty(self) -> list:
        a = self.box_items.copy()
        self.box_items.clear()
        return a

    def count(self) -> int:
        return len(self.box_items)

class DictBox(Box):
    def __init__(self):
        self.box_items = dict()
        self.__id = 0

    def add(self, *args: Item) -> None:
        for i in args:
            self.box_items[self.__id] = i
            self.__id += 1

    def empty(self) -> list:
        a = []
        for i in self.box_items:
            a.append(self.box_items[i])
        self.box_items.clear()
        return a

    def count(self) -> int:
        return len(self.box_items)


def repack_boxes(*args: Box) -> None:
    items = list()
    for i in args:
        items.extend(i.empty())

    idx = 0
    for i in items:
        if idx+1 == len(items)//len(args):
            idx = 0
        else:
            args[idx].add(i)
            idx += 1

    return None


a = ListBox()
a.add(Item('1name', 'value'), Item('2name', 'value'), Item('3name', 'value'), Item('name', 'value') , Item('name', 'value'), Item('name', 'value'), Item('name', 'value'), Item('name', 'value'), Item('name', 'value') , Item('name', 'value'), Item('name', 'value'), Item('name', 'value'), Item('n12ame', 'value'), Item('na12me', 'value'))

d = DictBox()

c = ListBox()

print(repack_boxes(a, d, c))

print(a.count())
print(a.empty())

print(d.count())
print(d.empty())

print(c.count())
print(c.empty())
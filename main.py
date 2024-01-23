# task 1
fib_one = fib_two = 1
n = int(input('Enter number: '))
print(fib_one, fib_two, end=' ')
for i in range(2, n):
    fib_one, fib_two = fib_two, fib_one + fib_two
    print(fib_two, end=' ')


# task 2


# task 3


class Pizza:
    def product(self):
        pass

    def size(self) -> None:
        pass

    def cheese(self) -> None:
        pass

    def pepperoni(self) -> None:
        pass

    def onions(self) -> None:
        pass

    def mushrooms(self) -> None:
        pass

    def bacon(self) -> None:
        pass


class PizzaBuilder(Pizza):
    def __init__(self) -> None:
        self.reset()
        self._product = Product1()

    def reset(self) -> None:
        pass


@property
def product(self, product) -> 'Product_one':
    product = self._product
    self.reset()
    return product


def size(self) -> None:
    self._size.add('Size_part')


def cheese(self) -> None:
    self._cheese.add('Cheese_part')


def pepperoni(self) -> None:
    self._pepperoni.add('Pepperoni_part')


def onions(self) -> None:
    self._onions.add('Onions_part')


def mushrooms(self) -> None:
    self._mushrooms.add('Mushrooms_part')


def bacon(self) -> None:
    self._bacon.add('Bacon_part')


class Product1(Pizza):
    def __init__(self) -> None:
        self.parts = []

    def add(self, part) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f'Product parts: {(self.parts)}', end=' ')


class Director:
    def __init__(self) -> None:
        self._pizza = None


@property
def pizza(self) -> Pizza:
    return self._pizza


@pizza.setter
def pizza(self, pizza: Pizza) -> None:
    self._pizza = pizza


def pizza_minimal_viable_product(self) -> None:
    self.pizza.product_size_part()


def pizza_full_featured_product(self) -> None:
    self.pizza.product_size_part()
    self.pizza.product_cheese_part()
    self.pizza.product_mushrooms_part()
    self.pizza.product_onions_part()
    self.pizza.product_pepperoni_part()
    self.pizza.product_bacon_part()


if __name__ == '__main__':
    director = Director()
    pizza = PizzaBuilder()
    director.pizza = pizza

print('Standard basic product: ')
pizza_minimal_viable_product()
pizza.product.list_parts()

print('\n')

print('Standard full featured product: ')
pizza_full_featured_product()
pizza.product.list_parts()

print('\n')

print('Custom product: ')
pizza.product_size_part()
pizza.product_cheese_part()
pizza.product_pepperoni_part()
pizza.product_onions_part()
pizza.product_bacon_part()
pizza.product_mushrooms_part()
pizza.product.list_parts()

# task 4


# task 5

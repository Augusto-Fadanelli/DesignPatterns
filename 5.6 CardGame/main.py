from compositeDP import *

def client_code(component: Component):
    print(f'RESULT: {component.operation()}')

def client_code2(component1: Component, component2: Component):
    if component1.is_composite():
        component1.add(component2)

    print(f'RESULT: {component1.operation()}')

if __name__ == '__main__':
    simple = Leaf()
    print("Client: I've got a simple component:")
    client_code(simple)
    print()

    tree = Composite()

    branch1 = Composite()
    branch1.add(Leaf())
    branch1.add(Leaf())

    branch2 = Composite()
    branch2.add(Leaf())

    tree.add(branch1)
    tree.add(branch2)

    print("Client: Now I've got a composite tree:")
    client_code(tree)
    print()

    print("Client: I don't need to check the components classes even when managing the tree:")
    client_code2(tree, simple)
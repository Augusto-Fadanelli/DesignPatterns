from compositeDP import *
from facadeDP import *


def showBranch(component: Component):
    print(f'RESULT: {component.operation()}')


def addLeaf(component1: Component, component2: Component):
    if component1.is_composite():
        component1.add(component2)

    print(f'RESULT: {component1.operation()}')


if __name__ == '__main__':
    root = Composite()
    tree = Tree()

    # Heavenly Branch
    heavenly_branch = tree.createHeavenlyBranch()
    showBranch(heavenly_branch)
    print()

    # Human Branch
    human_branch = tree.createHumanBranch()
    showBranch(human_branch)
    print()

    # Support Branch
    support_branch = tree.createSupportBranch()
    showBranch(support_branch)
    print()

    # Potion Branch
    potion_branch = tree.createPotionBranch()
    showBranch(potion_branch)
    print()

    # Spell Branch
    spell_branch = tree.createSpellBranch()
    showBranch(spell_branch)
    print()

    # Trap Branch
    trap_branch = tree.createTrapBranch()
    showBranch(trap_branch)
    print()

    # Land Branch
    land_branch = tree.createLandBranch()
    showBranch(land_branch)
    print()

    # Tree
    root.add(heavenly_branch)
    root.add(human_branch)
    root.add(support_branch)
    root.add(potion_branch)
    root.add(spell_branch)
    root.add(trap_branch)
    root.add(land_branch)

    print("Client: Now I've got a composite tree:")
    showBranch(root)
    print()

    # Adicionar Leaf direto na Tree
    # addLeaf(tree, simple)

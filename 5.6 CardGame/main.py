from facadeDP import *
from compositeDP import *
from heavenlyBranch import *
from humanBranch import *
from supportBranch import *
from potionBranch import *
from spellBranch import *
from trapBranch import *
from landBranch import *

def showBranch(component: Component):
    print(f'RESULT: {component.operation()}')

def addLeaf(component1: Component, component2: Component):
    if component1.is_composite():
        component1.add(component2)

    print(f'RESULT: {component1.operation()}')

def createHeavenlyBranch(magician: Magician, sorcerer: Sorcerer, elf: Elf):
    heavenly_branch = Heavenly()

    # Magician Leafs
    magician.add(DarkMagician())
    magician.add(LightMagician())

    # Magician Branch
    heavenly_branch.add(magician)

    # Sorcerer Leafs
    sorcerer.add(DarkSorcerer())
    sorcerer.add(LightSorcerer())

    # Sorcerer Branch
    heavenly_branch.add(sorcerer)

    # Elf Leafs
    elf.add(ShapeshifterElf())
    elf.add(SummonerElf())
    elf.add(ElfArcher())

    # Elf Branch
    heavenly_branch.add(elf)

    return heavenly_branch

def createHumanBranch(knight: Knight, assassin: Assassin):
    human_branch = Human()

    # Knight Leafs
    knight.add(Templar())
    knight.add(Paladin())

    # Knight Branch
    human_branch.add(knight)

    # Assassin Leafs
    assassin.add(Ninja())
    assassin.add(StealthKiller())
    assassin.add(Fighter())

    # Assassin Branch
    human_branch.add(assassin)

    return human_branch

def createSupportBranch(divine: Divine, druid: Druid):
    support_branch = Support()

    # Divine Leafs
    divine.add(Cleric())

    # Divine Branch
    support_branch.add(divine)

    # Druid Leafs
    druid.add(Nymph())

    # Druid Branch
    support_branch.add(druid)

    return support_branch

def createPotionBranch():
    potion_branch = Potion()

    # Potion Leafs
    potion_branch.add(CurePotion())
    potion_branch.add(WeaknessPotion())
    potion_branch.add(StrengthPotion())
    potion_branch.add(PoisonPotion())

    return potion_branch

def createSpellBranch(healing_spell: HealingSpell):
    spell_branch = Spell()

    # Spell Leafs
    spell_branch.add(FireRain())
    spell_branch.add(TrailOfDead())

    # Healing Spell Leafs
    healing_spell.add(Esculapio())
    healing_spell.add(NightHerbs())

    # Healing Spell Branch
    spell_branch.add(healing_spell)

    return spell_branch

def createTrapBranch(terrestrial: Terrestrial):
    trap_branch = Trap()

    # Trap Leafs
    trap_branch.add(MeteorRain())
    trap_branch.add(Necromancy())
    trap_branch.add(AlternateReality())
    trap_branch.add(Madness())

    # Terrestrial Leafs
    terrestrial.add(Thorns())
    terrestrial.add(LightStatue())

    # Terrestrial Branch
    trap_branch.add(terrestrial)

    return trap_branch

def createLandBranch():
    land_branch = Land()

    # Land Leafs
    land_branch.add(FlatLand())
    land_branch.add(Hell())
    land_branch.add(Forest())

    return land_branch

if __name__ == '__main__':
    tree = Composite()

    # Heavenly Branch
    magician_branch = Magician()
    sorcerer_branch = Sorcerer()
    elf_branch = Elf()
    heavenly_branch = createHeavenlyBranch(magician_branch, sorcerer_branch, elf_branch)

    showBranch(heavenly_branch)
    print()

    # Human Branch
    knight_branch = Knight()
    assassin_branch = Assassin()
    human_branch = createHumanBranch(knight_branch, assassin_branch)

    showBranch(human_branch)
    print()

    # Support Branch
    divine_branch = Divine()
    druid_branch = Druid()
    support_branch = createSupportBranch(divine_branch, druid_branch)

    showBranch(support_branch)
    print()

    # Potion Branch
    potion_branch = createPotionBranch()

    showBranch(potion_branch)
    print()

    # Spell Branch
    healing_spell_branch = HealingSpell()
    spell_branch = createSpellBranch(healing_spell_branch)

    showBranch(spell_branch)
    print()

    # Trap Branch
    terrestrial_branch = Terrestrial()
    trap_branch = createTrapBranch(terrestrial_branch)

    showBranch(trap_branch)
    print()

    # Land Branch
    land_branch = createLandBranch()

    showBranch(land_branch)
    print()

    # Tree
    tree.add(heavenly_branch)
    tree.add(human_branch)
    tree.add(support_branch)
    tree.add(potion_branch)
    tree.add(spell_branch)
    tree.add(trap_branch)
    tree.add(land_branch)

    print("Client: Now I've got a composite tree:")
    showBranch(tree)
    print()

    #Adicionar Leaf direto na Tree
    #addLeaf(tree, simple)
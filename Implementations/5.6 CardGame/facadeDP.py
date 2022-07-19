from heavenlyBranch import *
from humanBranch import *
from landBranch import *
from potionBranch import *
from spellBranch import *
from supportBranch import *
from trapBranch import *


class Tree:
    """
    Docstring:
    Facade for Composite
    """

    def createHeavenlyBranch(self):
        magician = Magician()
        sorcerer = Sorcerer()
        elf = Elf()

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

    def createHumanBranch(self):
        knight = Knight()
        assassin = Assassin()

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

    def createSupportBranch(self):
        divine = Divine()
        druid = Druid()

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

    def createPotionBranch(self):
        potion_branch = Potion()

        # Potion Leafs
        potion_branch.add(CurePotion())
        potion_branch.add(WeaknessPotion())
        potion_branch.add(StrengthPotion())
        potion_branch.add(PoisonPotion())

        return potion_branch

    def createSpellBranch(self):
        healing_spell = HealingSpell()

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

    def createTrapBranch(self):
        terrestrial = Terrestrial()

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

    def createLandBranch(self):
        land_branch = Land()

        # Land Leafs
        land_branch.add(FlatLand())
        land_branch.add(Hell())
        land_branch.add(Forest())

        return land_branch

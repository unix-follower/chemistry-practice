import chemlib
from chemlib import Compound

from src.component import constants
from src.config.logging import get_logger

logger = get_logger()


def calculate_mass(molecules: float = 1):
    nitrogen = Compound(constants.NITROGEN_SYMBOL)
    result = nitrogen.get_amounts(molecules=molecules)
    logger.debug(result)
    return result


def calculate_compound_atoms(compound_formula: str, total_grams: float, element_fraction: float):
    compound = Compound(compound_formula)
    grams = total_grams * element_fraction

    amounts = compound.get_amounts(grams=grams)
    one_mole = amounts.get(constants.MOLES)
    two_mole = one_mole + one_mole
    result = two_mole * chemlib.AVOGADROS_NUMBER

    amounts[constants.TOTAL_FRACTION_ATOMS] = result
    logger.debug(amounts)

    return amounts


def calculate_ammonium_compound_atoms(total_grams: float, nitrogen_fraction: float):
    return calculate_compound_atoms("(NH4)2CO3", total_grams, nitrogen_fraction)


def calculate_urea_compound_atoms(total_grams: float, nitrogen_fraction: float):
    return calculate_compound_atoms("(NH2)2CO", total_grams, nitrogen_fraction)

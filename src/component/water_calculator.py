from chemlib import Compound

from src.config.logging import get_logger

logger = get_logger()


def calculate_molecules(milliliters: float = 200):
    water = Compound("H2O")
    result = water.get_amounts(grams=milliliters)
    logger.debug(result)
    return result

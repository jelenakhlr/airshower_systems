#!/usr/bin/env python3
# author: Jelena

class CoordinateTranslator:
  """
  This class translates coordinates between CORSIKA, AUGER, and GRAND systems.
  """

  def __init__(self):
    self.corsika_to_auger = {
        "phi": lambda phi: 90 - phi,
        "theta": lambda theta: theta
    }
    self.corsika_to_grand = {
        "phi": lambda phi: phi,
        "theta": lambda theta: 180 + theta
    }
    self.auger_to_corsika = {
        "phi": lambda phi: 90 - phi,
        "theta": lambda theta: theta
    }
    self.auger_to_grand = {
        "phi": lambda phi: phi - 90,
        "theta": lambda theta: 180 - theta
    }
    self.grand_to_corsika = {
        "phi": lambda phi: phi,
        "theta": lambda theta: 180 - theta
    }
    self.grand_to_auger = {
        "phi": lambda phi: phi + 90,
        "theta": lambda theta: 180 - theta
    }

  def translate(self, source_system, target_system, coordinates):
    """
    Translates coordinates from one system to another.

    Args:
      source_system: The source coordinate system (e.g., "CORSIKA").
      target_system: The target coordinate system (e.g., "AUGER").
      coordinates: A dictionary containing "phi" and "theta" keys.

    Returns:
      A dictionary containing the translated coordinates for the target system.
    """

    if source_system == target_system:
      return coordinates

    translation_map = getattr(self, f"{source_system}_to_{target_system}")
    return {key: translation_map[key](coordinates[key]) for key in coordinates}

# Example usage
translator = CoordinateTranslator()

# Convert from CORSIKA to AUGER
corsika_coords = {"phi": 45, "theta": 60}
translated_coords = translator.translate("corsika", "auger", corsika_coords)
print(translated_coords)

# Convert from AUGER to GRAND
auger_coords = {"phi": 30, "theta": 75}
translated_coords = translator.translate("auger", "grand", auger_coords)
print(translated_coords)

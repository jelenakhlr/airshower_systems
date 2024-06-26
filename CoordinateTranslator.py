#!/usr/bin/env python3
# author: Jelena

class CoordinateTranslator:
  """
  This class translates coordinates between CORSIKA, ZHAIRES, AUGER, and GRAND systems.
  """

  def __init__(self):
    self.corsika_to_auger = {
        "phi": lambda phi: phi - 90,
        "theta": lambda theta: theta +2.66 # account for geomagnetic vs geographic north
    }
    self.corsika_to_grand = {
        "phi": lambda phi: phi,
        "theta": lambda theta: 180 + theta # both use geomagnetic north
    }
    self.corsika_to_zhaires = {
        "phi": lambda phi: (phi + 180) % 360,
        "theta": lambda theta: 180 - theta
    }
    self.auger_to_corsika = {
        "phi": lambda phi: phi + 90,
        "theta": lambda theta: theta - 2.66 # account for geomagnetic vs geographic north
    }
    self.auger_to_grand = {
        "phi": lambda phi: 90 + phi,
        "theta": lambda theta: theta  + 2.66 # account for geomagnetic vs geographic north
    }
    self.grand_to_corsika = {
        "phi": lambda phi: phi,
        "theta": lambda theta: 180 - theta # both use geomagnetic north
    }
    self.grand_to_auger = {
        "phi": lambda phi: phi - 90,
        "theta": lambda theta: theta - 2.66 # account for geomagnetic vs geographic north
    }
    self.zhaires_to_corsika = {
        "phi": lambda phi: (phi - 180) % 360,
        "theta": lambda theta: 180 - theta
    }
    self.zhaires_to_grand = {
        "phi": lambda phi: (phi + 180) % 360,
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


if __name__ == "__main__":
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

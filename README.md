Python Coordinate Translator for Air Shower Simulations

This Python code defines a CoordinateTranslator class that translates coordinates between four commonly used coordinate systems in air shower simulations.

Usage

    Import the CoordinateTranslator class in your Python script:

Python

from CoordinateTranslator import CoordinateTranslator

    Create an instance of the CoordinateTranslator class:

Python

translator = CoordinateTranslator()


    Use the translate function to convert coordinates between systems:

Python

# Convert from CORSIKA to AUGER
corsika_coords = {"phi": 45, "theta": 60}
translated_coords = translator.translate("corsika", "auger", corsika_coords)
print(translated_coords)

# Convert from ZHAIRES to GRAND
zhaires_coords = {"phi": 120, "theta": 45}
translated_coords = translator.translate("zhaires", "grand", zhaires_coords)
print(translated_coords)

The translate function takes three arguments:

    source_system: The source coordinate system (e.g., "corsika").
    target_system: The target coordinate system (e.g., "auger").
    coordinates: A dictionary containing "phi" and "theta" keys with the values in degrees.

The function returns a dictionary containing the translated coordinates for the target system.

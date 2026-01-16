"""app_brandon.py - Project script.

Author: brandon
Date: 2026-01

  Practice key Python skills related to:
    - imports
    - logging
    - variables
    - type hints
    - global constants
    - f-strings
    - functions
    - main function
    - conditional execution guard

OBS:
  This is your file to practice and customize.
  Find the TODO comments, and as you complete each task, remove the TODO note.
"""


# === DECLARE IMPORTS (BRING IN FREE CODE) ===

import logging
import statistics
from typing import Final

from datafun_toolkit.logger import get_logger, log_header

# === CONFIGURE LOGGER ONCE PER MODULE (PYTHON FILE) ===

LOG: logging.Logger = get_logger("P01", level="INFO")


# === DECLARE GLOBAL CONSTANTS ===

# All these global variables are CONSTANT, they do NOT change when the program runs.
# By convention, constants are named in UPPERCASE_WITH_UNDERSCORES.
# The following illustrates variables that hold these common types:
#    str, int, float, bool, list of strings.
# `Final` is added to indicate these variables should not be reassigned.
# Examples:


# See the other file for examples.
MILITARY_UNIT_NAME: Final[str] = "893 Infantry Division"
MILITARY_SOLDIER_COUNT: Final[int] = 15000
MILITARY_READINESS_LEVEL: Final[float] = 92.5
HAS_OVERSEAS_PRESENCE: Final[bool] = True
MILITARY_BASES: Final[list[str]] = [
    "Camp Eagle, Germany",
    "Fort Bravo, Quatar",
    "Base Delta, South Korea",
    "Station Foxtrot, Japan",
    "Outpost Gamma, Italy",
]

# === DECLARE A FUNCTION TO FORMAT THE INFORMATION ===


def get_summary() -> str:
    """Get a formatted summary of the information held in the global variables.

    Arguments: None (nothing is passed in the parentheses after `get_summary`).

    Returns: - a formatted multi-line string (starts with f and wrapped in triple quotes).
    """

    summary: str = f"""
    Unit Total Information:
        Military unit name: {MILITARY_UNIT_NAME}
        Total soldiers assigned: {MILITARY_SOLDIER_COUNT}
        Operational readiness level: {MILITARY_READINESS_LEVEL}
        Overseas deployment capability: {HAS_OVERSEAS_PRESENCE}
        Forward operating bases: {MILITARY_BASES}
    """

    LOG.info("Generated formatted multi-line SUMMARY string.")
    LOG.info("Returning the str to the calling function.")
    return summary


# === DECLARE A FUNCTION TO FORMAT DESCRIPTIVE STATISTICS ===


def get_statistics() -> str:
    """Get a formatted summary showing descriptive statistics.

    Arguments: None (nothing is passed in the parentheses).

    Returns: - a formatted multi-line string.
    """
    # Initialize sample data - snowfall measurements in inches.
    # REQ: Vary ONE of the sample data values.
    # See how the statistics change when you do.
    snowfall_inches: list[float] = [2.5, 6.9, 4.5, 5.5, 6.5]

    # Calculate descriptive statistics below - see other file for examples.

    # Example: Calculate total snowfall.
    total: float = sum(snowfall_inches)
    count: int = len(snowfall_inches)

    minimum: float = min(snowfall_inches) if count > 0 else 0.0
    maximum: float = max(snowfall_inches) if count > 0 else 0

    average: float = statistics.mean(snowfall_inches) if count > 0 else 0.0
    std_dev: float = statistics.stdev(snowfall_inches) if count > 1 else 0.0

    # Build a formatted multi-line string using f and triple quotes.
    summary: str = f"""
    Descriptive Statistics for Snowfall (inches):
        Total snowfall: {total:.2f} inches
        Count of measurements: {count}
        Minimum snowfall: {minimum:.2f} inches
        Average snowfall: {average:.2f} inches
        Standard deviation: {std_dev:.2f} inches
        Maximum snowfall: {maximum:.2f} inches
    """

    LOG.info("Generated formatted multi-line SUMMARY string.")
    LOG.info("Returning the str to the calling function.")
    return summary


# === DEFINE THE MAIN FUNCTION THAT CALLS OTHER FUNCTIONS ===


def main() -> None:
    """Entry point when running this file as a Python script.

    Arguments: None.

    Returns: None.
    """
    # Log a header for the application.
    LOG.info("=================")
    log_header(LOG, "Foundations of Professional Python")
    LOG.info("=================")

    # Log start of main processing.
    LOG.info("START main()..................")

    # Call functions to get formatted strings and log them.
    summary: str = get_summary()
    LOG.info(summary)

    stats: str = get_statistics()
    LOG.info(stats)

    # Log end of main processing.
    LOG.info("END main()..................")


# === CONDITIONAL EXECUTION GUARD ===

# WHY: If running this file as a script, then call main() function.
# OBS: This is just standard Python boilerplate.

if __name__ == "__main__":
    main()

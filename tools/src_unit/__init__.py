"""Unit test helpers for page objects (no real browser).
This package contains pytest-based unit tests living under tools/.

The unit tests use a seeded in-memory env in tools/conftest.py, 
so they don’t depend on the .env and won’t raise from parse_locator.

To run the unit tests:

pytest tools/ -v

(the v means verbose mode, it shows more information about the tests)

Or:
Only unit tests:
pytest tools -q 

(the q means quiet mode, it shows less information about the tests)
"""

# tests/step_defs/conftest.py

import pytest

@pytest.fixture(scope="scenario")
def scenario_context():
    """
    Creates a new, empty dictionary for each scenario.
    
    This fixture is used to pass data between Gherkin
    steps (Given, When, Then).
    
    It is 'scenario' scoped, so it is created at the
    start of a scenario and destroyed at the end,
    ensuring no data leaks between tests.
    """
    # Create the context object
    context = {}
    
    # Yield the object to the steps
    yield context
    
    # Teardown: (Optional) Clear the context after the
    # scenario is done, just for good measure.
    context.clear()
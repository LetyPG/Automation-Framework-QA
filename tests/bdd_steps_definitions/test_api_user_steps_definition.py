
from pytest_bdd import scenario, given, when, then, parsers
from api.user_service_api import UserServiceAPI
from utils.api_helpers.schema_validator import SchemaValidator



@scenario(
    '../../features/api/user_service.feature',
    'Retrieve a specific user\'s data'
)
def test_retrieve_specific_user():
    pass

# --- Step Definitions ---

@given('the user service is available')
def user_service_is_ready(user_api_client: UserServiceAPI):
    # This step still gets the GLOBAL fixture from the root conftest
    assert user_api_client is not None

@when(parsers.parse('I request the user with ID "{user_id}"'))
def request_user(user_api_client: UserServiceAPI, user_id, scenario_context):
    # ^-- Pytest injects the NEW fixture
    
    response = user_api_client.get_user(user_id)
    
    # Store the response in the scenario-scoped context
    scenario_context['response'] = response

@then(parsers.parse('the response status code should be {status_code}'))
def check_status_code(status_code, scenario_context):
    # ^-- Pytest injects the SAME fixture
    assert scenario_context['response'].status_code == int(status_code)

@then(parsers.parse('the response body should contain the user email "{email}"'))
def check_email_in_body(email, scenario_context):
    response_json = scenario_context['response'].json()
    assert response_json['data']['email'] == email

@then('the response schema should be valid')
def validate_schema(scenario_context):
    validator = SchemaValidator(schema_name='user_schema.json')
    is_valid = validator.validate(scenario_context['response'].json())
    assert is_valid, "API response schema is invalid"
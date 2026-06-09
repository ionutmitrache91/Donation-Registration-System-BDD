import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../..")
    )
)

from behave import *
from behave import given, when, then
from donation import DonationSystem

@given('a donor named "{name}"')
def step_given_donor(context, name):
    context.name = name

@given('an empty donor name')
def step_empty_donor(context):
    context.name = ""

@when('they donate {amount:d}')
def step_when_donate(context, amount):
    system = DonationSystem()
    context.result = system.register_donation(
        context.name,
        amount
    )

@then('the system should display "{message}"')
def step_then_verify(context, message):
    assert context.result == message

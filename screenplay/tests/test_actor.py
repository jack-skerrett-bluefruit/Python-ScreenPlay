import pytest
from screenplay import Actor, Ability
from .stub_abilities import *
from .stub_tasks import *

def test_An_actors_name_can_be_retrieved():
    frank = Actor.named('Frank')

    assert frank.name == 'Frank'

def test_An_Ability_can_be_added_and_reterived_from_an_Actor():
    bob = Actor.named('Bob')

    bob.can(StubAbility())

    ability = bob.ability(StubAbility)

    assert ability != None, "Ability not found"

def test_Multiple_Ability_objects_can_be_added_and_reterived_from_an_Actor():
    bob = Actor.named('Bob')

    bob.can(StubAbility())
    bob.can(SecondStubAbility())

    assert bob.ability(StubAbility) != None, "Ability not found"
    assert bob.ability(SecondStubAbility) != None, "Ability not found"

def test_Trying_to_get_an_ability_an_Actor_does_not_have_causes_an_assertion():
    bob = Actor.named('Bob')

    bob.can(SecondStubAbility())

    with pytest.raises(AssertionError):
        bob.ability(StubAbility)

def test_Multiple_Ability_objects_are_cleaned_up_with_an_Actor_is_cleaned_up():
    bob = Actor.named('Bob')

    first_ability = StubAbility()
    second_ability = SecondStubAbility()
    bob.can(first_ability)
    bob.can(second_ability)

    bob.clean_up()

    assert first_ability.clean_up_run, 'Ability not cleaned up'
    assert second_ability.clean_up_run, 'Ability not cleaned up'

def test_An_Actor_can_perform_Tasks():
    claire = Actor.named('Claire')

    task1 = StubTask()
    task2 = StubTask()

    claire.attempts_to(
        task1,
        task2
        )
    
    assert task1.called, "Task 1 not run"
    assert task2.called, "Task 2 not run"

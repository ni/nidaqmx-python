"""Tests for validating persisted channel properties for different data types."""
import pytest


@pytest.mark.parametrize("persisted_channel", ["VoltageTesterChannel"], indirect=True)
def test__persisted_channel__get_bool_property__returns_persisted_value(persisted_channel):
    """Test for validating boolean properties in persisted channel."""
    assert persisted_channel.allow_interactive_editing


@pytest.mark.parametrize("persisted_channel", ["VoltageTesterChannel"], indirect=True)
def test__persisted_channel__get_string_property__returns_persisted_value(persisted_channel):
    """Test for validating string properties in persisted channel."""
    assert persisted_channel.author == "Test Author"

"Contains a collection of pytest tests that validates the persisted scale properties."
import pytest

@pytest.mark.parametrize("persisted_scale", ["double_gain_scale"], indirect=True)
def test__persisted_scale__get_bool_property__returns_value(persisted_scale):
    """Test for validating bool attributes in persisted scale."""
    assert persisted_scale.allow_interactive_editing

@pytest.mark.parametrize("persisted_scale", ["double_gain_scale"], indirect=True)
def test__persisted_scale__get_string_property__returns_value(persisted_scale):
    """Test for validating string attributes in persisted scale."""
    assert persisted_scale.author == "Test Author"

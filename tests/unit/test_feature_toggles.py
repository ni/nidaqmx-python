from __future__ import annotations

import pytest
from pytest_mock import MockerFixture

from nidaqmx._feature_toggles import (
    CodeReadiness,
    FeatureNotSupportedError,
    FeatureToggle,
    get_code_readiness_level,
    requires_feature,
)

RELEASE_FEATURE = FeatureToggle("RELEASE_FEATURE", CodeReadiness.RELEASE)
NEXT_RELEASE_FEATURE = FeatureToggle("NEXT_RELEASE_FEATURE", CodeReadiness.NEXT_RELEASE)
INCOMPLETE_FEATURE = FeatureToggle("INCOMPLETE_FEATURE", CodeReadiness.INCOMPLETE)
PROTOTYPE_FEATURE = FeatureToggle("PROTOTYPE_FEATURE", CodeReadiness.PROTOTYPE)


@requires_feature(PROTOTYPE_FEATURE)
def _prototype_function(x: int, y: str, z: list[int]) -> str:
    return _prototype_function_impl(x, y, z)


def _prototype_function_impl(x: int, y: str, z: list[int]) -> str:
    return ""


def test___default_code_readiness_level___get_code_readiness_level___equals_prototype() -> None:
    assert get_code_readiness_level() == CodeReadiness.PROTOTYPE


@pytest.mark.use_code_readiness(CodeReadiness.RELEASE)
def test___use_release_readiness___get_code_readiness_level___equals_release() -> None:
    assert get_code_readiness_level() == CodeReadiness.RELEASE


@pytest.mark.use_code_readiness(CodeReadiness.NEXT_RELEASE)
def test___use_next_release_readiness___get_code_readiness_level___equals_next_release() -> None:
    assert get_code_readiness_level() == CodeReadiness.NEXT_RELEASE


def test___default_code_readiness_level___is_enabled___returns_true() -> None:
    assert RELEASE_FEATURE.is_enabled
    assert NEXT_RELEASE_FEATURE.is_enabled
    assert INCOMPLETE_FEATURE.is_enabled
    assert PROTOTYPE_FEATURE.is_enabled


@pytest.mark.use_code_readiness(CodeReadiness.INCOMPLETE)
def test___use_incomplete_readiness___is_enabled___reflects_code_readiness_level() -> None:
    assert RELEASE_FEATURE.is_enabled
    assert NEXT_RELEASE_FEATURE.is_enabled
    assert INCOMPLETE_FEATURE.is_enabled
    assert not PROTOTYPE_FEATURE.is_enabled


@pytest.mark.use_code_readiness(CodeReadiness.NEXT_RELEASE)
def test___use_next_release_readiness___is_enabled___reflects_code_readiness_level() -> None:
    assert RELEASE_FEATURE.is_enabled
    assert NEXT_RELEASE_FEATURE.is_enabled
    assert not INCOMPLETE_FEATURE.is_enabled
    assert not PROTOTYPE_FEATURE.is_enabled


@pytest.mark.use_code_readiness(CodeReadiness.RELEASE)
def test___release_readiness_level___is_enabled___reflects_code_readiness_level() -> None:
    assert RELEASE_FEATURE.is_enabled
    assert not NEXT_RELEASE_FEATURE.is_enabled
    assert not INCOMPLETE_FEATURE.is_enabled
    assert not PROTOTYPE_FEATURE.is_enabled


@pytest.mark.enable_feature_toggle(PROTOTYPE_FEATURE)
def test___feature_toggle_enabled___is_enabled___returns_true() -> None:
    assert PROTOTYPE_FEATURE.is_enabled


@pytest.mark.disable_feature_toggle(PROTOTYPE_FEATURE)
def test___feature_toggle_disabled___is_enabled___returns_false() -> None:
    assert not PROTOTYPE_FEATURE.is_enabled


@pytest.mark.enable_feature_toggle(PROTOTYPE_FEATURE)
def test___feature_toggle_enabled___call_decorated_function___impl_called(
    mocker: MockerFixture,
) -> None:
    impl = mocker.patch("tests.unit.test_feature_toggles._prototype_function_impl")
    impl.return_value = "def"

    result = _prototype_function(123, "abc", [4, 5, 6])

    impl.assert_called_once_with(123, "abc", [4, 5, 6])
    assert result == "def"


@pytest.mark.disable_feature_toggle(PROTOTYPE_FEATURE)
def test___feature_toggle_disabled___call_decorated_function___error_raised(
    mocker: MockerFixture,
) -> None:
    impl = mocker.patch("tests.unit.test_feature_toggles._prototype_function_impl")
    impl.return_value = "def"

    with pytest.raises(FeatureNotSupportedError) as exc_info:
        _ = _prototype_function(123, "abc", [4, 5, 6])

    impl.assert_not_called()
    assert "set NIDAQMX_ENABLE_PROTOTYPE_FEATURE" in exc_info.value.args[0]

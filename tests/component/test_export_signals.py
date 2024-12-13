import pytest

import nidaqmx


def test___export_signals___set_nonexistent_property___raises_exception(task: nidaqmx.Task):
    with pytest.raises(AttributeError):
        task.export_signals.nonexistent_property = "foo"  # type: ignore[attr-defined]

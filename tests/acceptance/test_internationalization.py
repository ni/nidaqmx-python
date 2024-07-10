import locale
import pathlib
from typing import Any, Dict, List, Optional, Union

import pytest

from nidaqmx._lib import lib_importer
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.errors import DaqError
from nidaqmx.system import Device
from nidaqmx.task import Task


@pytest.fixture()
def ai_task(task, sim_6363_device):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    return task


def _get_encoding(obj: Union[Task, Dict[str, Any]]) -> Optional[str]:
    if getattr(obj, "_grpc_options", None) or (isinstance(obj, dict) and "grpc_options" in obj):
        # gRPC server limited to MBCS encoding
        return locale.getlocale()[1]
    else:
        return lib_importer.encoding


@pytest.mark.parametrize(
    "device_name, supported_encodings",
    [
        ("Gerät", ["1252", "iso-8859-1", "utf-8"]),
        ("l' appareil", ["1252", "iso-8859-1", "utf-8"]),
        ("デバイス", ["932", "shift-jis", "utf-8"]),
        ("장치", ["utf-8", "euc-kr"]),
        ("设备", ["utf-8", "gbk"]),
    ],
)
def test___supported_encoding___reset_nonexistent_device___returns_error_with_device_name(
    init_kwargs: Dict[str, Any], device_name: str, supported_encodings: List[str]
):
    if _get_encoding(init_kwargs) not in supported_encodings:
        pytest.skip("requires compatible encoding")
    with pytest.raises(DaqError) as exc_info:
        Device(device_name, **init_kwargs).reset_device()

    assert f"Device Specified: {device_name}\n" in exc_info.value.args[0]
    assert exc_info.value.error_code == DAQmxErrors.INVALID_DEVICE_ID


@pytest.mark.grpc_xfail(
    reason="AB#2393811: DAQmxGetLoggingFilePath returns kErrorNULLPtr (-200604) when called from grpc-device.",
    raises=DaqError,
)
@pytest.mark.parametrize(
    "file_path, supported_encodings",
    [
        ("Zu prüfende Daten.tdms", ["1252", "iso-8859-1", "utf-8"]),
        ("Données de test.tdms", ["1252", "iso-8859-1", "utf-8"]),
        ("テストデータ.tdms", ["932", "shift-jis", "utf-8"]),
        ("테스트 데이터.tdms", ["utf-8", "euc-kr"]),
        ("测试数据.tdms", ["utf-8", "gbk"]),
    ],
)
def test___supported_encoding___logging_file_path___returns_assigned_value(
    ai_task: Task, file_path: str, supported_encodings: List[str]
):
    if _get_encoding(ai_task) not in supported_encodings:
        pytest.skip("requires compatible encoding")
    ai_task.in_stream.logging_file_path = file_path  # type: ignore[assignment] # https://github.com/ni/nidaqmx-python/issues/613

    assert ai_task.in_stream.logging_file_path == pathlib.Path(file_path)

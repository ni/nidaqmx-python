from nidaqmx.system import Device


def test___devices_with_same_name___compare___equal(init_kwargs):
    device1 = Device("bridgeTester", **init_kwargs)
    device2 = Device("bridgeTester", **init_kwargs)

    assert device1 is not device2
    assert device1 == device2


def test___devices_with_different_names___compare___not_equal(init_kwargs):
    device1 = Device("bridgeTester", **init_kwargs)
    device2 = Device("tsVoltageTester1", **init_kwargs)

    assert device1 != device2


def test___devices_with_same_name___hash___equal(init_kwargs):
    device1 = Device("bridgeTester", **init_kwargs)
    device2 = Device("bridgeTester", **init_kwargs)

    assert device1 is not device2
    assert hash(device1) == hash(device2)


def test___devices_with_different_names___hash___not_equal(init_kwargs):
    device1 = Device("bridgeTester", **init_kwargs)
    device2 = Device("tsVoltageTester1", **init_kwargs)

    assert hash(device1) != hash(device2)


def test___self_test_device___no_errors(sim_6363_device: Device) -> None:
    sim_6363_device.self_test_device()


def test___restore_last_ext_cal_const___no_errors(sim_6363_device: Device) -> None:
    sim_6363_device.restore_last_ext_cal_const()


def test___self_cal___no_errors(sim_6363_device: Device) -> None:
    sim_6363_device.self_cal()

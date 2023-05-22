from nidaqmx.system import PhysicalChannel


def test___physical_channels_with_same_name___compare___are_equal(init_kwargs):
    phys_chan1 = PhysicalChannel("bridgeTester/ai2", **init_kwargs)
    phys_chan2 = PhysicalChannel("bridgeTester/ai2", **init_kwargs)

    assert phys_chan1 is not phys_chan2
    assert phys_chan1 == phys_chan2


def test___physical_channels_with_different_names___compare___are_not_equal(
    init_kwargs,
):
    phys_chan1 = PhysicalChannel("bridgeTester/ai2", **init_kwargs)
    phys_chan2 = PhysicalChannel("bridgeTester/ai3", **init_kwargs)
    phys_chan3 = PhysicalChannel("tsVoltageTester1/ai2", **init_kwargs)

    assert phys_chan1 != phys_chan2
    assert phys_chan1 != phys_chan3

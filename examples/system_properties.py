"""Examples for using system properties in DAQmx."""

import nidaqmx

local_system = nidaqmx.system.System.local()
driver_version = local_system.driver_version

print(
    "DAQmx {}.{}.{}".format(
        driver_version.major_version,
        driver_version.minor_version,
        driver_version.update_version,
    )
)

for device in local_system.devices:
    print(
        "Device Name: {}, Product Category: {}, Product Type: {}".format(
            device.name, device.product_category, device.product_type
        )
    )

"""Examples for using system properties in DAQmx."""
import nidaqmx

local_system = nidaqmx.system.System.local()
driver_version = local_system.driver_version

print(
    "DAQmx {0}.{1}.{2}".format(
        driver_version.major_version,
        driver_version.minor_version,
        driver_version.update_version,
    )
)

for device in local_system.devices:
    print(
        "Device Name: {0}, Product Category: {1}, Product Type: {2}".format(
            device.name, device.product_category, device.product_type
        )
    )

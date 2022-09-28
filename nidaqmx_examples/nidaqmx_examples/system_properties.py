import nidaqmx


system = nidaqmx.System.local()
print('DAQmx {0}.{1}.{2}'.format(system.major_version, system.minor_version,
                                 system.update_version))

for device in system.devices:
    print('Device Name: {0}, Product Category: {1}, Product Type: {2}'.format(
        device.name, device.product_category, device.product_type))

# ``DAQmx`` enum metadata format

## Example

```python
'CurrentShuntResistorLocation1': {
        'values': [
            {
                'documentation': {
                    'description': 'Use the built-in shunt resistor of the device.'
                },
                'name': 'INTERNAL',
                'value': 10200
            },
            {
                'documentation': {
                    'description': ' Use a shunt resistor ...'
                },
                'name': 'EXTERNAL',
                'value': 10167
            }
        ]
    }
```
## Key for enums

- `'name'`
    - The name of the enum.
    - This is the key for an enum.

- `'values'`
    - The enum values.
    - Each enum value consists of the following keys,
        - `'documentation'`: The documentation for the enum value.
        - `'name'`: The name of the enum value
        - `'value'`: The value of the enum.
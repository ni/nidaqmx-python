def enum_bitfield_to_list(bitfield_value, bitfield_enum_type,
                          actual_enum_type):
    """
    Converts a bitfield value to a list of enums.

    Args:
        bitfield_value (int): Specifies the value of the bitfield.
        bitfield_enum_type (enum.Enum): Specifies the bitfield enum type
            from which to mask and extract the enum values.
        actual_enum_type (enum.Enum): Specifies the actual enum type.
    Returns:
        List[enum.Enum]: Indicates the converted list of enums.
    """
    supported_values = []
    for bitfield_mask in bitfield_enum_type:
        if bitfield_value & bitfield_mask.value:
            enum_value = next(
                e for e in actual_enum_type if e.name == bitfield_mask.name)
            supported_values.append(enum_value)

    return supported_values


def enum_list_to_bitfield(enum_list, bitfield_enum_type):
    """
    Converts a list of enums to a bitfield value.

    Args:
        enum_list (List[enum.Enum]): Specifies the list of enums.
        bitfield_enum_type (enum.Enum): Specifies the bitfield enum type
            from which to mask and extract the enum values.
    Returns:
        int: Indicates the value of the bitfield.
    """
    bitfield_value = 0
    for enum_value in enum_list:
        bitfield_mask = next(
            b for b in bitfield_enum_type if b.name == enum_value.name)
        bitfield_value |= bitfield_mask.value

    return bitfield_value
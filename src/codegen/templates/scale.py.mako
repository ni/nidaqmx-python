<%
    from codegen.utilities.attribute_helpers import get_attributes, get_enums_used
    from codegen.utilities.text_wrappers import wrap
    attributes = get_attributes(data, "Scale")
    enums_used = get_enums_used(attributes)
%>\
# Do not edit this file; it was automatically generated.

import ctypes
import numpy

from nidaqmx import utils
from nidaqmx.constants import (
    ${', '.join([c for c in enums_used]) | wrap(4, 4)})

__all__ = ['Scale']


class Scale:
    """
    Represents a DAQmx scale.
    """
    __slots__ = ['_name', '_interpreter', '__weakref__']

    def __init__(self, name, *, grpc_options=None):
        """
        Args:
            name (str): Specifies the name of the scale to create.
            grpc_options (Optional[GrpcSessionOptions]): Specifies the gRPC session options.
        """
        self._name = name
        self._interpreter = utils._select_interpreter(grpc_options)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._name == other._name
        return False

    def __hash__(self):
        return hash(self._name)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return f'Scale(name={self._name})'

    @property
    def name(self):
        """
        str: Specifies the name of this scale.
        """
        return self._name

<%namespace name="property_template" file="/property_template.py.mako"/>\
%for attribute in attributes:
${property_template.script_property(attribute)}\
%endfor
\
    @staticmethod
    def calculate_reverse_poly_coeff(
            forward_coeffs, min_val_x=-5.0, max_val_x=5.0,
            num_points_to_compute=1000, reverse_poly_order=-1, *, grpc_options=None):
        """
        Computes a set of coefficients for a polynomial that
        approximates the inverse of the polynomial with the coefficients
        you specify with the "forward_coeffs" input. This function
        generates a table of x versus y values over the range of x. This
        function then finds a polynomial fit, using the least squares
        method to compute a polynomial that computes x when given a
        value for y.

        Args:
            forward_coeffs (List[float]): Is the list of coefficients
                for the polynomial that computes y given a value of x.
                Each element of the list corresponds to a term of the
                equation.
            min_val_x (Optional[float]): Is the minimum value of x for
                which you use the polynomial. This is the smallest value
                of x for which the function generates a y value in the
                table.
            max_val_x (Optional[float]): Is the maximum value of x for
                which you use the polynomial. This is the largest value
                of x for which the function generates a y value in the
                table.
            num_points_to_compute (Optional[int]): Is the number of
                points in the table of x versus y values. The function
                spaces the values evenly between "min_val_x" and
                "max_val_x".
            reverse_poly_order (Optional[int]): Is the order of the
                reverse polynomial to compute. For example, an input of
                3 indicates a 3rd order polynomial. A value of -1
                indicates a reverse polynomial of the same order as the
                forward polynomial.
            grpc_options (Optional[GrpcSessionOptions]): Specifies the 
                gRPC session options.
        Returns:
            List[float]: 
            
            Specifies the list of coefficients for the reverse 
            polynomial. Each element of the list corresponds to a term 
            of the equation. For example, if index three of the list is 
            9, the fourth term of the equation is 9y^3.
        """
        forward_coeffs = numpy.float64(forward_coeffs)

        interpreter = utils._select_interpreter(grpc_options)

        reverse_coeffs = interpreter.calculate_reverse_poly_coeff(
            forward_coeffs, min_val_x, max_val_x, num_points_to_compute, reverse_poly_order)

        return reverse_coeffs

    @staticmethod
    def create_lin_scale(
            scale_name, slope, y_intercept=0.0,
            pre_scaled_units=UnitsPreScaled.VOLTS, scaled_units=None, *, grpc_options=None):
        """
        Creates a custom scale that uses the equation y=mx+b, where x is
        a pre-scaled value, and y is a scaled value. The equation is
        identical for input and output. If the equation is in the form
        x=my+b, you must first solve for y in terms of x.

        Args:
            scale_name (str): Specifies the name of the scale to create.
            slope (float): Is the slope, m, in the equation.
            y_intercept (Optional[float]): Is the y-intercept, b, in the
                equation.
            pre_scaled_units (Optional[nidaqmx.constants.UnitsPreScaled]):
                Is the units of the values to scale.
            scaled_units (Optional[str]): Is the units to use for the
                scaled value. You can use an arbitrary string. NI-DAQmx
                uses the units to label a graph or chart.
            grpc_options (Optional[GrpcSessionOptions]): Specifies the 
                gRPC session options.
        Returns:
            nidaqmx.scale.Scale:
            
            Indicates an object that represents the created custom scale.
        """
        scale = Scale(scale_name, grpc_options=grpc_options)

        scale._interpreter.create_lin_scale(
            scale_name, slope, y_intercept, pre_scaled_units.value, scaled_units)

        return scale

    @staticmethod
    def create_map_scale(
            scale_name, prescaled_min, prescaled_max, scaled_min, scaled_max,
            pre_scaled_units=UnitsPreScaled.VOLTS, scaled_units=None, *, grpc_options=None):
        """
        Creates a custom scale that scales values proportionally from a
        range of pre-scaled values to a range of scaled values.

        Args:
            scale_name (str): Specifies the name of the scale to create.
            prescaled_min (float): Is the smallest value in the range of
                pre-scaled values. NI-DAQmx maps this value to
                "scaled_min".
            prescaled_max (float): Is the largest value in the range of
                pre-scaled values. NI-DAQmx maps this value to
                "scaled_max".
            scaled_min (float): Is the smallest value in the range of
                scaled values. NI-DAQmx maps this value to
                "prescaled_min". Read operations clip samples that are
                smaller than this value. Write operations generate
                errors for samples that are smaller than this value.
            scaled_max (float): Is the largest value in the range of
                scaled values. NI-DAQmx maps this value to
                "prescaled_max". Read operations clip samples that are
                larger than this value. Write operations generate errors
                for samples that are larger than this value.
            pre_scaled_units (Optional[nidaqmx.constants.UnitsPreScaled]):
                Is the units of the values to scale.
            scaled_units (Optional[str]): Is the units to use for the
                scaled value. You can use an arbitrary string. NI-DAQmx
                uses the units to label a graph or chart.
            grpc_options (Optional[GrpcSessionOptions]): Specifies the 
                gRPC session options.
        Returns:
            nidaqmx.scale.Scale: 
            
            Indicates an object that represents the created custom scale.
        """
        scale = Scale(scale_name, grpc_options=grpc_options)

        scale._interpreter.create_map_scale(
            scale_name, prescaled_min, prescaled_max, scaled_min, scaled_max, 
            pre_scaled_units.value, scaled_units)

        return scale

    @staticmethod
    def create_polynomial_scale(
            scale_name, forward_coeffs, reverse_coeffs,
            pre_scaled_units=UnitsPreScaled.VOLTS, scaled_units=None, *, grpc_options=None):
        """
        Creates a custom scale that uses an nth order polynomial
        equation. NI-DAQmx requires both a polynomial to convert pre-
        scaled values to scaled values (forward) and a polynomial to
        convert scaled values to pre-scaled values (reverse). If you
        only know one set of coefficients, use the DAQmx Compute Reverse
        Polynomial Coefficients function to generate the other set.

        Args:
            scale_name (str): Specifies the name of the scale to create.
            forward_coeffs (List[float]): Is an list of coefficients for
                the polynomial that converts pre-scaled values to scaled
                values. Each element of the list corresponds to a term
                of the equation.
            reverse_coeffs (List[float]): Is an list of coefficients for
                the polynomial that converts scaled values to pre-scaled
                values. Each element of the list corresponds to a term
                of the equation.
            pre_scaled_units (Optional[nidaqmx.constants.UnitsPreScaled]):
                Is the units of the values to scale.
            scaled_units (Optional[str]): Is the units to use for the
                scaled value. You can use an arbitrary string. NI-DAQmx
                uses the units to label a graph or chart.
            grpc_options (Optional[GrpcSessionOptions]): Specifies the 
                gRPC session options.
        Returns:
            nidaqmx.scale.Scale: 
            
            Indicates an object that represents the created custom scale.
        """
        if forward_coeffs is None:
            forward_coeffs = []

        if reverse_coeffs is None:
            reverse_coeffs = []

        forward_coeffs = numpy.float64(forward_coeffs)
        reverse_coeffs = numpy.float64(reverse_coeffs)

        scale = Scale(scale_name, grpc_options=grpc_options)

        scale._interpreter.create_polynomial_scale(
            scale_name, forward_coeffs, reverse_coeffs, pre_scaled_units.value, scaled_units)

        return scale

    @staticmethod
    def create_table_scale(
            scale_name, prescaled_vals, scaled_vals,
            pre_scaled_units=UnitsPreScaled.VOLTS, scaled_units=None, *, grpc_options=None):
        """
        Creates a custom scale that maps an list of pre-scaled values to
        an list of corresponding scaled values. NI-DAQmx applies linear
        interpolation to values that fall between the values in the
        table. Read operations clip scaled samples that are outside the
        maximum and minimum scaled values found in the table. Write
        operations generate errors for samples that are outside the
        minimum and maximum scaled values found in the table.

        Args:
            scale_name (str): Specifies the name of the scale to create.
            prescaled_vals (List[float]): Is the list of pre-scaled
                values that map to the values in "scaled_vals".
            scaled_vals (List[float]): Is the list of scaled values that
                map to the values in "prescaled_vals".
            pre_scaled_units (Optional[nidaqmx.constants.UnitsPreScaled]):
                Is the units of the values to scale.
            scaled_units (Optional[str]): Is the units to use for the
                scaled value. You can use an arbitrary string. NI-DAQmx
                uses the units to label a graph or chart.
            grpc_options (Optional[GrpcSessionOptions]): Specifies the 
                gRPC session options.
        Returns:
            nidaqmx.scale.Scale: 
            
            Indicates an object that represents the created custom scale.
        """
        if prescaled_vals is None:
            prescaled_vals = []

        if scaled_vals is None:
            scaled_vals = []

        prescaled_vals = numpy.float64(prescaled_vals)
        scaled_vals = numpy.float64(scaled_vals)
        
        scale = Scale(scale_name, grpc_options=grpc_options)

        scale._interpreter.create_table_scale(
            scale_name, prescaled_vals, scaled_vals, pre_scaled_units.value, scaled_units)

        return scale

    def save(self, save_as="", author="", overwrite_existing_scale=False,
             allow_interactive_editing=True, allow_interactive_deletion=True):
        """
        Saves this custom scale to MAX.

        Args:
            save_as (Optional[str]): Is the name to save the task,
                global channel, or custom scale as. If you do not
                specify a value for this input, NI-DAQmx uses the name
                currently assigned to the task, global channel, or
                custom scale.
            author (Optional[str]): Is a name to store with the task,
                global channel, or custom scale.
            options (Optional[int]): Specifies whether to allow the
                task, global channel, or custom scale to be deleted
                through MAX.
            overwrite_existing_scale (Optional[bool]): Specifies whether to
                overwrite a custom scale of the same name if one is already
                saved in MAX. If this input is False and a custom scale of
                the same name is already saved in MAX, this function returns
                an error.
            allow_interactive_editing (Optional[bool]): Specifies whether to
                allow the task, global channel, or custom scale to be edited
                in the DAQ Assistant. If allow_interactive_editing is True,
                the DAQ Assistant must support all task or global channel
                settings.
            allow_interactive_deletion (Optional[bool]): Specifies whether
                to allow the task, global channel, or custom scale to be
                deleted through MAX.
        """
        options = 0
        if overwrite_existing_scale:
            options |= _Save.OVERWRITE.value
        if allow_interactive_editing:
            options |= _Save.ALLOW_INTERACTIVE_EDITING.value
        if allow_interactive_deletion:
            options |= _Save.ALLOW_INTERACTIVE_DELETION.value

        self._interpreter.save_scale(self._name, save_as, author, options)


class _ScaleAlternateConstructor(Scale):
    """
    Provide an alternate constructor for the Scale object.

    This is a private API used to instantiate a Scale with an existing interpreter.
    """
    # Setting __slots__ avoids TypeError: __class__ assignment: 'Base' object layout differs from 'Derived'.
    __slots__ = []

    def __init__(self, name, interpreter):
        """
        Args:
            name: Specifies the name of the Scale.
            interpreter: Specifies the interpreter instance.
            
        """
        self._name = name
        self._interpreter = interpreter

        # Use meta-programming to change the type of this object to Scale,
        # so the user isn't confused when doing introspection.
        self.__class__ = Scale
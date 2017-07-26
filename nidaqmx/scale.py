from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import ctypes
import numpy

from nidaqmx._lib import lib_importer, wrapped_ndpointer, ctypes_byte_str
from nidaqmx.errors import (
    check_for_error, is_string_buffer_too_small, is_array_buffer_too_small)
from nidaqmx.constants import (
    ScaleType, UnitsPreScaled, _Save)

__all__ = ['Scale']


class Scale(object):
    """
    Represents a DAQmx scale.
    """
    __slots__ = ['_name', '__weakref__']

    def __init__(self, name):
        """
        Args:
            name (str): Specifies the name of the scale to create.
        """
        self._name = name

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._name == other._name
        return False

    def __hash__(self):
        return hash(self._name)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return 'Scale(name={0})'.format(self._name)

    @property
    def name(self):
        """
        str: Specifies the name of this scale.
        """
        return self._name

    @property
    def description(self):
        """
        str: Specifies a description for the scale.
        """
        cfunc = lib_importer.windll.DAQmxGetScaleDescr
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.c_char_p, ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._name, val, temp_size)

            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return val.value.decode('ascii')

    @description.setter
    def description(self, val):
        cfunc = lib_importer.windll.DAQmxSetScaleDescr
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes_byte_str]

        error_code = cfunc(
            self._name, val)
        check_for_error(error_code)

    @property
    def lin_slope(self):
        """
        float: Specifies the slope, m, in the equation y=mx+b.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetScaleLinSlope
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @lin_slope.setter
    def lin_slope(self, val):
        cfunc = lib_importer.windll.DAQmxSetScaleLinSlope
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._name, val)
        check_for_error(error_code)

    @property
    def lin_y_intercept(self):
        """
        float: Specifies the y-intercept, b, in the equation y=mx+b.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetScaleLinYIntercept
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @lin_y_intercept.setter
    def lin_y_intercept(self, val):
        cfunc = lib_importer.windll.DAQmxSetScaleLinYIntercept
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._name, val)
        check_for_error(error_code)

    @property
    def map_pre_scaled_max(self):
        """
        float: Specifies the largest value in the range of pre-scaled
            values. NI-DAQmx maps this value to **map_scaled_max**.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetScaleMapPreScaledMax
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @map_pre_scaled_max.setter
    def map_pre_scaled_max(self, val):
        cfunc = lib_importer.windll.DAQmxSetScaleMapPreScaledMax
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._name, val)
        check_for_error(error_code)

    @property
    def map_pre_scaled_min(self):
        """
        float: Specifies the smallest value in the range of pre-scaled
            values. NI-DAQmx maps this value to **map_scaled_min**.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetScaleMapPreScaledMin
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @map_pre_scaled_min.setter
    def map_pre_scaled_min(self, val):
        cfunc = lib_importer.windll.DAQmxSetScaleMapPreScaledMin
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._name, val)
        check_for_error(error_code)

    @property
    def map_scaled_max(self):
        """
        float: Specifies the largest value in the range of scaled
            values. NI-DAQmx maps this value to **map_pre_scaled_max**.
            Reads coerce samples that are larger than this value to
            match this value. Writes generate errors for samples that
            are larger than this value.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetScaleMapScaledMax
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @map_scaled_max.setter
    def map_scaled_max(self, val):
        cfunc = lib_importer.windll.DAQmxSetScaleMapScaledMax
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._name, val)
        check_for_error(error_code)

    @property
    def map_scaled_min(self):
        """
        float: Specifies the smallest value in the range of scaled
            values. NI-DAQmx maps this value to **map_pre_scaled_min**.
            Reads coerce samples that are smaller than this value to
            match this value. Writes generate errors for samples that
            are smaller than this value.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetScaleMapScaledMin
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._name, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @map_scaled_min.setter
    def map_scaled_min(self, val):
        cfunc = lib_importer.windll.DAQmxSetScaleMapScaledMin
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.c_double]

        error_code = cfunc(
            self._name, val)
        check_for_error(error_code)

    @property
    def poly_forward_coeff(self):
        """
        List[float]: Specifies a list of coefficients for the polynomial
            that converts pre-scaled values to scaled values. Each
            element of the list corresponds to a term of the equation.
            For example, if index three of the list is 9, the fourth
            term of the equation is 9x^3.
        """
        cfunc = lib_importer.windll.DAQmxGetScalePolyForwardCoeff
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str,
                        wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C','W')), ctypes.c_uint]

        temp_size = 0
        while True:
            val = numpy.zeros(temp_size, dtype=numpy.float64)

            size_or_code = cfunc(
                self._name, val, temp_size)

            if is_array_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return val.tolist()

    @poly_forward_coeff.setter
    def poly_forward_coeff(self, val):
        val = numpy.float64(val)
        cfunc = lib_importer.windll.DAQmxSetScalePolyForwardCoeff
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str,
                        wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C','W')), ctypes.c_uint]

        error_code = cfunc(
            self._name, val, len(val))
        check_for_error(error_code)

    @property
    def poly_reverse_coeff(self):
        """
        List[float]: Specifies a list of coefficients for the polynomial
            that converts scaled values to pre-scaled values. Each
            element of the list corresponds to a term of the equation.
            For example, if index three of the list is 9, the fourth
            term of the equation is 9y^3.
        """
        cfunc = lib_importer.windll.DAQmxGetScalePolyReverseCoeff
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str,
                        wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C','W')), ctypes.c_uint]

        temp_size = 0
        while True:
            val = numpy.zeros(temp_size, dtype=numpy.float64)

            size_or_code = cfunc(
                self._name, val, temp_size)

            if is_array_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return val.tolist()

    @poly_reverse_coeff.setter
    def poly_reverse_coeff(self, val):
        val = numpy.float64(val)
        cfunc = lib_importer.windll.DAQmxSetScalePolyReverseCoeff
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str,
                        wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C','W')), ctypes.c_uint]

        error_code = cfunc(
            self._name, val, len(val))
        check_for_error(error_code)

    @property
    def pre_scaled_units(self):
        """
        :class:`nidaqmx.constants.UnitsPreScaled`: Specifies the units
            of the values that you want to scale.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetScalePreScaledUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._name, ctypes.byref(val))
        check_for_error(error_code)

        return UnitsPreScaled(val.value)

    @pre_scaled_units.setter
    def pre_scaled_units(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetScalePreScaledUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._name, val)
        check_for_error(error_code)

    @property
    def scale_type(self):
        """
        :class:`nidaqmx.constants.ScaleType`: Indicates the method or
            equation form that the custom scale uses.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetScaleType
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._name, ctypes.byref(val))
        check_for_error(error_code)

        return ScaleType(val.value)

    @property
    def scaled_units(self):
        """
        str: Specifies the units to use for scaled values. You can use
            an arbitrary string.
        """
        cfunc = lib_importer.windll.DAQmxGetScaleScaledUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.c_char_p, ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._name, val, temp_size)

            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return val.value.decode('ascii')

    @scaled_units.setter
    def scaled_units(self, val):
        cfunc = lib_importer.windll.DAQmxSetScaleScaledUnits
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes_byte_str]

        error_code = cfunc(
            self._name, val)
        check_for_error(error_code)

    @property
    def table_pre_scaled_vals(self):
        """
        List[float]: Specifies a list of pre-scaled values. These values
            map directly to the values in **table_scaled_vals**.
        """
        cfunc = lib_importer.windll.DAQmxGetScaleTablePreScaledVals
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str,
                        wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C','W')), ctypes.c_uint]

        temp_size = 0
        while True:
            val = numpy.zeros(temp_size, dtype=numpy.float64)

            size_or_code = cfunc(
                self._name, val, temp_size)

            if is_array_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return val.tolist()

    @table_pre_scaled_vals.setter
    def table_pre_scaled_vals(self, val):
        val = numpy.float64(val)
        cfunc = lib_importer.windll.DAQmxSetScaleTablePreScaledVals
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str,
                        wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C','W')), ctypes.c_uint]

        error_code = cfunc(
            self._name, val, len(val))
        check_for_error(error_code)

    @property
    def table_scaled_vals(self):
        """
        List[float]: Specifies a list of scaled values. These values map
            directly to the values in **table_pre_scaled_vals**.
        """
        cfunc = lib_importer.windll.DAQmxGetScaleTableScaledVals
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str,
                        wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C','W')), ctypes.c_uint]

        temp_size = 0
        while True:
            val = numpy.zeros(temp_size, dtype=numpy.float64)

            size_or_code = cfunc(
                self._name, val, temp_size)

            if is_array_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return val.tolist()

    @table_scaled_vals.setter
    def table_scaled_vals(self, val):
        val = numpy.float64(val)
        cfunc = lib_importer.windll.DAQmxSetScaleTableScaledVals
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str,
                        wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C','W')), ctypes.c_uint]

        error_code = cfunc(
            self._name, val, len(val))
        check_for_error(error_code)

    @staticmethod
    def calculate_reverse_poly_coeff(
            forward_coeffs, min_val_x=-5.0, max_val_x=5.0,
            num_points_to_compute=1000, reverse_poly_order=-1):
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
        Returns:
            List[float]: 
            
            Specifies the list of coefficients for the reverse 
            polynomial. Each element of the list corresponds to a term 
            of the equation. For example, if index three of the list is 
            9, the fourth term of the equation is 9y^3.
        """
        forward_coeffs = numpy.float64(forward_coeffs)

        if reverse_poly_order == -1:
            size = len(forward_coeffs)
        else:
            size = reverse_poly_order + 1

        reverse_coeffs = numpy.zeros(size, dtype=numpy.float64)

        cfunc = lib_importer.windll.DAQmxCalculateReversePolyCoeff
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        numpy.ctypeslib.ndpointer(
                            dtype=numpy.float64, flags=('C', 'W')),
                        ctypes.c_uint, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int,
                        numpy.ctypeslib.ndpointer(
                            dtype=numpy.float64, flags=('C', 'W'))]

        error_code = cfunc(
            forward_coeffs, len(forward_coeffs), min_val_x, max_val_x,
            num_points_to_compute, reverse_poly_order, reverse_coeffs)
        check_for_error(error_code)

        return reverse_coeffs.tolist()

    @staticmethod
    def create_lin_scale(
            scale_name, slope, y_intercept=0.0,
            pre_scaled_units=UnitsPreScaled.VOLTS, scaled_units=None):
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
        Returns:
            nidaqmx.scale.Scale:
            
            Indicates an object that represents the created custom scale.
        """
        scale = Scale(scale_name)

        cfunc = lib_importer.windll.DAQmxCreateLinScale
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes_byte_str]

        error_code = cfunc(
            scale_name, slope, y_intercept, pre_scaled_units.value,
            scaled_units)
        check_for_error(error_code)

        return scale

    @staticmethod
    def create_map_scale(
            scale_name, prescaled_min, prescaled_max, scaled_min, scaled_max,
            pre_scaled_units=UnitsPreScaled.VOLTS, scaled_units=None):
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
        Returns:
            nidaqmx.scale.Scale: 
            
            Indicates an object that represents the created custom scale.
        """
        scale = Scale(scale_name)

        cfunc = lib_importer.windll.DAQmxCreateMapScale
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_double, ctypes.c_double, ctypes.c_int,
                        ctypes_byte_str]

        error_code = cfunc(
            scale_name, prescaled_min, prescaled_max, scaled_min, scaled_max,
            pre_scaled_units.value, scaled_units)
        check_for_error(error_code)

        return scale

    @staticmethod
    def create_polynomial_scale(
            scale_name, forward_coeffs, reverse_coeffs,
            pre_scaled_units=UnitsPreScaled.VOLTS, scaled_units=None):
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
        Returns:
            nidaqmx.scale.Scale: 
            
            Indicates an object that represents the created custom scale.
        """
        scale = Scale(scale_name)

        if forward_coeffs is None:
            forward_coeffs = []

        if reverse_coeffs is None:
            reverse_coeffs = []

        forward_coeffs = numpy.float64(forward_coeffs)
        reverse_coeffs = numpy.float64(reverse_coeffs)

        cfunc = lib_importer.windll.DAQmxCreatePolynomialScale
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str,
                        wrapped_ndpointer(dtype=numpy.float64,
                                          flags=('C', 'W')),
                        ctypes.c_uint,
                        wrapped_ndpointer(dtype=numpy.float64,
                                          flags=('C', 'W')),
                        ctypes.c_uint, ctypes.c_int, ctypes_byte_str]

        error_code = cfunc(
            scale_name, forward_coeffs, len(forward_coeffs), reverse_coeffs,
            len(reverse_coeffs), pre_scaled_units.value, scaled_units)
        check_for_error(error_code)

        return scale

    @staticmethod
    def create_table_scale(
            scale_name, prescaled_vals, scaled_vals,
            pre_scaled_units=UnitsPreScaled.VOLTS, scaled_units=None):
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
        Returns:
            nidaqmx.scale.Scale: 
            
            Indicates an object that represents the created custom scale.
        """
        scale = Scale(scale_name)

        if prescaled_vals is None:
            prescaled_vals = []

        if scaled_vals is None:
            scaled_vals = []

        prescaled_vals = numpy.float64(prescaled_vals)
        scaled_vals = numpy.float64(scaled_vals)

        cfunc = lib_importer.windll.DAQmxCreateTableScale
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str,
                        wrapped_ndpointer(dtype=numpy.float64,
                                          flags=('C', 'W')),
                        ctypes.c_uint,
                        wrapped_ndpointer(dtype=numpy.float64,
                                          flags=('C', 'W')),
                        ctypes.c_uint, ctypes.c_int, ctypes_byte_str]

        error_code = cfunc(
            scale_name, prescaled_vals, len(prescaled_vals), scaled_vals,
            len(scaled_vals), pre_scaled_units.value, scaled_units)
        check_for_error(error_code)

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

        cfunc = lib_importer.windll.DAQmxSaveScale
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str, ctypes_byte_str, ctypes_byte_str,
                        ctypes.c_uint]

        error_code = cfunc(
            self._name, save_as, author, options)
        check_for_error(error_code)

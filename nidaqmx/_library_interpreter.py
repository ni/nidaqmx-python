import ctypes
from nidaqmx.errors import check_for_error

from nidaqmx._lib import lib_importer, ctypes_byte_str

class LibraryInterpreter(object):
    '''Library C<->Python interpreter.

    This class is responsible for interpreting the Library's C API. It is responsible for:
    * Converting ctypes to native Python types.
    * Dealing with string encoding.
    * Allocating memory.
    * Converting errors returned by Library into Python exceptions.
    '''

    def __init__(self, encoding):
        self._encoding = encoding
        self.set_task_handle()
        self.set_system_handle()
        self.set_scale_handle()
    
    def set_task_handle(self, value=0):
        self._task_handle = value

    def get_task_handle(self):
        return self._task_handle
    
    def set_system_handle(self, value=0):
        self._system_handle = value

    def get_system_handle(self):
        return self._system_handle

    def set_scale_handle(self, value=0):
        self._scale_handle = value

    def get_scale_handle(self):
        return self._scale_handle

    def create_task(self, new_task_name):
        
        handle = lib_importer.task_handle(0)

        cfunc = lib_importer.windll.DAQmxCreateTask
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        ctypes_byte_str,
                        ctypes.POINTER(lib_importer.task_handle)]
        error_code = cfunc(
            new_task_name, ctypes.byref(handle))
        check_for_error(error_code)

        return handle
    
    def close(self):

        cfunc = lib_importer.windll.DAQmxClearTask
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._task_handle)
        check_for_error(error_code)
    
    def add_ai_voltage_chan(
            self, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val,
            max_val, units, custom_scale_name):
            
        cfunc = lib_importer.windll.DAQmxCreateAIVoltageChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_int, ctypes.c_double,
                        ctypes.c_double, ctypes.c_int, ctypes_byte_str]

        error_code = cfunc(
            self._handle, physical_channel, name_to_assign_to_channel,
            terminal_config.value, min_val, max_val, units.value,
            custom_scale_name)
        check_for_error(error_code)

    def add_ai_temp_built_in_sensor_chan(
            self, physical_channel, name_to_assign_to_channel,
            units):

            cfunc = lib_importer.windll.DAQmxCreateAITempBuiltInSensorChan
            if cfunc.argtypes is None:
                with cfunc.arglock:
                    if cfunc.argtypes is None:
                        cfunc.argtypes = [
                            lib_importer.task_handle, ctypes_byte_str,
                            ctypes_byte_str, ctypes.c_int]

            error_code = cfunc(
                self._handle, physical_channel, name_to_assign_to_channel,
                units.value)
            check_for_error(error_code)

    def get_chan_attribute_bool(
        self, channel_name, attribute_id):

        val = ctypes.c_bool()

        cfunc = lib_importer.windll.DAQmxGetChanAttribute
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int, ctypes.POINTER(ctypes.c_bool)]

        error_code = cfunc(
            self._task_handle, channel_name, attribute_id, ctypes.byref(val))
        check_for_error(error_code)

        return bool(val.value)

    def get_chan_attribute_int32(
        self, channel_name, attribute_id):

        val = ctypes.c_int32()

        cfunc = lib_importer.windll.DAQmxGetChanAttribute
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int, ctypes.POINTER(ctypes.c_int32)]

        error_code = cfunc(
            self._task_handle, channel_name, attribute_id, ctypes.byref(val))
        check_for_error(error_code)

        return int(val.value)
    
    def get_chan_attribute_string(
        self,channel_name, attribute_id):

        val = ctypes.c_char_p()

        cfunc = lib_importer.windll.DAQmxGetChanAttribute
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int, ctypes.c_char_p]

        error_code = cfunc(
            self._task_handle, channel_name, attribute_id, ctypes.byref(val))
        check_for_error(error_code)

        return str(val.value)
        
    def get_task_attribute_string(
        self, attribute_id):

        val = ctypes.c_char_p()

        cfunc = lib_importer.windll.DAQmxGetTaskAttribute
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int, ctypes.c_char_p]

        error_code = cfunc(
            self._task_handle, attribute_id, ctypes.byref(val))
        check_for_error(error_code)

        return str(val.value)

    def set_chan_attribute_bool(
        self, channel_name, attribute_id, attribute_value):

        cfunc = lib_importer.windll.DAQmxSetChanAttribute
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int, ctypes.c_bool]

        error_code = cfunc(
            self._task_handle, channel_name, attribute_id, attribute_value)
        check_for_error(error_code)

    def set_chan_attribute_int32(
        self, channel_name, attribute_id, attribute_value):

        cfunc = lib_importer.windll.DAQmxSetChanAttribute
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int, ctypes.c_int32]

        error_code = cfunc(
            self._task_handle, channel_name, attribute_id, attribute_value)
        check_for_error(error_code)

    def set_chan_attribute_string(
        self, channel_name, attribute_id, attribute_value):

        cfunc = lib_importer.windll.DAQmxSetChanAttribute
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int, ctypes.c_char_p]

        error_code = cfunc(
            self._task_handle, channel_name, attribute_id, attribute_value)
        check_for_error(error_code)

    def reset_channel_attribute(
        self, channel_name, attribute_id):

        cfunc = lib_importer.windll.DAQmxResetChanAttribute
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = cfunc(
            self._task_handle, channel_name, attribute_id)
        check_for_error(error_code)
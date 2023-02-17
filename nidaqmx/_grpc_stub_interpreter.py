import threading
import warnings

import grpc
import nidaqmx.nidaqmx_pb2 as grpc_types
import nidaqmx.nidaqmx_pb2_grpc as nidaqmx_grpc
import nidaqmx.session_pb2 as session_grpc_types

class GrpcStubInterpreter(object):
    '''Interpreter for interacting with a gRPC Stub class'''

    def __init__(self, grpc_options):
        self._grpc_options = grpc_options
        self._lock = threading.RLock()
        self._client = nidaqmx_grpc.NiDAQmxStub(grpc_options.grpc_channel)
        self.session_initialization_behavior = grpc_options.initialization_behavior
        self.set_task_handle()
        self.set_system_handle()
        self.set_scale_handle()

    def set_task_handle(self, value=session_grpc_types.Session()):
        self._task_handle = value

    def get_task_handle(self):
        return self._task_handle
    
    def set_system_handle(self, value=session_grpc_types.Session()):
        self._system_handle = value

    def get_system_handle(self):
        return self._system_handle

    def set_scale_handle(self, value=session_grpc_types.Session()):
        self._scale_handle = value

    def get_scale_handle(self):
        return self._scale_handle

    def _invoke(self, func, request, metadata=None):
        try:
            response = func(request, metadata=metadata)
            error_code = response.status
            error_message = ''
        except grpc.RpcError as rpc_error:
            raise RPCException(rpc_error)
            # more handling needs to be done here...

        return response

    def create_task(self, new_task_name, ):
        '''
        Creates a Task object.
        '''

        response = self._invoke(
            self._client.CreateTask,
            grpc_types.CreateTaskRequest(
                session_name = new_task_name,
                initialization_behavior = self.session_initialization_behavior
            )
        )

        return response.task

    def clear_task(self):

        self._invoke(
            self._client.ClearTask,
            grpc_types.ClearTaskRequest(
                task = self._task_handle
            )
        )

    def add_ai_voltage_chan(
            self, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val,
            max_val, units, custom_scale_name):
            
            self._invoke(
                self._client.CreateAIVoltageChan,
                grpc_types.CreateAIVoltageChanRequest(
                    task = self._task_handle,
                    physical_channel = physical_channel,
                    name_to_assign_to_channel = name_to_assign_to_channel,
                    terminal_config_raw = terminal_config.value,
                    min_val = min_val,
                    max_val = max_val,
                    units_raw = units.value,
                    custom_scale_name = custom_scale_name
                )
            )
    def add_ai_temp_built_in_sensor_chan(
            self, physical_channel, name_to_assign_to_channel,
            units):
            '''
             A simple example of a function with enum parameter.
            '''
            self._invoke(
                self._client.CreateAITempBuiltInSensorChan, 
                grpc_types.CreateAITempBuiltInSensorChanRequest(
                    task = self._task_handle,
                    physical_channel = physical_channel,
                    name_to_assign_to_channel = name_to_assign_to_channel,
                    units_raw = units.value
                )
            )
    
    def auto_configure_cdaq_sync_connections(
            self, chassis_devices_ports, timeout):
            '''
             A method that returns a list of clusters
            '''

            self._invoke(
                self._client.AutoConfigureCDAQSyncConnections,
                grpc_types.AutoConfigureCDAQSyncConnectionsRequest(
                    chassis_devices_ports = chassis_devices_ports,
                    timeout = timeout
                )
            )
    
    def get_chan_attribute_bool(
        self, channel_name, attribute_id):

        response = self._invoke(
            self._client.GetChanAttributeBool, 
            grpc_types.GetChanAttributeBoolRequest(
                task = self._task_handle,
                channel_name = channel_name,
                attribute_raw = attribute_id
            )
        )
        return response.value

    def get_chan_attribute_int32(
        self, channel_name, attribute_id):

        response = self._invoke(
            self._client.GetChanAttributeInt32, 
            grpc_types.GetChanAttributeInt32Request(
                task = self._task_handle,
                channel_name = channel_name,
                attribute_raw = attribute_id
            )
        )
        return response.value
    
    def get_chan_attribute_string(
        self, channel_name, attribute_id):

        response = self._invoke(
            self._client.GetChanAttributeString, 
            grpc_types.GetChanAttributeStringRequest(
                task = self._task_handle,
                channel_name = channel_name,
                attribute_raw = attribute_id
            )
        )
        return response.value

    def get_task_attribute_string(
            self, attribute_id):

        response = self._invoke(
            self._client.GetTaskAttributeString,
            grpc_types.GetTaskAttributeStringRequest(
                task = self._task_handle,
                attribute_raw = attribute_id
            )
        )

        return response.value



    def set_chan_attribute_bool(
        self, channel_name, attribute_id, attribute_value):

        self._invoke(
            self._client.SetChanAttributeBool,
            grpc_types.GetChanAttributeBoolRequest(
                task = self._task_handle,
                channel_name = channel_name,
                attribute_raw = attribute_id,
                value = attribute_value
            )
        )
    
    def set_chan_attribute_int32(
        self, channel_name, attribute_id, attribute_value):

        self._invoke(
            self._client.SetChanAttributeInt32,
            grpc_types.GetChanAttributeInt32Request(
                task = self._task_handle,
                channel_name = channel_name,
                attribute_raw = attribute_id,
                value = attribute_value
            )
        )

    def set_chan_attribute_string(
        self, channel_name, attribute_id, attribute_value):

        self._invoke(
            self._client.SetChanAttributeString,
            grpc_types.GetChanAttributeInt32Request(
                task = self._task_handle,
                channel_name = channel_name,
                attribute_raw = attribute_id,
                value = attribute_value
            )
        )

    def reset_channel_attribute(
        self, channel_name, attribute_id):

        self._invoke(
            self._client.ResetChanAttribute(
                task = self._task_handle,
                channel_name = channel_name,
                attribute_raw = attribute_id,
            )
        )
    
    # @property
    # def ai_ac_excit_sync_enable(self):
    #     """
    #     bool: Specifies whether to synchronize the AC excitation source
    #         of the channel to that of another channel. Synchronize the
    #         excitation sources of multiple channels to use multichannel
    #         sensors. Set this property to False for the master channel
    #         and to True for the slave channels.
    #     """
    #     val = c_bool32()

    #     cfunc = lib_importer.windll.DAQmxGetAIACExcitSyncEnable
    #     if cfunc.argtypes is None:
    #         with cfunc.arglock:
    #             if cfunc.argtypes is None:
    #                 cfunc.argtypes = [
    #                     lib_importer.task_handle, ctypes_byte_str,
    #                     ctypes.POINTER(c_bool32)]

    #     error_code = cfunc(
    #         self._handle, self._name, ctypes.byref(val))
    #     check_for_error(error_code)

    #     return val.value

    # @ai_ac_excit_sync_enable.setter
    # def ai_ac_excit_sync_enable(self, val):
    #     cfunc = lib_importer.windll.DAQmxSetAIACExcitSyncEnable
    #     if cfunc.argtypes is None:
    #         with cfunc.arglock:
    #             if cfunc.argtypes is None:
    #                 cfunc.argtypes = [
    #                     lib_importer.task_handle, ctypes_byte_str, c_bool32]

    #     error_code = cfunc(
    #         self._handle, self._name, val)
    #     check_for_error(error_code)

    # @ai_ac_excit_sync_enable.deleter
    # def ai_ac_excit_sync_enable(self):
    #     cfunc = lib_importer.windll.DAQmxResetAIACExcitSyncEnable
    #     if cfunc.argtypes is None:
    #         with cfunc.arglock:
    #             if cfunc.argtypes is None:
    #                 cfunc.argtypes = [
    #                     lib_importer.task_handle, ctypes_byte_str]

    #     error_code = cfunc(
    #         self._handle, self._name)
    #     check_for_error(error_code)

    #  @property
    # def ai_ac_excit_wire_mode(self):
    #     """
    #     :class:`nidaqmx.constants.ACExcitWireMode`: Specifies the number
    #         of leads on the LVDT or RVDT. Some sensors require you to
    #         tie leads together to create a four- or five- wire sensor.
    #         Refer to the sensor documentation for more information.
    #     """
    #     val = ctypes.c_int()

    #     cfunc = lib_importer.windll.DAQmxGetAIACExcitWireMode
    #     if cfunc.argtypes is None:
    #         with cfunc.arglock:
    #             if cfunc.argtypes is None:
    #                 cfunc.argtypes = [
    #                     lib_importer.task_handle, ctypes_byte_str,
    #                     ctypes.POINTER(ctypes.c_int)]

    #     error_code = cfunc(
    #         self._handle, self._name, ctypes.byref(val))
    #     check_for_error(error_code)

    #     return ACExcitWireMode(val.value)

    # @ai_ac_excit_wire_mode.setter
    # def ai_ac_excit_wire_mode(self, val):
    #     val = val.value
    #     cfunc = lib_importer.windll.DAQmxSetAIACExcitWireMode
    #     if cfunc.argtypes is None:
    #         with cfunc.arglock:
    #             if cfunc.argtypes is None:
    #                 cfunc.argtypes = [
    #                     lib_importer.task_handle, ctypes_byte_str,
    #                     ctypes.c_int]

    #     error_code = cfunc(
    #         self._handle, self._name, val)
    #     check_for_error(error_code)

    # @ai_ac_excit_wire_mode.deleter
    # def ai_ac_excit_wire_mode(self):
    #     cfunc = lib_importer.windll.DAQmxResetAIACExcitWireMode
    #     if cfunc.argtypes is None:
    #         with cfunc.arglock:
    #             if cfunc.argtypes is None:
    #                 cfunc.argtypes = [
    #                     lib_importer.task_handle, ctypes_byte_str]

    #     error_code = cfunc(
    #         self._handle, self._name)
    #     check_for_error(error_code)
    
    #     @property
    # def ai_custom_scale(self):
    #     """
    #     :class:`nidaqmx.system.scale.Scale`: Specifies the name of a
    #         custom scale for the channel.
    #     """
    #     cfunc = lib_importer.windll.DAQmxGetAICustomScaleName
    #     if cfunc.argtypes is None:
    #         with cfunc.arglock:
    #             if cfunc.argtypes is None:
    #                 cfunc.argtypes = [
    #                     lib_importer.task_handle, ctypes_byte_str,
    #                     ctypes.c_char_p, ctypes.c_uint]

    #     temp_size = 0
    #     while True:
    #         val = ctypes.create_string_buffer(temp_size)

    #         size_or_code = cfunc(
    #             self._handle, self._name, val, temp_size)

    #         if is_string_buffer_too_small(size_or_code):
    #             # Buffer size must have changed between calls; check again.
    #             temp_size = 0
    #         elif size_or_code > 0 and temp_size == 0:
    #             # Buffer size obtained, use to retrieve data.
    #             temp_size = size_or_code
    #         else:
    #             break

    #     check_for_error(size_or_code)

    #     return Scale(val.value.decode('ascii'))

    # @ai_custom_scale.setter
    # def ai_custom_scale(self, val):
    #     val = val.name
    #     cfunc = lib_importer.windll.DAQmxSetAICustomScaleName
    #     if cfunc.argtypes is None:
    #         with cfunc.arglock:
    #             if cfunc.argtypes is None:
    #                 cfunc.argtypes = [
    #                     lib_importer.task_handle, ctypes_byte_str,
    #                     ctypes_byte_str]

    #     error_code = cfunc(
    #         self._handle, self._name, val)
    #     check_for_error(error_code)

    # @ai_custom_scale.deleter
    # def ai_custom_scale(self):
    #     cfunc = lib_importer.windll.DAQmxResetAICustomScaleName
    #     if cfunc.argtypes is None:
    #         with cfunc.arglock:
    #             if cfunc.argtypes is None:
    #                 cfunc.argtypes = [
    #                     lib_importer.task_handle, ctypes_byte_str]

    #     error_code = cfunc(
    #         self._handle, self._name)
    #     check_for_error(error_code)

    
    # ## System methods and properties

    # ## Scale methods and properties


==============================
Tools API
==============================
oneAPI Level Zero Specification - Version 1.15.31

 

 

Common
============================================================
* Enumerations


    * :ref:`zet-structure-type-t`
    * :ref:`zet-value-type-t`

 
* Structures


    * :ref:`zet-base-properties-t`
    * :ref:`zet-base-desc-t`
    * :ref:`zet-value-t`
    * :ref:`zet-typed-value-t`




Common Enums
------------------------------------------------------------------------------


.. _zet-structure-type-t:

zet_structure_type_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenenum:: zet_structure_type_t
    :project: LevelZero


.. _zet-value-type-t:

zet_value_type_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenenum:: zet_value_type_t
    :project: LevelZero

 
Common Structures
------------------------------------------------------------------------------

.. _zet-base-properties-t:

zet_base_properties_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenstruct:: zet_base_properties_t
    :project: LevelZero
    :members:
    :undoc-members:

.. _zet-base-desc-t:

zet_base_desc_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenstruct:: zet_base_desc_t
    :project: LevelZero
    :members:
    :undoc-members:

.. _zet-value-t:

zet_value_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenunion:: zet_value_t
    :project: LevelZero

.. _zet-typed-value-t:

zet_typed_value_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenstruct:: zet_typed_value_t
    :project: LevelZero
    :members:
    :undoc-members:


 

 

 




 

 

 

 




 

 

 

 




 

 

Module
============================================================
* Functions


    * :ref:`zetModuleGetDebugInfo`

 
* Enumerations


    * :ref:`zet-module-debug-info-format-t`

 


Module Functions
------------------------------------------------------------------------------


.. _zetModuleGetDebugInfo:

zetModuleGetDebugInfo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetModuleGetDebugInfo
    :project: LevelZero



Module Enums
------------------------------------------------------------------------------


.. _zet-module-debug-info-format-t:

zet_module_debug_info_format_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenenum:: zet_module_debug_info_format_t
    :project: LevelZero

 

 

Debug
============================================================
* Functions


    * :ref:`zetDeviceGetDebugProperties`
    * :ref:`zetDebugAttach`
    * :ref:`zetDebugDetach`
    * :ref:`zetDebugReadEvent`
    * :ref:`zetDebugAcknowledgeEvent`
    * :ref:`zetDebugInterrupt`
    * :ref:`zetDebugResume`
    * :ref:`zetDebugReadMemory`
    * :ref:`zetDebugWriteMemory`
    * :ref:`zetDebugGetRegisterSetProperties`
    * :ref:`zetDebugGetThreadRegisterSetProperties`
    * :ref:`zetDebugReadRegisters`
    * :ref:`zetDebugWriteRegisters`

 
* Enumerations


    * :ref:`zet-device-debug-property-flags-t`
    * :ref:`zet-debug-event-flags-t`
    * :ref:`zet-debug-event-type-t`
    * :ref:`zet-debug-detach-reason-t`
    * :ref:`zet-debug-page-fault-reason-t`
    * :ref:`zet-debug-memory-space-type-t`
    * :ref:`zet-debug-regset-flags-t`

 
* Structures


    * :ref:`zet-device-debug-properties-t`
    * :ref:`zet-debug-config-t`
    * :ref:`zet-debug-event-info-detached-t`
    * :ref:`zet-debug-event-info-module-t`
    * :ref:`zet-debug-event-info-thread-stopped-t`
    * :ref:`zet-debug-event-info-page-fault-t`
    * :ref:`zet-debug-event-info-t`
    * :ref:`zet-debug-event-t`
    * :ref:`zet-debug-memory-space-desc-t`
    * :ref:`zet-debug-regset-properties-t`


Debug Functions
------------------------------------------------------------------------------


.. _zetDeviceGetDebugProperties:

zetDeviceGetDebugProperties
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetDeviceGetDebugProperties
    :project: LevelZero


.. _zetDebugAttach:

zetDebugAttach
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetDebugAttach
    :project: LevelZero


.. _zetDebugDetach:

zetDebugDetach
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetDebugDetach
    :project: LevelZero


.. _zetDebugReadEvent:

zetDebugReadEvent
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetDebugReadEvent
    :project: LevelZero


.. _zetDebugAcknowledgeEvent:

zetDebugAcknowledgeEvent
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetDebugAcknowledgeEvent
    :project: LevelZero


.. _zetDebugInterrupt:

zetDebugInterrupt
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetDebugInterrupt
    :project: LevelZero


.. _zetDebugResume:

zetDebugResume
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetDebugResume
    :project: LevelZero


.. _zetDebugReadMemory:

zetDebugReadMemory
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetDebugReadMemory
    :project: LevelZero


.. _zetDebugWriteMemory:

zetDebugWriteMemory
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetDebugWriteMemory
    :project: LevelZero


.. _zetDebugGetRegisterSetProperties:

zetDebugGetRegisterSetProperties
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetDebugGetRegisterSetProperties
    :project: LevelZero


.. _zetDebugGetThreadRegisterSetProperties:

zetDebugGetThreadRegisterSetProperties
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetDebugGetThreadRegisterSetProperties
    :project: LevelZero


.. _zetDebugReadRegisters:

zetDebugReadRegisters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetDebugReadRegisters
    :project: LevelZero


.. _zetDebugWriteRegisters:

zetDebugWriteRegisters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetDebugWriteRegisters
    :project: LevelZero



Debug Enums
------------------------------------------------------------------------------


.. _zet-device-debug-property-flags-t:

zet_device_debug_property_flags_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenenum:: zet_device_debug_property_flag_t
    :project: LevelZero


.. _zet-debug-event-flags-t:

zet_debug_event_flags_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenenum:: zet_debug_event_flag_t
    :project: LevelZero


.. _zet-debug-event-type-t:

zet_debug_event_type_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenenum:: zet_debug_event_type_t
    :project: LevelZero


.. _zet-debug-detach-reason-t:

zet_debug_detach_reason_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenenum:: zet_debug_detach_reason_t
    :project: LevelZero


.. _zet-debug-page-fault-reason-t:

zet_debug_page_fault_reason_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenenum:: zet_debug_page_fault_reason_t
    :project: LevelZero


.. _zet-debug-memory-space-type-t:

zet_debug_memory_space_type_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenenum:: zet_debug_memory_space_type_t
    :project: LevelZero


.. _zet-debug-regset-flags-t:

zet_debug_regset_flags_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenenum:: zet_debug_regset_flag_t
    :project: LevelZero

 
Debug Structures
------------------------------------------------------------------------------

.. _zet-device-debug-properties-t:

zet_device_debug_properties_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenstruct:: zet_device_debug_properties_t
    :project: LevelZero
    :members:
    :undoc-members:

.. _zet-debug-config-t:

zet_debug_config_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenstruct:: zet_debug_config_t
    :project: LevelZero
    :members:
    :undoc-members:

.. _zet-debug-event-info-detached-t:

zet_debug_event_info_detached_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenstruct:: zet_debug_event_info_detached_t
    :project: LevelZero
    :members:
    :undoc-members:

.. _zet-debug-event-info-module-t:

zet_debug_event_info_module_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenstruct:: zet_debug_event_info_module_t
    :project: LevelZero
    :members:
    :undoc-members:

.. _zet-debug-event-info-thread-stopped-t:

zet_debug_event_info_thread_stopped_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenstruct:: zet_debug_event_info_thread_stopped_t
    :project: LevelZero
    :members:
    :undoc-members:

.. _zet-debug-event-info-page-fault-t:

zet_debug_event_info_page_fault_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenstruct:: zet_debug_event_info_page_fault_t
    :project: LevelZero
    :members:
    :undoc-members:

.. _zet-debug-event-info-t:

zet_debug_event_info_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenunion:: zet_debug_event_info_t
    :project: LevelZero

.. _zet-debug-event-t:

zet_debug_event_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenstruct:: zet_debug_event_t
    :project: LevelZero
    :members:
    :undoc-members:

.. _zet-debug-memory-space-desc-t:

zet_debug_memory_space_desc_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenstruct:: zet_debug_memory_space_desc_t
    :project: LevelZero
    :members:
    :undoc-members:

.. _zet-debug-regset-properties-t:

zet_debug_regset_properties_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenstruct:: zet_debug_regset_properties_t
    :project: LevelZero
    :members:
    :undoc-members:


 

Metric
============================================================
* Functions


    * :ref:`zetMetricGroupGet`
    * :ref:`zetMetricGroupGetProperties`
    * :ref:`zetMetricGroupCalculateMetricValues`
    * :ref:`zetMetricGet`
    * :ref:`zetMetricGetProperties`
    * :ref:`zetContextActivateMetricGroups`
    * :ref:`zetMetricStreamerOpen`
    * :ref:`zetCommandListAppendMetricStreamerMarker`
    * :ref:`zetMetricStreamerClose`
    * :ref:`zetMetricStreamerReadData`
    * :ref:`zetMetricQueryPoolCreate`
    * :ref:`zetMetricQueryPoolDestroy`
    * :ref:`zetMetricQueryCreate`
    * :ref:`zetMetricQueryDestroy`
    * :ref:`zetMetricQueryReset`
    * :ref:`zetCommandListAppendMetricQueryBegin`
    * :ref:`zetCommandListAppendMetricQueryEnd`
    * :ref:`zetCommandListAppendMetricMemoryBarrier`
    * :ref:`zetMetricQueryGetData`

 
* Enumerations


    * :ref:`zet-metric-group-sampling-type-flags-t`
    * :ref:`zet-metric-type-t`
    * :ref:`zet-metric-group-calculation-type-t`
    * :ref:`zet-metric-query-pool-type-t`

 
* Structures


    * :ref:`zet-metric-group-properties-t`
    * :ref:`zet-metric-properties-t`
    * :ref:`zet-metric-streamer-desc-t`
    * :ref:`zet-metric-query-pool-desc-t`


Metric Functions
------------------------------------------------------------------------------


.. _zetMetricGroupGet:

zetMetricGroupGet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetMetricGroupGet
    :project: LevelZero


.. _zetMetricGroupGetProperties:

zetMetricGroupGetProperties
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetMetricGroupGetProperties
    :project: LevelZero


.. _zetMetricGroupCalculateMetricValues:

zetMetricGroupCalculateMetricValues
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetMetricGroupCalculateMetricValues
    :project: LevelZero


.. _zetMetricGet:

zetMetricGet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetMetricGet
    :project: LevelZero


.. _zetMetricGetProperties:

zetMetricGetProperties
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetMetricGetProperties
    :project: LevelZero


.. _zetContextActivateMetricGroups:

zetContextActivateMetricGroups
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetContextActivateMetricGroups
    :project: LevelZero


.. _zetMetricStreamerOpen:

zetMetricStreamerOpen
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetMetricStreamerOpen
    :project: LevelZero


.. _zetCommandListAppendMetricStreamerMarker:

zetCommandListAppendMetricStreamerMarker
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetCommandListAppendMetricStreamerMarker
    :project: LevelZero


.. _zetMetricStreamerClose:

zetMetricStreamerClose
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetMetricStreamerClose
    :project: LevelZero


.. _zetMetricStreamerReadData:

zetMetricStreamerReadData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetMetricStreamerReadData
    :project: LevelZero


.. _zetMetricQueryPoolCreate:

zetMetricQueryPoolCreate
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetMetricQueryPoolCreate
    :project: LevelZero


.. _zetMetricQueryPoolDestroy:

zetMetricQueryPoolDestroy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetMetricQueryPoolDestroy
    :project: LevelZero


.. _zetMetricQueryCreate:

zetMetricQueryCreate
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetMetricQueryCreate
    :project: LevelZero


.. _zetMetricQueryDestroy:

zetMetricQueryDestroy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetMetricQueryDestroy
    :project: LevelZero


.. _zetMetricQueryReset:

zetMetricQueryReset
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetMetricQueryReset
    :project: LevelZero


.. _zetCommandListAppendMetricQueryBegin:

zetCommandListAppendMetricQueryBegin
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetCommandListAppendMetricQueryBegin
    :project: LevelZero


.. _zetCommandListAppendMetricQueryEnd:

zetCommandListAppendMetricQueryEnd
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetCommandListAppendMetricQueryEnd
    :project: LevelZero


.. _zetCommandListAppendMetricMemoryBarrier:

zetCommandListAppendMetricMemoryBarrier
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetCommandListAppendMetricMemoryBarrier
    :project: LevelZero


.. _zetMetricQueryGetData:

zetMetricQueryGetData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetMetricQueryGetData
    :project: LevelZero



Metric Enums
------------------------------------------------------------------------------


.. _zet-metric-group-sampling-type-flags-t:

zet_metric_group_sampling_type_flags_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenenum:: zet_metric_group_sampling_type_flag_t
    :project: LevelZero


.. _zet-metric-type-t:

zet_metric_type_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenenum:: zet_metric_type_t
    :project: LevelZero


.. _zet-metric-group-calculation-type-t:

zet_metric_group_calculation_type_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenenum:: zet_metric_group_calculation_type_t
    :project: LevelZero


.. _zet-metric-query-pool-type-t:

zet_metric_query_pool_type_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenenum:: zet_metric_query_pool_type_t
    :project: LevelZero

 
Metric Structures
------------------------------------------------------------------------------

.. _zet-metric-group-properties-t:

zet_metric_group_properties_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenstruct:: zet_metric_group_properties_t
    :project: LevelZero
    :members:
    :undoc-members:

.. _zet-metric-properties-t:

zet_metric_properties_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenstruct:: zet_metric_properties_t
    :project: LevelZero
    :members:
    :undoc-members:

.. _zet-metric-streamer-desc-t:

zet_metric_streamer_desc_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenstruct:: zet_metric_streamer_desc_t
    :project: LevelZero
    :members:
    :undoc-members:

.. _zet-metric-query-pool-desc-t:

zet_metric_query_pool_desc_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenstruct:: zet_metric_query_pool_desc_t
    :project: LevelZero
    :members:
    :undoc-members:


 

Pin
============================================================
* Functions


    * :ref:`zetKernelGetProfileInfo`

 
* Enumerations


    * :ref:`zet-profile-flags-t`
    * :ref:`zet-profile-token-type-t`

 
* Structures


    * :ref:`zet-profile-properties-t`
    * :ref:`zet-profile-free-register-token-t`
    * :ref:`zet-profile-register-sequence-t`


Pin Functions
------------------------------------------------------------------------------


.. _zetKernelGetProfileInfo:

zetKernelGetProfileInfo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetKernelGetProfileInfo
    :project: LevelZero



Pin Enums
------------------------------------------------------------------------------


.. _zet-profile-flags-t:

zet_profile_flags_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenenum:: zet_profile_flag_t
    :project: LevelZero


.. _zet-profile-token-type-t:

zet_profile_token_type_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenenum:: zet_profile_token_type_t
    :project: LevelZero

 
Pin Structures
------------------------------------------------------------------------------

.. _zet-profile-properties-t:

zet_profile_properties_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenstruct:: zet_profile_properties_t
    :project: LevelZero
    :members:
    :undoc-members:

.. _zet-profile-free-register-token-t:

zet_profile_free_register_token_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenstruct:: zet_profile_free_register_token_t
    :project: LevelZero
    :members:
    :undoc-members:

.. _zet-profile-register-sequence-t:

zet_profile_register_sequence_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenstruct:: zet_profile_register_sequence_t
    :project: LevelZero
    :members:
    :undoc-members:


 

Tracing
============================================================
* Functions


    * :ref:`zetTracerExpCreate`
    * :ref:`zetTracerExpDestroy`
    * :ref:`zetTracerExpSetPrologues`
    * :ref:`zetTracerExpSetEpilogues`
    * :ref:`zetTracerExpSetEnabled`

 
* Enumerations


    * :ref:`zet-api-tracing-exp-version-t`

 
* Structures


    * :ref:`zet-tracer-exp-desc-t`


Tracing Functions
------------------------------------------------------------------------------


.. _zetTracerExpCreate:

zetTracerExpCreate
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetTracerExpCreate
    :project: LevelZero


.. _zetTracerExpDestroy:

zetTracerExpDestroy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetTracerExpDestroy
    :project: LevelZero


.. _zetTracerExpSetPrologues:

zetTracerExpSetPrologues
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetTracerExpSetPrologues
    :project: LevelZero


.. _zetTracerExpSetEpilogues:

zetTracerExpSetEpilogues
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetTracerExpSetEpilogues
    :project: LevelZero


.. _zetTracerExpSetEnabled:

zetTracerExpSetEnabled
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetTracerExpSetEnabled
    :project: LevelZero



Tracing Enums
------------------------------------------------------------------------------


.. _zet-api-tracing-exp-version-t:

zet_api_tracing_exp_version_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenenum:: zet_api_tracing_exp_version_t
    :project: LevelZero

 
Tracing Structures
------------------------------------------------------------------------------

.. _zet-tracer-exp-desc-t:

zet_tracer_exp_desc_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenstruct:: zet_tracer_exp_desc_t
    :project: LevelZero
    :members:
    :undoc-members:


 

Concurrentmetricgroup
============================================================
* Functions


    * :ref:`zetDeviceGetConcurrentMetricGroupsExp`

 
* Enumerations


    * :ref:`zet-concurrent-metric-groups-exp-version-t`

 


Concurrentmetricgroup Functions
------------------------------------------------------------------------------


.. _zetDeviceGetConcurrentMetricGroupsExp:

zetDeviceGetConcurrentMetricGroupsExp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetDeviceGetConcurrentMetricGroupsExp
    :project: LevelZero



Concurrentmetricgroup Enums
------------------------------------------------------------------------------


.. _zet-concurrent-metric-groups-exp-version-t:

zet_concurrent_metric_groups_exp_version_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenenum:: zet_concurrent_metric_groups_exp_version_t
    :project: LevelZero

 

 

Metrictracer
============================================================
* Functions


    * :ref:`zetMetricTracerCreateExp`
    * :ref:`zetMetricTracerDestroyExp`
    * :ref:`zetMetricTracerEnableExp`
    * :ref:`zetMetricTracerDisableExp`
    * :ref:`zetMetricTracerReadDataExp`
    * :ref:`zetMetricDecoderCreateExp`
    * :ref:`zetMetricDecoderDestroyExp`
    * :ref:`zetMetricDecoderGetDecodableMetricsExp`
    * :ref:`zetMetricTracerDecodeExp`

 
* Enumerations


    * :ref:`zet-metric-tracer-exp-version-t`

 
* Structures


    * :ref:`zet-metric-tracer-exp-desc-t`
    * :ref:`zet-metric-entry-exp-t`


Metrictracer Functions
------------------------------------------------------------------------------


.. _zetMetricTracerCreateExp:

zetMetricTracerCreateExp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetMetricTracerCreateExp
    :project: LevelZero


.. _zetMetricTracerDestroyExp:

zetMetricTracerDestroyExp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetMetricTracerDestroyExp
    :project: LevelZero


.. _zetMetricTracerEnableExp:

zetMetricTracerEnableExp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetMetricTracerEnableExp
    :project: LevelZero


.. _zetMetricTracerDisableExp:

zetMetricTracerDisableExp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetMetricTracerDisableExp
    :project: LevelZero


.. _zetMetricTracerReadDataExp:

zetMetricTracerReadDataExp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetMetricTracerReadDataExp
    :project: LevelZero


.. _zetMetricDecoderCreateExp:

zetMetricDecoderCreateExp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetMetricDecoderCreateExp
    :project: LevelZero


.. _zetMetricDecoderDestroyExp:

zetMetricDecoderDestroyExp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetMetricDecoderDestroyExp
    :project: LevelZero


.. _zetMetricDecoderGetDecodableMetricsExp:

zetMetricDecoderGetDecodableMetricsExp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetMetricDecoderGetDecodableMetricsExp
    :project: LevelZero


.. _zetMetricTracerDecodeExp:

zetMetricTracerDecodeExp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetMetricTracerDecodeExp
    :project: LevelZero



Metrictracer Enums
------------------------------------------------------------------------------


.. _zet-metric-tracer-exp-version-t:

zet_metric_tracer_exp_version_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenenum:: zet_metric_tracer_exp_version_t
    :project: LevelZero

 
Metrictracer Structures
------------------------------------------------------------------------------

.. _zet-metric-tracer-exp-desc-t:

zet_metric_tracer_exp_desc_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenstruct:: zet_metric_tracer_exp_desc_t
    :project: LevelZero
    :members:
    :undoc-members:

.. _zet-metric-entry-exp-t:

zet_metric_entry_exp_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenstruct:: zet_metric_entry_exp_t
    :project: LevelZero
    :members:
    :undoc-members:


 

 

Metricexportmemory
============================================================
* Enumerations


    * :ref:`zet-metric-group-type-exp-flags-t`

 
* Structures


    * :ref:`zet-metric-group-type-exp-t`
    * :ref:`zet-export-dma-buf-exp-properties-t`




Metricexportmemory Enums
------------------------------------------------------------------------------


.. _zet-metric-group-type-exp-flags-t:

zet_metric_group_type_exp_flags_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenenum:: zet_metric_group_type_exp_flag_t
    :project: LevelZero

 
Metricexportmemory Structures
------------------------------------------------------------------------------

.. _zet-metric-group-type-exp-t:

zet_metric_group_type_exp_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenstruct:: zet_metric_group_type_exp_t
    :project: LevelZero
    :members:
    :undoc-members:

.. _zet-export-dma-buf-exp-properties-t:

zet_export_dma_buf_exp_properties_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenstruct:: zet_export_dma_buf_exp_properties_t
    :project: LevelZero
    :members:
    :undoc-members:


 

Metricgroupmarker
============================================================
* Functions


    * :ref:`zetCommandListAppendMarkerExp`

 
* Enumerations


    * :ref:`zet-metric-group-marker-exp-version-t`

 
* Structures


    * :ref:`zet-metric-source-id-exp-t`


Metricgroupmarker Functions
------------------------------------------------------------------------------


.. _zetCommandListAppendMarkerExp:

zetCommandListAppendMarkerExp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetCommandListAppendMarkerExp
    :project: LevelZero



Metricgroupmarker Enums
------------------------------------------------------------------------------


.. _zet-metric-group-marker-exp-version-t:

zet_metric_group_marker_exp_version_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenenum:: zet_metric_group_marker_exp_version_t
    :project: LevelZero

 
Metricgroupmarker Structures
------------------------------------------------------------------------------

.. _zet-metric-source-id-exp-t:

zet_metric_source_id_exp_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenstruct:: zet_metric_source_id_exp_t
    :project: LevelZero
    :members:
    :undoc-members:


 

Metricruntimeenabledisable
============================================================
* Functions


    * :ref:`zetDeviceEnableMetricsExp`
    * :ref:`zetDeviceDisableMetricsExp`

 
* Enumerations


    * :ref:`zet-metrics-runtime-enable-disable-exp-version-t`

 


Metricruntimeenabledisable Functions
------------------------------------------------------------------------------


.. _zetDeviceEnableMetricsExp:

zetDeviceEnableMetricsExp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetDeviceEnableMetricsExp
    :project: LevelZero


.. _zetDeviceDisableMetricsExp:

zetDeviceDisableMetricsExp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetDeviceDisableMetricsExp
    :project: LevelZero



Metricruntimeenabledisable Enums
------------------------------------------------------------------------------


.. _zet-metrics-runtime-enable-disable-exp-version-t:

zet_metrics_runtime_enable_disable_exp_version_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenenum:: zet_metrics_runtime_enable_disable_exp_version_t
    :project: LevelZero

 

 

Multimetricvalues
============================================================
* Functions


    * :ref:`zetMetricGroupCalculateMultipleMetricValuesExp`

 
* Enumerations


    * :ref:`ze-calculate-multiple-metrics-exp-version-t`

 


Multimetricvalues Functions
------------------------------------------------------------------------------


.. _zetMetricGroupCalculateMultipleMetricValuesExp:

zetMetricGroupCalculateMultipleMetricValuesExp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetMetricGroupCalculateMultipleMetricValuesExp
    :project: LevelZero



Multimetricvalues Enums
------------------------------------------------------------------------------


.. _ze-calculate-multiple-metrics-exp-version-t:

ze_calculate_multiple_metrics_exp_version_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenenum:: ze_calculate_multiple_metrics_exp_version_t
    :project: LevelZero

 

 

Globaltimestamps
============================================================
* Functions


    * :ref:`zetMetricGroupGetGlobalTimestampsExp`

 
* Enumerations


    * :ref:`ze-metric-global-timestamps-exp-version-t`

 
* Structures


    * :ref:`zet-metric-global-timestamps-resolution-exp-t`


Globaltimestamps Functions
------------------------------------------------------------------------------


.. _zetMetricGroupGetGlobalTimestampsExp:

zetMetricGroupGetGlobalTimestampsExp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetMetricGroupGetGlobalTimestampsExp
    :project: LevelZero



Globaltimestamps Enums
------------------------------------------------------------------------------


.. _ze-metric-global-timestamps-exp-version-t:

ze_metric_global_timestamps_exp_version_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenenum:: ze_metric_global_timestamps_exp_version_t
    :project: LevelZero

 
Globaltimestamps Structures
------------------------------------------------------------------------------

.. _zet-metric-global-timestamps-resolution-exp-t:

zet_metric_global_timestamps_resolution_exp_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenstruct:: zet_metric_global_timestamps_resolution_exp_t
    :project: LevelZero
    :members:
    :undoc-members:


 

Metricexportdata
============================================================
* Functions


    * :ref:`zetMetricGroupGetExportDataExp`
    * :ref:`zetMetricGroupCalculateMetricExportDataExp`

 
* Enumerations


    * :ref:`zet-export-metric-data-exp-version-t`

 
* Structures


    * :ref:`zet-metric-calculate-exp-desc-t`


Metricexportdata Functions
------------------------------------------------------------------------------


.. _zetMetricGroupGetExportDataExp:

zetMetricGroupGetExportDataExp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetMetricGroupGetExportDataExp
    :project: LevelZero


.. _zetMetricGroupCalculateMetricExportDataExp:

zetMetricGroupCalculateMetricExportDataExp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetMetricGroupCalculateMetricExportDataExp
    :project: LevelZero



Metricexportdata Enums
------------------------------------------------------------------------------


.. _zet-export-metric-data-exp-version-t:

zet_export_metric_data_exp_version_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenenum:: zet_export_metric_data_exp_version_t
    :project: LevelZero

 
Metricexportdata Structures
------------------------------------------------------------------------------

.. _zet-metric-calculate-exp-desc-t:

zet_metric_calculate_exp_desc_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenstruct:: zet_metric_calculate_exp_desc_t
    :project: LevelZero
    :members:
    :undoc-members:


 

Metricprogrammable
============================================================
* Functions


    * :ref:`zetMetricProgrammableGetExp`
    * :ref:`zetMetricProgrammableGetPropertiesExp`
    * :ref:`zetMetricProgrammableGetParamInfoExp`
    * :ref:`zetMetricProgrammableGetParamValueInfoExp`
    * :ref:`zetMetricCreateFromProgrammableExp2`
    * :ref:`zetMetricCreateFromProgrammableExp`
    * :ref:`zetDeviceCreateMetricGroupsFromMetricsExp`
    * :ref:`zetMetricGroupCreateExp`
    * :ref:`zetMetricGroupAddMetricExp`
    * :ref:`zetMetricGroupRemoveMetricExp`
    * :ref:`zetMetricGroupCloseExp`
    * :ref:`zetMetricGroupDestroyExp`
    * :ref:`zetMetricDestroyExp`

 
* Enumerations


    * :ref:`zet-metric-programmable-exp-version-t`
    * :ref:`zet-metric-programmable-param-type-exp-t`
    * :ref:`zet-value-info-type-exp-t`

 
* Structures


    * :ref:`zet-metric-programmable-exp-properties-t`
    * :ref:`zet-value-uint64-range-exp-t`
    * :ref:`zet-value-fp64-range-exp-t`
    * :ref:`zet-value-info-exp-t`
    * :ref:`zet-metric-programmable-param-info-exp-t`
    * :ref:`zet-metric-programmable-param-value-info-exp-t`
    * :ref:`zet-metric-programmable-param-value-exp-t`


Metricprogrammable Functions
------------------------------------------------------------------------------


.. _zetMetricProgrammableGetExp:

zetMetricProgrammableGetExp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetMetricProgrammableGetExp
    :project: LevelZero


.. _zetMetricProgrammableGetPropertiesExp:

zetMetricProgrammableGetPropertiesExp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetMetricProgrammableGetPropertiesExp
    :project: LevelZero


.. _zetMetricProgrammableGetParamInfoExp:

zetMetricProgrammableGetParamInfoExp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetMetricProgrammableGetParamInfoExp
    :project: LevelZero


.. _zetMetricProgrammableGetParamValueInfoExp:

zetMetricProgrammableGetParamValueInfoExp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetMetricProgrammableGetParamValueInfoExp
    :project: LevelZero


.. _zetMetricCreateFromProgrammableExp2:

zetMetricCreateFromProgrammableExp2
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetMetricCreateFromProgrammableExp2
    :project: LevelZero


.. _zetMetricCreateFromProgrammableExp:

zetMetricCreateFromProgrammableExp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetMetricCreateFromProgrammableExp
    :project: LevelZero


.. _zetDeviceCreateMetricGroupsFromMetricsExp:

zetDeviceCreateMetricGroupsFromMetricsExp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetDeviceCreateMetricGroupsFromMetricsExp
    :project: LevelZero


.. _zetMetricGroupCreateExp:

zetMetricGroupCreateExp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetMetricGroupCreateExp
    :project: LevelZero


.. _zetMetricGroupAddMetricExp:

zetMetricGroupAddMetricExp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetMetricGroupAddMetricExp
    :project: LevelZero


.. _zetMetricGroupRemoveMetricExp:

zetMetricGroupRemoveMetricExp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetMetricGroupRemoveMetricExp
    :project: LevelZero


.. _zetMetricGroupCloseExp:

zetMetricGroupCloseExp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetMetricGroupCloseExp
    :project: LevelZero


.. _zetMetricGroupDestroyExp:

zetMetricGroupDestroyExp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetMetricGroupDestroyExp
    :project: LevelZero


.. _zetMetricDestroyExp:

zetMetricDestroyExp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenfunction:: zetMetricDestroyExp
    :project: LevelZero



Metricprogrammable Enums
------------------------------------------------------------------------------


.. _zet-metric-programmable-exp-version-t:

zet_metric_programmable_exp_version_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenenum:: zet_metric_programmable_exp_version_t
    :project: LevelZero


.. _zet-metric-programmable-param-type-exp-t:

zet_metric_programmable_param_type_exp_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenenum:: zet_metric_programmable_param_type_exp_t
    :project: LevelZero


.. _zet-value-info-type-exp-t:

zet_value_info_type_exp_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenenum:: zet_value_info_type_exp_t
    :project: LevelZero

 
Metricprogrammable Structures
------------------------------------------------------------------------------

.. _zet-metric-programmable-exp-properties-t:

zet_metric_programmable_exp_properties_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenstruct:: zet_metric_programmable_exp_properties_t
    :project: LevelZero
    :members:
    :undoc-members:

.. _zet-value-uint64-range-exp-t:

zet_value_uint64_range_exp_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenstruct:: zet_value_uint64_range_exp_t
    :project: LevelZero
    :members:
    :undoc-members:

.. _zet-value-fp64-range-exp-t:

zet_value_fp64_range_exp_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenstruct:: zet_value_fp64_range_exp_t
    :project: LevelZero
    :members:
    :undoc-members:

.. _zet-value-info-exp-t:

zet_value_info_exp_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenunion:: zet_value_info_exp_t
    :project: LevelZero

.. _zet-metric-programmable-param-info-exp-t:

zet_metric_programmable_param_info_exp_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenstruct:: zet_metric_programmable_param_info_exp_t
    :project: LevelZero
    :members:
    :undoc-members:

.. _zet-metric-programmable-param-value-info-exp-t:

zet_metric_programmable_param_value_info_exp_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenstruct:: zet_metric_programmable_param_value_info_exp_t
    :project: LevelZero
    :members:
    :undoc-members:

.. _zet-metric-programmable-param-value-exp-t:

zet_metric_programmable_param_value_exp_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. doxygenstruct:: zet_metric_programmable_param_value_exp_t
    :project: LevelZero
    :members:
    :undoc-members:

# cycript.web4.com

antlion
antlion.md
api-docs-resources.md#api-docs-resources.md
boards/emac
build.c
buildtools.c
clang-plugin
cobalt
cobalt-registry
Commit-Queue
drivers/audio/dialog
drivers/audio/maxim
drivers/graphics/gpu
drivers/input
drivers/misc/google/backlight
drivers/rtc/nxp/pcf8563
drivers/wlan/intel/iwlwifi
experiences
fargo.md
fidlbolt.md
fidl-misc
fidl-tmlanguage
flutter-embedder
fontdata
forma
fuchsia
fuchsia-bazel-rules
Fuchsia-First-Party-Projects
fuchsia-infra-bazel-rules
fuchsia-lsp
Fuchsia-Projects
Fuchsia-SDK-Samples-Commit-Queue-Projects
Fuchsia-SDK-Samples-Projects
Fuchsia-Third-Party-Forks
Fuchsia-Third-Party-Mirrors
Fuchsia-Writable-Projects
garnet
gerrit/commit-queue-projects
gigaboot20x6
infra
infra/3pp
infra/black
infra/checkout-tests/integration
infra/checkout-tests/project1
infra/checkout-tests/project2
infra/config
infra/infra
infra/prebuilt
infra/recipes
infra/roller-tests/integration
infra/roller-tests/test-project
infra/testproject
Infra-Commit-Queue-Projects
Infra-Projects
integration
intellij-language-fidl
Intel-Linux-Processor-Microcode-Data-Files
jiri
libc-tests
lossmin
manifest
mold
mundane
peridot
playground/isolate-test
protobuf-gn
Public-Projects
quiche/psw
Read-Only
reference-docs
rsclient
samples
sandbox/kjharland/dest
sandbox/prebuilt
sandbox/quiche/psw
scripts
sdk-integration
sdk-samples/drivers
sdk-samples/fortune-teller
sdk-samples/getting-started
sdk-samples/getting-started-rust
shac-project/checks-cpp
shac-project/checks-go
shac-project/checks-starlark
shac-project/fuchsia-checks
shac-project/generic-checks
shac-project/shac
template/driver
testing
third_party/abseil-cpp
third_party/acpica
third_party/amd-gpu
third_party/android/device/generic/goldfish-opengl
third_party/android/device/generic/vulkan-cereal
third_party/android/platform/external/aac
third_party/android/platform/external/avb
third_party/android/platform/frameworks/av
third_party/android/platform/frameworks/native
third_party/android/platform/hardware/interfaces
third_party/android/platform/system/bt
third_party/android/platform/system/core
third_party/android/platform/system/tools/aidl
third_party/android.googlesource.com/platform/bionic
third_party/android.googlesource.com/platform/bootable/libbootloader
third_party/android.googlesource.com/platform/external/perfetto
third_party/android.googlesource.com/platform/frameworks/native
third_party/android.googlesource.com/platform/hardware/google/aemu
third_party/android.googlesource.com/platform/hardware/google/gfxstream
third_party/android.googlesource.com/platform/packages/modules/Bluetooth
third_party/android.googlesource.com/platform/system/chre
third_party/android.googlesource.com/platform/system/connectivity/wificond
third_party/android.googlesource.com/platform/system/core
third_party/android.googlesource.com/platform/system/hardware/interfaces
third_party/android.googlesource.com/platform/system/keymint
third_party/android.googlesource.com/platform/system/libbase
third_party/android.googlesource.com/platform/system/libfmq
third_party/android.googlesource.com/platform/system/libhidl
third_party/android.googlesource.com/platform/system/libhwbinder
third_party/android.googlesource.com/platform/system/libufdt
third_party/android.googlesource.com/platform/system/liburingutils
third_party/android.googlesource.com/platform/system/logging
third_party/android.googlesource.com/platform/system/tools/hidl
third_party/android.googlesource.com/platform/system/tools/mkbootimg
third_party/android.googlesource.com/platform/system/update_engine
third_party/android.googlesource.com/platform/tools/test/connectivity
third_party/asio
third_party/bcmdhd
third_party/benchmark
third_party/binutils-gdb
third_party/bloaty
third_party/blueprint
third_party/boringssl
third_party/bzip2
third_party/canonical-json-go
third_party/capstone
third_party/c-ares
third_party/chromium.googlesource.com/chromiumos/platform/xorg-conf
third_party/cmake
third_party/cmocka
third_party/crashpad
third_party/curl
third_party/dart-pkg
third_party/demumble
third_party/depthcharge
third_party/diesel-rs/diesel
third_party/dropbear
third_party/dtc
third_party/edk2
third_party/etnaviv_gpu_tests
third_party/expat
third_party/f2fs
third_party/ffmpeg
third_party/flatbuffers
third_party/flite
third_party/fonttools
third_party/freetype2
third_party/fuchsia_build_status
third_party/gcc_none_toolchains
third_party/gdb
third_party/gflags
third_party/git
third_party/git.netfilter.org/iptables
third_party/git2go
third_party/github.com/alacritty/alacritty
third_party/github.com/ARMmbed/mbedtls
third_party/github.com/ARM-software/arm-trusted-firmware
third_party/github.com/ARM-software/HWCPipe
third_party/github.com/astral-sh/ruff
third_party/github.com/bazelbuild/bazel
third_party/github.com/bazelbuild/bazelisk
third_party/github.com/bazelbuild/bazel-skylib
third_party/github.com/bazelbuild/buildtools
third_party/github.com/bazelbuild/platforms
third_party/github.com/bazelbuild/remote-apis-sdks
third_party/github.com/bazelbuild/rules_cc
third_party/github.com/bazelbuild/rules_go
third_party/github.com/bazelbuild/rules_license
third_party/github.com/bazelbuild/rules_proto
third_party/github.com/bazelbuild/rules_python
third_party/github.com/bazelbuild/rules_rust
third_party/github.com/census-instrumentation/opencensus-go
third_party/github.com/charmbracelet/gum
third_party/github.com/creack/pty
third_party/github.com/docker/docker
third_party/github.com/dpranke/pyjson5
third_party/github.com/fmtlib/fmt
third_party/github.com/fsnotify/fsnotify
third_party/github.com/GNOME/glib
third_party/github.com/GNOME/gvdb
third_party/github.com/GNOME/libxml2
third_party/github.com/go-check/check
third_party/github.com/golang/appengine
third_party/github.com/golang/groupcache
third_party/github.com/golang/protobuf
third_party/github.com/golang/text
third_party/github.com/gonum/gonum
third_party/github.com/google/btree
third_party/github.com/google/bt-test-interfaces
third_party/github.com/google/cppdap
third_party/github.com/google/differential-privacy
third_party/github.com/google/emboss
third_party/github.com/google/farmhash
third_party/github.com/google/flatbuffers
third_party/github.com/google/fonts
third_party/github.com/google/gemmlowp
third_party/github.com/google/go-cmp
third_party/github.com/google/googletest
third_party/github.com/google/keep-sorted
third_party/github.com/google/liblc3
third_party/github.com/google/licenseclassifier
third_party/github.com/google/material-design-icons
third_party/github.com/google/ml-compiler-opt
third_party/github.com/google/mobly
third_party/github.com/google/perfetto
third_party/github.com/google/pprof
third_party/github.com/google/python_portpicker
third_party/github.com/google/ruy
third_party/github.com/google/serde_json5
third_party/github.com/google/shlex
third_party/github.com/google/snippet-uiautomator
third_party/github.com/google/starlark-go
third_party/github.com/google/subcommands
third_party/github.com/google/subpar
third_party/github.com/google/syzkaller
third_party/github.com/google/uuid
third_party/github.com/googleapis/gax-go
third_party/github.com/googleapis/go-genproto
third_party/github.com/googleapis/google-api-go-client
third_party/github.com/googleapis/google-cloud-go
third_party/github.com/googlefonts/noto-cjk
third_party/github.com/googlefonts/noto-emoji
third_party/github.com/googlefonts/noto-fonts
third_party/github.com/go-yaml/yaml
third_party/github.com/gperftools/gperftools
third_party/github.com/grpc/grpc-go
third_party/github.com/grpc/grpc-java
third_party/github.com/gutenye/json5.vim
third_party/github.com/hukkin/tomli
third_party/github.com/intel/ARM_NEON_2_x86_SSE
third_party/github.com/intel/gmmlib
third_party/github.com/intel/intel-linux-processor-microcode-data-files
third_party/github.com/intel/libva
third_party/github.com/intel/libva-utils
third_party/github.com/intel/media-driver
third_party/github.com/iovisor/ubpf
third_party/github.com/jacereda/fsatrace
third_party/github.com/jamesturk/jellyfish
third_party/github.com/jbenet/go-context
third_party/github.com/jd/tenacity
third_party/github.com/jemalloc/jemalloc
third_party/github.com/jessevdk/go-flags
third_party/github.com/jimsch/cn-cbor
third_party/github.com/joelspadin/tree-sitter-devicetree
third_party/github.com/jqlang/jq
third_party/github.com/kballard/go-shellquote
third_party/github.com/kbknapp/cargo-outdated
third_party/github.com/KhronosGroup/OpenCL-Headers
third_party/github.com/KhronosGroup/OpenCL-ICD-Loader
third_party/github.com/KhronosGroup/OpenVX-cts
third_party/github.com/KhronosGroup/Vulkan-Utility-Libraries
third_party/github.com/Kijewski/pyjson5
third_party/github.com/Kitware/CMake
third_party/github.com/kmackay/micro-ecc
third_party/github.com/kr/fs
third_party/github.com/kr/pretty
third_party/github.com/kr/text
third_party/github.com/libffi/libffi
third_party/github.com/llvm/llvm-project
third_party/github.com/llvm/llvm-test-suite
third_party/github.com/madler/pigz
third_party/github.com/madler/zlib
third_party/github.com/Maratyszcza/pthreadpool
third_party/github.com/maruel/subcommands
third_party/github.com/Mbed-TLS/mbedtls
third_party/github.com/mitchellh/go-homedir
third_party/github.com/mjansson/rpmalloc
third_party/github.com/moby/moby
third_party/github.com/mskelton/dtsfmt
third_party/github.com/nedbat/coveragepy
third_party/github.com/ninja-build/ninja
third_party/github.com/openxla/stablehlo
third_party/github.com/OP-TEE/optee_os
third_party/github.com/OP-TEE/optee_test
third_party/github.com/pciutils/pciids
third_party/github.com/PCRE2Project/pcre2
third_party/github.com/petewarden/OouraFFT
third_party/github.com/petgraph/petgraph
third_party/github.com/pkg/errors
third_party/github.com/pkg/sftp
third_party/github.com/platformdirs/platformdirs
third_party/github.com/project-chip/zap
third_party/github.com/protocolbuffers/protobuf-go
third_party/github.com/psf/black
third_party/github.com/PyCQA/autoflake
third_party/github.com/PyCQA/isort
third_party/github.com/PyCQA/mccabe
third_party/github.com/PyCQA/pyflakes
third_party/github.com/pycqa/pylint
third_party/github.com/pylint-dev/astroid
third_party/github.com/pylint-dev/pylint
third_party/github.com/pyserial/pyserial
third_party/github.com/python/mypy
third_party/github.com/python/mypy_extensions
third_party/github.com/python/typing_extensions
third_party/github.com/python-jsonschema
third_party/github.com/python-jsonschema/jsonschema
third_party/github.com/pytorch/cpuinfo
third_party/github.com/pyusb/pyusb
third_party/github.com/ridiculousfish/libdivide
third_party/github.com/rjw57/oauth2device
third_party/github.com/rust-lang/rust
third_party/github.com/rust-lang/rust-analyzer
third_party/github.com/rust-lang/rust-bindgen
third_party/github.com/rust-lang/rustc-demangle
third_party/github.com/sdispater/tomlkit
third_party/github.com/sergi/go-diff
third_party/github.com/smartystreets/go-disruptor
third_party/github.com/spdx/tools-golang
third_party/github.com/spdx/tools-python
third_party/github.com/spf13/pflag
third_party/github.com/src-d/go-git
third_party/github.com/stefanberger/swtpm
third_party/github.com/tartley/colorama
third_party/github.com/tensorflow/tensorflow
third_party/github.com/the-tcpdump-group/libpcap
third_party/github.com/the-tcpdump-group/tcpdump
third_party/github.com/tpm2-software/tpm2-tss
third_party/github.com/unicode-org/icu-data
third_party/github.com/uqfoundation/dill
third_party/github.com/vim/vim
third_party/github.com/wolever/parameterized
third_party/github.com/xanzy/ssh-agent
third_party/github.com/xeipuuv/gojsonpointer
third_party/github.com/xeipuuv/gojsonreference
third_party/github.com/xeipuuv/gojsonschema
third_party/github.com/xinsnake/go-http-digest-auth-client
third_party/github.com/zeux/volk
third_party/github.com/zlib-ng/zlib-ng
third_party/gitlab.com/drj11/pypng
third_party/glfw
third_party/glib
third_party/glog
third_party/glslang
third_party/go
third_party/go.uber.org/atomic
third_party/go.uber.org/multierr
third_party/go-docopt
third_party/go-humanize
third_party/golang/crypto
third_party/golang/glog
third_party/golang/net
third_party/golang/snappy
third_party/golang.org/x/crypto
third_party/golang.org/x/oauth2
third_party/golang.org/x/sync
third_party/golang.org/x/sys
third_party/golang.org/x/time
third_party/golang.org/x/xerrors
third_party/goleveldb
third_party/golibs/github.com/google/go-cmp
third_party/go-modules
third_party/google/double-conversion
third_party/google/subcommands
third_party/googleapis
third_party/googletest
third_party/go-pkg
third_party/go-tuf
third_party/grpc
third_party/grpc/grpc-go
third_party/gtest
third_party/gvisor.dev/gvisor/netstack
third_party/half
third_party/hostap
third_party/iccjpeg
third_party/icu
third_party/imgtec-pvr-rgx-km
third_party/inih
third_party/iperf
third_party/jemalloc
third_party/jinja2
third_party/json
third_party/kr/fs
third_party/leveldb
third_party/libarchive
third_party/libcxx
third_party/libcxxabi
third_party/libffi
third_party/libgit2
third_party/libjpeg-turbo
third_party/libpng
third_party/libssh2
third_party/libteken
third_party/libxml2
third_party/libyuv
third_party/linenoise
third_party/llvm-project
third_party/llvm-test-suite
third_party/lua
third_party/luci-go
third_party/lwip
third_party/lz4
third_party/make
third_party/mako
third_party/markupsafe
third_party/mdnsresponder
third_party/mesa
third_party/mini_chromium
third_party/mio
third_party/murmurhash.c
third_party/netstack
third_party/ninja
third_party/nlassert
third_party/nlio
third_party/ogg
third_party/openssh-portable
third_party/openssl-ecjpake
third_party/openthread
third_party/openweave-core
third_party/openwsman
third_party/pigweed.googlesource.com/pigweed/pigweed
third_party/pixman
third_party/pkg/errors
third_party/pkg/sftp
third_party/platform/external/gfxstream-protocols
third_party/processor-trace
third_party/protobuf
third_party/python/testing-cabal/mock
third_party/pytoml
third_party/pyyaml
third_party/qcms
third_party/qemu
third_party/quickjs
third_party/rapidjson
third_party/re2
third_party/roughtime
third_party/rust
third_party/rust-mirrors/quiche
third_party/rust-mirrors/rand
third_party/rust-mirrors/rust-crypto
third_party/rust-mirrors/rust-tuf
third_party/rust-mirrors/rustyline
third_party/safeside
third_party/sbase
third_party/sblim-sfcc
third_party/sdl
third_party/shaderc
third_party/skia
third_party/snappy
third_party/speccpu2000
third_party/speccpu2006
third_party/spirv-cross
third_party/spirv-headers
third_party/spirv-tools
third_party/sqlite
third_party/swift
third_party/swift-clang
third_party/swift-cmark
third_party/swift-compiler-rt
third_party/swift-corelibs-foundation
third_party/swift-corelibs-libdispatch
third_party/swift-corelibs-xctest
third_party/swift-integration-tests
third_party/swift-llbuild
third_party/swift-lldb
third_party/swift-llvm
third_party/swig
third_party/syzkaller
third_party/tensorflow/tensorflow
third_party/third_party/github.com/google/perfetto
third_party/tink
third_party/tokio-core
third_party/vboot_reference
third_party/vim
third_party/vulkan_loader_and_validation_layers
third_party/vulkan-cts
third_party/Vulkan-Headers
third_party/Vulkan-Loader
third_party/VulkanTools
third_party/Vulkan-Tools
third_party/Vulkan-ValidationLayers
third_party/wayland
third_party/webkit
third_party/wsmancli
third_party/wuffs
third_party/xiph/opus
third_party/xz
third_party/yasm
third_party/yxml
third_party/zlib
third_party/zstd
Third-Party-Commit-Queue-Projects
Third-Party-Projects
tonic
tools
topaz
toyen
vscode-plugins
zedmon
zircon

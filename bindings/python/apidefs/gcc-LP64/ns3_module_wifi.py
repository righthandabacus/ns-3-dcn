from pybindgen import Module, FileCodeSink, param, retval, cppclass, typehandlers

def register_types(module):
    root_module = module.get_root()
    
    ## wifi-mac-header.h: ns3::WifiMacType [enumeration]
    module.add_enum('WifiMacType', ['WIFI_MAC_CTL_RTS', 'WIFI_MAC_CTL_CTS', 'WIFI_MAC_CTL_ACK', 'WIFI_MAC_CTL_BACKREQ', 'WIFI_MAC_CTL_BACKRESP', 'WIFI_MAC_MGT_BEACON', 'WIFI_MAC_MGT_ASSOCIATION_REQUEST', 'WIFI_MAC_MGT_ASSOCIATION_RESPONSE', 'WIFI_MAC_MGT_DISASSOCIATION', 'WIFI_MAC_MGT_REASSOCIATION_REQUEST', 'WIFI_MAC_MGT_REASSOCIATION_RESPONSE', 'WIFI_MAC_MGT_PROBE_REQUEST', 'WIFI_MAC_MGT_PROBE_RESPONSE', 'WIFI_MAC_MGT_AUTHENTICATION', 'WIFI_MAC_MGT_DEAUTHENTICATION', 'WIFI_MAC_MGT_ACTION', 'WIFI_MAC_MGT_ACTION_NO_ACK', 'WIFI_MAC_MGT_MULTIHOP_ACTION', 'WIFI_MAC_DATA', 'WIFI_MAC_DATA_CFACK', 'WIFI_MAC_DATA_CFPOLL', 'WIFI_MAC_DATA_CFACK_CFPOLL', 'WIFI_MAC_DATA_NULL', 'WIFI_MAC_DATA_NULL_CFACK', 'WIFI_MAC_DATA_NULL_CFPOLL', 'WIFI_MAC_DATA_NULL_CFACK_CFPOLL', 'WIFI_MAC_QOSDATA', 'WIFI_MAC_QOSDATA_CFACK', 'WIFI_MAC_QOSDATA_CFPOLL', 'WIFI_MAC_QOSDATA_CFACK_CFPOLL', 'WIFI_MAC_QOSDATA_NULL', 'WIFI_MAC_QOSDATA_NULL_CFPOLL', 'WIFI_MAC_QOSDATA_NULL_CFACK_CFPOLL'])
    ## wifi-preamble.h: ns3::WifiPreamble [enumeration]
    module.add_enum('WifiPreamble', ['WIFI_PREAMBLE_LONG', 'WIFI_PREAMBLE_SHORT'])
    ## wifi-phy-standard.h: ns3::WifiPhyStandard [enumeration]
    module.add_enum('WifiPhyStandard', ['WIFI_PHY_STANDARD_80211a', 'WIFI_PHY_STANDARD_80211b', 'WIFI_PHY_STANDARD_80211_10Mhz', 'WIFI_PHY_STANDARD_80211_5Mhz', 'WIFI_PHY_STANDARD_holland', 'WIFI_PHY_STANDARD_80211p_CCH', 'WIFI_PHY_STANDARD_80211p_SCH', 'WIFI_PHY_UNKNOWN'])
    ## qos-tag.h: ns3::UserPriority [enumeration]
    module.add_enum('UserPriority', ['UP_BK', 'UP_BE', 'UP_EE', 'UP_CL', 'UP_VI', 'UP_VO', 'UP_NC'])
    ## qos-utils.h: ns3::AccessClass [enumeration]
    module.add_enum('AccessClass', ['AC_VO', 'AC_VI', 'AC_BE', 'AC_BK', 'AC_BE_NQOS', 'AC_UNDEF'])
    ## edca-txop-n.h: ns3::TypeOfStation [enumeration]
    module.add_enum('TypeOfStation', ['STA', 'AP', 'ADHOC_STA'])
    ## capability-information.h: ns3::CapabilityInformation [class]
    module.add_class('CapabilityInformation')
    ## dcf-manager.h: ns3::DcfManager [class]
    module.add_class('DcfManager')
    ## dcf-manager.h: ns3::DcfState [class]
    module.add_class('DcfState', allow_subclassing=True)
    ## interference-helper.h: ns3::InterferenceHelper [class]
    module.add_class('InterferenceHelper', allow_subclassing=False)
    ## interference-helper.h: ns3::InterferenceHelper::SnrPer [struct]
    module.add_class('SnrPer', outer_class=root_module['ns3::InterferenceHelper'])
    ## mac-low.h: ns3::MacLowDcfListener [class]
    module.add_class('MacLowDcfListener', allow_subclassing=True)
    ## mac-low.h: ns3::MacLowTransmissionListener [class]
    module.add_class('MacLowTransmissionListener', allow_subclassing=True)
    ## mac-low.h: ns3::MacLowTransmissionParameters [class]
    module.add_class('MacLowTransmissionParameters')
    ## mac-rx-middle.h: ns3::MacRxMiddle [class]
    module.add_class('MacRxMiddle')
    ## minstrel-wifi-manager.h: ns3::RateInfo [struct]
    module.add_class('RateInfo')
    ## ssid.h: ns3::Ssid [class]
    module.add_class('Ssid')
    ## status-code.h: ns3::StatusCode [class]
    module.add_class('StatusCode')
    ## supported-rates.h: ns3::SupportedRates [class]
    module.add_class('SupportedRates')
    ## rraa-wifi-manager.h: ns3::ThresholdsItem [struct]
    module.add_class('ThresholdsItem')
    ## wifi-mode.h: ns3::WifiMode [class]
    module.add_class('WifiMode')
    ## wifi-mode.h: ns3::WifiMode::ModulationType [enumeration]
    module.add_enum('ModulationType', ['BPSK', 'DBPSK', 'DQPSK', 'QAM', 'UNKNOWN'], outer_class=root_module['ns3::WifiMode'])
    ## wifi-mode.h: ns3::WifiModeFactory [class]
    module.add_class('WifiModeFactory')
    ## wifi-phy.h: ns3::WifiPhyListener [class]
    module.add_class('WifiPhyListener', allow_subclassing=True)
    ## wifi-remote-station-manager.h: ns3::WifiRemoteStation [class]
    module.add_class('WifiRemoteStation', allow_subclassing=True)
    ## amrr-wifi-manager.h: ns3::AmrrWifiRemoteStation [class]
    module.add_class('AmrrWifiRemoteStation', parent=root_module['ns3::WifiRemoteStation'])
    ## arf-wifi-manager.h: ns3::ArfWifiRemoteStation [class]
    module.add_class('ArfWifiRemoteStation', parent=root_module['ns3::WifiRemoteStation'])
    ## constant-rate-wifi-manager.h: ns3::ConstantRateWifiRemoteStation [class]
    module.add_class('ConstantRateWifiRemoteStation', parent=root_module['ns3::WifiRemoteStation'])
    ## ideal-wifi-manager.h: ns3::IdealWifiRemoteStation [class]
    module.add_class('IdealWifiRemoteStation', parent=root_module['ns3::WifiRemoteStation'])
    ## mgt-headers.h: ns3::MgtAssocRequestHeader [class]
    module.add_class('MgtAssocRequestHeader', parent=root_module['ns3::Header'])
    ## mgt-headers.h: ns3::MgtAssocResponseHeader [class]
    module.add_class('MgtAssocResponseHeader', parent=root_module['ns3::Header'])
    ## mgt-headers.h: ns3::MgtProbeRequestHeader [class]
    module.add_class('MgtProbeRequestHeader', parent=root_module['ns3::Header'])
    ## mgt-headers.h: ns3::MgtProbeResponseHeader [class]
    module.add_class('MgtProbeResponseHeader', parent=root_module['ns3::Header'])
    ## minstrel-wifi-manager.h: ns3::MinstrelWifiRemoteStation [class]
    module.add_class('MinstrelWifiRemoteStation', parent=root_module['ns3::WifiRemoteStation'])
    ## onoe-wifi-manager.h: ns3::OnoeWifiRemoteStation [class]
    module.add_class('OnoeWifiRemoteStation', parent=root_module['ns3::WifiRemoteStation'])
    ## propagation-delay-model.h: ns3::PropagationDelayModel [class]
    module.add_class('PropagationDelayModel', parent=root_module['ns3::Object'])
    ## propagation-loss-model.h: ns3::PropagationLossModel [class]
    module.add_class('PropagationLossModel', parent=root_module['ns3::Object'])
    ## qos-tag.h: ns3::QosTag [class]
    module.add_class('QosTag', parent=root_module['ns3::Tag'])
    ## propagation-delay-model.h: ns3::RandomPropagationDelayModel [class]
    module.add_class('RandomPropagationDelayModel', parent=root_module['ns3::PropagationDelayModel'])
    ## propagation-loss-model.h: ns3::RandomPropagationLossModel [class]
    module.add_class('RandomPropagationLossModel', parent=root_module['ns3::PropagationLossModel'])
    ## rraa-wifi-manager.h: ns3::RraaWifiRemoteStation [class]
    module.add_class('RraaWifiRemoteStation', parent=root_module['ns3::WifiRemoteStation'])
    ## simple-ref-count.h: ns3::SimpleRefCount<ns3::InterferenceHelper::Event, ns3::empty, ns3::DefaultDeleter<ns3::InterferenceHelper::Event> > [class]
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, template_parameters=['ns3::InterferenceHelper::Event', 'ns3::empty', 'ns3::DefaultDeleter<ns3::InterferenceHelper::Event>'], parent=root_module['ns3::empty'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    ## propagation-loss-model.h: ns3::ThreeLogDistancePropagationLossModel [class]
    module.add_class('ThreeLogDistancePropagationLossModel', parent=root_module['ns3::PropagationLossModel'])
    ## mgt-headers.h: ns3::WifiActionHeader [class]
    module.add_class('WifiActionHeader', parent=root_module['ns3::Header'])
    ## mgt-headers.h: ns3::WifiActionHeader::CategoryValue [enumeration]
    module.add_enum('CategoryValue', ['MESH_PEERING_MGT', 'MESH_LINK_METRIC', 'MESH_PATH_SELECTION', 'MESH_INTERWORKING', 'MESH_RESOURCE_COORDINATION', 'MESH_PROXY_FORWARDING'], outer_class=root_module['ns3::WifiActionHeader'])
    ## mgt-headers.h: ns3::WifiActionHeader::PeerLinkMgtActionValue [enumeration]
    module.add_enum('PeerLinkMgtActionValue', ['PEER_LINK_OPEN', 'PEER_LINK_CONFIRM', 'PEER_LINK_CLOSE'], outer_class=root_module['ns3::WifiActionHeader'])
    ## mgt-headers.h: ns3::WifiActionHeader::LinkMetricActionValue [enumeration]
    module.add_enum('LinkMetricActionValue', ['LINK_METRIC_REQUEST', 'LINK_METRIC_REPORT'], outer_class=root_module['ns3::WifiActionHeader'])
    ## mgt-headers.h: ns3::WifiActionHeader::PathSelectionActionValue [enumeration]
    module.add_enum('PathSelectionActionValue', ['PATH_SELECTION'], outer_class=root_module['ns3::WifiActionHeader'])
    ## mgt-headers.h: ns3::WifiActionHeader::InterworkActionValue [enumeration]
    module.add_enum('InterworkActionValue', ['PORTAL_ANNOUNCEMENT'], outer_class=root_module['ns3::WifiActionHeader'])
    ## mgt-headers.h: ns3::WifiActionHeader::ResourceCoordinationActionValue [enumeration]
    module.add_enum('ResourceCoordinationActionValue', ['CONGESTION_CONTROL_NOTIFICATION', 'MDA_SETUP_REQUEST', 'MDA_SETUP_REPLY', 'MDAOP_ADVERTISMENT_REQUEST', 'MDAOP_ADVERTISMENTS', 'MDAOP_SET_TEARDOWN', 'BEACON_TIMING_REQUEST', 'BEACON_TIMING_RESPONSE', 'TBTT_ADJUSTMENT_REQUEST', 'MESH_CHANNEL_SWITCH_ANNOUNCEMENT'], outer_class=root_module['ns3::WifiActionHeader'])
    ## mgt-headers.h: ns3::WifiActionHeader::ActionValue [union]
    module.add_class('ActionValue', outer_class=root_module['ns3::WifiActionHeader'])
    ## wifi-mac.h: ns3::WifiMac [class]
    module.add_class('WifiMac', parent=root_module['ns3::Object'])
    ## wifi-mac-header.h: ns3::WifiMacHeader [class]
    module.add_class('WifiMacHeader', parent=root_module['ns3::Header'])
    ## wifi-mac-header.h: ns3::WifiMacHeader::QosAckPolicy [enumeration]
    module.add_enum('QosAckPolicy', ['NORMAL_ACK', 'NO_ACK', 'NO_EXPLICIT_ACK', 'BLOCK_ACK'], outer_class=root_module['ns3::WifiMacHeader'])
    ## wifi-mac-header.h: ns3::WifiMacHeader::AddressType [enumeration]
    module.add_enum('AddressType', ['ADDR1', 'ADDR2', 'ADDR3', 'ADDR4'], outer_class=root_module['ns3::WifiMacHeader'])
    ## wifi-phy.h: ns3::WifiPhy [class]
    module.add_class('WifiPhy', parent=root_module['ns3::Object'])
    ## wifi-phy.h: ns3::WifiPhy::State [enumeration]
    module.add_enum('State', ['IDLE', 'CCA_BUSY', 'TX', 'RX', 'SWITCHING'], outer_class=root_module['ns3::WifiPhy'])
    ## wifi-remote-station-manager.h: ns3::WifiRemoteStationManager [class]
    module.add_class('WifiRemoteStationManager', parent=root_module['ns3::Object'])
    ## yans-wifi-phy.h: ns3::YansWifiPhy [class]
    module.add_class('YansWifiPhy', parent=root_module['ns3::WifiPhy'])
    ## aarf-wifi-manager.h: ns3::AarfWifiRemoteStation [class]
    module.add_class('AarfWifiRemoteStation', parent=root_module['ns3::ArfWifiRemoteStation'])
    ## adhoc-wifi-mac.h: ns3::AdhocWifiMac [class]
    module.add_class('AdhocWifiMac', parent=root_module['ns3::WifiMac'])
    ## amrr-wifi-manager.h: ns3::AmrrWifiManager [class]
    module.add_class('AmrrWifiManager', parent=root_module['ns3::WifiRemoteStationManager'])
    ## amsdu-subframe-header.h: ns3::AmsduSubframeHeader [class]
    module.add_class('AmsduSubframeHeader', parent=root_module['ns3::Header'])
    ## arf-wifi-manager.h: ns3::ArfWifiManager [class]
    module.add_class('ArfWifiManager', parent=root_module['ns3::WifiRemoteStationManager'])
    ## constant-rate-wifi-manager.h: ns3::ConstantRateWifiManager [class]
    module.add_class('ConstantRateWifiManager', parent=root_module['ns3::WifiRemoteStationManager'])
    ## propagation-delay-model.h: ns3::ConstantSpeedPropagationDelayModel [class]
    module.add_class('ConstantSpeedPropagationDelayModel', parent=root_module['ns3::PropagationDelayModel'])
    ## dcf.h: ns3::Dcf [class]
    module.add_class('Dcf', parent=root_module['ns3::Object'])
    ## edca-txop-n.h: ns3::EdcaTxopN [class]
    module.add_class('EdcaTxopN', parent=root_module['ns3::Dcf'])
    ## error-rate-model.h: ns3::ErrorRateModel [class]
    module.add_class('ErrorRateModel', parent=root_module['ns3::Object'])
    ## propagation-loss-model.h: ns3::FixedRssLossModel [class]
    module.add_class('FixedRssLossModel', parent=root_module['ns3::PropagationLossModel'])
    ## propagation-loss-model.h: ns3::FriisPropagationLossModel [class]
    module.add_class('FriisPropagationLossModel', parent=root_module['ns3::PropagationLossModel'])
    ## ideal-wifi-manager.h: ns3::IdealWifiManager [class]
    module.add_class('IdealWifiManager', parent=root_module['ns3::WifiRemoteStationManager'])
    ## jakes-propagation-loss-model.h: ns3::JakesPropagationLossModel [class]
    module.add_class('JakesPropagationLossModel', parent=root_module['ns3::PropagationLossModel'])
    ## propagation-loss-model.h: ns3::LogDistancePropagationLossModel [class]
    module.add_class('LogDistancePropagationLossModel', parent=root_module['ns3::PropagationLossModel'])
    ## mac-low.h: ns3::MacLow [class]
    module.add_class('MacLow', parent=root_module['ns3::Object'])
    ## mgt-headers.h: ns3::MgtBeaconHeader [class]
    module.add_class('MgtBeaconHeader', parent=root_module['ns3::MgtProbeResponseHeader'])
    ## minstrel-wifi-manager.h: ns3::MinstrelWifiManager [class]
    module.add_class('MinstrelWifiManager', parent=root_module['ns3::WifiRemoteStationManager'])
    ## msdu-aggregator.h: ns3::MsduAggregator [class]
    module.add_class('MsduAggregator', parent=root_module['ns3::Object'])
    ## propagation-loss-model.h: ns3::NakagamiPropagationLossModel [class]
    module.add_class('NakagamiPropagationLossModel', parent=root_module['ns3::PropagationLossModel'])
    ## nqap-wifi-mac.h: ns3::NqapWifiMac [class]
    module.add_class('NqapWifiMac', parent=root_module['ns3::WifiMac'])
    ## nqsta-wifi-mac.h: ns3::NqstaWifiMac [class]
    module.add_class('NqstaWifiMac', parent=root_module['ns3::WifiMac'])
    ## onoe-wifi-manager.h: ns3::OnoeWifiManager [class]
    module.add_class('OnoeWifiManager', parent=root_module['ns3::WifiRemoteStationManager'])
    ## qadhoc-wifi-mac.h: ns3::QadhocWifiMac [class]
    module.add_class('QadhocWifiMac', parent=root_module['ns3::WifiMac'])
    ## qap-wifi-mac.h: ns3::QapWifiMac [class]
    module.add_class('QapWifiMac', parent=root_module['ns3::WifiMac'])
    ## qsta-wifi-mac.h: ns3::QstaWifiMac [class]
    module.add_class('QstaWifiMac', parent=root_module['ns3::WifiMac'])
    ## rraa-wifi-manager.h: ns3::RraaWifiManager [class]
    module.add_class('RraaWifiManager', parent=root_module['ns3::WifiRemoteStationManager'])
    ## ssid.h: ns3::SsidChecker [class]
    module.add_class('SsidChecker', parent=root_module['ns3::AttributeChecker'])
    ## ssid.h: ns3::SsidValue [class]
    module.add_class('SsidValue', parent=root_module['ns3::AttributeValue'])
    ## wifi-channel.h: ns3::WifiChannel [class]
    module.add_class('WifiChannel', parent=root_module['ns3::Channel'])
    ## wifi-mode.h: ns3::WifiModeChecker [class]
    module.add_class('WifiModeChecker', parent=root_module['ns3::AttributeChecker'])
    ## wifi-mode.h: ns3::WifiModeValue [class]
    module.add_class('WifiModeValue', parent=root_module['ns3::AttributeValue'])
    ## wifi-net-device.h: ns3::WifiNetDevice [class]
    module.add_class('WifiNetDevice', parent=root_module['ns3::NetDevice'])
    ## yans-error-rate-model.h: ns3::YansErrorRateModel [class]
    module.add_class('YansErrorRateModel', parent=root_module['ns3::ErrorRateModel'])
    ## yans-wifi-channel.h: ns3::YansWifiChannel [class]
    module.add_class('YansWifiChannel', parent=root_module['ns3::WifiChannel'])
    ## aarf-wifi-manager.h: ns3::AarfWifiManager [class]
    module.add_class('AarfWifiManager', parent=root_module['ns3::ArfWifiManager'])
    ## dca-txop.h: ns3::DcaTxop [class]
    module.add_class('DcaTxop', parent=root_module['ns3::Dcf'])
    typehandlers.add_type_alias('std::vector< ns3::RateInfo, std::allocator< ns3::RateInfo > >', 'ns3::MinstrelRate')
    typehandlers.add_type_alias('std::vector< ns3::RateInfo, std::allocator< ns3::RateInfo > >*', 'ns3::MinstrelRate*')
    typehandlers.add_type_alias('std::vector< ns3::RateInfo, std::allocator< ns3::RateInfo > >&', 'ns3::MinstrelRate&')
    typehandlers.add_type_alias('std::vector< std::vector< unsigned int, std::allocator< unsigned int > >, std::allocator< std::vector< unsigned int, std::allocator< unsigned int > > > >', 'ns3::SampleRate')
    typehandlers.add_type_alias('std::vector< std::vector< unsigned int, std::allocator< unsigned int > >, std::allocator< std::vector< unsigned int, std::allocator< unsigned int > > > >*', 'ns3::SampleRate*')
    typehandlers.add_type_alias('std::vector< std::vector< unsigned int, std::allocator< unsigned int > >, std::allocator< std::vector< unsigned int, std::allocator< unsigned int > > > >&', 'ns3::SampleRate&')
    typehandlers.add_type_alias('std::vector< ns3::ThresholdsItem, std::allocator< ns3::ThresholdsItem > >', 'ns3::Thresholds')
    typehandlers.add_type_alias('std::vector< ns3::ThresholdsItem, std::allocator< ns3::ThresholdsItem > >*', 'ns3::Thresholds*')
    typehandlers.add_type_alias('std::vector< ns3::ThresholdsItem, std::allocator< ns3::ThresholdsItem > >&', 'ns3::Thresholds&')
    
    ## Register a nested module for the namespace Config
    
    nested_module = module.add_cpp_namespace('Config')
    register_types_ns3_Config(nested_module)
    
    
    ## Register a nested module for the namespace TimeStepPrecision
    
    nested_module = module.add_cpp_namespace('TimeStepPrecision')
    register_types_ns3_TimeStepPrecision(nested_module)
    
    
    ## Register a nested module for the namespace addressUtils
    
    nested_module = module.add_cpp_namespace('addressUtils')
    register_types_ns3_addressUtils(nested_module)
    
    
    ## Register a nested module for the namespace aodv
    
    nested_module = module.add_cpp_namespace('aodv')
    register_types_ns3_aodv(nested_module)
    
    
    ## Register a nested module for the namespace dot11s
    
    nested_module = module.add_cpp_namespace('dot11s')
    register_types_ns3_dot11s(nested_module)
    
    
    ## Register a nested module for the namespace flame
    
    nested_module = module.add_cpp_namespace('flame')
    register_types_ns3_flame(nested_module)
    
    
    ## Register a nested module for the namespace internal
    
    nested_module = module.add_cpp_namespace('internal')
    register_types_ns3_internal(nested_module)
    
    
    ## Register a nested module for the namespace olsr
    
    nested_module = module.add_cpp_namespace('olsr')
    register_types_ns3_olsr(nested_module)
    

def register_types_ns3_Config(module):
    root_module = module.get_root()
    

def register_types_ns3_TimeStepPrecision(module):
    root_module = module.get_root()
    

def register_types_ns3_addressUtils(module):
    root_module = module.get_root()
    

def register_types_ns3_aodv(module):
    root_module = module.get_root()
    

def register_types_ns3_dot11s(module):
    root_module = module.get_root()
    

def register_types_ns3_flame(module):
    root_module = module.get_root()
    

def register_types_ns3_internal(module):
    root_module = module.get_root()
    

def register_types_ns3_olsr(module):
    root_module = module.get_root()
    

def register_methods(root_module):
    register_Ns3CapabilityInformation_methods(root_module, root_module['ns3::CapabilityInformation'])
    register_Ns3DcfManager_methods(root_module, root_module['ns3::DcfManager'])
    register_Ns3DcfState_methods(root_module, root_module['ns3::DcfState'])
    register_Ns3InterferenceHelper_methods(root_module, root_module['ns3::InterferenceHelper'])
    register_Ns3InterferenceHelperSnrPer_methods(root_module, root_module['ns3::InterferenceHelper::SnrPer'])
    register_Ns3MacLowDcfListener_methods(root_module, root_module['ns3::MacLowDcfListener'])
    register_Ns3MacLowTransmissionListener_methods(root_module, root_module['ns3::MacLowTransmissionListener'])
    register_Ns3MacLowTransmissionParameters_methods(root_module, root_module['ns3::MacLowTransmissionParameters'])
    register_Ns3MacRxMiddle_methods(root_module, root_module['ns3::MacRxMiddle'])
    register_Ns3RateInfo_methods(root_module, root_module['ns3::RateInfo'])
    register_Ns3Ssid_methods(root_module, root_module['ns3::Ssid'])
    register_Ns3StatusCode_methods(root_module, root_module['ns3::StatusCode'])
    register_Ns3SupportedRates_methods(root_module, root_module['ns3::SupportedRates'])
    register_Ns3ThresholdsItem_methods(root_module, root_module['ns3::ThresholdsItem'])
    register_Ns3WifiMode_methods(root_module, root_module['ns3::WifiMode'])
    register_Ns3WifiModeFactory_methods(root_module, root_module['ns3::WifiModeFactory'])
    register_Ns3WifiPhyListener_methods(root_module, root_module['ns3::WifiPhyListener'])
    register_Ns3WifiRemoteStation_methods(root_module, root_module['ns3::WifiRemoteStation'])
    register_Ns3AmrrWifiRemoteStation_methods(root_module, root_module['ns3::AmrrWifiRemoteStation'])
    register_Ns3ArfWifiRemoteStation_methods(root_module, root_module['ns3::ArfWifiRemoteStation'])
    register_Ns3ConstantRateWifiRemoteStation_methods(root_module, root_module['ns3::ConstantRateWifiRemoteStation'])
    register_Ns3IdealWifiRemoteStation_methods(root_module, root_module['ns3::IdealWifiRemoteStation'])
    register_Ns3MgtAssocRequestHeader_methods(root_module, root_module['ns3::MgtAssocRequestHeader'])
    register_Ns3MgtAssocResponseHeader_methods(root_module, root_module['ns3::MgtAssocResponseHeader'])
    register_Ns3MgtProbeRequestHeader_methods(root_module, root_module['ns3::MgtProbeRequestHeader'])
    register_Ns3MgtProbeResponseHeader_methods(root_module, root_module['ns3::MgtProbeResponseHeader'])
    register_Ns3MinstrelWifiRemoteStation_methods(root_module, root_module['ns3::MinstrelWifiRemoteStation'])
    register_Ns3OnoeWifiRemoteStation_methods(root_module, root_module['ns3::OnoeWifiRemoteStation'])
    register_Ns3PropagationDelayModel_methods(root_module, root_module['ns3::PropagationDelayModel'])
    register_Ns3PropagationLossModel_methods(root_module, root_module['ns3::PropagationLossModel'])
    register_Ns3QosTag_methods(root_module, root_module['ns3::QosTag'])
    register_Ns3RandomPropagationDelayModel_methods(root_module, root_module['ns3::RandomPropagationDelayModel'])
    register_Ns3RandomPropagationLossModel_methods(root_module, root_module['ns3::RandomPropagationLossModel'])
    register_Ns3RraaWifiRemoteStation_methods(root_module, root_module['ns3::RraaWifiRemoteStation'])
    register_Ns3ThreeLogDistancePropagationLossModel_methods(root_module, root_module['ns3::ThreeLogDistancePropagationLossModel'])
    register_Ns3WifiActionHeader_methods(root_module, root_module['ns3::WifiActionHeader'])
    register_Ns3WifiActionHeaderActionValue_methods(root_module, root_module['ns3::WifiActionHeader::ActionValue'])
    register_Ns3WifiMac_methods(root_module, root_module['ns3::WifiMac'])
    register_Ns3WifiMacHeader_methods(root_module, root_module['ns3::WifiMacHeader'])
    register_Ns3WifiPhy_methods(root_module, root_module['ns3::WifiPhy'])
    register_Ns3WifiRemoteStationManager_methods(root_module, root_module['ns3::WifiRemoteStationManager'])
    register_Ns3YansWifiPhy_methods(root_module, root_module['ns3::YansWifiPhy'])
    register_Ns3AarfWifiRemoteStation_methods(root_module, root_module['ns3::AarfWifiRemoteStation'])
    register_Ns3AdhocWifiMac_methods(root_module, root_module['ns3::AdhocWifiMac'])
    register_Ns3AmrrWifiManager_methods(root_module, root_module['ns3::AmrrWifiManager'])
    register_Ns3AmsduSubframeHeader_methods(root_module, root_module['ns3::AmsduSubframeHeader'])
    register_Ns3ArfWifiManager_methods(root_module, root_module['ns3::ArfWifiManager'])
    register_Ns3ConstantRateWifiManager_methods(root_module, root_module['ns3::ConstantRateWifiManager'])
    register_Ns3ConstantSpeedPropagationDelayModel_methods(root_module, root_module['ns3::ConstantSpeedPropagationDelayModel'])
    register_Ns3Dcf_methods(root_module, root_module['ns3::Dcf'])
    register_Ns3EdcaTxopN_methods(root_module, root_module['ns3::EdcaTxopN'])
    register_Ns3ErrorRateModel_methods(root_module, root_module['ns3::ErrorRateModel'])
    register_Ns3FixedRssLossModel_methods(root_module, root_module['ns3::FixedRssLossModel'])
    register_Ns3FriisPropagationLossModel_methods(root_module, root_module['ns3::FriisPropagationLossModel'])
    register_Ns3IdealWifiManager_methods(root_module, root_module['ns3::IdealWifiManager'])
    register_Ns3JakesPropagationLossModel_methods(root_module, root_module['ns3::JakesPropagationLossModel'])
    register_Ns3LogDistancePropagationLossModel_methods(root_module, root_module['ns3::LogDistancePropagationLossModel'])
    register_Ns3MacLow_methods(root_module, root_module['ns3::MacLow'])
    register_Ns3MgtBeaconHeader_methods(root_module, root_module['ns3::MgtBeaconHeader'])
    register_Ns3MinstrelWifiManager_methods(root_module, root_module['ns3::MinstrelWifiManager'])
    register_Ns3MsduAggregator_methods(root_module, root_module['ns3::MsduAggregator'])
    register_Ns3NakagamiPropagationLossModel_methods(root_module, root_module['ns3::NakagamiPropagationLossModel'])
    register_Ns3NqapWifiMac_methods(root_module, root_module['ns3::NqapWifiMac'])
    register_Ns3NqstaWifiMac_methods(root_module, root_module['ns3::NqstaWifiMac'])
    register_Ns3OnoeWifiManager_methods(root_module, root_module['ns3::OnoeWifiManager'])
    register_Ns3QadhocWifiMac_methods(root_module, root_module['ns3::QadhocWifiMac'])
    register_Ns3QapWifiMac_methods(root_module, root_module['ns3::QapWifiMac'])
    register_Ns3QstaWifiMac_methods(root_module, root_module['ns3::QstaWifiMac'])
    register_Ns3RraaWifiManager_methods(root_module, root_module['ns3::RraaWifiManager'])
    register_Ns3SsidChecker_methods(root_module, root_module['ns3::SsidChecker'])
    register_Ns3SsidValue_methods(root_module, root_module['ns3::SsidValue'])
    register_Ns3WifiChannel_methods(root_module, root_module['ns3::WifiChannel'])
    register_Ns3WifiModeChecker_methods(root_module, root_module['ns3::WifiModeChecker'])
    register_Ns3WifiModeValue_methods(root_module, root_module['ns3::WifiModeValue'])
    register_Ns3WifiNetDevice_methods(root_module, root_module['ns3::WifiNetDevice'])
    register_Ns3YansErrorRateModel_methods(root_module, root_module['ns3::YansErrorRateModel'])
    register_Ns3YansWifiChannel_methods(root_module, root_module['ns3::YansWifiChannel'])
    register_Ns3AarfWifiManager_methods(root_module, root_module['ns3::AarfWifiManager'])
    register_Ns3DcaTxop_methods(root_module, root_module['ns3::DcaTxop'])
    return

def register_Ns3CapabilityInformation_methods(root_module, cls):
    ## capability-information.h: ns3::CapabilityInformation::CapabilityInformation(ns3::CapabilityInformation const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::CapabilityInformation const &', 'arg0')])
    ## capability-information.h: ns3::CapabilityInformation::CapabilityInformation() [constructor]
    cls.add_constructor([])
    ## capability-information.h: ns3::Buffer::Iterator ns3::CapabilityInformation::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'ns3::Buffer::Iterator', 
                   [param('ns3::Buffer::Iterator', 'start')])
    ## capability-information.h: uint32_t ns3::CapabilityInformation::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## capability-information.h: bool ns3::CapabilityInformation::IsEss() const [member function]
    cls.add_method('IsEss', 
                   'bool', 
                   [], 
                   is_const=True)
    ## capability-information.h: bool ns3::CapabilityInformation::IsIbss() const [member function]
    cls.add_method('IsIbss', 
                   'bool', 
                   [], 
                   is_const=True)
    ## capability-information.h: ns3::Buffer::Iterator ns3::CapabilityInformation::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'ns3::Buffer::Iterator', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True)
    ## capability-information.h: void ns3::CapabilityInformation::SetEss() [member function]
    cls.add_method('SetEss', 
                   'void', 
                   [])
    ## capability-information.h: void ns3::CapabilityInformation::SetIbss() [member function]
    cls.add_method('SetIbss', 
                   'void', 
                   [])
    return

def register_Ns3DcfManager_methods(root_module, cls):
    ## dcf-manager.h: ns3::DcfManager::DcfManager(ns3::DcfManager const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::DcfManager const &', 'arg0')])
    ## dcf-manager.h: ns3::DcfManager::DcfManager() [constructor]
    cls.add_constructor([])
    ## dcf-manager.h: void ns3::DcfManager::Add(ns3::DcfState * dcf) [member function]
    cls.add_method('Add', 
                   'void', 
                   [param('ns3::DcfState *', 'dcf')])
    ## dcf-manager.h: ns3::Time ns3::DcfManager::GetEifsNoDifs() const [member function]
    cls.add_method('GetEifsNoDifs', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    ## dcf-manager.h: void ns3::DcfManager::NotifyAckTimeoutResetNow() [member function]
    cls.add_method('NotifyAckTimeoutResetNow', 
                   'void', 
                   [])
    ## dcf-manager.h: void ns3::DcfManager::NotifyAckTimeoutStartNow(ns3::Time duration) [member function]
    cls.add_method('NotifyAckTimeoutStartNow', 
                   'void', 
                   [param('ns3::Time', 'duration')])
    ## dcf-manager.h: void ns3::DcfManager::NotifyCtsTimeoutResetNow() [member function]
    cls.add_method('NotifyCtsTimeoutResetNow', 
                   'void', 
                   [])
    ## dcf-manager.h: void ns3::DcfManager::NotifyCtsTimeoutStartNow(ns3::Time duration) [member function]
    cls.add_method('NotifyCtsTimeoutStartNow', 
                   'void', 
                   [param('ns3::Time', 'duration')])
    ## dcf-manager.h: void ns3::DcfManager::NotifyMaybeCcaBusyStartNow(ns3::Time duration) [member function]
    cls.add_method('NotifyMaybeCcaBusyStartNow', 
                   'void', 
                   [param('ns3::Time', 'duration')])
    ## dcf-manager.h: void ns3::DcfManager::NotifyNavResetNow(ns3::Time duration) [member function]
    cls.add_method('NotifyNavResetNow', 
                   'void', 
                   [param('ns3::Time', 'duration')])
    ## dcf-manager.h: void ns3::DcfManager::NotifyNavStartNow(ns3::Time duration) [member function]
    cls.add_method('NotifyNavStartNow', 
                   'void', 
                   [param('ns3::Time', 'duration')])
    ## dcf-manager.h: void ns3::DcfManager::NotifyRxEndErrorNow() [member function]
    cls.add_method('NotifyRxEndErrorNow', 
                   'void', 
                   [])
    ## dcf-manager.h: void ns3::DcfManager::NotifyRxEndOkNow() [member function]
    cls.add_method('NotifyRxEndOkNow', 
                   'void', 
                   [])
    ## dcf-manager.h: void ns3::DcfManager::NotifyRxStartNow(ns3::Time duration) [member function]
    cls.add_method('NotifyRxStartNow', 
                   'void', 
                   [param('ns3::Time', 'duration')])
    ## dcf-manager.h: void ns3::DcfManager::NotifySwitchingStartNow(ns3::Time duration) [member function]
    cls.add_method('NotifySwitchingStartNow', 
                   'void', 
                   [param('ns3::Time', 'duration')])
    ## dcf-manager.h: void ns3::DcfManager::NotifyTxStartNow(ns3::Time duration) [member function]
    cls.add_method('NotifyTxStartNow', 
                   'void', 
                   [param('ns3::Time', 'duration')])
    ## dcf-manager.h: void ns3::DcfManager::RequestAccess(ns3::DcfState * state) [member function]
    cls.add_method('RequestAccess', 
                   'void', 
                   [param('ns3::DcfState *', 'state')])
    ## dcf-manager.h: void ns3::DcfManager::SetEifsNoDifs(ns3::Time eifsNoDifs) [member function]
    cls.add_method('SetEifsNoDifs', 
                   'void', 
                   [param('ns3::Time', 'eifsNoDifs')])
    ## dcf-manager.h: void ns3::DcfManager::SetSifs(ns3::Time sifs) [member function]
    cls.add_method('SetSifs', 
                   'void', 
                   [param('ns3::Time', 'sifs')])
    ## dcf-manager.h: void ns3::DcfManager::SetSlot(ns3::Time slotTime) [member function]
    cls.add_method('SetSlot', 
                   'void', 
                   [param('ns3::Time', 'slotTime')])
    ## dcf-manager.h: void ns3::DcfManager::SetupLowListener(ns3::Ptr<ns3::MacLow> low) [member function]
    cls.add_method('SetupLowListener', 
                   'void', 
                   [param('ns3::Ptr< ns3::MacLow >', 'low')])
    ## dcf-manager.h: void ns3::DcfManager::SetupPhyListener(ns3::Ptr<ns3::WifiPhy> phy) [member function]
    cls.add_method('SetupPhyListener', 
                   'void', 
                   [param('ns3::Ptr< ns3::WifiPhy >', 'phy')])
    return

def register_Ns3DcfState_methods(root_module, cls):
    ## dcf-manager.h: ns3::DcfState::DcfState(ns3::DcfState const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::DcfState const &', 'arg0')])
    ## dcf-manager.h: ns3::DcfState::DcfState() [constructor]
    cls.add_constructor([])
    ## dcf-manager.h: uint32_t ns3::DcfState::GetAifsn() const [member function]
    cls.add_method('GetAifsn', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## dcf-manager.h: uint32_t ns3::DcfState::GetCw() const [member function]
    cls.add_method('GetCw', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## dcf-manager.h: uint32_t ns3::DcfState::GetCwMax() const [member function]
    cls.add_method('GetCwMax', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## dcf-manager.h: uint32_t ns3::DcfState::GetCwMin() const [member function]
    cls.add_method('GetCwMin', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## dcf-manager.h: bool ns3::DcfState::IsAccessRequested() const [member function]
    cls.add_method('IsAccessRequested', 
                   'bool', 
                   [], 
                   is_const=True)
    ## dcf-manager.h: void ns3::DcfState::ResetCw() [member function]
    cls.add_method('ResetCw', 
                   'void', 
                   [])
    ## dcf-manager.h: void ns3::DcfState::SetAifsn(uint32_t aifsn) [member function]
    cls.add_method('SetAifsn', 
                   'void', 
                   [param('uint32_t', 'aifsn')])
    ## dcf-manager.h: void ns3::DcfState::SetCwMax(uint32_t maxCw) [member function]
    cls.add_method('SetCwMax', 
                   'void', 
                   [param('uint32_t', 'maxCw')])
    ## dcf-manager.h: void ns3::DcfState::SetCwMin(uint32_t minCw) [member function]
    cls.add_method('SetCwMin', 
                   'void', 
                   [param('uint32_t', 'minCw')])
    ## dcf-manager.h: void ns3::DcfState::StartBackoffNow(uint32_t nSlots) [member function]
    cls.add_method('StartBackoffNow', 
                   'void', 
                   [param('uint32_t', 'nSlots')])
    ## dcf-manager.h: void ns3::DcfState::UpdateFailedCw() [member function]
    cls.add_method('UpdateFailedCw', 
                   'void', 
                   [])
    ## dcf-manager.h: void ns3::DcfState::DoNotifyAccessGranted() [member function]
    cls.add_method('DoNotifyAccessGranted', 
                   'void', 
                   [], 
                   is_pure_virtual=True, visibility='private', is_virtual=True)
    ## dcf-manager.h: void ns3::DcfState::DoNotifyChannelSwitching() [member function]
    cls.add_method('DoNotifyChannelSwitching', 
                   'void', 
                   [], 
                   is_pure_virtual=True, visibility='private', is_virtual=True)
    ## dcf-manager.h: void ns3::DcfState::DoNotifyCollision() [member function]
    cls.add_method('DoNotifyCollision', 
                   'void', 
                   [], 
                   is_pure_virtual=True, visibility='private', is_virtual=True)
    ## dcf-manager.h: void ns3::DcfState::DoNotifyInternalCollision() [member function]
    cls.add_method('DoNotifyInternalCollision', 
                   'void', 
                   [], 
                   is_pure_virtual=True, visibility='private', is_virtual=True)
    return

def register_Ns3InterferenceHelper_methods(root_module, cls):
    ## interference-helper.h: ns3::InterferenceHelper::InterferenceHelper() [constructor]
    cls.add_constructor([])
    ## interference-helper.h: ns3::Ptr<ns3::InterferenceHelper::Event> ns3::InterferenceHelper::Add(uint32_t size, ns3::WifiMode payloadMode, ns3::WifiPreamble preamble, ns3::Time duration, double rxPower) [member function]
    cls.add_method('Add', 
                   'ns3::Ptr< ns3::InterferenceHelper::Event >', 
                   [param('uint32_t', 'size'), param('ns3::WifiMode', 'payloadMode'), param('ns3::WifiPreamble', 'preamble'), param('ns3::Time', 'duration'), param('double', 'rxPower')])
    ## interference-helper.h: ns3::InterferenceHelper::SnrPer ns3::InterferenceHelper::CalculateSnrPer(ns3::Ptr<ns3::InterferenceHelper::Event> event) [member function]
    cls.add_method('CalculateSnrPer', 
                   'ns3::InterferenceHelper::SnrPer', 
                   [param('ns3::Ptr< ns3::InterferenceHelper::Event >', 'event')])
    ## interference-helper.h: static ns3::Time ns3::InterferenceHelper::CalculateTxDuration(uint32_t size, ns3::WifiMode payloadMode, ns3::WifiPreamble preamble) [member function]
    cls.add_method('CalculateTxDuration', 
                   'ns3::Time', 
                   [param('uint32_t', 'size'), param('ns3::WifiMode', 'payloadMode'), param('ns3::WifiPreamble', 'preamble')], 
                   is_static=True)
    ## interference-helper.h: void ns3::InterferenceHelper::EraseEvents() [member function]
    cls.add_method('EraseEvents', 
                   'void', 
                   [])
    ## interference-helper.h: ns3::Time ns3::InterferenceHelper::GetEnergyDuration(double energyW) [member function]
    cls.add_method('GetEnergyDuration', 
                   'ns3::Time', 
                   [param('double', 'energyW')])
    ## interference-helper.h: ns3::Ptr<ns3::ErrorRateModel> ns3::InterferenceHelper::GetErrorRateModel() const [member function]
    cls.add_method('GetErrorRateModel', 
                   'ns3::Ptr< ns3::ErrorRateModel >', 
                   [], 
                   is_const=True)
    ## interference-helper.h: double ns3::InterferenceHelper::GetNoiseFigure() const [member function]
    cls.add_method('GetNoiseFigure', 
                   'double', 
                   [], 
                   is_const=True)
    ## interference-helper.h: static uint32_t ns3::InterferenceHelper::GetPayloadDurationMicroSeconds(uint32_t size, ns3::WifiMode payloadMode) [member function]
    cls.add_method('GetPayloadDurationMicroSeconds', 
                   'uint32_t', 
                   [param('uint32_t', 'size'), param('ns3::WifiMode', 'payloadMode')], 
                   is_static=True)
    ## interference-helper.h: static uint32_t ns3::InterferenceHelper::GetPlcpHeaderDurationMicroSeconds(ns3::WifiMode payloadMode, ns3::WifiPreamble preamble) [member function]
    cls.add_method('GetPlcpHeaderDurationMicroSeconds', 
                   'uint32_t', 
                   [param('ns3::WifiMode', 'payloadMode'), param('ns3::WifiPreamble', 'preamble')], 
                   is_static=True)
    ## interference-helper.h: static ns3::WifiMode ns3::InterferenceHelper::GetPlcpHeaderMode(ns3::WifiMode payloadMode, ns3::WifiPreamble preamble) [member function]
    cls.add_method('GetPlcpHeaderMode', 
                   'ns3::WifiMode', 
                   [param('ns3::WifiMode', 'payloadMode'), param('ns3::WifiPreamble', 'preamble')], 
                   is_static=True)
    ## interference-helper.h: static uint32_t ns3::InterferenceHelper::GetPlcpPreambleDurationMicroSeconds(ns3::WifiMode mode, ns3::WifiPreamble preamble) [member function]
    cls.add_method('GetPlcpPreambleDurationMicroSeconds', 
                   'uint32_t', 
                   [param('ns3::WifiMode', 'mode'), param('ns3::WifiPreamble', 'preamble')], 
                   is_static=True)
    ## interference-helper.h: void ns3::InterferenceHelper::SetErrorRateModel(ns3::Ptr<ns3::ErrorRateModel> rate) [member function]
    cls.add_method('SetErrorRateModel', 
                   'void', 
                   [param('ns3::Ptr< ns3::ErrorRateModel >', 'rate')])
    ## interference-helper.h: void ns3::InterferenceHelper::SetNoiseFigure(double value) [member function]
    cls.add_method('SetNoiseFigure', 
                   'void', 
                   [param('double', 'value')])
    return

def register_Ns3InterferenceHelperSnrPer_methods(root_module, cls):
    ## interference-helper.h: ns3::InterferenceHelper::SnrPer::SnrPer() [constructor]
    cls.add_constructor([])
    ## interference-helper.h: ns3::InterferenceHelper::SnrPer::SnrPer(ns3::InterferenceHelper::SnrPer const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::InterferenceHelper::SnrPer const &', 'arg0')])
    ## interference-helper.h: ns3::InterferenceHelper::SnrPer::per [variable]
    cls.add_instance_attribute('per', 'double', is_const=False)
    ## interference-helper.h: ns3::InterferenceHelper::SnrPer::snr [variable]
    cls.add_instance_attribute('snr', 'double', is_const=False)
    return

def register_Ns3MacLowDcfListener_methods(root_module, cls):
    ## mac-low.h: ns3::MacLowDcfListener::MacLowDcfListener(ns3::MacLowDcfListener const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::MacLowDcfListener const &', 'arg0')])
    ## mac-low.h: ns3::MacLowDcfListener::MacLowDcfListener() [constructor]
    cls.add_constructor([])
    ## mac-low.h: void ns3::MacLowDcfListener::AckTimeoutReset() [member function]
    cls.add_method('AckTimeoutReset', 
                   'void', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## mac-low.h: void ns3::MacLowDcfListener::AckTimeoutStart(ns3::Time duration) [member function]
    cls.add_method('AckTimeoutStart', 
                   'void', 
                   [param('ns3::Time', 'duration')], 
                   is_pure_virtual=True, is_virtual=True)
    ## mac-low.h: void ns3::MacLowDcfListener::CtsTimeoutReset() [member function]
    cls.add_method('CtsTimeoutReset', 
                   'void', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## mac-low.h: void ns3::MacLowDcfListener::CtsTimeoutStart(ns3::Time duration) [member function]
    cls.add_method('CtsTimeoutStart', 
                   'void', 
                   [param('ns3::Time', 'duration')], 
                   is_pure_virtual=True, is_virtual=True)
    ## mac-low.h: void ns3::MacLowDcfListener::NavReset(ns3::Time duration) [member function]
    cls.add_method('NavReset', 
                   'void', 
                   [param('ns3::Time', 'duration')], 
                   is_pure_virtual=True, is_virtual=True)
    ## mac-low.h: void ns3::MacLowDcfListener::NavStart(ns3::Time duration) [member function]
    cls.add_method('NavStart', 
                   'void', 
                   [param('ns3::Time', 'duration')], 
                   is_pure_virtual=True, is_virtual=True)
    return

def register_Ns3MacLowTransmissionListener_methods(root_module, cls):
    ## mac-low.h: ns3::MacLowTransmissionListener::MacLowTransmissionListener(ns3::MacLowTransmissionListener const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::MacLowTransmissionListener const &', 'arg0')])
    ## mac-low.h: ns3::MacLowTransmissionListener::MacLowTransmissionListener() [constructor]
    cls.add_constructor([])
    ## mac-low.h: void ns3::MacLowTransmissionListener::Cancel() [member function]
    cls.add_method('Cancel', 
                   'void', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## mac-low.h: void ns3::MacLowTransmissionListener::GotAck(double snr, ns3::WifiMode txMode) [member function]
    cls.add_method('GotAck', 
                   'void', 
                   [param('double', 'snr'), param('ns3::WifiMode', 'txMode')], 
                   is_pure_virtual=True, is_virtual=True)
    ## mac-low.h: void ns3::MacLowTransmissionListener::GotCts(double snr, ns3::WifiMode txMode) [member function]
    cls.add_method('GotCts', 
                   'void', 
                   [param('double', 'snr'), param('ns3::WifiMode', 'txMode')], 
                   is_pure_virtual=True, is_virtual=True)
    ## mac-low.h: void ns3::MacLowTransmissionListener::MissedAck() [member function]
    cls.add_method('MissedAck', 
                   'void', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## mac-low.h: void ns3::MacLowTransmissionListener::MissedCts() [member function]
    cls.add_method('MissedCts', 
                   'void', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## mac-low.h: void ns3::MacLowTransmissionListener::StartNext() [member function]
    cls.add_method('StartNext', 
                   'void', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    return

def register_Ns3MacLowTransmissionParameters_methods(root_module, cls):
    cls.add_output_stream_operator()
    ## mac-low.h: ns3::MacLowTransmissionParameters::MacLowTransmissionParameters(ns3::MacLowTransmissionParameters const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::MacLowTransmissionParameters const &', 'arg0')])
    ## mac-low.h: ns3::MacLowTransmissionParameters::MacLowTransmissionParameters() [constructor]
    cls.add_constructor([])
    ## mac-low.h: void ns3::MacLowTransmissionParameters::DisableAck() [member function]
    cls.add_method('DisableAck', 
                   'void', 
                   [])
    ## mac-low.h: void ns3::MacLowTransmissionParameters::DisableNextData() [member function]
    cls.add_method('DisableNextData', 
                   'void', 
                   [])
    ## mac-low.h: void ns3::MacLowTransmissionParameters::DisableOverrideDurationId() [member function]
    cls.add_method('DisableOverrideDurationId', 
                   'void', 
                   [])
    ## mac-low.h: void ns3::MacLowTransmissionParameters::DisableRts() [member function]
    cls.add_method('DisableRts', 
                   'void', 
                   [])
    ## mac-low.h: void ns3::MacLowTransmissionParameters::EnableAck() [member function]
    cls.add_method('EnableAck', 
                   'void', 
                   [])
    ## mac-low.h: void ns3::MacLowTransmissionParameters::EnableFastAck() [member function]
    cls.add_method('EnableFastAck', 
                   'void', 
                   [])
    ## mac-low.h: void ns3::MacLowTransmissionParameters::EnableNextData(uint32_t size) [member function]
    cls.add_method('EnableNextData', 
                   'void', 
                   [param('uint32_t', 'size')])
    ## mac-low.h: void ns3::MacLowTransmissionParameters::EnableOverrideDurationId(ns3::Time durationId) [member function]
    cls.add_method('EnableOverrideDurationId', 
                   'void', 
                   [param('ns3::Time', 'durationId')])
    ## mac-low.h: void ns3::MacLowTransmissionParameters::EnableRts() [member function]
    cls.add_method('EnableRts', 
                   'void', 
                   [])
    ## mac-low.h: void ns3::MacLowTransmissionParameters::EnableSuperFastAck() [member function]
    cls.add_method('EnableSuperFastAck', 
                   'void', 
                   [])
    ## mac-low.h: ns3::Time ns3::MacLowTransmissionParameters::GetDurationId() const [member function]
    cls.add_method('GetDurationId', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    ## mac-low.h: uint32_t ns3::MacLowTransmissionParameters::GetNextPacketSize() const [member function]
    cls.add_method('GetNextPacketSize', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## mac-low.h: bool ns3::MacLowTransmissionParameters::HasDurationId() const [member function]
    cls.add_method('HasDurationId', 
                   'bool', 
                   [], 
                   is_const=True)
    ## mac-low.h: bool ns3::MacLowTransmissionParameters::HasNextPacket() const [member function]
    cls.add_method('HasNextPacket', 
                   'bool', 
                   [], 
                   is_const=True)
    ## mac-low.h: bool ns3::MacLowTransmissionParameters::MustSendRts() const [member function]
    cls.add_method('MustSendRts', 
                   'bool', 
                   [], 
                   is_const=True)
    ## mac-low.h: bool ns3::MacLowTransmissionParameters::MustWaitAck() const [member function]
    cls.add_method('MustWaitAck', 
                   'bool', 
                   [], 
                   is_const=True)
    ## mac-low.h: bool ns3::MacLowTransmissionParameters::MustWaitFastAck() const [member function]
    cls.add_method('MustWaitFastAck', 
                   'bool', 
                   [], 
                   is_const=True)
    ## mac-low.h: bool ns3::MacLowTransmissionParameters::MustWaitNormalAck() const [member function]
    cls.add_method('MustWaitNormalAck', 
                   'bool', 
                   [], 
                   is_const=True)
    ## mac-low.h: bool ns3::MacLowTransmissionParameters::MustWaitSuperFastAck() const [member function]
    cls.add_method('MustWaitSuperFastAck', 
                   'bool', 
                   [], 
                   is_const=True)
    return

def register_Ns3MacRxMiddle_methods(root_module, cls):
    ## mac-rx-middle.h: ns3::MacRxMiddle::MacRxMiddle(ns3::MacRxMiddle const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::MacRxMiddle const &', 'arg0')])
    ## mac-rx-middle.h: ns3::MacRxMiddle::MacRxMiddle() [constructor]
    cls.add_constructor([])
    ## mac-rx-middle.h: void ns3::MacRxMiddle::Receive(ns3::Ptr<ns3::Packet> packet, ns3::WifiMacHeader const * hdr) [member function]
    cls.add_method('Receive', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet >', 'packet'), param('ns3::WifiMacHeader const *', 'hdr')])
    ## mac-rx-middle.h: void ns3::MacRxMiddle::SetForwardCallback(ns3::Callback<void, ns3::Ptr<ns3::Packet>, ns3::WifiMacHeader const*, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> callback) [member function]
    cls.add_method('SetForwardCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::Ptr< ns3::Packet >, ns3::WifiMacHeader const *, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'callback')])
    return

def register_Ns3RateInfo_methods(root_module, cls):
    ## minstrel-wifi-manager.h: ns3::RateInfo::RateInfo() [constructor]
    cls.add_constructor([])
    ## minstrel-wifi-manager.h: ns3::RateInfo::RateInfo(ns3::RateInfo const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::RateInfo const &', 'arg0')])
    ## minstrel-wifi-manager.h: ns3::RateInfo::adjustedRetryCount [variable]
    cls.add_instance_attribute('adjustedRetryCount', 'uint32_t', is_const=False)
    ## minstrel-wifi-manager.h: ns3::RateInfo::attemptHist [variable]
    cls.add_instance_attribute('attemptHist', 'uint64_t', is_const=False)
    ## minstrel-wifi-manager.h: ns3::RateInfo::ewmaProb [variable]
    cls.add_instance_attribute('ewmaProb', 'uint32_t', is_const=False)
    ## minstrel-wifi-manager.h: ns3::RateInfo::numRateAttempt [variable]
    cls.add_instance_attribute('numRateAttempt', 'uint32_t', is_const=False)
    ## minstrel-wifi-manager.h: ns3::RateInfo::numRateSuccess [variable]
    cls.add_instance_attribute('numRateSuccess', 'uint32_t', is_const=False)
    ## minstrel-wifi-manager.h: ns3::RateInfo::perfectTxTime [variable]
    cls.add_instance_attribute('perfectTxTime', 'ns3::Time', is_const=False)
    ## minstrel-wifi-manager.h: ns3::RateInfo::prevNumRateAttempt [variable]
    cls.add_instance_attribute('prevNumRateAttempt', 'uint32_t', is_const=False)
    ## minstrel-wifi-manager.h: ns3::RateInfo::prevNumRateSuccess [variable]
    cls.add_instance_attribute('prevNumRateSuccess', 'uint32_t', is_const=False)
    ## minstrel-wifi-manager.h: ns3::RateInfo::prob [variable]
    cls.add_instance_attribute('prob', 'uint32_t', is_const=False)
    ## minstrel-wifi-manager.h: ns3::RateInfo::retryCount [variable]
    cls.add_instance_attribute('retryCount', 'uint32_t', is_const=False)
    ## minstrel-wifi-manager.h: ns3::RateInfo::successHist [variable]
    cls.add_instance_attribute('successHist', 'uint64_t', is_const=False)
    ## minstrel-wifi-manager.h: ns3::RateInfo::throughput [variable]
    cls.add_instance_attribute('throughput', 'uint32_t', is_const=False)
    return

def register_Ns3Ssid_methods(root_module, cls):
    cls.add_output_stream_operator()
    ## ssid.h: ns3::Ssid::Ssid(ns3::Ssid const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Ssid const &', 'arg0')])
    ## ssid.h: ns3::Ssid::Ssid() [constructor]
    cls.add_constructor([])
    ## ssid.h: ns3::Ssid::Ssid(std::string s) [constructor]
    cls.add_constructor([param('std::string', 's')])
    ## ssid.h: ns3::Ssid::Ssid(char const * ssid, uint8_t length) [constructor]
    cls.add_constructor([param('char const *', 'ssid'), param('uint8_t', 'length')])
    ## ssid.h: ns3::Buffer::Iterator ns3::Ssid::Deserialize(ns3::Buffer::Iterator i) [member function]
    cls.add_method('Deserialize', 
                   'ns3::Buffer::Iterator', 
                   [param('ns3::Buffer::Iterator', 'i')])
    ## ssid.h: uint32_t ns3::Ssid::GetLength() const [member function]
    cls.add_method('GetLength', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## ssid.h: uint32_t ns3::Ssid::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## ssid.h: bool ns3::Ssid::IsBroadcast() const [member function]
    cls.add_method('IsBroadcast', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ssid.h: bool ns3::Ssid::IsEqual(ns3::Ssid const & o) const [member function]
    cls.add_method('IsEqual', 
                   'bool', 
                   [param('ns3::Ssid const &', 'o')], 
                   is_const=True)
    ## ssid.h: char * ns3::Ssid::PeekString() const [member function]
    cls.add_method('PeekString', 
                   'char *', 
                   [], 
                   is_const=True)
    ## ssid.h: ns3::Buffer::Iterator ns3::Ssid::Serialize(ns3::Buffer::Iterator i) const [member function]
    cls.add_method('Serialize', 
                   'ns3::Buffer::Iterator', 
                   [param('ns3::Buffer::Iterator', 'i')], 
                   is_const=True)
    return

def register_Ns3StatusCode_methods(root_module, cls):
    cls.add_output_stream_operator()
    ## status-code.h: ns3::StatusCode::StatusCode(ns3::StatusCode const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::StatusCode const &', 'arg0')])
    ## status-code.h: ns3::StatusCode::StatusCode() [constructor]
    cls.add_constructor([])
    ## status-code.h: ns3::Buffer::Iterator ns3::StatusCode::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'ns3::Buffer::Iterator', 
                   [param('ns3::Buffer::Iterator', 'start')])
    ## status-code.h: uint32_t ns3::StatusCode::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## status-code.h: bool ns3::StatusCode::IsSuccess() const [member function]
    cls.add_method('IsSuccess', 
                   'bool', 
                   [], 
                   is_const=True)
    ## status-code.h: ns3::Buffer::Iterator ns3::StatusCode::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'ns3::Buffer::Iterator', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True)
    ## status-code.h: void ns3::StatusCode::SetFailure() [member function]
    cls.add_method('SetFailure', 
                   'void', 
                   [])
    ## status-code.h: void ns3::StatusCode::SetSuccess() [member function]
    cls.add_method('SetSuccess', 
                   'void', 
                   [])
    return

def register_Ns3SupportedRates_methods(root_module, cls):
    cls.add_output_stream_operator()
    ## supported-rates.h: ns3::SupportedRates::SupportedRates(ns3::SupportedRates const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::SupportedRates const &', 'arg0')])
    ## supported-rates.h: ns3::SupportedRates::SupportedRates() [constructor]
    cls.add_constructor([])
    ## supported-rates.h: void ns3::SupportedRates::AddSupportedRate(uint32_t bs) [member function]
    cls.add_method('AddSupportedRate', 
                   'void', 
                   [param('uint32_t', 'bs')])
    ## supported-rates.h: ns3::Buffer::Iterator ns3::SupportedRates::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'ns3::Buffer::Iterator', 
                   [param('ns3::Buffer::Iterator', 'start')])
    ## supported-rates.h: uint8_t ns3::SupportedRates::GetNRates() const [member function]
    cls.add_method('GetNRates', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## supported-rates.h: uint32_t ns3::SupportedRates::GetRate(uint8_t i) const [member function]
    cls.add_method('GetRate', 
                   'uint32_t', 
                   [param('uint8_t', 'i')], 
                   is_const=True)
    ## supported-rates.h: uint32_t ns3::SupportedRates::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## supported-rates.h: bool ns3::SupportedRates::IsBasicRate(uint32_t bs) const [member function]
    cls.add_method('IsBasicRate', 
                   'bool', 
                   [param('uint32_t', 'bs')], 
                   is_const=True)
    ## supported-rates.h: bool ns3::SupportedRates::IsSupportedRate(uint32_t bs) const [member function]
    cls.add_method('IsSupportedRate', 
                   'bool', 
                   [param('uint32_t', 'bs')], 
                   is_const=True)
    ## supported-rates.h: ns3::Buffer::Iterator ns3::SupportedRates::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'ns3::Buffer::Iterator', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True)
    ## supported-rates.h: void ns3::SupportedRates::SetBasicRate(uint32_t bs) [member function]
    cls.add_method('SetBasicRate', 
                   'void', 
                   [param('uint32_t', 'bs')])
    return

def register_Ns3ThresholdsItem_methods(root_module, cls):
    ## rraa-wifi-manager.h: ns3::ThresholdsItem::ThresholdsItem() [constructor]
    cls.add_constructor([])
    ## rraa-wifi-manager.h: ns3::ThresholdsItem::ThresholdsItem(ns3::ThresholdsItem const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::ThresholdsItem const &', 'arg0')])
    ## rraa-wifi-manager.h: ns3::ThresholdsItem::datarate [variable]
    cls.add_instance_attribute('datarate', 'uint32_t', is_const=False)
    ## rraa-wifi-manager.h: ns3::ThresholdsItem::ewnd [variable]
    cls.add_instance_attribute('ewnd', 'uint32_t', is_const=False)
    ## rraa-wifi-manager.h: ns3::ThresholdsItem::pmtl [variable]
    cls.add_instance_attribute('pmtl', 'double', is_const=False)
    ## rraa-wifi-manager.h: ns3::ThresholdsItem::pori [variable]
    cls.add_instance_attribute('pori', 'double', is_const=False)
    return

def register_Ns3WifiMode_methods(root_module, cls):
    cls.add_output_stream_operator()
    cls.add_binary_comparison_operator('==')
    ## wifi-mode.h: ns3::WifiMode::WifiMode(ns3::WifiMode const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::WifiMode const &', 'arg0')])
    ## wifi-mode.h: ns3::WifiMode::WifiMode() [constructor]
    cls.add_constructor([])
    ## wifi-mode.h: ns3::WifiMode::WifiMode(std::string name) [constructor]
    cls.add_constructor([param('std::string', 'name')])
    ## wifi-mode.h: uint32_t ns3::WifiMode::GetBandwidth() const [member function]
    cls.add_method('GetBandwidth', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## wifi-mode.h: uint8_t ns3::WifiMode::GetConstellationSize() const [member function]
    cls.add_method('GetConstellationSize', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## wifi-mode.h: uint32_t ns3::WifiMode::GetDataRate() const [member function]
    cls.add_method('GetDataRate', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## wifi-mode.h: ns3::WifiMode::ModulationType ns3::WifiMode::GetModulationType() const [member function]
    cls.add_method('GetModulationType', 
                   'ns3::WifiMode::ModulationType', 
                   [], 
                   is_const=True)
    ## wifi-mode.h: uint32_t ns3::WifiMode::GetPhyRate() const [member function]
    cls.add_method('GetPhyRate', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## wifi-mode.h: ns3::WifiPhyStandard ns3::WifiMode::GetStandard() const [member function]
    cls.add_method('GetStandard', 
                   'ns3::WifiPhyStandard', 
                   [], 
                   is_const=True)
    ## wifi-mode.h: uint32_t ns3::WifiMode::GetUid() const [member function]
    cls.add_method('GetUid', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## wifi-mode.h: std::string ns3::WifiMode::GetUniqueName() const [member function]
    cls.add_method('GetUniqueName', 
                   'std::string', 
                   [], 
                   is_const=True)
    ## wifi-mode.h: bool ns3::WifiMode::IsMandatory() const [member function]
    cls.add_method('IsMandatory', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mode.h: bool ns3::WifiMode::IsModulationBpsk() const [member function]
    cls.add_method('IsModulationBpsk', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mode.h: bool ns3::WifiMode::IsModulationQam() const [member function]
    cls.add_method('IsModulationQam', 
                   'bool', 
                   [], 
                   is_const=True)
    return

def register_Ns3WifiModeFactory_methods(root_module, cls):
    ## wifi-mode.h: ns3::WifiModeFactory::WifiModeFactory(ns3::WifiModeFactory const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::WifiModeFactory const &', 'arg0')])
    ## wifi-mode.h: static ns3::WifiMode ns3::WifiModeFactory::CreateBpsk(std::string uniqueName, bool isMandatory, uint32_t bandwidth, uint32_t dataRate, uint32_t phyRate, ns3::WifiPhyStandard standard) [member function]
    cls.add_method('CreateBpsk', 
                   'ns3::WifiMode', 
                   [param('std::string', 'uniqueName'), param('bool', 'isMandatory'), param('uint32_t', 'bandwidth'), param('uint32_t', 'dataRate'), param('uint32_t', 'phyRate'), param('ns3::WifiPhyStandard', 'standard')], 
                   is_static=True)
    ## wifi-mode.h: static ns3::WifiMode ns3::WifiModeFactory::CreateDbpsk(std::string uniqueName, bool isMandatory, uint32_t bandwidth, uint32_t dataRate, uint32_t phyRate, ns3::WifiPhyStandard standard) [member function]
    cls.add_method('CreateDbpsk', 
                   'ns3::WifiMode', 
                   [param('std::string', 'uniqueName'), param('bool', 'isMandatory'), param('uint32_t', 'bandwidth'), param('uint32_t', 'dataRate'), param('uint32_t', 'phyRate'), param('ns3::WifiPhyStandard', 'standard')], 
                   is_static=True)
    ## wifi-mode.h: static ns3::WifiMode ns3::WifiModeFactory::CreateDqpsk(std::string uniqueName, bool isMandatory, uint32_t bandwidth, uint32_t dataRate, uint32_t phyRate, ns3::WifiPhyStandard standard) [member function]
    cls.add_method('CreateDqpsk', 
                   'ns3::WifiMode', 
                   [param('std::string', 'uniqueName'), param('bool', 'isMandatory'), param('uint32_t', 'bandwidth'), param('uint32_t', 'dataRate'), param('uint32_t', 'phyRate'), param('ns3::WifiPhyStandard', 'standard')], 
                   is_static=True)
    ## wifi-mode.h: static ns3::WifiMode ns3::WifiModeFactory::CreateQam(std::string uniqueName, bool isMandatory, uint32_t bandwidth, uint32_t dataRate, uint32_t phyRate, uint8_t constellationSize, ns3::WifiPhyStandard standard) [member function]
    cls.add_method('CreateQam', 
                   'ns3::WifiMode', 
                   [param('std::string', 'uniqueName'), param('bool', 'isMandatory'), param('uint32_t', 'bandwidth'), param('uint32_t', 'dataRate'), param('uint32_t', 'phyRate'), param('uint8_t', 'constellationSize'), param('ns3::WifiPhyStandard', 'standard')], 
                   is_static=True)
    return

def register_Ns3WifiPhyListener_methods(root_module, cls):
    ## wifi-phy.h: ns3::WifiPhyListener::WifiPhyListener() [constructor]
    cls.add_constructor([])
    ## wifi-phy.h: ns3::WifiPhyListener::WifiPhyListener(ns3::WifiPhyListener const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::WifiPhyListener const &', 'arg0')])
    ## wifi-phy.h: void ns3::WifiPhyListener::NotifyMaybeCcaBusyStart(ns3::Time duration) [member function]
    cls.add_method('NotifyMaybeCcaBusyStart', 
                   'void', 
                   [param('ns3::Time', 'duration')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-phy.h: void ns3::WifiPhyListener::NotifyRxEndError() [member function]
    cls.add_method('NotifyRxEndError', 
                   'void', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-phy.h: void ns3::WifiPhyListener::NotifyRxEndOk() [member function]
    cls.add_method('NotifyRxEndOk', 
                   'void', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-phy.h: void ns3::WifiPhyListener::NotifyRxStart(ns3::Time duration) [member function]
    cls.add_method('NotifyRxStart', 
                   'void', 
                   [param('ns3::Time', 'duration')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-phy.h: void ns3::WifiPhyListener::NotifySwitchingStart(ns3::Time duration) [member function]
    cls.add_method('NotifySwitchingStart', 
                   'void', 
                   [param('ns3::Time', 'duration')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-phy.h: void ns3::WifiPhyListener::NotifyTxStart(ns3::Time duration) [member function]
    cls.add_method('NotifyTxStart', 
                   'void', 
                   [param('ns3::Time', 'duration')], 
                   is_pure_virtual=True, is_virtual=True)
    return

def register_Ns3WifiRemoteStation_methods(root_module, cls):
    ## wifi-remote-station-manager.h: ns3::WifiRemoteStation::WifiRemoteStation(ns3::WifiRemoteStation const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::WifiRemoteStation const &', 'arg0')])
    ## wifi-remote-station-manager.h: ns3::WifiRemoteStation::WifiRemoteStation() [constructor]
    cls.add_constructor([])
    ## wifi-remote-station-manager.h: void ns3::WifiRemoteStation::AddSupportedMode(ns3::WifiMode mode) [member function]
    cls.add_method('AddSupportedMode', 
                   'void', 
                   [param('ns3::WifiMode', 'mode')])
    ## wifi-remote-station-manager.h: ns3::WifiMode ns3::WifiRemoteStation::GetAckMode(ns3::WifiMode dataMode) [member function]
    cls.add_method('GetAckMode', 
                   'ns3::WifiMode', 
                   [param('ns3::WifiMode', 'dataMode')])
    ## wifi-remote-station-manager.h: ns3::Mac48Address ns3::WifiRemoteStation::GetAddress() [member function]
    cls.add_method('GetAddress', 
                   'ns3::Mac48Address', 
                   [])
    ## wifi-remote-station-manager.h: double ns3::WifiRemoteStation::GetAvgSlrc() const [member function]
    cls.add_method('GetAvgSlrc', 
                   'double', 
                   [], 
                   is_const=True)
    ## wifi-remote-station-manager.h: ns3::WifiMode ns3::WifiRemoteStation::GetCtsMode(ns3::WifiMode rtsMode) [member function]
    cls.add_method('GetCtsMode', 
                   'ns3::WifiMode', 
                   [param('ns3::WifiMode', 'rtsMode')])
    ## wifi-remote-station-manager.h: ns3::WifiMode ns3::WifiRemoteStation::GetDataMode(ns3::Ptr<ns3::Packet const> packet, uint32_t fullPacketSize) [member function]
    cls.add_method('GetDataMode', 
                   'ns3::WifiMode', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet'), param('uint32_t', 'fullPacketSize')])
    ## wifi-remote-station-manager.h: uint32_t ns3::WifiRemoteStation::GetFragmentOffset(ns3::Ptr<ns3::Packet const> packet, uint32_t fragmentNumber) [member function]
    cls.add_method('GetFragmentOffset', 
                   'uint32_t', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet'), param('uint32_t', 'fragmentNumber')], 
                   is_virtual=True)
    ## wifi-remote-station-manager.h: uint32_t ns3::WifiRemoteStation::GetFragmentSize(ns3::Ptr<ns3::Packet const> packet, uint32_t fragmentNumber) [member function]
    cls.add_method('GetFragmentSize', 
                   'uint32_t', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet'), param('uint32_t', 'fragmentNumber')], 
                   is_virtual=True)
    ## wifi-remote-station-manager.h: ns3::WifiMode ns3::WifiRemoteStation::GetRtsMode(ns3::Ptr<ns3::Packet const> packet) [member function]
    cls.add_method('GetRtsMode', 
                   'ns3::WifiMode', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet')])
    ## wifi-remote-station-manager.h: static ns3::TypeId ns3::WifiRemoteStation::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## wifi-remote-station-manager.h: bool ns3::WifiRemoteStation::IsAssociated() const [member function]
    cls.add_method('IsAssociated', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-remote-station-manager.h: bool ns3::WifiRemoteStation::IsBrandNew() const [member function]
    cls.add_method('IsBrandNew', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-remote-station-manager.h: bool ns3::WifiRemoteStation::IsLastFragment(ns3::Ptr<ns3::Packet const> packet, uint32_t fragmentNumber) [member function]
    cls.add_method('IsLastFragment', 
                   'bool', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet'), param('uint32_t', 'fragmentNumber')], 
                   is_virtual=True)
    ## wifi-remote-station-manager.h: bool ns3::WifiRemoteStation::IsWaitAssocTxOk() const [member function]
    cls.add_method('IsWaitAssocTxOk', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-remote-station-manager.h: bool ns3::WifiRemoteStation::NeedDataRetransmission(ns3::Ptr<ns3::Packet const> packet) [member function]
    cls.add_method('NeedDataRetransmission', 
                   'bool', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet')], 
                   is_virtual=True)
    ## wifi-remote-station-manager.h: bool ns3::WifiRemoteStation::NeedFragmentation(ns3::Ptr<ns3::Packet const> packet) [member function]
    cls.add_method('NeedFragmentation', 
                   'bool', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet')], 
                   is_virtual=True)
    ## wifi-remote-station-manager.h: bool ns3::WifiRemoteStation::NeedRts(ns3::Ptr<ns3::Packet const> packet) [member function]
    cls.add_method('NeedRts', 
                   'bool', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet')], 
                   is_virtual=True)
    ## wifi-remote-station-manager.h: bool ns3::WifiRemoteStation::NeedRtsRetransmission(ns3::Ptr<ns3::Packet const> packet) [member function]
    cls.add_method('NeedRtsRetransmission', 
                   'bool', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet')], 
                   is_virtual=True)
    ## wifi-remote-station-manager.h: void ns3::WifiRemoteStation::PrepareForQueue(ns3::Ptr<ns3::Packet const> packet, uint32_t fullPacketSize) [member function]
    cls.add_method('PrepareForQueue', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet'), param('uint32_t', 'fullPacketSize')])
    ## wifi-remote-station-manager.h: void ns3::WifiRemoteStation::RecordDisassociated() [member function]
    cls.add_method('RecordDisassociated', 
                   'void', 
                   [])
    ## wifi-remote-station-manager.h: void ns3::WifiRemoteStation::RecordGotAssocTxFailed() [member function]
    cls.add_method('RecordGotAssocTxFailed', 
                   'void', 
                   [])
    ## wifi-remote-station-manager.h: void ns3::WifiRemoteStation::RecordGotAssocTxOk() [member function]
    cls.add_method('RecordGotAssocTxOk', 
                   'void', 
                   [])
    ## wifi-remote-station-manager.h: void ns3::WifiRemoteStation::RecordWaitAssocTxOk() [member function]
    cls.add_method('RecordWaitAssocTxOk', 
                   'void', 
                   [])
    ## wifi-remote-station-manager.h: void ns3::WifiRemoteStation::ReportDataFailed() [member function]
    cls.add_method('ReportDataFailed', 
                   'void', 
                   [])
    ## wifi-remote-station-manager.h: void ns3::WifiRemoteStation::ReportDataOk(double ackSnr, ns3::WifiMode ackMode, double dataSnr) [member function]
    cls.add_method('ReportDataOk', 
                   'void', 
                   [param('double', 'ackSnr'), param('ns3::WifiMode', 'ackMode'), param('double', 'dataSnr')])
    ## wifi-remote-station-manager.h: void ns3::WifiRemoteStation::ReportFinalDataFailed() [member function]
    cls.add_method('ReportFinalDataFailed', 
                   'void', 
                   [])
    ## wifi-remote-station-manager.h: void ns3::WifiRemoteStation::ReportFinalRtsFailed() [member function]
    cls.add_method('ReportFinalRtsFailed', 
                   'void', 
                   [])
    ## wifi-remote-station-manager.h: void ns3::WifiRemoteStation::ReportRtsFailed() [member function]
    cls.add_method('ReportRtsFailed', 
                   'void', 
                   [])
    ## wifi-remote-station-manager.h: void ns3::WifiRemoteStation::ReportRtsOk(double ctsSnr, ns3::WifiMode ctsMode, double rtsSnr) [member function]
    cls.add_method('ReportRtsOk', 
                   'void', 
                   [param('double', 'ctsSnr'), param('ns3::WifiMode', 'ctsMode'), param('double', 'rtsSnr')])
    ## wifi-remote-station-manager.h: void ns3::WifiRemoteStation::ReportRxOk(double rxSnr, ns3::WifiMode txMode) [member function]
    cls.add_method('ReportRxOk', 
                   'void', 
                   [param('double', 'rxSnr'), param('ns3::WifiMode', 'txMode')])
    ## wifi-remote-station-manager.h: void ns3::WifiRemoteStation::Reset() [member function]
    cls.add_method('Reset', 
                   'void', 
                   [])
    ## wifi-remote-station-manager.h: void ns3::WifiRemoteStation::SetAddress(ns3::Mac48Address address) [member function]
    cls.add_method('SetAddress', 
                   'void', 
                   [param('ns3::Mac48Address', 'address')])
    ## wifi-remote-station-manager.h: uint32_t ns3::WifiRemoteStation::GetNSupportedModes() const [member function]
    cls.add_method('GetNSupportedModes', 
                   'uint32_t', 
                   [], 
                   is_const=True, visibility='protected')
    ## wifi-remote-station-manager.h: ns3::WifiMode ns3::WifiRemoteStation::GetSupportedMode(uint32_t i) const [member function]
    cls.add_method('GetSupportedMode', 
                   'ns3::WifiMode', 
                   [param('uint32_t', 'i')], 
                   is_const=True, visibility='protected')
    ## wifi-remote-station-manager.h: ns3::WifiMode ns3::WifiRemoteStation::DoGetDataMode(uint32_t size) [member function]
    cls.add_method('DoGetDataMode', 
                   'ns3::WifiMode', 
                   [param('uint32_t', 'size')], 
                   is_pure_virtual=True, visibility='private', is_virtual=True)
    ## wifi-remote-station-manager.h: ns3::WifiMode ns3::WifiRemoteStation::DoGetRtsMode() [member function]
    cls.add_method('DoGetRtsMode', 
                   'ns3::WifiMode', 
                   [], 
                   is_pure_virtual=True, visibility='private', is_virtual=True)
    ## wifi-remote-station-manager.h: void ns3::WifiRemoteStation::DoReportDataFailed() [member function]
    cls.add_method('DoReportDataFailed', 
                   'void', 
                   [], 
                   is_pure_virtual=True, visibility='private', is_virtual=True)
    ## wifi-remote-station-manager.h: void ns3::WifiRemoteStation::DoReportDataOk(double ackSnr, ns3::WifiMode ackMode, double dataSnr) [member function]
    cls.add_method('DoReportDataOk', 
                   'void', 
                   [param('double', 'ackSnr'), param('ns3::WifiMode', 'ackMode'), param('double', 'dataSnr')], 
                   is_pure_virtual=True, visibility='private', is_virtual=True)
    ## wifi-remote-station-manager.h: void ns3::WifiRemoteStation::DoReportFinalDataFailed() [member function]
    cls.add_method('DoReportFinalDataFailed', 
                   'void', 
                   [], 
                   is_pure_virtual=True, visibility='private', is_virtual=True)
    ## wifi-remote-station-manager.h: void ns3::WifiRemoteStation::DoReportFinalRtsFailed() [member function]
    cls.add_method('DoReportFinalRtsFailed', 
                   'void', 
                   [], 
                   is_pure_virtual=True, visibility='private', is_virtual=True)
    ## wifi-remote-station-manager.h: void ns3::WifiRemoteStation::DoReportRtsFailed() [member function]
    cls.add_method('DoReportRtsFailed', 
                   'void', 
                   [], 
                   is_pure_virtual=True, visibility='private', is_virtual=True)
    ## wifi-remote-station-manager.h: void ns3::WifiRemoteStation::DoReportRtsOk(double ctsSnr, ns3::WifiMode ctsMode, double rtsSnr) [member function]
    cls.add_method('DoReportRtsOk', 
                   'void', 
                   [param('double', 'ctsSnr'), param('ns3::WifiMode', 'ctsMode'), param('double', 'rtsSnr')], 
                   is_pure_virtual=True, visibility='private', is_virtual=True)
    ## wifi-remote-station-manager.h: void ns3::WifiRemoteStation::DoReportRxOk(double rxSnr, ns3::WifiMode txMode) [member function]
    cls.add_method('DoReportRxOk', 
                   'void', 
                   [param('double', 'rxSnr'), param('ns3::WifiMode', 'txMode')], 
                   is_pure_virtual=True, visibility='private', is_virtual=True)
    ## wifi-remote-station-manager.h: ns3::Ptr<ns3::WifiRemoteStationManager> ns3::WifiRemoteStation::GetManager() const [member function]
    cls.add_method('GetManager', 
                   'ns3::Ptr< ns3::WifiRemoteStationManager >', 
                   [], 
                   is_pure_virtual=True, is_const=True, visibility='private', is_virtual=True)
    return

def register_Ns3AmrrWifiRemoteStation_methods(root_module, cls):
    ## amrr-wifi-manager.h: ns3::AmrrWifiRemoteStation::AmrrWifiRemoteStation(ns3::AmrrWifiRemoteStation const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::AmrrWifiRemoteStation const &', 'arg0')])
    ## amrr-wifi-manager.h: ns3::AmrrWifiRemoteStation::AmrrWifiRemoteStation(ns3::Ptr<ns3::AmrrWifiManager> stations) [constructor]
    cls.add_constructor([param('ns3::Ptr< ns3::AmrrWifiManager >', 'stations')])
    ## amrr-wifi-manager.h: void ns3::AmrrWifiRemoteStation::DoReportDataFailed() [member function]
    cls.add_method('DoReportDataFailed', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## amrr-wifi-manager.h: void ns3::AmrrWifiRemoteStation::DoReportDataOk(double ackSnr, ns3::WifiMode ackMode, double dataSnr) [member function]
    cls.add_method('DoReportDataOk', 
                   'void', 
                   [param('double', 'ackSnr'), param('ns3::WifiMode', 'ackMode'), param('double', 'dataSnr')], 
                   visibility='protected', is_virtual=True)
    ## amrr-wifi-manager.h: void ns3::AmrrWifiRemoteStation::DoReportFinalDataFailed() [member function]
    cls.add_method('DoReportFinalDataFailed', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## amrr-wifi-manager.h: void ns3::AmrrWifiRemoteStation::DoReportFinalRtsFailed() [member function]
    cls.add_method('DoReportFinalRtsFailed', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## amrr-wifi-manager.h: void ns3::AmrrWifiRemoteStation::DoReportRtsFailed() [member function]
    cls.add_method('DoReportRtsFailed', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## amrr-wifi-manager.h: void ns3::AmrrWifiRemoteStation::DoReportRtsOk(double ctsSnr, ns3::WifiMode ctsMode, double rtsSnr) [member function]
    cls.add_method('DoReportRtsOk', 
                   'void', 
                   [param('double', 'ctsSnr'), param('ns3::WifiMode', 'ctsMode'), param('double', 'rtsSnr')], 
                   visibility='protected', is_virtual=True)
    ## amrr-wifi-manager.h: void ns3::AmrrWifiRemoteStation::DoReportRxOk(double rxSnr, ns3::WifiMode txMode) [member function]
    cls.add_method('DoReportRxOk', 
                   'void', 
                   [param('double', 'rxSnr'), param('ns3::WifiMode', 'txMode')], 
                   visibility='protected', is_virtual=True)
    ## amrr-wifi-manager.h: ns3::WifiMode ns3::AmrrWifiRemoteStation::DoGetDataMode(uint32_t size) [member function]
    cls.add_method('DoGetDataMode', 
                   'ns3::WifiMode', 
                   [param('uint32_t', 'size')], 
                   visibility='private', is_virtual=True)
    ## amrr-wifi-manager.h: ns3::WifiMode ns3::AmrrWifiRemoteStation::DoGetRtsMode() [member function]
    cls.add_method('DoGetRtsMode', 
                   'ns3::WifiMode', 
                   [], 
                   visibility='private', is_virtual=True)
    ## amrr-wifi-manager.h: ns3::Ptr<ns3::WifiRemoteStationManager> ns3::AmrrWifiRemoteStation::GetManager() const [member function]
    cls.add_method('GetManager', 
                   'ns3::Ptr< ns3::WifiRemoteStationManager >', 
                   [], 
                   is_const=True, visibility='private', is_virtual=True)
    return

def register_Ns3ArfWifiRemoteStation_methods(root_module, cls):
    ## arf-wifi-manager.h: ns3::ArfWifiRemoteStation::ArfWifiRemoteStation(ns3::ArfWifiRemoteStation const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::ArfWifiRemoteStation const &', 'arg0')])
    ## arf-wifi-manager.h: ns3::ArfWifiRemoteStation::ArfWifiRemoteStation(ns3::Ptr<ns3::ArfWifiManager> manager) [constructor]
    cls.add_constructor([param('ns3::Ptr< ns3::ArfWifiManager >', 'manager')])
    ## arf-wifi-manager.h: void ns3::ArfWifiRemoteStation::DoReportDataFailed() [member function]
    cls.add_method('DoReportDataFailed', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## arf-wifi-manager.h: void ns3::ArfWifiRemoteStation::DoReportDataOk(double ackSnr, ns3::WifiMode ackMode, double dataSnr) [member function]
    cls.add_method('DoReportDataOk', 
                   'void', 
                   [param('double', 'ackSnr'), param('ns3::WifiMode', 'ackMode'), param('double', 'dataSnr')], 
                   visibility='protected', is_virtual=True)
    ## arf-wifi-manager.h: void ns3::ArfWifiRemoteStation::DoReportFinalDataFailed() [member function]
    cls.add_method('DoReportFinalDataFailed', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## arf-wifi-manager.h: void ns3::ArfWifiRemoteStation::DoReportFinalRtsFailed() [member function]
    cls.add_method('DoReportFinalRtsFailed', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## arf-wifi-manager.h: void ns3::ArfWifiRemoteStation::DoReportRtsFailed() [member function]
    cls.add_method('DoReportRtsFailed', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## arf-wifi-manager.h: void ns3::ArfWifiRemoteStation::DoReportRtsOk(double ctsSnr, ns3::WifiMode ctsMode, double rtsSnr) [member function]
    cls.add_method('DoReportRtsOk', 
                   'void', 
                   [param('double', 'ctsSnr'), param('ns3::WifiMode', 'ctsMode'), param('double', 'rtsSnr')], 
                   visibility='protected', is_virtual=True)
    ## arf-wifi-manager.h: void ns3::ArfWifiRemoteStation::DoReportRxOk(double rxSnr, ns3::WifiMode txMode) [member function]
    cls.add_method('DoReportRxOk', 
                   'void', 
                   [param('double', 'rxSnr'), param('ns3::WifiMode', 'txMode')], 
                   visibility='protected', is_virtual=True)
    ## arf-wifi-manager.h: uint32_t ns3::ArfWifiRemoteStation::GetMinSuccessThreshold() [member function]
    cls.add_method('GetMinSuccessThreshold', 
                   'uint32_t', 
                   [], 
                   visibility='protected')
    ## arf-wifi-manager.h: uint32_t ns3::ArfWifiRemoteStation::GetMinTimerTimeout() [member function]
    cls.add_method('GetMinTimerTimeout', 
                   'uint32_t', 
                   [], 
                   visibility='protected')
    ## arf-wifi-manager.h: uint32_t ns3::ArfWifiRemoteStation::GetSuccessThreshold() [member function]
    cls.add_method('GetSuccessThreshold', 
                   'uint32_t', 
                   [], 
                   visibility='protected')
    ## arf-wifi-manager.h: uint32_t ns3::ArfWifiRemoteStation::GetTimerTimeout() [member function]
    cls.add_method('GetTimerTimeout', 
                   'uint32_t', 
                   [], 
                   visibility='protected')
    ## arf-wifi-manager.h: void ns3::ArfWifiRemoteStation::SetSuccessThreshold(uint32_t successThreshold) [member function]
    cls.add_method('SetSuccessThreshold', 
                   'void', 
                   [param('uint32_t', 'successThreshold')], 
                   visibility='protected')
    ## arf-wifi-manager.h: void ns3::ArfWifiRemoteStation::SetTimerTimeout(uint32_t timerTimeout) [member function]
    cls.add_method('SetTimerTimeout', 
                   'void', 
                   [param('uint32_t', 'timerTimeout')], 
                   visibility='protected')
    ## arf-wifi-manager.h: ns3::WifiMode ns3::ArfWifiRemoteStation::DoGetDataMode(uint32_t size) [member function]
    cls.add_method('DoGetDataMode', 
                   'ns3::WifiMode', 
                   [param('uint32_t', 'size')], 
                   visibility='private', is_virtual=True)
    ## arf-wifi-manager.h: ns3::WifiMode ns3::ArfWifiRemoteStation::DoGetRtsMode() [member function]
    cls.add_method('DoGetRtsMode', 
                   'ns3::WifiMode', 
                   [], 
                   visibility='private', is_virtual=True)
    ## arf-wifi-manager.h: ns3::Ptr<ns3::WifiRemoteStationManager> ns3::ArfWifiRemoteStation::GetManager() const [member function]
    cls.add_method('GetManager', 
                   'ns3::Ptr< ns3::WifiRemoteStationManager >', 
                   [], 
                   is_const=True, visibility='private', is_virtual=True)
    ## arf-wifi-manager.h: void ns3::ArfWifiRemoteStation::ReportFailure() [member function]
    cls.add_method('ReportFailure', 
                   'void', 
                   [], 
                   visibility='private', is_virtual=True)
    ## arf-wifi-manager.h: void ns3::ArfWifiRemoteStation::ReportRecoveryFailure() [member function]
    cls.add_method('ReportRecoveryFailure', 
                   'void', 
                   [], 
                   visibility='private', is_virtual=True)
    return

def register_Ns3ConstantRateWifiRemoteStation_methods(root_module, cls):
    ## constant-rate-wifi-manager.h: ns3::ConstantRateWifiRemoteStation::ConstantRateWifiRemoteStation(ns3::ConstantRateWifiRemoteStation const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::ConstantRateWifiRemoteStation const &', 'arg0')])
    ## constant-rate-wifi-manager.h: ns3::ConstantRateWifiRemoteStation::ConstantRateWifiRemoteStation(ns3::Ptr<ns3::ConstantRateWifiManager> stations) [constructor]
    cls.add_constructor([param('ns3::Ptr< ns3::ConstantRateWifiManager >', 'stations')])
    ## constant-rate-wifi-manager.h: void ns3::ConstantRateWifiRemoteStation::DoReportDataFailed() [member function]
    cls.add_method('DoReportDataFailed', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## constant-rate-wifi-manager.h: void ns3::ConstantRateWifiRemoteStation::DoReportDataOk(double ackSnr, ns3::WifiMode ackMode, double dataSnr) [member function]
    cls.add_method('DoReportDataOk', 
                   'void', 
                   [param('double', 'ackSnr'), param('ns3::WifiMode', 'ackMode'), param('double', 'dataSnr')], 
                   visibility='protected', is_virtual=True)
    ## constant-rate-wifi-manager.h: void ns3::ConstantRateWifiRemoteStation::DoReportFinalDataFailed() [member function]
    cls.add_method('DoReportFinalDataFailed', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## constant-rate-wifi-manager.h: void ns3::ConstantRateWifiRemoteStation::DoReportFinalRtsFailed() [member function]
    cls.add_method('DoReportFinalRtsFailed', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## constant-rate-wifi-manager.h: void ns3::ConstantRateWifiRemoteStation::DoReportRtsFailed() [member function]
    cls.add_method('DoReportRtsFailed', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## constant-rate-wifi-manager.h: void ns3::ConstantRateWifiRemoteStation::DoReportRtsOk(double ctsSnr, ns3::WifiMode ctsMode, double rtsSnr) [member function]
    cls.add_method('DoReportRtsOk', 
                   'void', 
                   [param('double', 'ctsSnr'), param('ns3::WifiMode', 'ctsMode'), param('double', 'rtsSnr')], 
                   visibility='protected', is_virtual=True)
    ## constant-rate-wifi-manager.h: void ns3::ConstantRateWifiRemoteStation::DoReportRxOk(double rxSnr, ns3::WifiMode txMode) [member function]
    cls.add_method('DoReportRxOk', 
                   'void', 
                   [param('double', 'rxSnr'), param('ns3::WifiMode', 'txMode')], 
                   visibility='protected', is_virtual=True)
    ## constant-rate-wifi-manager.h: ns3::WifiMode ns3::ConstantRateWifiRemoteStation::DoGetDataMode(uint32_t size) [member function]
    cls.add_method('DoGetDataMode', 
                   'ns3::WifiMode', 
                   [param('uint32_t', 'size')], 
                   visibility='private', is_virtual=True)
    ## constant-rate-wifi-manager.h: ns3::WifiMode ns3::ConstantRateWifiRemoteStation::DoGetRtsMode() [member function]
    cls.add_method('DoGetRtsMode', 
                   'ns3::WifiMode', 
                   [], 
                   visibility='private', is_virtual=True)
    ## constant-rate-wifi-manager.h: ns3::Ptr<ns3::WifiRemoteStationManager> ns3::ConstantRateWifiRemoteStation::GetManager() const [member function]
    cls.add_method('GetManager', 
                   'ns3::Ptr< ns3::WifiRemoteStationManager >', 
                   [], 
                   is_const=True, visibility='private', is_virtual=True)
    return

def register_Ns3IdealWifiRemoteStation_methods(root_module, cls):
    ## ideal-wifi-manager.h: ns3::IdealWifiRemoteStation::IdealWifiRemoteStation(ns3::IdealWifiRemoteStation const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::IdealWifiRemoteStation const &', 'arg0')])
    ## ideal-wifi-manager.h: ns3::IdealWifiRemoteStation::IdealWifiRemoteStation(ns3::Ptr<ns3::IdealWifiManager> stations) [constructor]
    cls.add_constructor([param('ns3::Ptr< ns3::IdealWifiManager >', 'stations')])
    ## ideal-wifi-manager.h: void ns3::IdealWifiRemoteStation::DoReportDataFailed() [member function]
    cls.add_method('DoReportDataFailed', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## ideal-wifi-manager.h: void ns3::IdealWifiRemoteStation::DoReportDataOk(double ackSnr, ns3::WifiMode ackMode, double dataSnr) [member function]
    cls.add_method('DoReportDataOk', 
                   'void', 
                   [param('double', 'ackSnr'), param('ns3::WifiMode', 'ackMode'), param('double', 'dataSnr')], 
                   visibility='protected', is_virtual=True)
    ## ideal-wifi-manager.h: void ns3::IdealWifiRemoteStation::DoReportFinalDataFailed() [member function]
    cls.add_method('DoReportFinalDataFailed', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## ideal-wifi-manager.h: void ns3::IdealWifiRemoteStation::DoReportFinalRtsFailed() [member function]
    cls.add_method('DoReportFinalRtsFailed', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## ideal-wifi-manager.h: void ns3::IdealWifiRemoteStation::DoReportRtsFailed() [member function]
    cls.add_method('DoReportRtsFailed', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## ideal-wifi-manager.h: void ns3::IdealWifiRemoteStation::DoReportRtsOk(double ctsSnr, ns3::WifiMode ctsMode, double rtsSnr) [member function]
    cls.add_method('DoReportRtsOk', 
                   'void', 
                   [param('double', 'ctsSnr'), param('ns3::WifiMode', 'ctsMode'), param('double', 'rtsSnr')], 
                   visibility='protected', is_virtual=True)
    ## ideal-wifi-manager.h: void ns3::IdealWifiRemoteStation::DoReportRxOk(double rxSnr, ns3::WifiMode txMode) [member function]
    cls.add_method('DoReportRxOk', 
                   'void', 
                   [param('double', 'rxSnr'), param('ns3::WifiMode', 'txMode')], 
                   visibility='protected', is_virtual=True)
    ## ideal-wifi-manager.h: ns3::WifiMode ns3::IdealWifiRemoteStation::DoGetDataMode(uint32_t size) [member function]
    cls.add_method('DoGetDataMode', 
                   'ns3::WifiMode', 
                   [param('uint32_t', 'size')], 
                   visibility='private', is_virtual=True)
    ## ideal-wifi-manager.h: ns3::WifiMode ns3::IdealWifiRemoteStation::DoGetRtsMode() [member function]
    cls.add_method('DoGetRtsMode', 
                   'ns3::WifiMode', 
                   [], 
                   visibility='private', is_virtual=True)
    ## ideal-wifi-manager.h: ns3::Ptr<ns3::WifiRemoteStationManager> ns3::IdealWifiRemoteStation::GetManager() const [member function]
    cls.add_method('GetManager', 
                   'ns3::Ptr< ns3::WifiRemoteStationManager >', 
                   [], 
                   is_const=True, visibility='private', is_virtual=True)
    return

def register_Ns3MgtAssocRequestHeader_methods(root_module, cls):
    ## mgt-headers.h: ns3::MgtAssocRequestHeader::MgtAssocRequestHeader(ns3::MgtAssocRequestHeader const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::MgtAssocRequestHeader const &', 'arg0')])
    ## mgt-headers.h: ns3::MgtAssocRequestHeader::MgtAssocRequestHeader() [constructor]
    cls.add_constructor([])
    ## mgt-headers.h: uint32_t ns3::MgtAssocRequestHeader::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    ## mgt-headers.h: ns3::TypeId ns3::MgtAssocRequestHeader::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## mgt-headers.h: uint16_t ns3::MgtAssocRequestHeader::GetListenInterval() const [member function]
    cls.add_method('GetListenInterval', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## mgt-headers.h: uint32_t ns3::MgtAssocRequestHeader::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## mgt-headers.h: ns3::Ssid ns3::MgtAssocRequestHeader::GetSsid() const [member function]
    cls.add_method('GetSsid', 
                   'ns3::Ssid', 
                   [], 
                   is_const=True)
    ## mgt-headers.h: ns3::SupportedRates ns3::MgtAssocRequestHeader::GetSupportedRates() const [member function]
    cls.add_method('GetSupportedRates', 
                   'ns3::SupportedRates', 
                   [], 
                   is_const=True)
    ## mgt-headers.h: static ns3::TypeId ns3::MgtAssocRequestHeader::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## mgt-headers.h: void ns3::MgtAssocRequestHeader::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    ## mgt-headers.h: void ns3::MgtAssocRequestHeader::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    ## mgt-headers.h: void ns3::MgtAssocRequestHeader::SetListenInterval(uint16_t interval) [member function]
    cls.add_method('SetListenInterval', 
                   'void', 
                   [param('uint16_t', 'interval')])
    ## mgt-headers.h: void ns3::MgtAssocRequestHeader::SetSsid(ns3::Ssid ssid) [member function]
    cls.add_method('SetSsid', 
                   'void', 
                   [param('ns3::Ssid', 'ssid')])
    ## mgt-headers.h: void ns3::MgtAssocRequestHeader::SetSupportedRates(ns3::SupportedRates rates) [member function]
    cls.add_method('SetSupportedRates', 
                   'void', 
                   [param('ns3::SupportedRates', 'rates')])
    return

def register_Ns3MgtAssocResponseHeader_methods(root_module, cls):
    ## mgt-headers.h: ns3::MgtAssocResponseHeader::MgtAssocResponseHeader(ns3::MgtAssocResponseHeader const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::MgtAssocResponseHeader const &', 'arg0')])
    ## mgt-headers.h: ns3::MgtAssocResponseHeader::MgtAssocResponseHeader() [constructor]
    cls.add_constructor([])
    ## mgt-headers.h: uint32_t ns3::MgtAssocResponseHeader::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    ## mgt-headers.h: ns3::TypeId ns3::MgtAssocResponseHeader::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## mgt-headers.h: uint32_t ns3::MgtAssocResponseHeader::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## mgt-headers.h: ns3::StatusCode ns3::MgtAssocResponseHeader::GetStatusCode() [member function]
    cls.add_method('GetStatusCode', 
                   'ns3::StatusCode', 
                   [])
    ## mgt-headers.h: ns3::SupportedRates ns3::MgtAssocResponseHeader::GetSupportedRates() [member function]
    cls.add_method('GetSupportedRates', 
                   'ns3::SupportedRates', 
                   [])
    ## mgt-headers.h: static ns3::TypeId ns3::MgtAssocResponseHeader::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## mgt-headers.h: void ns3::MgtAssocResponseHeader::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    ## mgt-headers.h: void ns3::MgtAssocResponseHeader::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    ## mgt-headers.h: void ns3::MgtAssocResponseHeader::SetStatusCode(ns3::StatusCode code) [member function]
    cls.add_method('SetStatusCode', 
                   'void', 
                   [param('ns3::StatusCode', 'code')])
    ## mgt-headers.h: void ns3::MgtAssocResponseHeader::SetSupportedRates(ns3::SupportedRates rates) [member function]
    cls.add_method('SetSupportedRates', 
                   'void', 
                   [param('ns3::SupportedRates', 'rates')])
    return

def register_Ns3MgtProbeRequestHeader_methods(root_module, cls):
    ## mgt-headers.h: ns3::MgtProbeRequestHeader::MgtProbeRequestHeader() [constructor]
    cls.add_constructor([])
    ## mgt-headers.h: ns3::MgtProbeRequestHeader::MgtProbeRequestHeader(ns3::MgtProbeRequestHeader const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::MgtProbeRequestHeader const &', 'arg0')])
    ## mgt-headers.h: uint32_t ns3::MgtProbeRequestHeader::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    ## mgt-headers.h: ns3::TypeId ns3::MgtProbeRequestHeader::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## mgt-headers.h: uint32_t ns3::MgtProbeRequestHeader::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## mgt-headers.h: ns3::Ssid ns3::MgtProbeRequestHeader::GetSsid() const [member function]
    cls.add_method('GetSsid', 
                   'ns3::Ssid', 
                   [], 
                   is_const=True)
    ## mgt-headers.h: ns3::SupportedRates ns3::MgtProbeRequestHeader::GetSupportedRates() const [member function]
    cls.add_method('GetSupportedRates', 
                   'ns3::SupportedRates', 
                   [], 
                   is_const=True)
    ## mgt-headers.h: static ns3::TypeId ns3::MgtProbeRequestHeader::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## mgt-headers.h: void ns3::MgtProbeRequestHeader::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    ## mgt-headers.h: void ns3::MgtProbeRequestHeader::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    ## mgt-headers.h: void ns3::MgtProbeRequestHeader::SetSsid(ns3::Ssid ssid) [member function]
    cls.add_method('SetSsid', 
                   'void', 
                   [param('ns3::Ssid', 'ssid')])
    ## mgt-headers.h: void ns3::MgtProbeRequestHeader::SetSupportedRates(ns3::SupportedRates rates) [member function]
    cls.add_method('SetSupportedRates', 
                   'void', 
                   [param('ns3::SupportedRates', 'rates')])
    return

def register_Ns3MgtProbeResponseHeader_methods(root_module, cls):
    ## mgt-headers.h: ns3::MgtProbeResponseHeader::MgtProbeResponseHeader(ns3::MgtProbeResponseHeader const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::MgtProbeResponseHeader const &', 'arg0')])
    ## mgt-headers.h: ns3::MgtProbeResponseHeader::MgtProbeResponseHeader() [constructor]
    cls.add_constructor([])
    ## mgt-headers.h: uint32_t ns3::MgtProbeResponseHeader::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    ## mgt-headers.h: uint64_t ns3::MgtProbeResponseHeader::GetBeaconIntervalUs() const [member function]
    cls.add_method('GetBeaconIntervalUs', 
                   'uint64_t', 
                   [], 
                   is_const=True)
    ## mgt-headers.h: ns3::TypeId ns3::MgtProbeResponseHeader::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## mgt-headers.h: uint32_t ns3::MgtProbeResponseHeader::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## mgt-headers.h: ns3::Ssid ns3::MgtProbeResponseHeader::GetSsid() const [member function]
    cls.add_method('GetSsid', 
                   'ns3::Ssid', 
                   [], 
                   is_const=True)
    ## mgt-headers.h: ns3::SupportedRates ns3::MgtProbeResponseHeader::GetSupportedRates() const [member function]
    cls.add_method('GetSupportedRates', 
                   'ns3::SupportedRates', 
                   [], 
                   is_const=True)
    ## mgt-headers.h: uint64_t ns3::MgtProbeResponseHeader::GetTimestamp() [member function]
    cls.add_method('GetTimestamp', 
                   'uint64_t', 
                   [])
    ## mgt-headers.h: static ns3::TypeId ns3::MgtProbeResponseHeader::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## mgt-headers.h: void ns3::MgtProbeResponseHeader::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    ## mgt-headers.h: void ns3::MgtProbeResponseHeader::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    ## mgt-headers.h: void ns3::MgtProbeResponseHeader::SetBeaconIntervalUs(uint64_t us) [member function]
    cls.add_method('SetBeaconIntervalUs', 
                   'void', 
                   [param('uint64_t', 'us')])
    ## mgt-headers.h: void ns3::MgtProbeResponseHeader::SetSsid(ns3::Ssid ssid) [member function]
    cls.add_method('SetSsid', 
                   'void', 
                   [param('ns3::Ssid', 'ssid')])
    ## mgt-headers.h: void ns3::MgtProbeResponseHeader::SetSupportedRates(ns3::SupportedRates rates) [member function]
    cls.add_method('SetSupportedRates', 
                   'void', 
                   [param('ns3::SupportedRates', 'rates')])
    return

def register_Ns3MinstrelWifiRemoteStation_methods(root_module, cls):
    ## minstrel-wifi-manager.h: ns3::MinstrelWifiRemoteStation::MinstrelWifiRemoteStation(ns3::MinstrelWifiRemoteStation const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::MinstrelWifiRemoteStation const &', 'arg0')])
    ## minstrel-wifi-manager.h: ns3::MinstrelWifiRemoteStation::MinstrelWifiRemoteStation(ns3::Ptr<ns3::MinstrelWifiManager> stations) [constructor]
    cls.add_constructor([param('ns3::Ptr< ns3::MinstrelWifiManager >', 'stations')])
    ## minstrel-wifi-manager.h: void ns3::MinstrelWifiRemoteStation::DoReportDataFailed() [member function]
    cls.add_method('DoReportDataFailed', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## minstrel-wifi-manager.h: void ns3::MinstrelWifiRemoteStation::DoReportDataOk(double ackSnr, ns3::WifiMode ackMode, double dataSnr) [member function]
    cls.add_method('DoReportDataOk', 
                   'void', 
                   [param('double', 'ackSnr'), param('ns3::WifiMode', 'ackMode'), param('double', 'dataSnr')], 
                   visibility='protected', is_virtual=True)
    ## minstrel-wifi-manager.h: void ns3::MinstrelWifiRemoteStation::DoReportFinalDataFailed() [member function]
    cls.add_method('DoReportFinalDataFailed', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## minstrel-wifi-manager.h: void ns3::MinstrelWifiRemoteStation::DoReportFinalRtsFailed() [member function]
    cls.add_method('DoReportFinalRtsFailed', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## minstrel-wifi-manager.h: void ns3::MinstrelWifiRemoteStation::DoReportRtsFailed() [member function]
    cls.add_method('DoReportRtsFailed', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## minstrel-wifi-manager.h: void ns3::MinstrelWifiRemoteStation::DoReportRtsOk(double ctsSnr, ns3::WifiMode ctsMode, double rtsSnr) [member function]
    cls.add_method('DoReportRtsOk', 
                   'void', 
                   [param('double', 'ctsSnr'), param('ns3::WifiMode', 'ctsMode'), param('double', 'rtsSnr')], 
                   visibility='protected', is_virtual=True)
    ## minstrel-wifi-manager.h: void ns3::MinstrelWifiRemoteStation::DoReportRxOk(double rxSnr, ns3::WifiMode txMode) [member function]
    cls.add_method('DoReportRxOk', 
                   'void', 
                   [param('double', 'rxSnr'), param('ns3::WifiMode', 'txMode')], 
                   visibility='protected', is_virtual=True)
    ## minstrel-wifi-manager.h: ns3::WifiMode ns3::MinstrelWifiRemoteStation::DoGetDataMode(uint32_t size) [member function]
    cls.add_method('DoGetDataMode', 
                   'ns3::WifiMode', 
                   [param('uint32_t', 'size')], 
                   visibility='private', is_virtual=True)
    ## minstrel-wifi-manager.h: ns3::WifiMode ns3::MinstrelWifiRemoteStation::DoGetRtsMode() [member function]
    cls.add_method('DoGetRtsMode', 
                   'ns3::WifiMode', 
                   [], 
                   visibility='private', is_virtual=True)
    ## minstrel-wifi-manager.h: ns3::Ptr<ns3::WifiRemoteStationManager> ns3::MinstrelWifiRemoteStation::GetManager() const [member function]
    cls.add_method('GetManager', 
                   'ns3::Ptr< ns3::WifiRemoteStationManager >', 
                   [], 
                   is_const=True, visibility='private', is_virtual=True)
    return

def register_Ns3OnoeWifiRemoteStation_methods(root_module, cls):
    ## onoe-wifi-manager.h: ns3::OnoeWifiRemoteStation::OnoeWifiRemoteStation(ns3::OnoeWifiRemoteStation const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::OnoeWifiRemoteStation const &', 'arg0')])
    ## onoe-wifi-manager.h: ns3::OnoeWifiRemoteStation::OnoeWifiRemoteStation(ns3::Ptr<ns3::OnoeWifiManager> stations) [constructor]
    cls.add_constructor([param('ns3::Ptr< ns3::OnoeWifiManager >', 'stations')])
    ## onoe-wifi-manager.h: void ns3::OnoeWifiRemoteStation::DoReportDataFailed() [member function]
    cls.add_method('DoReportDataFailed', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## onoe-wifi-manager.h: void ns3::OnoeWifiRemoteStation::DoReportDataOk(double ackSnr, ns3::WifiMode ackMode, double dataSnr) [member function]
    cls.add_method('DoReportDataOk', 
                   'void', 
                   [param('double', 'ackSnr'), param('ns3::WifiMode', 'ackMode'), param('double', 'dataSnr')], 
                   visibility='protected', is_virtual=True)
    ## onoe-wifi-manager.h: void ns3::OnoeWifiRemoteStation::DoReportFinalDataFailed() [member function]
    cls.add_method('DoReportFinalDataFailed', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## onoe-wifi-manager.h: void ns3::OnoeWifiRemoteStation::DoReportFinalRtsFailed() [member function]
    cls.add_method('DoReportFinalRtsFailed', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## onoe-wifi-manager.h: void ns3::OnoeWifiRemoteStation::DoReportRtsFailed() [member function]
    cls.add_method('DoReportRtsFailed', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## onoe-wifi-manager.h: void ns3::OnoeWifiRemoteStation::DoReportRtsOk(double ctsSnr, ns3::WifiMode ctsMode, double rtsSnr) [member function]
    cls.add_method('DoReportRtsOk', 
                   'void', 
                   [param('double', 'ctsSnr'), param('ns3::WifiMode', 'ctsMode'), param('double', 'rtsSnr')], 
                   visibility='protected', is_virtual=True)
    ## onoe-wifi-manager.h: void ns3::OnoeWifiRemoteStation::DoReportRxOk(double rxSnr, ns3::WifiMode txMode) [member function]
    cls.add_method('DoReportRxOk', 
                   'void', 
                   [param('double', 'rxSnr'), param('ns3::WifiMode', 'txMode')], 
                   visibility='protected', is_virtual=True)
    ## onoe-wifi-manager.h: ns3::WifiMode ns3::OnoeWifiRemoteStation::DoGetDataMode(uint32_t size) [member function]
    cls.add_method('DoGetDataMode', 
                   'ns3::WifiMode', 
                   [param('uint32_t', 'size')], 
                   visibility='private', is_virtual=True)
    ## onoe-wifi-manager.h: ns3::WifiMode ns3::OnoeWifiRemoteStation::DoGetRtsMode() [member function]
    cls.add_method('DoGetRtsMode', 
                   'ns3::WifiMode', 
                   [], 
                   visibility='private', is_virtual=True)
    ## onoe-wifi-manager.h: ns3::Ptr<ns3::WifiRemoteStationManager> ns3::OnoeWifiRemoteStation::GetManager() const [member function]
    cls.add_method('GetManager', 
                   'ns3::Ptr< ns3::WifiRemoteStationManager >', 
                   [], 
                   is_const=True, visibility='private', is_virtual=True)
    return

def register_Ns3PropagationDelayModel_methods(root_module, cls):
    ## propagation-delay-model.h: ns3::PropagationDelayModel::PropagationDelayModel() [constructor]
    cls.add_constructor([])
    ## propagation-delay-model.h: ns3::PropagationDelayModel::PropagationDelayModel(ns3::PropagationDelayModel const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::PropagationDelayModel const &', 'arg0')])
    ## propagation-delay-model.h: ns3::Time ns3::PropagationDelayModel::GetDelay(ns3::Ptr<ns3::MobilityModel> a, ns3::Ptr<ns3::MobilityModel> b) const [member function]
    cls.add_method('GetDelay', 
                   'ns3::Time', 
                   [param('ns3::Ptr< ns3::MobilityModel >', 'a'), param('ns3::Ptr< ns3::MobilityModel >', 'b')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## propagation-delay-model.h: static ns3::TypeId ns3::PropagationDelayModel::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    return

def register_Ns3PropagationLossModel_methods(root_module, cls):
    ## propagation-loss-model.h: static ns3::TypeId ns3::PropagationLossModel::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## propagation-loss-model.h: ns3::PropagationLossModel::PropagationLossModel() [constructor]
    cls.add_constructor([])
    ## propagation-loss-model.h: void ns3::PropagationLossModel::SetNext(ns3::Ptr<ns3::PropagationLossModel> next) [member function]
    cls.add_method('SetNext', 
                   'void', 
                   [param('ns3::Ptr< ns3::PropagationLossModel >', 'next')])
    ## propagation-loss-model.h: double ns3::PropagationLossModel::CalcRxPower(double txPowerDbm, ns3::Ptr<ns3::MobilityModel> a, ns3::Ptr<ns3::MobilityModel> b) const [member function]
    cls.add_method('CalcRxPower', 
                   'double', 
                   [param('double', 'txPowerDbm'), param('ns3::Ptr< ns3::MobilityModel >', 'a'), param('ns3::Ptr< ns3::MobilityModel >', 'b')], 
                   is_const=True)
    ## propagation-loss-model.h: double ns3::PropagationLossModel::DoCalcRxPower(double txPowerDbm, ns3::Ptr<ns3::MobilityModel> a, ns3::Ptr<ns3::MobilityModel> b) const [member function]
    cls.add_method('DoCalcRxPower', 
                   'double', 
                   [param('double', 'txPowerDbm'), param('ns3::Ptr< ns3::MobilityModel >', 'a'), param('ns3::Ptr< ns3::MobilityModel >', 'b')], 
                   is_pure_virtual=True, is_const=True, visibility='private', is_virtual=True)
    return

def register_Ns3QosTag_methods(root_module, cls):
    ## qos-tag.h: ns3::QosTag::QosTag(ns3::QosTag const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::QosTag const &', 'arg0')])
    ## qos-tag.h: ns3::QosTag::QosTag() [constructor]
    cls.add_constructor([])
    ## qos-tag.h: ns3::QosTag::QosTag(uint8_t tid) [constructor]
    cls.add_constructor([param('uint8_t', 'tid')])
    ## qos-tag.h: void ns3::QosTag::Deserialize(ns3::TagBuffer i) [member function]
    cls.add_method('Deserialize', 
                   'void', 
                   [param('ns3::TagBuffer', 'i')], 
                   is_virtual=True)
    ## qos-tag.h: ns3::TypeId ns3::QosTag::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## qos-tag.h: uint32_t ns3::QosTag::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## qos-tag.h: uint8_t ns3::QosTag::GetTid() const [member function]
    cls.add_method('GetTid', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## qos-tag.h: static ns3::TypeId ns3::QosTag::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## qos-tag.h: void ns3::QosTag::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    ## qos-tag.h: void ns3::QosTag::Serialize(ns3::TagBuffer i) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::TagBuffer', 'i')], 
                   is_const=True, is_virtual=True)
    ## qos-tag.h: void ns3::QosTag::SetTid(uint8_t tid) [member function]
    cls.add_method('SetTid', 
                   'void', 
                   [param('uint8_t', 'tid')])
    ## qos-tag.h: void ns3::QosTag::SetUserPriority(ns3::UserPriority up) [member function]
    cls.add_method('SetUserPriority', 
                   'void', 
                   [param('ns3::UserPriority', 'up')])
    return

def register_Ns3RandomPropagationDelayModel_methods(root_module, cls):
    ## propagation-delay-model.h: ns3::RandomPropagationDelayModel::RandomPropagationDelayModel(ns3::RandomPropagationDelayModel const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::RandomPropagationDelayModel const &', 'arg0')])
    ## propagation-delay-model.h: ns3::RandomPropagationDelayModel::RandomPropagationDelayModel() [constructor]
    cls.add_constructor([])
    ## propagation-delay-model.h: ns3::Time ns3::RandomPropagationDelayModel::GetDelay(ns3::Ptr<ns3::MobilityModel> a, ns3::Ptr<ns3::MobilityModel> b) const [member function]
    cls.add_method('GetDelay', 
                   'ns3::Time', 
                   [param('ns3::Ptr< ns3::MobilityModel >', 'a'), param('ns3::Ptr< ns3::MobilityModel >', 'b')], 
                   is_const=True, is_virtual=True)
    ## propagation-delay-model.h: static ns3::TypeId ns3::RandomPropagationDelayModel::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    return

def register_Ns3RandomPropagationLossModel_methods(root_module, cls):
    ## propagation-loss-model.h: static ns3::TypeId ns3::RandomPropagationLossModel::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## propagation-loss-model.h: ns3::RandomPropagationLossModel::RandomPropagationLossModel() [constructor]
    cls.add_constructor([])
    ## propagation-loss-model.h: double ns3::RandomPropagationLossModel::DoCalcRxPower(double txPowerDbm, ns3::Ptr<ns3::MobilityModel> a, ns3::Ptr<ns3::MobilityModel> b) const [member function]
    cls.add_method('DoCalcRxPower', 
                   'double', 
                   [param('double', 'txPowerDbm'), param('ns3::Ptr< ns3::MobilityModel >', 'a'), param('ns3::Ptr< ns3::MobilityModel >', 'b')], 
                   is_const=True, visibility='private', is_virtual=True)
    return

def register_Ns3RraaWifiRemoteStation_methods(root_module, cls):
    ## rraa-wifi-manager.h: ns3::RraaWifiRemoteStation::RraaWifiRemoteStation(ns3::RraaWifiRemoteStation const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::RraaWifiRemoteStation const &', 'arg0')])
    ## rraa-wifi-manager.h: ns3::RraaWifiRemoteStation::RraaWifiRemoteStation(ns3::Ptr<ns3::RraaWifiManager> stations) [constructor]
    cls.add_constructor([param('ns3::Ptr< ns3::RraaWifiManager >', 'stations')])
    ## rraa-wifi-manager.h: bool ns3::RraaWifiRemoteStation::NeedRts(ns3::Ptr<ns3::Packet const> packet) [member function]
    cls.add_method('NeedRts', 
                   'bool', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet')], 
                   is_virtual=True)
    ## rraa-wifi-manager.h: void ns3::RraaWifiRemoteStation::DoReportDataFailed() [member function]
    cls.add_method('DoReportDataFailed', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## rraa-wifi-manager.h: void ns3::RraaWifiRemoteStation::DoReportDataOk(double ackSnr, ns3::WifiMode ackMode, double dataSnr) [member function]
    cls.add_method('DoReportDataOk', 
                   'void', 
                   [param('double', 'ackSnr'), param('ns3::WifiMode', 'ackMode'), param('double', 'dataSnr')], 
                   visibility='protected', is_virtual=True)
    ## rraa-wifi-manager.h: void ns3::RraaWifiRemoteStation::DoReportFinalDataFailed() [member function]
    cls.add_method('DoReportFinalDataFailed', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## rraa-wifi-manager.h: void ns3::RraaWifiRemoteStation::DoReportFinalRtsFailed() [member function]
    cls.add_method('DoReportFinalRtsFailed', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## rraa-wifi-manager.h: void ns3::RraaWifiRemoteStation::DoReportRtsFailed() [member function]
    cls.add_method('DoReportRtsFailed', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## rraa-wifi-manager.h: void ns3::RraaWifiRemoteStation::DoReportRtsOk(double ctsSnr, ns3::WifiMode ctsMode, double rtsSnr) [member function]
    cls.add_method('DoReportRtsOk', 
                   'void', 
                   [param('double', 'ctsSnr'), param('ns3::WifiMode', 'ctsMode'), param('double', 'rtsSnr')], 
                   visibility='protected', is_virtual=True)
    ## rraa-wifi-manager.h: void ns3::RraaWifiRemoteStation::DoReportRxOk(double rxSnr, ns3::WifiMode txMode) [member function]
    cls.add_method('DoReportRxOk', 
                   'void', 
                   [param('double', 'rxSnr'), param('ns3::WifiMode', 'txMode')], 
                   visibility='protected', is_virtual=True)
    ## rraa-wifi-manager.h: ns3::WifiMode ns3::RraaWifiRemoteStation::DoGetDataMode(uint32_t size) [member function]
    cls.add_method('DoGetDataMode', 
                   'ns3::WifiMode', 
                   [param('uint32_t', 'size')], 
                   visibility='private', is_virtual=True)
    ## rraa-wifi-manager.h: ns3::WifiMode ns3::RraaWifiRemoteStation::DoGetRtsMode() [member function]
    cls.add_method('DoGetRtsMode', 
                   'ns3::WifiMode', 
                   [], 
                   visibility='private', is_virtual=True)
    ## rraa-wifi-manager.h: ns3::Ptr<ns3::WifiRemoteStationManager> ns3::RraaWifiRemoteStation::GetManager() const [member function]
    cls.add_method('GetManager', 
                   'ns3::Ptr< ns3::WifiRemoteStationManager >', 
                   [], 
                   is_const=True, visibility='private', is_virtual=True)
    return

def register_Ns3ThreeLogDistancePropagationLossModel_methods(root_module, cls):
    ## propagation-loss-model.h: static ns3::TypeId ns3::ThreeLogDistancePropagationLossModel::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## propagation-loss-model.h: ns3::ThreeLogDistancePropagationLossModel::ThreeLogDistancePropagationLossModel() [constructor]
    cls.add_constructor([])
    ## propagation-loss-model.h: double ns3::ThreeLogDistancePropagationLossModel::DoCalcRxPower(double txPowerDbm, ns3::Ptr<ns3::MobilityModel> a, ns3::Ptr<ns3::MobilityModel> b) const [member function]
    cls.add_method('DoCalcRxPower', 
                   'double', 
                   [param('double', 'txPowerDbm'), param('ns3::Ptr< ns3::MobilityModel >', 'a'), param('ns3::Ptr< ns3::MobilityModel >', 'b')], 
                   is_const=True, visibility='private', is_virtual=True)
    return

def register_Ns3WifiActionHeader_methods(root_module, cls):
    ## mgt-headers.h: ns3::WifiActionHeader::WifiActionHeader(ns3::WifiActionHeader const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::WifiActionHeader const &', 'arg0')])
    ## mgt-headers.h: ns3::WifiActionHeader::WifiActionHeader() [constructor]
    cls.add_constructor([])
    ## mgt-headers.h: uint32_t ns3::WifiActionHeader::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    ## mgt-headers.h: ns3::WifiActionHeader::ActionValue ns3::WifiActionHeader::GetAction() [member function]
    cls.add_method('GetAction', 
                   'ns3::WifiActionHeader::ActionValue', 
                   [])
    ## mgt-headers.h: ns3::WifiActionHeader::CategoryValue ns3::WifiActionHeader::GetCategory() [member function]
    cls.add_method('GetCategory', 
                   'ns3::WifiActionHeader::CategoryValue', 
                   [])
    ## mgt-headers.h: ns3::TypeId ns3::WifiActionHeader::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## mgt-headers.h: uint32_t ns3::WifiActionHeader::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## mgt-headers.h: static ns3::TypeId ns3::WifiActionHeader::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## mgt-headers.h: void ns3::WifiActionHeader::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    ## mgt-headers.h: void ns3::WifiActionHeader::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    ## mgt-headers.h: void ns3::WifiActionHeader::SetAction(ns3::WifiActionHeader::CategoryValue type, ns3::WifiActionHeader::ActionValue action) [member function]
    cls.add_method('SetAction', 
                   'void', 
                   [param('ns3::WifiActionHeader::CategoryValue', 'type'), param('ns3::WifiActionHeader::ActionValue', 'action')])
    return

def register_Ns3WifiActionHeaderActionValue_methods(root_module, cls):
    ## mgt-headers.h: ns3::WifiActionHeader::ActionValue::ActionValue() [constructor]
    cls.add_constructor([])
    ## mgt-headers.h: ns3::WifiActionHeader::ActionValue::ActionValue(ns3::WifiActionHeader::ActionValue const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::WifiActionHeader::ActionValue const &', 'arg0')])
    ## mgt-headers.h: ns3::WifiActionHeader::ActionValue::interwork [variable]
    cls.add_instance_attribute('interwork', 'ns3::WifiActionHeader::InterworkActionValue', is_const=False)
    ## mgt-headers.h: ns3::WifiActionHeader::ActionValue::linkMetrtic [variable]
    cls.add_instance_attribute('linkMetrtic', 'ns3::WifiActionHeader::LinkMetricActionValue', is_const=False)
    ## mgt-headers.h: ns3::WifiActionHeader::ActionValue::pathSelection [variable]
    cls.add_instance_attribute('pathSelection', 'ns3::WifiActionHeader::PathSelectionActionValue', is_const=False)
    ## mgt-headers.h: ns3::WifiActionHeader::ActionValue::peerLink [variable]
    cls.add_instance_attribute('peerLink', 'ns3::WifiActionHeader::PeerLinkMgtActionValue', is_const=False)
    ## mgt-headers.h: ns3::WifiActionHeader::ActionValue::resourceCoordination [variable]
    cls.add_instance_attribute('resourceCoordination', 'ns3::WifiActionHeader::ResourceCoordinationActionValue', is_const=False)
    return

def register_Ns3WifiMac_methods(root_module, cls):
    ## wifi-mac.h: ns3::WifiMac::WifiMac() [constructor]
    cls.add_constructor([])
    ## wifi-mac.h: ns3::WifiMac::WifiMac(ns3::WifiMac const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::WifiMac const &', 'arg0')])
    ## wifi-mac.h: void ns3::WifiMac::ConfigureStandard(ns3::WifiPhyStandard standard) [member function]
    cls.add_method('ConfigureStandard', 
                   'void', 
                   [param('ns3::WifiPhyStandard', 'standard')])
    ## wifi-mac.h: void ns3::WifiMac::Enqueue(ns3::Ptr<ns3::Packet const> packet, ns3::Mac48Address to, ns3::Mac48Address from) [member function]
    cls.add_method('Enqueue', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet'), param('ns3::Mac48Address', 'to'), param('ns3::Mac48Address', 'from')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-mac.h: void ns3::WifiMac::Enqueue(ns3::Ptr<ns3::Packet const> packet, ns3::Mac48Address to) [member function]
    cls.add_method('Enqueue', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet'), param('ns3::Mac48Address', 'to')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-mac.h: ns3::Time ns3::WifiMac::GetAckTimeout() const [member function]
    cls.add_method('GetAckTimeout', 
                   'ns3::Time', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-mac.h: ns3::Mac48Address ns3::WifiMac::GetAddress() const [member function]
    cls.add_method('GetAddress', 
                   'ns3::Mac48Address', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-mac.h: ns3::Mac48Address ns3::WifiMac::GetBssid() const [member function]
    cls.add_method('GetBssid', 
                   'ns3::Mac48Address', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-mac.h: ns3::Time ns3::WifiMac::GetCtsTimeout() const [member function]
    cls.add_method('GetCtsTimeout', 
                   'ns3::Time', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-mac.h: ns3::Time ns3::WifiMac::GetEifsNoDifs() const [member function]
    cls.add_method('GetEifsNoDifs', 
                   'ns3::Time', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-mac.h: uint32_t ns3::WifiMac::GetMaxMsduSize() const [member function]
    cls.add_method('GetMaxMsduSize', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## wifi-mac.h: ns3::Time ns3::WifiMac::GetMaxPropagationDelay() const [member function]
    cls.add_method('GetMaxPropagationDelay', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    ## wifi-mac.h: ns3::Time ns3::WifiMac::GetMsduLifetime() const [member function]
    cls.add_method('GetMsduLifetime', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    ## wifi-mac.h: ns3::Time ns3::WifiMac::GetPifs() const [member function]
    cls.add_method('GetPifs', 
                   'ns3::Time', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-mac.h: ns3::Time ns3::WifiMac::GetSifs() const [member function]
    cls.add_method('GetSifs', 
                   'ns3::Time', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-mac.h: ns3::Time ns3::WifiMac::GetSlot() const [member function]
    cls.add_method('GetSlot', 
                   'ns3::Time', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-mac.h: ns3::Ssid ns3::WifiMac::GetSsid() const [member function]
    cls.add_method('GetSsid', 
                   'ns3::Ssid', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-mac.h: static ns3::TypeId ns3::WifiMac::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## wifi-mac.h: void ns3::WifiMac::NotifyPromiscRx(ns3::Ptr<ns3::Packet const> packet) [member function]
    cls.add_method('NotifyPromiscRx', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet')])
    ## wifi-mac.h: void ns3::WifiMac::NotifyRx(ns3::Ptr<ns3::Packet const> packet) [member function]
    cls.add_method('NotifyRx', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet')])
    ## wifi-mac.h: void ns3::WifiMac::NotifyRxDrop(ns3::Ptr<ns3::Packet const> packet) [member function]
    cls.add_method('NotifyRxDrop', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet')])
    ## wifi-mac.h: void ns3::WifiMac::NotifyTx(ns3::Ptr<ns3::Packet const> packet) [member function]
    cls.add_method('NotifyTx', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet')])
    ## wifi-mac.h: void ns3::WifiMac::NotifyTxDrop(ns3::Ptr<ns3::Packet const> packet) [member function]
    cls.add_method('NotifyTxDrop', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet')])
    ## wifi-mac.h: void ns3::WifiMac::SetAckTimeout(ns3::Time ackTimeout) [member function]
    cls.add_method('SetAckTimeout', 
                   'void', 
                   [param('ns3::Time', 'ackTimeout')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-mac.h: void ns3::WifiMac::SetAddress(ns3::Mac48Address address) [member function]
    cls.add_method('SetAddress', 
                   'void', 
                   [param('ns3::Mac48Address', 'address')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-mac.h: void ns3::WifiMac::SetCtsTimeout(ns3::Time ctsTimeout) [member function]
    cls.add_method('SetCtsTimeout', 
                   'void', 
                   [param('ns3::Time', 'ctsTimeout')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-mac.h: void ns3::WifiMac::SetEifsNoDifs(ns3::Time eifsNoDifs) [member function]
    cls.add_method('SetEifsNoDifs', 
                   'void', 
                   [param('ns3::Time', 'eifsNoDifs')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-mac.h: void ns3::WifiMac::SetForwardUpCallback(ns3::Callback<void, ns3::Ptr<ns3::Packet>, ns3::Mac48Address, ns3::Mac48Address, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> upCallback) [member function]
    cls.add_method('SetForwardUpCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::Ptr< ns3::Packet >, ns3::Mac48Address, ns3::Mac48Address, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'upCallback')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-mac.h: void ns3::WifiMac::SetLinkDownCallback(ns3::Callback<void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> linkDown) [member function]
    cls.add_method('SetLinkDownCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'linkDown')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-mac.h: void ns3::WifiMac::SetLinkUpCallback(ns3::Callback<void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> linkUp) [member function]
    cls.add_method('SetLinkUpCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'linkUp')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-mac.h: void ns3::WifiMac::SetMaxPropagationDelay(ns3::Time delay) [member function]
    cls.add_method('SetMaxPropagationDelay', 
                   'void', 
                   [param('ns3::Time', 'delay')])
    ## wifi-mac.h: void ns3::WifiMac::SetPifs(ns3::Time pifs) [member function]
    cls.add_method('SetPifs', 
                   'void', 
                   [param('ns3::Time', 'pifs')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-mac.h: void ns3::WifiMac::SetSifs(ns3::Time sifs) [member function]
    cls.add_method('SetSifs', 
                   'void', 
                   [param('ns3::Time', 'sifs')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-mac.h: void ns3::WifiMac::SetSlot(ns3::Time slotTime) [member function]
    cls.add_method('SetSlot', 
                   'void', 
                   [param('ns3::Time', 'slotTime')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-mac.h: void ns3::WifiMac::SetSsid(ns3::Ssid ssid) [member function]
    cls.add_method('SetSsid', 
                   'void', 
                   [param('ns3::Ssid', 'ssid')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-mac.h: void ns3::WifiMac::SetWifiPhy(ns3::Ptr<ns3::WifiPhy> phy) [member function]
    cls.add_method('SetWifiPhy', 
                   'void', 
                   [param('ns3::Ptr< ns3::WifiPhy >', 'phy')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-mac.h: void ns3::WifiMac::SetWifiRemoteStationManager(ns3::Ptr<ns3::WifiRemoteStationManager> stationManager) [member function]
    cls.add_method('SetWifiRemoteStationManager', 
                   'void', 
                   [param('ns3::Ptr< ns3::WifiRemoteStationManager >', 'stationManager')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-mac.h: bool ns3::WifiMac::SupportsSendFrom() const [member function]
    cls.add_method('SupportsSendFrom', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-mac.h: void ns3::WifiMac::ConfigureCCHDcf(ns3::Ptr<ns3::Dcf> dcf, uint32_t cwmin, uint32_t cwmax, ns3::AccessClass ac) [member function]
    cls.add_method('ConfigureCCHDcf', 
                   'void', 
                   [param('ns3::Ptr< ns3::Dcf >', 'dcf'), param('uint32_t', 'cwmin'), param('uint32_t', 'cwmax'), param('ns3::AccessClass', 'ac')], 
                   visibility='protected')
    ## wifi-mac.h: void ns3::WifiMac::ConfigureDcf(ns3::Ptr<ns3::Dcf> dcf, uint32_t cwmin, uint32_t cwmax, ns3::AccessClass ac) [member function]
    cls.add_method('ConfigureDcf', 
                   'void', 
                   [param('ns3::Ptr< ns3::Dcf >', 'dcf'), param('uint32_t', 'cwmin'), param('uint32_t', 'cwmax'), param('ns3::AccessClass', 'ac')], 
                   visibility='protected')
    ## wifi-mac.h: void ns3::WifiMac::FinishConfigureStandard(ns3::WifiPhyStandard standard) [member function]
    cls.add_method('FinishConfigureStandard', 
                   'void', 
                   [param('ns3::WifiPhyStandard', 'standard')], 
                   is_pure_virtual=True, visibility='private', is_virtual=True)
    return

def register_Ns3WifiMacHeader_methods(root_module, cls):
    ## wifi-mac-header.h: ns3::WifiMacHeader::WifiMacHeader(ns3::WifiMacHeader const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::WifiMacHeader const &', 'arg0')])
    ## wifi-mac-header.h: ns3::WifiMacHeader::WifiMacHeader() [constructor]
    cls.add_constructor([])
    ## wifi-mac-header.h: uint32_t ns3::WifiMacHeader::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    ## wifi-mac-header.h: ns3::Mac48Address ns3::WifiMacHeader::GetAddr1() const [member function]
    cls.add_method('GetAddr1', 
                   'ns3::Mac48Address', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h: ns3::Mac48Address ns3::WifiMacHeader::GetAddr2() const [member function]
    cls.add_method('GetAddr2', 
                   'ns3::Mac48Address', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h: ns3::Mac48Address ns3::WifiMacHeader::GetAddr3() const [member function]
    cls.add_method('GetAddr3', 
                   'ns3::Mac48Address', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h: ns3::Mac48Address ns3::WifiMacHeader::GetAddr4() const [member function]
    cls.add_method('GetAddr4', 
                   'ns3::Mac48Address', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h: ns3::Time ns3::WifiMacHeader::GetDuration() const [member function]
    cls.add_method('GetDuration', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h: uint16_t ns3::WifiMacHeader::GetFragmentNumber() const [member function]
    cls.add_method('GetFragmentNumber', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h: ns3::TypeId ns3::WifiMacHeader::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## wifi-mac-header.h: ns3::WifiMacHeader::QosAckPolicy ns3::WifiMacHeader::GetQosAckPolicy() const [member function]
    cls.add_method('GetQosAckPolicy', 
                   'ns3::WifiMacHeader::QosAckPolicy', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h: uint8_t ns3::WifiMacHeader::GetQosTid() const [member function]
    cls.add_method('GetQosTid', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h: uint8_t ns3::WifiMacHeader::GetQosTxopLimit() const [member function]
    cls.add_method('GetQosTxopLimit', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h: uint16_t ns3::WifiMacHeader::GetRawDuration() const [member function]
    cls.add_method('GetRawDuration', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h: uint16_t ns3::WifiMacHeader::GetSequenceControl() const [member function]
    cls.add_method('GetSequenceControl', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h: uint16_t ns3::WifiMacHeader::GetSequenceNumber() const [member function]
    cls.add_method('GetSequenceNumber', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h: uint32_t ns3::WifiMacHeader::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## wifi-mac-header.h: uint32_t ns3::WifiMacHeader::GetSize() const [member function]
    cls.add_method('GetSize', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h: ns3::WifiMacType ns3::WifiMacHeader::GetType() const [member function]
    cls.add_method('GetType', 
                   'ns3::WifiMacType', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h: static ns3::TypeId ns3::WifiMacHeader::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## wifi-mac-header.h: char const * ns3::WifiMacHeader::GetTypeString() const [member function]
    cls.add_method('GetTypeString', 
                   'char const *', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h: bool ns3::WifiMacHeader::IsAck() const [member function]
    cls.add_method('IsAck', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h: bool ns3::WifiMacHeader::IsAction() const [member function]
    cls.add_method('IsAction', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h: bool ns3::WifiMacHeader::IsAssocReq() const [member function]
    cls.add_method('IsAssocReq', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h: bool ns3::WifiMacHeader::IsAssocResp() const [member function]
    cls.add_method('IsAssocResp', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h: bool ns3::WifiMacHeader::IsAuthentication() const [member function]
    cls.add_method('IsAuthentication', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h: bool ns3::WifiMacHeader::IsBeacon() const [member function]
    cls.add_method('IsBeacon', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h: bool ns3::WifiMacHeader::IsCfpoll() const [member function]
    cls.add_method('IsCfpoll', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h: bool ns3::WifiMacHeader::IsCtl() const [member function]
    cls.add_method('IsCtl', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h: bool ns3::WifiMacHeader::IsCts() const [member function]
    cls.add_method('IsCts', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h: bool ns3::WifiMacHeader::IsData() const [member function]
    cls.add_method('IsData', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h: bool ns3::WifiMacHeader::IsDeauthentication() const [member function]
    cls.add_method('IsDeauthentication', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h: bool ns3::WifiMacHeader::IsDisassociation() const [member function]
    cls.add_method('IsDisassociation', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h: bool ns3::WifiMacHeader::IsFromDs() const [member function]
    cls.add_method('IsFromDs', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h: bool ns3::WifiMacHeader::IsMgt() const [member function]
    cls.add_method('IsMgt', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h: bool ns3::WifiMacHeader::IsMoreFragments() const [member function]
    cls.add_method('IsMoreFragments', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h: bool ns3::WifiMacHeader::IsMultihopAction() const [member function]
    cls.add_method('IsMultihopAction', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h: bool ns3::WifiMacHeader::IsProbeReq() const [member function]
    cls.add_method('IsProbeReq', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h: bool ns3::WifiMacHeader::IsProbeResp() const [member function]
    cls.add_method('IsProbeResp', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h: bool ns3::WifiMacHeader::IsQosAck() const [member function]
    cls.add_method('IsQosAck', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h: bool ns3::WifiMacHeader::IsQosAmsdu() const [member function]
    cls.add_method('IsQosAmsdu', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h: bool ns3::WifiMacHeader::IsQosBlockAck() const [member function]
    cls.add_method('IsQosBlockAck', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h: bool ns3::WifiMacHeader::IsQosData() const [member function]
    cls.add_method('IsQosData', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h: bool ns3::WifiMacHeader::IsQosEosp() const [member function]
    cls.add_method('IsQosEosp', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h: bool ns3::WifiMacHeader::IsQosNoAck() const [member function]
    cls.add_method('IsQosNoAck', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h: bool ns3::WifiMacHeader::IsReassocReq() const [member function]
    cls.add_method('IsReassocReq', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h: bool ns3::WifiMacHeader::IsReassocResp() const [member function]
    cls.add_method('IsReassocResp', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h: bool ns3::WifiMacHeader::IsRetry() const [member function]
    cls.add_method('IsRetry', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h: bool ns3::WifiMacHeader::IsRts() const [member function]
    cls.add_method('IsRts', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h: bool ns3::WifiMacHeader::IsToDs() const [member function]
    cls.add_method('IsToDs', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h: void ns3::WifiMacHeader::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    ## wifi-mac-header.h: void ns3::WifiMacHeader::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    ## wifi-mac-header.h: void ns3::WifiMacHeader::SetAction() [member function]
    cls.add_method('SetAction', 
                   'void', 
                   [])
    ## wifi-mac-header.h: void ns3::WifiMacHeader::SetAddr1(ns3::Mac48Address address) [member function]
    cls.add_method('SetAddr1', 
                   'void', 
                   [param('ns3::Mac48Address', 'address')])
    ## wifi-mac-header.h: void ns3::WifiMacHeader::SetAddr2(ns3::Mac48Address address) [member function]
    cls.add_method('SetAddr2', 
                   'void', 
                   [param('ns3::Mac48Address', 'address')])
    ## wifi-mac-header.h: void ns3::WifiMacHeader::SetAddr3(ns3::Mac48Address address) [member function]
    cls.add_method('SetAddr3', 
                   'void', 
                   [param('ns3::Mac48Address', 'address')])
    ## wifi-mac-header.h: void ns3::WifiMacHeader::SetAddr4(ns3::Mac48Address address) [member function]
    cls.add_method('SetAddr4', 
                   'void', 
                   [param('ns3::Mac48Address', 'address')])
    ## wifi-mac-header.h: void ns3::WifiMacHeader::SetAssocReq() [member function]
    cls.add_method('SetAssocReq', 
                   'void', 
                   [])
    ## wifi-mac-header.h: void ns3::WifiMacHeader::SetAssocResp() [member function]
    cls.add_method('SetAssocResp', 
                   'void', 
                   [])
    ## wifi-mac-header.h: void ns3::WifiMacHeader::SetBeacon() [member function]
    cls.add_method('SetBeacon', 
                   'void', 
                   [])
    ## wifi-mac-header.h: void ns3::WifiMacHeader::SetDsFrom() [member function]
    cls.add_method('SetDsFrom', 
                   'void', 
                   [])
    ## wifi-mac-header.h: void ns3::WifiMacHeader::SetDsNotFrom() [member function]
    cls.add_method('SetDsNotFrom', 
                   'void', 
                   [])
    ## wifi-mac-header.h: void ns3::WifiMacHeader::SetDsNotTo() [member function]
    cls.add_method('SetDsNotTo', 
                   'void', 
                   [])
    ## wifi-mac-header.h: void ns3::WifiMacHeader::SetDsTo() [member function]
    cls.add_method('SetDsTo', 
                   'void', 
                   [])
    ## wifi-mac-header.h: void ns3::WifiMacHeader::SetDuration(ns3::Time duration) [member function]
    cls.add_method('SetDuration', 
                   'void', 
                   [param('ns3::Time', 'duration')])
    ## wifi-mac-header.h: void ns3::WifiMacHeader::SetFragmentNumber(uint8_t frag) [member function]
    cls.add_method('SetFragmentNumber', 
                   'void', 
                   [param('uint8_t', 'frag')])
    ## wifi-mac-header.h: void ns3::WifiMacHeader::SetId(uint16_t id) [member function]
    cls.add_method('SetId', 
                   'void', 
                   [param('uint16_t', 'id')])
    ## wifi-mac-header.h: void ns3::WifiMacHeader::SetMoreFragments() [member function]
    cls.add_method('SetMoreFragments', 
                   'void', 
                   [])
    ## wifi-mac-header.h: void ns3::WifiMacHeader::SetMultihopAction() [member function]
    cls.add_method('SetMultihopAction', 
                   'void', 
                   [])
    ## wifi-mac-header.h: void ns3::WifiMacHeader::SetNoMoreFragments() [member function]
    cls.add_method('SetNoMoreFragments', 
                   'void', 
                   [])
    ## wifi-mac-header.h: void ns3::WifiMacHeader::SetNoRetry() [member function]
    cls.add_method('SetNoRetry', 
                   'void', 
                   [])
    ## wifi-mac-header.h: void ns3::WifiMacHeader::SetProbeReq() [member function]
    cls.add_method('SetProbeReq', 
                   'void', 
                   [])
    ## wifi-mac-header.h: void ns3::WifiMacHeader::SetProbeResp() [member function]
    cls.add_method('SetProbeResp', 
                   'void', 
                   [])
    ## wifi-mac-header.h: void ns3::WifiMacHeader::SetQosAckPolicy(ns3::WifiMacHeader::QosAckPolicy arg0) [member function]
    cls.add_method('SetQosAckPolicy', 
                   'void', 
                   [param('ns3::WifiMacHeader::QosAckPolicy', 'arg0')])
    ## wifi-mac-header.h: void ns3::WifiMacHeader::SetQosAmsdu() [member function]
    cls.add_method('SetQosAmsdu', 
                   'void', 
                   [])
    ## wifi-mac-header.h: void ns3::WifiMacHeader::SetQosEosp() [member function]
    cls.add_method('SetQosEosp', 
                   'void', 
                   [])
    ## wifi-mac-header.h: void ns3::WifiMacHeader::SetQosNoAmsdu() [member function]
    cls.add_method('SetQosNoAmsdu', 
                   'void', 
                   [])
    ## wifi-mac-header.h: void ns3::WifiMacHeader::SetQosNoEosp() [member function]
    cls.add_method('SetQosNoEosp', 
                   'void', 
                   [])
    ## wifi-mac-header.h: void ns3::WifiMacHeader::SetQosTid(uint8_t tid) [member function]
    cls.add_method('SetQosTid', 
                   'void', 
                   [param('uint8_t', 'tid')])
    ## wifi-mac-header.h: void ns3::WifiMacHeader::SetQosTxopLimit(uint8_t txop) [member function]
    cls.add_method('SetQosTxopLimit', 
                   'void', 
                   [param('uint8_t', 'txop')])
    ## wifi-mac-header.h: void ns3::WifiMacHeader::SetRawDuration(uint16_t duration) [member function]
    cls.add_method('SetRawDuration', 
                   'void', 
                   [param('uint16_t', 'duration')])
    ## wifi-mac-header.h: void ns3::WifiMacHeader::SetRetry() [member function]
    cls.add_method('SetRetry', 
                   'void', 
                   [])
    ## wifi-mac-header.h: void ns3::WifiMacHeader::SetSequenceNumber(uint16_t seq) [member function]
    cls.add_method('SetSequenceNumber', 
                   'void', 
                   [param('uint16_t', 'seq')])
    ## wifi-mac-header.h: void ns3::WifiMacHeader::SetType(ns3::WifiMacType type) [member function]
    cls.add_method('SetType', 
                   'void', 
                   [param('ns3::WifiMacType', 'type')])
    ## wifi-mac-header.h: void ns3::WifiMacHeader::SetTypeData() [member function]
    cls.add_method('SetTypeData', 
                   'void', 
                   [])
    return

def register_Ns3WifiPhy_methods(root_module, cls):
    ## wifi-phy.h: ns3::WifiPhy::WifiPhy(ns3::WifiPhy const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::WifiPhy const &', 'arg0')])
    ## wifi-phy.h: ns3::WifiPhy::WifiPhy() [constructor]
    cls.add_constructor([])
    ## wifi-phy.h: double ns3::WifiPhy::CalculateSnr(ns3::WifiMode txMode, double ber) const [member function]
    cls.add_method('CalculateSnr', 
                   'double', 
                   [param('ns3::WifiMode', 'txMode'), param('double', 'ber')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-phy.h: ns3::Time ns3::WifiPhy::CalculateTxDuration(uint32_t size, ns3::WifiMode payloadMode, ns3::WifiPreamble preamble) const [member function]
    cls.add_method('CalculateTxDuration', 
                   'ns3::Time', 
                   [param('uint32_t', 'size'), param('ns3::WifiMode', 'payloadMode'), param('ns3::WifiPreamble', 'preamble')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-phy.h: void ns3::WifiPhy::ConfigureStandard(ns3::WifiPhyStandard standard) [member function]
    cls.add_method('ConfigureStandard', 
                   'void', 
                   [param('ns3::WifiPhyStandard', 'standard')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-phy.h: static ns3::WifiMode ns3::WifiPhy::Get11mbb() [member function]
    cls.add_method('Get11mbb', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h: static ns3::WifiMode ns3::WifiPhy::Get12mb10Mhz() [member function]
    cls.add_method('Get12mb10Mhz', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h: static ns3::WifiMode ns3::WifiPhy::Get12mb5Mhz() [member function]
    cls.add_method('Get12mb5Mhz', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h: static ns3::WifiMode ns3::WifiPhy::Get12mba() [member function]
    cls.add_method('Get12mba', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h: static ns3::WifiMode ns3::WifiPhy::Get13_5mb5Mhz() [member function]
    cls.add_method('Get13_5mb5Mhz', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h: static ns3::WifiMode ns3::WifiPhy::Get18mb10Mhz() [member function]
    cls.add_method('Get18mb10Mhz', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h: static ns3::WifiMode ns3::WifiPhy::Get18mba() [member function]
    cls.add_method('Get18mba', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h: static ns3::WifiMode ns3::WifiPhy::Get1_5mb5Mhz() [member function]
    cls.add_method('Get1_5mb5Mhz', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h: static ns3::WifiMode ns3::WifiPhy::Get1mbb() [member function]
    cls.add_method('Get1mbb', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h: static ns3::WifiMode ns3::WifiPhy::Get24mb10Mhz() [member function]
    cls.add_method('Get24mb10Mhz', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h: static ns3::WifiMode ns3::WifiPhy::Get24mba() [member function]
    cls.add_method('Get24mba', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h: static ns3::WifiMode ns3::WifiPhy::Get27mb10Mhz() [member function]
    cls.add_method('Get27mb10Mhz', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h: static ns3::WifiMode ns3::WifiPhy::Get2_25mb5Mhz() [member function]
    cls.add_method('Get2_25mb5Mhz', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h: static ns3::WifiMode ns3::WifiPhy::Get2mbb() [member function]
    cls.add_method('Get2mbb', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h: static ns3::WifiMode ns3::WifiPhy::Get36mba() [member function]
    cls.add_method('Get36mba', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h: static ns3::WifiMode ns3::WifiPhy::Get3mb10Mhz() [member function]
    cls.add_method('Get3mb10Mhz', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h: static ns3::WifiMode ns3::WifiPhy::Get3mb5Mhz() [member function]
    cls.add_method('Get3mb5Mhz', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h: static ns3::WifiMode ns3::WifiPhy::Get48mba() [member function]
    cls.add_method('Get48mba', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h: static ns3::WifiMode ns3::WifiPhy::Get4_5mb10Mhz() [member function]
    cls.add_method('Get4_5mb10Mhz', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h: static ns3::WifiMode ns3::WifiPhy::Get4_5mb5Mhz() [member function]
    cls.add_method('Get4_5mb5Mhz', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h: static ns3::WifiMode ns3::WifiPhy::Get54mba() [member function]
    cls.add_method('Get54mba', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h: static ns3::WifiMode ns3::WifiPhy::Get5_5mbb() [member function]
    cls.add_method('Get5_5mbb', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h: static ns3::WifiMode ns3::WifiPhy::Get6mb10Mhz() [member function]
    cls.add_method('Get6mb10Mhz', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h: static ns3::WifiMode ns3::WifiPhy::Get6mb5Mhz() [member function]
    cls.add_method('Get6mb5Mhz', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h: static ns3::WifiMode ns3::WifiPhy::Get6mba() [member function]
    cls.add_method('Get6mba', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h: static ns3::WifiMode ns3::WifiPhy::Get9mb10Mhz() [member function]
    cls.add_method('Get9mb10Mhz', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h: static ns3::WifiMode ns3::WifiPhy::Get9mb5Mhz() [member function]
    cls.add_method('Get9mb5Mhz', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h: static ns3::WifiMode ns3::WifiPhy::Get9mba() [member function]
    cls.add_method('Get9mba', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h: ns3::Ptr<ns3::WifiChannel> ns3::WifiPhy::GetChannel() const [member function]
    cls.add_method('GetChannel', 
                   'ns3::Ptr< ns3::WifiChannel >', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-phy.h: uint16_t ns3::WifiPhy::GetChannelNumber() const [member function]
    cls.add_method('GetChannelNumber', 
                   'uint16_t', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-phy.h: ns3::Time ns3::WifiPhy::GetDelayUntilIdle() [member function]
    cls.add_method('GetDelayUntilIdle', 
                   'ns3::Time', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-phy.h: ns3::Time ns3::WifiPhy::GetLastRxStartTime() const [member function]
    cls.add_method('GetLastRxStartTime', 
                   'ns3::Time', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-phy.h: ns3::WifiMode ns3::WifiPhy::GetMode(uint32_t mode) const [member function]
    cls.add_method('GetMode', 
                   'ns3::WifiMode', 
                   [param('uint32_t', 'mode')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-phy.h: uint32_t ns3::WifiPhy::GetNModes() const [member function]
    cls.add_method('GetNModes', 
                   'uint32_t', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-phy.h: uint32_t ns3::WifiPhy::GetNTxPower() const [member function]
    cls.add_method('GetNTxPower', 
                   'uint32_t', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-phy.h: ns3::Time ns3::WifiPhy::GetStateDuration() [member function]
    cls.add_method('GetStateDuration', 
                   'ns3::Time', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-phy.h: double ns3::WifiPhy::GetTxPowerEnd() const [member function]
    cls.add_method('GetTxPowerEnd', 
                   'double', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-phy.h: double ns3::WifiPhy::GetTxPowerStart() const [member function]
    cls.add_method('GetTxPowerStart', 
                   'double', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-phy.h: static ns3::TypeId ns3::WifiPhy::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## wifi-phy.h: bool ns3::WifiPhy::IsStateBusy() [member function]
    cls.add_method('IsStateBusy', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-phy.h: bool ns3::WifiPhy::IsStateCcaBusy() [member function]
    cls.add_method('IsStateCcaBusy', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-phy.h: bool ns3::WifiPhy::IsStateIdle() [member function]
    cls.add_method('IsStateIdle', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-phy.h: bool ns3::WifiPhy::IsStateRx() [member function]
    cls.add_method('IsStateRx', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-phy.h: bool ns3::WifiPhy::IsStateSwitching() [member function]
    cls.add_method('IsStateSwitching', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-phy.h: bool ns3::WifiPhy::IsStateTx() [member function]
    cls.add_method('IsStateTx', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-phy.h: void ns3::WifiPhy::NotifyPromiscSniffRx(ns3::Ptr<ns3::Packet const> packet, uint16_t channelFreqMhz, uint16_t channelNumber, uint32_t rate, bool isShortPreamble, double signalDbm, double noiseDbm) [member function]
    cls.add_method('NotifyPromiscSniffRx', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet'), param('uint16_t', 'channelFreqMhz'), param('uint16_t', 'channelNumber'), param('uint32_t', 'rate'), param('bool', 'isShortPreamble'), param('double', 'signalDbm'), param('double', 'noiseDbm')])
    ## wifi-phy.h: void ns3::WifiPhy::NotifyPromiscSniffTx(ns3::Ptr<ns3::Packet const> packet, uint16_t channelFreqMhz, uint16_t channelNumber, uint32_t rate, bool isShortPreamble) [member function]
    cls.add_method('NotifyPromiscSniffTx', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet'), param('uint16_t', 'channelFreqMhz'), param('uint16_t', 'channelNumber'), param('uint32_t', 'rate'), param('bool', 'isShortPreamble')])
    ## wifi-phy.h: void ns3::WifiPhy::NotifyRxBegin(ns3::Ptr<ns3::Packet const> packet) [member function]
    cls.add_method('NotifyRxBegin', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet')])
    ## wifi-phy.h: void ns3::WifiPhy::NotifyRxDrop(ns3::Ptr<ns3::Packet const> packet) [member function]
    cls.add_method('NotifyRxDrop', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet')])
    ## wifi-phy.h: void ns3::WifiPhy::NotifyRxEnd(ns3::Ptr<ns3::Packet const> packet) [member function]
    cls.add_method('NotifyRxEnd', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet')])
    ## wifi-phy.h: void ns3::WifiPhy::NotifyTxBegin(ns3::Ptr<ns3::Packet const> packet) [member function]
    cls.add_method('NotifyTxBegin', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet')])
    ## wifi-phy.h: void ns3::WifiPhy::NotifyTxDrop(ns3::Ptr<ns3::Packet const> packet) [member function]
    cls.add_method('NotifyTxDrop', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet')])
    ## wifi-phy.h: void ns3::WifiPhy::NotifyTxEnd(ns3::Ptr<ns3::Packet const> packet) [member function]
    cls.add_method('NotifyTxEnd', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet')])
    ## wifi-phy.h: void ns3::WifiPhy::RegisterListener(ns3::WifiPhyListener * listener) [member function]
    cls.add_method('RegisterListener', 
                   'void', 
                   [param('ns3::WifiPhyListener *', 'listener')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-phy.h: void ns3::WifiPhy::SendPacket(ns3::Ptr<ns3::Packet const> packet, ns3::WifiMode mode, ns3::WifiPreamble preamble, uint8_t txPowerLevel) [member function]
    cls.add_method('SendPacket', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet'), param('ns3::WifiMode', 'mode'), param('ns3::WifiPreamble', 'preamble'), param('uint8_t', 'txPowerLevel')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-phy.h: void ns3::WifiPhy::SetChannelNumber(uint16_t id) [member function]
    cls.add_method('SetChannelNumber', 
                   'void', 
                   [param('uint16_t', 'id')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-phy.h: void ns3::WifiPhy::SetReceiveErrorCallback(ns3::Callback<void,ns3::Ptr<const ns3::Packet>,double,ns3::empty,ns3::empty,ns3::empty,ns3::empty,ns3::empty,ns3::empty,ns3::empty> callback) [member function]
    cls.add_method('SetReceiveErrorCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::Ptr< ns3::Packet const >, double, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'callback')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-phy.h: void ns3::WifiPhy::SetReceiveOkCallback(ns3::Callback<void,ns3::Ptr<ns3::Packet>,double,ns3::WifiMode,ns3::WifiPreamble,ns3::empty,ns3::empty,ns3::empty,ns3::empty,ns3::empty> callback) [member function]
    cls.add_method('SetReceiveOkCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::Ptr< ns3::Packet >, double, ns3::WifiMode, ns3::WifiPreamble, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'callback')], 
                   is_pure_virtual=True, is_virtual=True)
    return

def register_Ns3WifiRemoteStationManager_methods(root_module, cls):
    ## wifi-remote-station-manager.h: ns3::WifiRemoteStationManager::WifiRemoteStationManager(ns3::WifiRemoteStationManager const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::WifiRemoteStationManager const &', 'arg0')])
    ## wifi-remote-station-manager.h: ns3::WifiRemoteStationManager::WifiRemoteStationManager() [constructor]
    cls.add_constructor([])
    ## wifi-remote-station-manager.h: void ns3::WifiRemoteStationManager::AddBasicMode(ns3::WifiMode mode) [member function]
    cls.add_method('AddBasicMode', 
                   'void', 
                   [param('ns3::WifiMode', 'mode')])
    ## wifi-remote-station-manager.h: __gnu_cxx::__normal_iterator<const ns3::WifiMode*,std::vector<ns3::WifiMode, std::allocator<ns3::WifiMode> > > ns3::WifiRemoteStationManager::BeginBasicModes() const [member function]
    cls.add_method('BeginBasicModes', 
                   '__gnu_cxx::__normal_iterator< ns3::WifiMode const *, std::vector< ns3::WifiMode > >', 
                   [], 
                   is_const=True)
    ## wifi-remote-station-manager.h: __gnu_cxx::__normal_iterator<const ns3::WifiMode*,std::vector<ns3::WifiMode, std::allocator<ns3::WifiMode> > > ns3::WifiRemoteStationManager::EndBasicModes() const [member function]
    cls.add_method('EndBasicModes', 
                   '__gnu_cxx::__normal_iterator< ns3::WifiMode const *, std::vector< ns3::WifiMode > >', 
                   [], 
                   is_const=True)
    ## wifi-remote-station-manager.h: ns3::WifiMode ns3::WifiRemoteStationManager::GetBasicMode(uint32_t i) const [member function]
    cls.add_method('GetBasicMode', 
                   'ns3::WifiMode', 
                   [param('uint32_t', 'i')], 
                   is_const=True)
    ## wifi-remote-station-manager.h: ns3::WifiMode ns3::WifiRemoteStationManager::GetDefaultMode() const [member function]
    cls.add_method('GetDefaultMode', 
                   'ns3::WifiMode', 
                   [], 
                   is_const=True)
    ## wifi-remote-station-manager.h: uint32_t ns3::WifiRemoteStationManager::GetFragmentationThreshold() const [member function]
    cls.add_method('GetFragmentationThreshold', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## wifi-remote-station-manager.h: uint32_t ns3::WifiRemoteStationManager::GetMaxSlrc() const [member function]
    cls.add_method('GetMaxSlrc', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## wifi-remote-station-manager.h: uint32_t ns3::WifiRemoteStationManager::GetMaxSsrc() const [member function]
    cls.add_method('GetMaxSsrc', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## wifi-remote-station-manager.h: uint32_t ns3::WifiRemoteStationManager::GetNBasicModes() const [member function]
    cls.add_method('GetNBasicModes', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## wifi-remote-station-manager.h: ns3::WifiMode ns3::WifiRemoteStationManager::GetNonUnicastMode() const [member function]
    cls.add_method('GetNonUnicastMode', 
                   'ns3::WifiMode', 
                   [], 
                   is_const=True)
    ## wifi-remote-station-manager.h: uint32_t ns3::WifiRemoteStationManager::GetRtsCtsThreshold() const [member function]
    cls.add_method('GetRtsCtsThreshold', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## wifi-remote-station-manager.h: static ns3::TypeId ns3::WifiRemoteStationManager::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## wifi-remote-station-manager.h: bool ns3::WifiRemoteStationManager::IsLowLatency() const [member function]
    cls.add_method('IsLowLatency', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-remote-station-manager.h: ns3::WifiRemoteStation * ns3::WifiRemoteStationManager::Lookup(ns3::Mac48Address address) [member function]
    cls.add_method('Lookup', 
                   'ns3::WifiRemoteStation *', 
                   [param('ns3::Mac48Address', 'address')])
    ## wifi-remote-station-manager.h: ns3::WifiRemoteStation * ns3::WifiRemoteStationManager::LookupNonUnicast() [member function]
    cls.add_method('LookupNonUnicast', 
                   'ns3::WifiRemoteStation *', 
                   [])
    ## wifi-remote-station-manager.h: void ns3::WifiRemoteStationManager::Reset() [member function]
    cls.add_method('Reset', 
                   'void', 
                   [])
    ## wifi-remote-station-manager.h: void ns3::WifiRemoteStationManager::SetFragmentationThreshold(uint32_t threshold) [member function]
    cls.add_method('SetFragmentationThreshold', 
                   'void', 
                   [param('uint32_t', 'threshold')])
    ## wifi-remote-station-manager.h: void ns3::WifiRemoteStationManager::SetMaxSlrc(uint32_t maxSlrc) [member function]
    cls.add_method('SetMaxSlrc', 
                   'void', 
                   [param('uint32_t', 'maxSlrc')])
    ## wifi-remote-station-manager.h: void ns3::WifiRemoteStationManager::SetMaxSsrc(uint32_t maxSsrc) [member function]
    cls.add_method('SetMaxSsrc', 
                   'void', 
                   [param('uint32_t', 'maxSsrc')])
    ## wifi-remote-station-manager.h: void ns3::WifiRemoteStationManager::SetRtsCtsThreshold(uint32_t threshold) [member function]
    cls.add_method('SetRtsCtsThreshold', 
                   'void', 
                   [param('uint32_t', 'threshold')])
    ## wifi-remote-station-manager.h: void ns3::WifiRemoteStationManager::SetupPhy(ns3::Ptr<ns3::WifiPhy> phy) [member function]
    cls.add_method('SetupPhy', 
                   'void', 
                   [param('ns3::Ptr< ns3::WifiPhy >', 'phy')], 
                   is_virtual=True)
    ## wifi-remote-station-manager.h: void ns3::WifiRemoteStationManager::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## wifi-remote-station-manager.h: ns3::WifiRemoteStation * ns3::WifiRemoteStationManager::CreateStation() [member function]
    cls.add_method('CreateStation', 
                   'ns3::WifiRemoteStation *', 
                   [], 
                   is_pure_virtual=True, visibility='private', is_virtual=True)
    return

def register_Ns3YansWifiPhy_methods(root_module, cls):
    ## yans-wifi-phy.h: static ns3::TypeId ns3::YansWifiPhy::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## yans-wifi-phy.h: ns3::YansWifiPhy::YansWifiPhy() [constructor]
    cls.add_constructor([])
    ## yans-wifi-phy.h: void ns3::YansWifiPhy::SetChannel(ns3::Ptr<ns3::YansWifiChannel> channel) [member function]
    cls.add_method('SetChannel', 
                   'void', 
                   [param('ns3::Ptr< ns3::YansWifiChannel >', 'channel')])
    ## yans-wifi-phy.h: void ns3::YansWifiPhy::SetChannelNumber(uint16_t id) [member function]
    cls.add_method('SetChannelNumber', 
                   'void', 
                   [param('uint16_t', 'id')], 
                   is_virtual=True)
    ## yans-wifi-phy.h: uint16_t ns3::YansWifiPhy::GetChannelNumber() const [member function]
    cls.add_method('GetChannelNumber', 
                   'uint16_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## yans-wifi-phy.h: double ns3::YansWifiPhy::GetChannelFrequencyMhz() const [member function]
    cls.add_method('GetChannelFrequencyMhz', 
                   'double', 
                   [], 
                   is_const=True)
    ## yans-wifi-phy.h: void ns3::YansWifiPhy::StartReceivePacket(ns3::Ptr<ns3::Packet> packet, double rxPowerDbm, ns3::WifiMode mode, ns3::WifiPreamble preamble) [member function]
    cls.add_method('StartReceivePacket', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet >', 'packet'), param('double', 'rxPowerDbm'), param('ns3::WifiMode', 'mode'), param('ns3::WifiPreamble', 'preamble')])
    ## yans-wifi-phy.h: void ns3::YansWifiPhy::SetRxNoiseFigure(double noiseFigureDb) [member function]
    cls.add_method('SetRxNoiseFigure', 
                   'void', 
                   [param('double', 'noiseFigureDb')])
    ## yans-wifi-phy.h: void ns3::YansWifiPhy::SetTxPowerStart(double start) [member function]
    cls.add_method('SetTxPowerStart', 
                   'void', 
                   [param('double', 'start')])
    ## yans-wifi-phy.h: void ns3::YansWifiPhy::SetTxPowerEnd(double end) [member function]
    cls.add_method('SetTxPowerEnd', 
                   'void', 
                   [param('double', 'end')])
    ## yans-wifi-phy.h: void ns3::YansWifiPhy::SetNTxPower(uint32_t n) [member function]
    cls.add_method('SetNTxPower', 
                   'void', 
                   [param('uint32_t', 'n')])
    ## yans-wifi-phy.h: void ns3::YansWifiPhy::SetTxGain(double gain) [member function]
    cls.add_method('SetTxGain', 
                   'void', 
                   [param('double', 'gain')])
    ## yans-wifi-phy.h: void ns3::YansWifiPhy::SetRxGain(double gain) [member function]
    cls.add_method('SetRxGain', 
                   'void', 
                   [param('double', 'gain')])
    ## yans-wifi-phy.h: void ns3::YansWifiPhy::SetEdThreshold(double threshold) [member function]
    cls.add_method('SetEdThreshold', 
                   'void', 
                   [param('double', 'threshold')])
    ## yans-wifi-phy.h: void ns3::YansWifiPhy::SetCcaMode1Threshold(double threshold) [member function]
    cls.add_method('SetCcaMode1Threshold', 
                   'void', 
                   [param('double', 'threshold')])
    ## yans-wifi-phy.h: void ns3::YansWifiPhy::SetErrorRateModel(ns3::Ptr<ns3::ErrorRateModel> rate) [member function]
    cls.add_method('SetErrorRateModel', 
                   'void', 
                   [param('ns3::Ptr< ns3::ErrorRateModel >', 'rate')])
    ## yans-wifi-phy.h: void ns3::YansWifiPhy::SetDevice(ns3::Ptr<ns3::Object> device) [member function]
    cls.add_method('SetDevice', 
                   'void', 
                   [param('ns3::Ptr< ns3::Object >', 'device')])
    ## yans-wifi-phy.h: void ns3::YansWifiPhy::SetMobility(ns3::Ptr<ns3::Object> mobility) [member function]
    cls.add_method('SetMobility', 
                   'void', 
                   [param('ns3::Ptr< ns3::Object >', 'mobility')])
    ## yans-wifi-phy.h: double ns3::YansWifiPhy::GetRxNoiseFigure() const [member function]
    cls.add_method('GetRxNoiseFigure', 
                   'double', 
                   [], 
                   is_const=True)
    ## yans-wifi-phy.h: double ns3::YansWifiPhy::GetTxGain() const [member function]
    cls.add_method('GetTxGain', 
                   'double', 
                   [], 
                   is_const=True)
    ## yans-wifi-phy.h: double ns3::YansWifiPhy::GetRxGain() const [member function]
    cls.add_method('GetRxGain', 
                   'double', 
                   [], 
                   is_const=True)
    ## yans-wifi-phy.h: double ns3::YansWifiPhy::GetEdThreshold() const [member function]
    cls.add_method('GetEdThreshold', 
                   'double', 
                   [], 
                   is_const=True)
    ## yans-wifi-phy.h: double ns3::YansWifiPhy::GetCcaMode1Threshold() const [member function]
    cls.add_method('GetCcaMode1Threshold', 
                   'double', 
                   [], 
                   is_const=True)
    ## yans-wifi-phy.h: ns3::Ptr<ns3::ErrorRateModel> ns3::YansWifiPhy::GetErrorRateModel() const [member function]
    cls.add_method('GetErrorRateModel', 
                   'ns3::Ptr< ns3::ErrorRateModel >', 
                   [], 
                   is_const=True)
    ## yans-wifi-phy.h: ns3::Ptr<ns3::Object> ns3::YansWifiPhy::GetDevice() const [member function]
    cls.add_method('GetDevice', 
                   'ns3::Ptr< ns3::Object >', 
                   [], 
                   is_const=True)
    ## yans-wifi-phy.h: ns3::Ptr<ns3::Object> ns3::YansWifiPhy::GetMobility() [member function]
    cls.add_method('GetMobility', 
                   'ns3::Ptr< ns3::Object >', 
                   [])
    ## yans-wifi-phy.h: double ns3::YansWifiPhy::GetTxPowerStart() const [member function]
    cls.add_method('GetTxPowerStart', 
                   'double', 
                   [], 
                   is_const=True, is_virtual=True)
    ## yans-wifi-phy.h: double ns3::YansWifiPhy::GetTxPowerEnd() const [member function]
    cls.add_method('GetTxPowerEnd', 
                   'double', 
                   [], 
                   is_const=True, is_virtual=True)
    ## yans-wifi-phy.h: uint32_t ns3::YansWifiPhy::GetNTxPower() const [member function]
    cls.add_method('GetNTxPower', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## yans-wifi-phy.h: void ns3::YansWifiPhy::SetReceiveOkCallback(ns3::Callback<void,ns3::Ptr<ns3::Packet>,double,ns3::WifiMode,ns3::WifiPreamble,ns3::empty,ns3::empty,ns3::empty,ns3::empty,ns3::empty> callback) [member function]
    cls.add_method('SetReceiveOkCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::Ptr< ns3::Packet >, double, ns3::WifiMode, ns3::WifiPreamble, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'callback')], 
                   is_virtual=True)
    ## yans-wifi-phy.h: void ns3::YansWifiPhy::SetReceiveErrorCallback(ns3::Callback<void,ns3::Ptr<const ns3::Packet>,double,ns3::empty,ns3::empty,ns3::empty,ns3::empty,ns3::empty,ns3::empty,ns3::empty> callback) [member function]
    cls.add_method('SetReceiveErrorCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::Ptr< ns3::Packet const >, double, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'callback')], 
                   is_virtual=True)
    ## yans-wifi-phy.h: void ns3::YansWifiPhy::SendPacket(ns3::Ptr<ns3::Packet const> packet, ns3::WifiMode mode, ns3::WifiPreamble preamble, uint8_t txPowerLevel) [member function]
    cls.add_method('SendPacket', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet'), param('ns3::WifiMode', 'mode'), param('ns3::WifiPreamble', 'preamble'), param('uint8_t', 'txPowerLevel')], 
                   is_virtual=True)
    ## yans-wifi-phy.h: void ns3::YansWifiPhy::RegisterListener(ns3::WifiPhyListener * listener) [member function]
    cls.add_method('RegisterListener', 
                   'void', 
                   [param('ns3::WifiPhyListener *', 'listener')], 
                   is_virtual=True)
    ## yans-wifi-phy.h: bool ns3::YansWifiPhy::IsStateCcaBusy() [member function]
    cls.add_method('IsStateCcaBusy', 
                   'bool', 
                   [], 
                   is_virtual=True)
    ## yans-wifi-phy.h: bool ns3::YansWifiPhy::IsStateIdle() [member function]
    cls.add_method('IsStateIdle', 
                   'bool', 
                   [], 
                   is_virtual=True)
    ## yans-wifi-phy.h: bool ns3::YansWifiPhy::IsStateBusy() [member function]
    cls.add_method('IsStateBusy', 
                   'bool', 
                   [], 
                   is_virtual=True)
    ## yans-wifi-phy.h: bool ns3::YansWifiPhy::IsStateRx() [member function]
    cls.add_method('IsStateRx', 
                   'bool', 
                   [], 
                   is_virtual=True)
    ## yans-wifi-phy.h: bool ns3::YansWifiPhy::IsStateTx() [member function]
    cls.add_method('IsStateTx', 
                   'bool', 
                   [], 
                   is_virtual=True)
    ## yans-wifi-phy.h: bool ns3::YansWifiPhy::IsStateSwitching() [member function]
    cls.add_method('IsStateSwitching', 
                   'bool', 
                   [], 
                   is_virtual=True)
    ## yans-wifi-phy.h: ns3::Time ns3::YansWifiPhy::GetStateDuration() [member function]
    cls.add_method('GetStateDuration', 
                   'ns3::Time', 
                   [], 
                   is_virtual=True)
    ## yans-wifi-phy.h: ns3::Time ns3::YansWifiPhy::GetDelayUntilIdle() [member function]
    cls.add_method('GetDelayUntilIdle', 
                   'ns3::Time', 
                   [], 
                   is_virtual=True)
    ## yans-wifi-phy.h: ns3::Time ns3::YansWifiPhy::GetLastRxStartTime() const [member function]
    cls.add_method('GetLastRxStartTime', 
                   'ns3::Time', 
                   [], 
                   is_const=True, is_virtual=True)
    ## yans-wifi-phy.h: ns3::Time ns3::YansWifiPhy::CalculateTxDuration(uint32_t size, ns3::WifiMode payloadMode, ns3::WifiPreamble preamble) const [member function]
    cls.add_method('CalculateTxDuration', 
                   'ns3::Time', 
                   [param('uint32_t', 'size'), param('ns3::WifiMode', 'payloadMode'), param('ns3::WifiPreamble', 'preamble')], 
                   is_const=True, is_virtual=True)
    ## yans-wifi-phy.h: uint32_t ns3::YansWifiPhy::GetNModes() const [member function]
    cls.add_method('GetNModes', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## yans-wifi-phy.h: ns3::WifiMode ns3::YansWifiPhy::GetMode(uint32_t mode) const [member function]
    cls.add_method('GetMode', 
                   'ns3::WifiMode', 
                   [param('uint32_t', 'mode')], 
                   is_const=True, is_virtual=True)
    ## yans-wifi-phy.h: double ns3::YansWifiPhy::CalculateSnr(ns3::WifiMode txMode, double ber) const [member function]
    cls.add_method('CalculateSnr', 
                   'double', 
                   [param('ns3::WifiMode', 'txMode'), param('double', 'ber')], 
                   is_const=True, is_virtual=True)
    ## yans-wifi-phy.h: ns3::Ptr<ns3::WifiChannel> ns3::YansWifiPhy::GetChannel() const [member function]
    cls.add_method('GetChannel', 
                   'ns3::Ptr< ns3::WifiChannel >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## yans-wifi-phy.h: void ns3::YansWifiPhy::ConfigureStandard(ns3::WifiPhyStandard standard) [member function]
    cls.add_method('ConfigureStandard', 
                   'void', 
                   [param('ns3::WifiPhyStandard', 'standard')], 
                   is_virtual=True)
    ## yans-wifi-phy.h: void ns3::YansWifiPhy::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   visibility='private', is_virtual=True)
    return

def register_Ns3AarfWifiRemoteStation_methods(root_module, cls):
    ## aarf-wifi-manager.h: ns3::AarfWifiRemoteStation::AarfWifiRemoteStation(ns3::AarfWifiRemoteStation const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::AarfWifiRemoteStation const &', 'arg0')])
    ## aarf-wifi-manager.h: ns3::AarfWifiRemoteStation::AarfWifiRemoteStation(ns3::Ptr<ns3::AarfWifiManager> stations) [constructor]
    cls.add_constructor([param('ns3::Ptr< ns3::AarfWifiManager >', 'stations')])
    ## aarf-wifi-manager.h: ns3::Ptr<ns3::WifiRemoteStationManager> ns3::AarfWifiRemoteStation::GetManager() const [member function]
    cls.add_method('GetManager', 
                   'ns3::Ptr< ns3::WifiRemoteStationManager >', 
                   [], 
                   is_const=True, visibility='private', is_virtual=True)
    ## aarf-wifi-manager.h: void ns3::AarfWifiRemoteStation::ReportFailure() [member function]
    cls.add_method('ReportFailure', 
                   'void', 
                   [], 
                   visibility='private', is_virtual=True)
    ## aarf-wifi-manager.h: void ns3::AarfWifiRemoteStation::ReportRecoveryFailure() [member function]
    cls.add_method('ReportRecoveryFailure', 
                   'void', 
                   [], 
                   visibility='private', is_virtual=True)
    return

def register_Ns3AdhocWifiMac_methods(root_module, cls):
    ## adhoc-wifi-mac.h: static ns3::TypeId ns3::AdhocWifiMac::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## adhoc-wifi-mac.h: ns3::AdhocWifiMac::AdhocWifiMac() [constructor]
    cls.add_constructor([])
    ## adhoc-wifi-mac.h: void ns3::AdhocWifiMac::SetSlot(ns3::Time slotTime) [member function]
    cls.add_method('SetSlot', 
                   'void', 
                   [param('ns3::Time', 'slotTime')], 
                   is_virtual=True)
    ## adhoc-wifi-mac.h: void ns3::AdhocWifiMac::SetSifs(ns3::Time sifs) [member function]
    cls.add_method('SetSifs', 
                   'void', 
                   [param('ns3::Time', 'sifs')], 
                   is_virtual=True)
    ## adhoc-wifi-mac.h: void ns3::AdhocWifiMac::SetEifsNoDifs(ns3::Time eifsNoDifs) [member function]
    cls.add_method('SetEifsNoDifs', 
                   'void', 
                   [param('ns3::Time', 'eifsNoDifs')], 
                   is_virtual=True)
    ## adhoc-wifi-mac.h: void ns3::AdhocWifiMac::SetAckTimeout(ns3::Time ackTimeout) [member function]
    cls.add_method('SetAckTimeout', 
                   'void', 
                   [param('ns3::Time', 'ackTimeout')], 
                   is_virtual=True)
    ## adhoc-wifi-mac.h: void ns3::AdhocWifiMac::SetCtsTimeout(ns3::Time ctsTimeout) [member function]
    cls.add_method('SetCtsTimeout', 
                   'void', 
                   [param('ns3::Time', 'ctsTimeout')], 
                   is_virtual=True)
    ## adhoc-wifi-mac.h: void ns3::AdhocWifiMac::SetPifs(ns3::Time pifs) [member function]
    cls.add_method('SetPifs', 
                   'void', 
                   [param('ns3::Time', 'pifs')], 
                   is_virtual=True)
    ## adhoc-wifi-mac.h: ns3::Time ns3::AdhocWifiMac::GetSlot() const [member function]
    cls.add_method('GetSlot', 
                   'ns3::Time', 
                   [], 
                   is_const=True, is_virtual=True)
    ## adhoc-wifi-mac.h: ns3::Time ns3::AdhocWifiMac::GetSifs() const [member function]
    cls.add_method('GetSifs', 
                   'ns3::Time', 
                   [], 
                   is_const=True, is_virtual=True)
    ## adhoc-wifi-mac.h: ns3::Time ns3::AdhocWifiMac::GetEifsNoDifs() const [member function]
    cls.add_method('GetEifsNoDifs', 
                   'ns3::Time', 
                   [], 
                   is_const=True, is_virtual=True)
    ## adhoc-wifi-mac.h: ns3::Time ns3::AdhocWifiMac::GetAckTimeout() const [member function]
    cls.add_method('GetAckTimeout', 
                   'ns3::Time', 
                   [], 
                   is_const=True, is_virtual=True)
    ## adhoc-wifi-mac.h: ns3::Time ns3::AdhocWifiMac::GetCtsTimeout() const [member function]
    cls.add_method('GetCtsTimeout', 
                   'ns3::Time', 
                   [], 
                   is_const=True, is_virtual=True)
    ## adhoc-wifi-mac.h: ns3::Time ns3::AdhocWifiMac::GetPifs() const [member function]
    cls.add_method('GetPifs', 
                   'ns3::Time', 
                   [], 
                   is_const=True, is_virtual=True)
    ## adhoc-wifi-mac.h: void ns3::AdhocWifiMac::SetWifiPhy(ns3::Ptr<ns3::WifiPhy> phy) [member function]
    cls.add_method('SetWifiPhy', 
                   'void', 
                   [param('ns3::Ptr< ns3::WifiPhy >', 'phy')], 
                   is_virtual=True)
    ## adhoc-wifi-mac.h: void ns3::AdhocWifiMac::SetWifiRemoteStationManager(ns3::Ptr<ns3::WifiRemoteStationManager> stationManager) [member function]
    cls.add_method('SetWifiRemoteStationManager', 
                   'void', 
                   [param('ns3::Ptr< ns3::WifiRemoteStationManager >', 'stationManager')], 
                   is_virtual=True)
    ## adhoc-wifi-mac.h: void ns3::AdhocWifiMac::Enqueue(ns3::Ptr<ns3::Packet const> packet, ns3::Mac48Address to, ns3::Mac48Address from) [member function]
    cls.add_method('Enqueue', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet'), param('ns3::Mac48Address', 'to'), param('ns3::Mac48Address', 'from')], 
                   is_virtual=True)
    ## adhoc-wifi-mac.h: void ns3::AdhocWifiMac::Enqueue(ns3::Ptr<ns3::Packet const> packet, ns3::Mac48Address to) [member function]
    cls.add_method('Enqueue', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet'), param('ns3::Mac48Address', 'to')], 
                   is_virtual=True)
    ## adhoc-wifi-mac.h: bool ns3::AdhocWifiMac::SupportsSendFrom() const [member function]
    cls.add_method('SupportsSendFrom', 
                   'bool', 
                   [], 
                   is_const=True, is_virtual=True)
    ## adhoc-wifi-mac.h: void ns3::AdhocWifiMac::SetForwardUpCallback(ns3::Callback<void, ns3::Ptr<ns3::Packet>, ns3::Mac48Address, ns3::Mac48Address, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> upCallback) [member function]
    cls.add_method('SetForwardUpCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::Ptr< ns3::Packet >, ns3::Mac48Address, ns3::Mac48Address, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'upCallback')], 
                   is_virtual=True)
    ## adhoc-wifi-mac.h: void ns3::AdhocWifiMac::SetLinkUpCallback(ns3::Callback<void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> linkUp) [member function]
    cls.add_method('SetLinkUpCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'linkUp')], 
                   is_virtual=True)
    ## adhoc-wifi-mac.h: void ns3::AdhocWifiMac::SetLinkDownCallback(ns3::Callback<void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> linkDown) [member function]
    cls.add_method('SetLinkDownCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'linkDown')], 
                   is_virtual=True)
    ## adhoc-wifi-mac.h: ns3::Mac48Address ns3::AdhocWifiMac::GetAddress() const [member function]
    cls.add_method('GetAddress', 
                   'ns3::Mac48Address', 
                   [], 
                   is_const=True, is_virtual=True)
    ## adhoc-wifi-mac.h: ns3::Ssid ns3::AdhocWifiMac::GetSsid() const [member function]
    cls.add_method('GetSsid', 
                   'ns3::Ssid', 
                   [], 
                   is_const=True, is_virtual=True)
    ## adhoc-wifi-mac.h: void ns3::AdhocWifiMac::SetAddress(ns3::Mac48Address address) [member function]
    cls.add_method('SetAddress', 
                   'void', 
                   [param('ns3::Mac48Address', 'address')], 
                   is_virtual=True)
    ## adhoc-wifi-mac.h: void ns3::AdhocWifiMac::SetSsid(ns3::Ssid ssid) [member function]
    cls.add_method('SetSsid', 
                   'void', 
                   [param('ns3::Ssid', 'ssid')], 
                   is_virtual=True)
    ## adhoc-wifi-mac.h: ns3::Mac48Address ns3::AdhocWifiMac::GetBssid() const [member function]
    cls.add_method('GetBssid', 
                   'ns3::Mac48Address', 
                   [], 
                   is_const=True, is_virtual=True)
    ## adhoc-wifi-mac.h: void ns3::AdhocWifiMac::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   visibility='private', is_virtual=True)
    ## adhoc-wifi-mac.h: void ns3::AdhocWifiMac::FinishConfigureStandard(ns3::WifiPhyStandard standard) [member function]
    cls.add_method('FinishConfigureStandard', 
                   'void', 
                   [param('ns3::WifiPhyStandard', 'standard')], 
                   visibility='private', is_virtual=True)
    return

def register_Ns3AmrrWifiManager_methods(root_module, cls):
    ## amrr-wifi-manager.h: ns3::AmrrWifiManager::AmrrWifiManager(ns3::AmrrWifiManager const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::AmrrWifiManager const &', 'arg0')])
    ## amrr-wifi-manager.h: ns3::AmrrWifiManager::AmrrWifiManager() [constructor]
    cls.add_constructor([])
    ## amrr-wifi-manager.h: static ns3::TypeId ns3::AmrrWifiManager::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## amrr-wifi-manager.h: ns3::WifiRemoteStation * ns3::AmrrWifiManager::CreateStation() [member function]
    cls.add_method('CreateStation', 
                   'ns3::WifiRemoteStation *', 
                   [], 
                   visibility='private', is_virtual=True)
    return

def register_Ns3AmsduSubframeHeader_methods(root_module, cls):
    ## amsdu-subframe-header.h: ns3::AmsduSubframeHeader::AmsduSubframeHeader(ns3::AmsduSubframeHeader const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::AmsduSubframeHeader const &', 'arg0')])
    ## amsdu-subframe-header.h: ns3::AmsduSubframeHeader::AmsduSubframeHeader() [constructor]
    cls.add_constructor([])
    ## amsdu-subframe-header.h: uint32_t ns3::AmsduSubframeHeader::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    ## amsdu-subframe-header.h: ns3::Mac48Address ns3::AmsduSubframeHeader::GetDestinationAddr() const [member function]
    cls.add_method('GetDestinationAddr', 
                   'ns3::Mac48Address', 
                   [], 
                   is_const=True)
    ## amsdu-subframe-header.h: ns3::TypeId ns3::AmsduSubframeHeader::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## amsdu-subframe-header.h: uint16_t ns3::AmsduSubframeHeader::GetLength() const [member function]
    cls.add_method('GetLength', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## amsdu-subframe-header.h: uint32_t ns3::AmsduSubframeHeader::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## amsdu-subframe-header.h: ns3::Mac48Address ns3::AmsduSubframeHeader::GetSourceAddr() const [member function]
    cls.add_method('GetSourceAddr', 
                   'ns3::Mac48Address', 
                   [], 
                   is_const=True)
    ## amsdu-subframe-header.h: static ns3::TypeId ns3::AmsduSubframeHeader::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## amsdu-subframe-header.h: void ns3::AmsduSubframeHeader::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    ## amsdu-subframe-header.h: void ns3::AmsduSubframeHeader::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    ## amsdu-subframe-header.h: void ns3::AmsduSubframeHeader::SetDestinationAddr(ns3::Mac48Address to) [member function]
    cls.add_method('SetDestinationAddr', 
                   'void', 
                   [param('ns3::Mac48Address', 'to')])
    ## amsdu-subframe-header.h: void ns3::AmsduSubframeHeader::SetLength(uint16_t arg0) [member function]
    cls.add_method('SetLength', 
                   'void', 
                   [param('uint16_t', 'arg0')])
    ## amsdu-subframe-header.h: void ns3::AmsduSubframeHeader::SetSourceAddr(ns3::Mac48Address to) [member function]
    cls.add_method('SetSourceAddr', 
                   'void', 
                   [param('ns3::Mac48Address', 'to')])
    return

def register_Ns3ArfWifiManager_methods(root_module, cls):
    ## arf-wifi-manager.h: ns3::ArfWifiManager::ArfWifiManager(ns3::ArfWifiManager const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::ArfWifiManager const &', 'arg0')])
    ## arf-wifi-manager.h: ns3::ArfWifiManager::ArfWifiManager() [constructor]
    cls.add_constructor([])
    ## arf-wifi-manager.h: static ns3::TypeId ns3::ArfWifiManager::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## arf-wifi-manager.h: ns3::WifiRemoteStation * ns3::ArfWifiManager::CreateStation() [member function]
    cls.add_method('CreateStation', 
                   'ns3::WifiRemoteStation *', 
                   [], 
                   visibility='private', is_virtual=True)
    return

def register_Ns3ConstantRateWifiManager_methods(root_module, cls):
    ## constant-rate-wifi-manager.h: ns3::ConstantRateWifiManager::ConstantRateWifiManager(ns3::ConstantRateWifiManager const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::ConstantRateWifiManager const &', 'arg0')])
    ## constant-rate-wifi-manager.h: ns3::ConstantRateWifiManager::ConstantRateWifiManager() [constructor]
    cls.add_constructor([])
    ## constant-rate-wifi-manager.h: ns3::WifiMode ns3::ConstantRateWifiManager::GetCtlMode() const [member function]
    cls.add_method('GetCtlMode', 
                   'ns3::WifiMode', 
                   [], 
                   is_const=True)
    ## constant-rate-wifi-manager.h: ns3::WifiMode ns3::ConstantRateWifiManager::GetDataMode() const [member function]
    cls.add_method('GetDataMode', 
                   'ns3::WifiMode', 
                   [], 
                   is_const=True)
    ## constant-rate-wifi-manager.h: static ns3::TypeId ns3::ConstantRateWifiManager::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## constant-rate-wifi-manager.h: ns3::WifiRemoteStation * ns3::ConstantRateWifiManager::CreateStation() [member function]
    cls.add_method('CreateStation', 
                   'ns3::WifiRemoteStation *', 
                   [], 
                   visibility='private', is_virtual=True)
    return

def register_Ns3ConstantSpeedPropagationDelayModel_methods(root_module, cls):
    ## propagation-delay-model.h: ns3::ConstantSpeedPropagationDelayModel::ConstantSpeedPropagationDelayModel(ns3::ConstantSpeedPropagationDelayModel const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::ConstantSpeedPropagationDelayModel const &', 'arg0')])
    ## propagation-delay-model.h: ns3::ConstantSpeedPropagationDelayModel::ConstantSpeedPropagationDelayModel() [constructor]
    cls.add_constructor([])
    ## propagation-delay-model.h: ns3::Time ns3::ConstantSpeedPropagationDelayModel::GetDelay(ns3::Ptr<ns3::MobilityModel> a, ns3::Ptr<ns3::MobilityModel> b) const [member function]
    cls.add_method('GetDelay', 
                   'ns3::Time', 
                   [param('ns3::Ptr< ns3::MobilityModel >', 'a'), param('ns3::Ptr< ns3::MobilityModel >', 'b')], 
                   is_const=True, is_virtual=True)
    ## propagation-delay-model.h: double ns3::ConstantSpeedPropagationDelayModel::GetSpeed() const [member function]
    cls.add_method('GetSpeed', 
                   'double', 
                   [], 
                   is_const=True)
    ## propagation-delay-model.h: static ns3::TypeId ns3::ConstantSpeedPropagationDelayModel::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## propagation-delay-model.h: void ns3::ConstantSpeedPropagationDelayModel::SetSpeed(double speed) [member function]
    cls.add_method('SetSpeed', 
                   'void', 
                   [param('double', 'speed')])
    return

def register_Ns3Dcf_methods(root_module, cls):
    ## dcf.h: ns3::Dcf::Dcf() [constructor]
    cls.add_constructor([])
    ## dcf.h: ns3::Dcf::Dcf(ns3::Dcf const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Dcf const &', 'arg0')])
    ## dcf.h: uint32_t ns3::Dcf::GetAifsn() const [member function]
    cls.add_method('GetAifsn', 
                   'uint32_t', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## dcf.h: uint32_t ns3::Dcf::GetMaxCw() const [member function]
    cls.add_method('GetMaxCw', 
                   'uint32_t', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## dcf.h: uint32_t ns3::Dcf::GetMinCw() const [member function]
    cls.add_method('GetMinCw', 
                   'uint32_t', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## dcf.h: static ns3::TypeId ns3::Dcf::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## dcf.h: void ns3::Dcf::SetAifsn(uint32_t aifsn) [member function]
    cls.add_method('SetAifsn', 
                   'void', 
                   [param('uint32_t', 'aifsn')], 
                   is_pure_virtual=True, is_virtual=True)
    ## dcf.h: void ns3::Dcf::SetMaxCw(uint32_t maxCw) [member function]
    cls.add_method('SetMaxCw', 
                   'void', 
                   [param('uint32_t', 'maxCw')], 
                   is_pure_virtual=True, is_virtual=True)
    ## dcf.h: void ns3::Dcf::SetMinCw(uint32_t minCw) [member function]
    cls.add_method('SetMinCw', 
                   'void', 
                   [param('uint32_t', 'minCw')], 
                   is_pure_virtual=True, is_virtual=True)
    return

def register_Ns3EdcaTxopN_methods(root_module, cls):
    ## edca-txop-n.h: static ns3::TypeId ns3::EdcaTxopN::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## edca-txop-n.h: ns3::EdcaTxopN::EdcaTxopN() [constructor]
    cls.add_constructor([])
    ## edca-txop-n.h: void ns3::EdcaTxopN::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   is_virtual=True)
    ## edca-txop-n.h: void ns3::EdcaTxopN::SetLow(ns3::Ptr<ns3::MacLow> low) [member function]
    cls.add_method('SetLow', 
                   'void', 
                   [param('ns3::Ptr< ns3::MacLow >', 'low')])
    ## edca-txop-n.h: void ns3::EdcaTxopN::SetTxMiddle(ns3::MacTxMiddle * txMiddle) [member function]
    cls.add_method('SetTxMiddle', 
                   'void', 
                   [param('ns3::MacTxMiddle *', 'txMiddle')])
    ## edca-txop-n.h: void ns3::EdcaTxopN::SetManager(ns3::DcfManager * manager) [member function]
    cls.add_method('SetManager', 
                   'void', 
                   [param('ns3::DcfManager *', 'manager')])
    ## edca-txop-n.h: void ns3::EdcaTxopN::SetTxOkCallback(ns3::Callback<void, ns3::WifiMacHeader const&, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> callback) [member function]
    cls.add_method('SetTxOkCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::WifiMacHeader const &, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'callback')])
    ## edca-txop-n.h: void ns3::EdcaTxopN::SetTxFailedCallback(ns3::Callback<void, ns3::WifiMacHeader const&, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> callback) [member function]
    cls.add_method('SetTxFailedCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::WifiMacHeader const &, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'callback')])
    ## edca-txop-n.h: void ns3::EdcaTxopN::SetWifiRemoteStationManager(ns3::Ptr<ns3::WifiRemoteStationManager> remoteManager) [member function]
    cls.add_method('SetWifiRemoteStationManager', 
                   'void', 
                   [param('ns3::Ptr< ns3::WifiRemoteStationManager >', 'remoteManager')])
    ## edca-txop-n.h: void ns3::EdcaTxopN::SetTypeOfStation(ns3::TypeOfStation type) [member function]
    cls.add_method('SetTypeOfStation', 
                   'void', 
                   [param('ns3::TypeOfStation', 'type')])
    ## edca-txop-n.h: ns3::TypeOfStation ns3::EdcaTxopN::GetTypeOfStation() const [member function]
    cls.add_method('GetTypeOfStation', 
                   'ns3::TypeOfStation', 
                   [], 
                   is_const=True)
    ## edca-txop-n.h: void ns3::EdcaTxopN::SetMaxQueueSize(uint32_t size) [member function]
    cls.add_method('SetMaxQueueSize', 
                   'void', 
                   [param('uint32_t', 'size')])
    ## edca-txop-n.h: void ns3::EdcaTxopN::SetMaxQueueDelay(ns3::Time delay) [member function]
    cls.add_method('SetMaxQueueDelay', 
                   'void', 
                   [param('ns3::Time', 'delay')])
    ## edca-txop-n.h: void ns3::EdcaTxopN::SetMinCw(uint32_t minCw) [member function]
    cls.add_method('SetMinCw', 
                   'void', 
                   [param('uint32_t', 'minCw')], 
                   is_virtual=True)
    ## edca-txop-n.h: void ns3::EdcaTxopN::SetMaxCw(uint32_t maxCw) [member function]
    cls.add_method('SetMaxCw', 
                   'void', 
                   [param('uint32_t', 'maxCw')], 
                   is_virtual=True)
    ## edca-txop-n.h: void ns3::EdcaTxopN::SetAifsn(uint32_t aifsn) [member function]
    cls.add_method('SetAifsn', 
                   'void', 
                   [param('uint32_t', 'aifsn')], 
                   is_virtual=True)
    ## edca-txop-n.h: uint32_t ns3::EdcaTxopN::GetMinCw() const [member function]
    cls.add_method('GetMinCw', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## edca-txop-n.h: uint32_t ns3::EdcaTxopN::GetMaxCw() const [member function]
    cls.add_method('GetMaxCw', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## edca-txop-n.h: uint32_t ns3::EdcaTxopN::GetAifsn() const [member function]
    cls.add_method('GetAifsn', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## edca-txop-n.h: ns3::Ptr<ns3::MacLow> ns3::EdcaTxopN::Low() [member function]
    cls.add_method('Low', 
                   'ns3::Ptr< ns3::MacLow >', 
                   [])
    ## edca-txop-n.h: ns3::Ptr<ns3::MsduAggregator> ns3::EdcaTxopN::GetMsduAggregator() const [member function]
    cls.add_method('GetMsduAggregator', 
                   'ns3::Ptr< ns3::MsduAggregator >', 
                   [], 
                   is_const=True)
    ## edca-txop-n.h: bool ns3::EdcaTxopN::NeedsAccess() const [member function]
    cls.add_method('NeedsAccess', 
                   'bool', 
                   [], 
                   is_const=True)
    ## edca-txop-n.h: void ns3::EdcaTxopN::NotifyAccessGranted() [member function]
    cls.add_method('NotifyAccessGranted', 
                   'void', 
                   [])
    ## edca-txop-n.h: void ns3::EdcaTxopN::NotifyInternalCollision() [member function]
    cls.add_method('NotifyInternalCollision', 
                   'void', 
                   [])
    ## edca-txop-n.h: void ns3::EdcaTxopN::NotifyCollision() [member function]
    cls.add_method('NotifyCollision', 
                   'void', 
                   [])
    ## edca-txop-n.h: void ns3::EdcaTxopN::NotifyChannelSwitching() [member function]
    cls.add_method('NotifyChannelSwitching', 
                   'void', 
                   [])
    ## edca-txop-n.h: void ns3::EdcaTxopN::GotCts(double snr, ns3::WifiMode txMode) [member function]
    cls.add_method('GotCts', 
                   'void', 
                   [param('double', 'snr'), param('ns3::WifiMode', 'txMode')])
    ## edca-txop-n.h: void ns3::EdcaTxopN::MissedCts() [member function]
    cls.add_method('MissedCts', 
                   'void', 
                   [])
    ## edca-txop-n.h: void ns3::EdcaTxopN::GotAck(double snr, ns3::WifiMode txMode) [member function]
    cls.add_method('GotAck', 
                   'void', 
                   [param('double', 'snr'), param('ns3::WifiMode', 'txMode')])
    ## edca-txop-n.h: void ns3::EdcaTxopN::MissedAck() [member function]
    cls.add_method('MissedAck', 
                   'void', 
                   [])
    ## edca-txop-n.h: void ns3::EdcaTxopN::StartNext() [member function]
    cls.add_method('StartNext', 
                   'void', 
                   [])
    ## edca-txop-n.h: void ns3::EdcaTxopN::Cancel() [member function]
    cls.add_method('Cancel', 
                   'void', 
                   [])
    ## edca-txop-n.h: void ns3::EdcaTxopN::RestartAccessIfNeeded() [member function]
    cls.add_method('RestartAccessIfNeeded', 
                   'void', 
                   [])
    ## edca-txop-n.h: void ns3::EdcaTxopN::StartAccessIfNeeded() [member function]
    cls.add_method('StartAccessIfNeeded', 
                   'void', 
                   [])
    ## edca-txop-n.h: bool ns3::EdcaTxopN::NeedRts() [member function]
    cls.add_method('NeedRts', 
                   'bool', 
                   [])
    ## edca-txop-n.h: bool ns3::EdcaTxopN::NeedRtsRetransmission() [member function]
    cls.add_method('NeedRtsRetransmission', 
                   'bool', 
                   [])
    ## edca-txop-n.h: bool ns3::EdcaTxopN::NeedDataRetransmission() [member function]
    cls.add_method('NeedDataRetransmission', 
                   'bool', 
                   [])
    ## edca-txop-n.h: bool ns3::EdcaTxopN::NeedFragmentation() const [member function]
    cls.add_method('NeedFragmentation', 
                   'bool', 
                   [], 
                   is_const=True)
    ## edca-txop-n.h: uint32_t ns3::EdcaTxopN::GetNextFragmentSize() [member function]
    cls.add_method('GetNextFragmentSize', 
                   'uint32_t', 
                   [])
    ## edca-txop-n.h: uint32_t ns3::EdcaTxopN::GetFragmentSize() [member function]
    cls.add_method('GetFragmentSize', 
                   'uint32_t', 
                   [])
    ## edca-txop-n.h: uint32_t ns3::EdcaTxopN::GetFragmentOffset() [member function]
    cls.add_method('GetFragmentOffset', 
                   'uint32_t', 
                   [])
    ## edca-txop-n.h: ns3::WifiRemoteStation * ns3::EdcaTxopN::GetStation(ns3::Mac48Address to) const [member function]
    cls.add_method('GetStation', 
                   'ns3::WifiRemoteStation *', 
                   [param('ns3::Mac48Address', 'to')], 
                   is_const=True)
    ## edca-txop-n.h: bool ns3::EdcaTxopN::IsLastFragment() const [member function]
    cls.add_method('IsLastFragment', 
                   'bool', 
                   [], 
                   is_const=True)
    ## edca-txop-n.h: void ns3::EdcaTxopN::NextFragment() [member function]
    cls.add_method('NextFragment', 
                   'void', 
                   [])
    ## edca-txop-n.h: ns3::Ptr<ns3::Packet> ns3::EdcaTxopN::GetFragmentPacket(ns3::WifiMacHeader * hdr) [member function]
    cls.add_method('GetFragmentPacket', 
                   'ns3::Ptr< ns3::Packet >', 
                   [param('ns3::WifiMacHeader *', 'hdr')])
    ## edca-txop-n.h: void ns3::EdcaTxopN::Queue(ns3::Ptr<ns3::Packet const> packet, ns3::WifiMacHeader const & hdr) [member function]
    cls.add_method('Queue', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet'), param('ns3::WifiMacHeader const &', 'hdr')])
    ## edca-txop-n.h: void ns3::EdcaTxopN::SetMsduAggregator(ns3::Ptr<ns3::MsduAggregator> aggr) [member function]
    cls.add_method('SetMsduAggregator', 
                   'void', 
                   [param('ns3::Ptr< ns3::MsduAggregator >', 'aggr')])
    return

def register_Ns3ErrorRateModel_methods(root_module, cls):
    ## error-rate-model.h: ns3::ErrorRateModel::ErrorRateModel() [constructor]
    cls.add_constructor([])
    ## error-rate-model.h: ns3::ErrorRateModel::ErrorRateModel(ns3::ErrorRateModel const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::ErrorRateModel const &', 'arg0')])
    ## error-rate-model.h: double ns3::ErrorRateModel::CalculateSnr(ns3::WifiMode txMode, double ber) const [member function]
    cls.add_method('CalculateSnr', 
                   'double', 
                   [param('ns3::WifiMode', 'txMode'), param('double', 'ber')], 
                   is_const=True)
    ## error-rate-model.h: double ns3::ErrorRateModel::GetChunkSuccessRate(ns3::WifiMode mode, double snr, uint32_t nbits) const [member function]
    cls.add_method('GetChunkSuccessRate', 
                   'double', 
                   [param('ns3::WifiMode', 'mode'), param('double', 'snr'), param('uint32_t', 'nbits')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## error-rate-model.h: static ns3::TypeId ns3::ErrorRateModel::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    return

def register_Ns3FixedRssLossModel_methods(root_module, cls):
    ## propagation-loss-model.h: static ns3::TypeId ns3::FixedRssLossModel::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## propagation-loss-model.h: ns3::FixedRssLossModel::FixedRssLossModel() [constructor]
    cls.add_constructor([])
    ## propagation-loss-model.h: void ns3::FixedRssLossModel::SetRss(double rss) [member function]
    cls.add_method('SetRss', 
                   'void', 
                   [param('double', 'rss')])
    ## propagation-loss-model.h: double ns3::FixedRssLossModel::DoCalcRxPower(double txPowerDbm, ns3::Ptr<ns3::MobilityModel> a, ns3::Ptr<ns3::MobilityModel> b) const [member function]
    cls.add_method('DoCalcRxPower', 
                   'double', 
                   [param('double', 'txPowerDbm'), param('ns3::Ptr< ns3::MobilityModel >', 'a'), param('ns3::Ptr< ns3::MobilityModel >', 'b')], 
                   is_const=True, visibility='private', is_virtual=True)
    return

def register_Ns3FriisPropagationLossModel_methods(root_module, cls):
    ## propagation-loss-model.h: static ns3::TypeId ns3::FriisPropagationLossModel::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## propagation-loss-model.h: ns3::FriisPropagationLossModel::FriisPropagationLossModel() [constructor]
    cls.add_constructor([])
    ## propagation-loss-model.h: void ns3::FriisPropagationLossModel::SetLambda(double frequency, double speed) [member function]
    cls.add_method('SetLambda', 
                   'void', 
                   [param('double', 'frequency'), param('double', 'speed')])
    ## propagation-loss-model.h: void ns3::FriisPropagationLossModel::SetLambda(double lambda) [member function]
    cls.add_method('SetLambda', 
                   'void', 
                   [param('double', 'lambda')])
    ## propagation-loss-model.h: void ns3::FriisPropagationLossModel::SetSystemLoss(double systemLoss) [member function]
    cls.add_method('SetSystemLoss', 
                   'void', 
                   [param('double', 'systemLoss')])
    ## propagation-loss-model.h: void ns3::FriisPropagationLossModel::SetMinDistance(double minDistance) [member function]
    cls.add_method('SetMinDistance', 
                   'void', 
                   [param('double', 'minDistance')])
    ## propagation-loss-model.h: double ns3::FriisPropagationLossModel::GetMinDistance() const [member function]
    cls.add_method('GetMinDistance', 
                   'double', 
                   [], 
                   is_const=True)
    ## propagation-loss-model.h: double ns3::FriisPropagationLossModel::GetLambda() const [member function]
    cls.add_method('GetLambda', 
                   'double', 
                   [], 
                   is_const=True)
    ## propagation-loss-model.h: double ns3::FriisPropagationLossModel::GetSystemLoss() const [member function]
    cls.add_method('GetSystemLoss', 
                   'double', 
                   [], 
                   is_const=True)
    ## propagation-loss-model.h: double ns3::FriisPropagationLossModel::DoCalcRxPower(double txPowerDbm, ns3::Ptr<ns3::MobilityModel> a, ns3::Ptr<ns3::MobilityModel> b) const [member function]
    cls.add_method('DoCalcRxPower', 
                   'double', 
                   [param('double', 'txPowerDbm'), param('ns3::Ptr< ns3::MobilityModel >', 'a'), param('ns3::Ptr< ns3::MobilityModel >', 'b')], 
                   is_const=True, visibility='private', is_virtual=True)
    return

def register_Ns3IdealWifiManager_methods(root_module, cls):
    ## ideal-wifi-manager.h: ns3::IdealWifiManager::IdealWifiManager(ns3::IdealWifiManager const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::IdealWifiManager const &', 'arg0')])
    ## ideal-wifi-manager.h: ns3::IdealWifiManager::IdealWifiManager() [constructor]
    cls.add_constructor([])
    ## ideal-wifi-manager.h: void ns3::IdealWifiManager::AddModeSnrThreshold(ns3::WifiMode mode, double ber) [member function]
    cls.add_method('AddModeSnrThreshold', 
                   'void', 
                   [param('ns3::WifiMode', 'mode'), param('double', 'ber')])
    ## ideal-wifi-manager.h: double ns3::IdealWifiManager::GetSnrThreshold(ns3::WifiMode mode) const [member function]
    cls.add_method('GetSnrThreshold', 
                   'double', 
                   [param('ns3::WifiMode', 'mode')], 
                   is_const=True)
    ## ideal-wifi-manager.h: static ns3::TypeId ns3::IdealWifiManager::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## ideal-wifi-manager.h: void ns3::IdealWifiManager::SetupPhy(ns3::Ptr<ns3::WifiPhy> phy) [member function]
    cls.add_method('SetupPhy', 
                   'void', 
                   [param('ns3::Ptr< ns3::WifiPhy >', 'phy')], 
                   is_virtual=True)
    ## ideal-wifi-manager.h: ns3::WifiRemoteStation * ns3::IdealWifiManager::CreateStation() [member function]
    cls.add_method('CreateStation', 
                   'ns3::WifiRemoteStation *', 
                   [], 
                   visibility='private', is_virtual=True)
    return

def register_Ns3JakesPropagationLossModel_methods(root_module, cls):
    ## jakes-propagation-loss-model.h: ns3::JakesPropagationLossModel::JakesPropagationLossModel() [constructor]
    cls.add_constructor([])
    ## jakes-propagation-loss-model.h: uint8_t ns3::JakesPropagationLossModel::GetNOscillators() const [member function]
    cls.add_method('GetNOscillators', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## jakes-propagation-loss-model.h: uint8_t ns3::JakesPropagationLossModel::GetNRays() const [member function]
    cls.add_method('GetNRays', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## jakes-propagation-loss-model.h: static ns3::TypeId ns3::JakesPropagationLossModel::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## jakes-propagation-loss-model.h: void ns3::JakesPropagationLossModel::SetNOscillators(uint8_t nOscillators) [member function]
    cls.add_method('SetNOscillators', 
                   'void', 
                   [param('uint8_t', 'nOscillators')])
    ## jakes-propagation-loss-model.h: void ns3::JakesPropagationLossModel::SetNRays(uint8_t nRays) [member function]
    cls.add_method('SetNRays', 
                   'void', 
                   [param('uint8_t', 'nRays')])
    ## jakes-propagation-loss-model.h: double ns3::JakesPropagationLossModel::DoCalcRxPower(double txPowerDbm, ns3::Ptr<ns3::MobilityModel> a, ns3::Ptr<ns3::MobilityModel> b) const [member function]
    cls.add_method('DoCalcRxPower', 
                   'double', 
                   [param('double', 'txPowerDbm'), param('ns3::Ptr< ns3::MobilityModel >', 'a'), param('ns3::Ptr< ns3::MobilityModel >', 'b')], 
                   is_const=True, visibility='private', is_virtual=True)
    return

def register_Ns3LogDistancePropagationLossModel_methods(root_module, cls):
    ## propagation-loss-model.h: static ns3::TypeId ns3::LogDistancePropagationLossModel::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## propagation-loss-model.h: ns3::LogDistancePropagationLossModel::LogDistancePropagationLossModel() [constructor]
    cls.add_constructor([])
    ## propagation-loss-model.h: void ns3::LogDistancePropagationLossModel::SetPathLossExponent(double n) [member function]
    cls.add_method('SetPathLossExponent', 
                   'void', 
                   [param('double', 'n')])
    ## propagation-loss-model.h: double ns3::LogDistancePropagationLossModel::GetPathLossExponent() const [member function]
    cls.add_method('GetPathLossExponent', 
                   'double', 
                   [], 
                   is_const=True)
    ## propagation-loss-model.h: void ns3::LogDistancePropagationLossModel::SetReference(double referenceDistance, double referenceLoss) [member function]
    cls.add_method('SetReference', 
                   'void', 
                   [param('double', 'referenceDistance'), param('double', 'referenceLoss')])
    ## propagation-loss-model.h: double ns3::LogDistancePropagationLossModel::DoCalcRxPower(double txPowerDbm, ns3::Ptr<ns3::MobilityModel> a, ns3::Ptr<ns3::MobilityModel> b) const [member function]
    cls.add_method('DoCalcRxPower', 
                   'double', 
                   [param('double', 'txPowerDbm'), param('ns3::Ptr< ns3::MobilityModel >', 'a'), param('ns3::Ptr< ns3::MobilityModel >', 'b')], 
                   is_const=True, visibility='private', is_virtual=True)
    return

def register_Ns3MacLow_methods(root_module, cls):
    ## mac-low.h: ns3::MacLow::MacLow(ns3::MacLow const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::MacLow const &', 'arg0')])
    ## mac-low.h: ns3::MacLow::MacLow() [constructor]
    cls.add_constructor([])
    ## mac-low.h: ns3::Time ns3::MacLow::CalculateTransmissionTime(ns3::Ptr<ns3::Packet const> packet, ns3::WifiMacHeader const * hdr, ns3::MacLowTransmissionParameters const & parameters) const [member function]
    cls.add_method('CalculateTransmissionTime', 
                   'ns3::Time', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet'), param('ns3::WifiMacHeader const *', 'hdr'), param('ns3::MacLowTransmissionParameters const &', 'parameters')], 
                   is_const=True)
    ## mac-low.h: ns3::Time ns3::MacLow::GetAckTimeout() const [member function]
    cls.add_method('GetAckTimeout', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    ## mac-low.h: ns3::Mac48Address ns3::MacLow::GetAddress() const [member function]
    cls.add_method('GetAddress', 
                   'ns3::Mac48Address', 
                   [], 
                   is_const=True)
    ## mac-low.h: ns3::Mac48Address ns3::MacLow::GetBssid() const [member function]
    cls.add_method('GetBssid', 
                   'ns3::Mac48Address', 
                   [], 
                   is_const=True)
    ## mac-low.h: ns3::Time ns3::MacLow::GetCtsTimeout() const [member function]
    cls.add_method('GetCtsTimeout', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    ## mac-low.h: ns3::Time ns3::MacLow::GetPifs() const [member function]
    cls.add_method('GetPifs', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    ## mac-low.h: ns3::Time ns3::MacLow::GetSifs() const [member function]
    cls.add_method('GetSifs', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    ## mac-low.h: ns3::Time ns3::MacLow::GetSlotTime() const [member function]
    cls.add_method('GetSlotTime', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    ## mac-low.h: void ns3::MacLow::NotifySwitchingStartNow(ns3::Time duration) [member function]
    cls.add_method('NotifySwitchingStartNow', 
                   'void', 
                   [param('ns3::Time', 'duration')])
    ## mac-low.h: void ns3::MacLow::ReceiveError(ns3::Ptr<ns3::Packet const> packet, double rxSnr) [member function]
    cls.add_method('ReceiveError', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet'), param('double', 'rxSnr')])
    ## mac-low.h: void ns3::MacLow::ReceiveOk(ns3::Ptr<ns3::Packet> packet, double rxSnr, ns3::WifiMode txMode, ns3::WifiPreamble preamble) [member function]
    cls.add_method('ReceiveOk', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet >', 'packet'), param('double', 'rxSnr'), param('ns3::WifiMode', 'txMode'), param('ns3::WifiPreamble', 'preamble')])
    ## mac-low.h: void ns3::MacLow::RegisterDcfListener(ns3::MacLowDcfListener * listener) [member function]
    cls.add_method('RegisterDcfListener', 
                   'void', 
                   [param('ns3::MacLowDcfListener *', 'listener')])
    ## mac-low.h: void ns3::MacLow::SetAckTimeout(ns3::Time ackTimeout) [member function]
    cls.add_method('SetAckTimeout', 
                   'void', 
                   [param('ns3::Time', 'ackTimeout')])
    ## mac-low.h: void ns3::MacLow::SetAddress(ns3::Mac48Address ad) [member function]
    cls.add_method('SetAddress', 
                   'void', 
                   [param('ns3::Mac48Address', 'ad')])
    ## mac-low.h: void ns3::MacLow::SetBssid(ns3::Mac48Address ad) [member function]
    cls.add_method('SetBssid', 
                   'void', 
                   [param('ns3::Mac48Address', 'ad')])
    ## mac-low.h: void ns3::MacLow::SetCtsTimeout(ns3::Time ctsTimeout) [member function]
    cls.add_method('SetCtsTimeout', 
                   'void', 
                   [param('ns3::Time', 'ctsTimeout')])
    ## mac-low.h: void ns3::MacLow::SetPhy(ns3::Ptr<ns3::WifiPhy> phy) [member function]
    cls.add_method('SetPhy', 
                   'void', 
                   [param('ns3::Ptr< ns3::WifiPhy >', 'phy')])
    ## mac-low.h: void ns3::MacLow::SetPifs(ns3::Time pifs) [member function]
    cls.add_method('SetPifs', 
                   'void', 
                   [param('ns3::Time', 'pifs')])
    ## mac-low.h: void ns3::MacLow::SetRxCallback(ns3::Callback<void, ns3::Ptr<ns3::Packet>, ns3::WifiMacHeader const*, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> callback) [member function]
    cls.add_method('SetRxCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::Ptr< ns3::Packet >, ns3::WifiMacHeader const *, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'callback')])
    ## mac-low.h: void ns3::MacLow::SetSifs(ns3::Time sifs) [member function]
    cls.add_method('SetSifs', 
                   'void', 
                   [param('ns3::Time', 'sifs')])
    ## mac-low.h: void ns3::MacLow::SetSlotTime(ns3::Time slotTime) [member function]
    cls.add_method('SetSlotTime', 
                   'void', 
                   [param('ns3::Time', 'slotTime')])
    ## mac-low.h: void ns3::MacLow::SetWifiRemoteStationManager(ns3::Ptr<ns3::WifiRemoteStationManager> manager) [member function]
    cls.add_method('SetWifiRemoteStationManager', 
                   'void', 
                   [param('ns3::Ptr< ns3::WifiRemoteStationManager >', 'manager')])
    ## mac-low.h: void ns3::MacLow::StartTransmission(ns3::Ptr<ns3::Packet const> packet, ns3::WifiMacHeader const * hdr, ns3::MacLowTransmissionParameters parameters, ns3::MacLowTransmissionListener * listener) [member function]
    cls.add_method('StartTransmission', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet'), param('ns3::WifiMacHeader const *', 'hdr'), param('ns3::MacLowTransmissionParameters', 'parameters'), param('ns3::MacLowTransmissionListener *', 'listener')])
    ## mac-low.h: void ns3::MacLow::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   visibility='private', is_virtual=True)
    return

def register_Ns3MgtBeaconHeader_methods(root_module, cls):
    ## mgt-headers.h: ns3::MgtBeaconHeader::MgtBeaconHeader() [constructor]
    cls.add_constructor([])
    ## mgt-headers.h: ns3::MgtBeaconHeader::MgtBeaconHeader(ns3::MgtBeaconHeader const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::MgtBeaconHeader const &', 'arg0')])
    return

def register_Ns3MinstrelWifiManager_methods(root_module, cls):
    ## minstrel-wifi-manager.h: ns3::MinstrelWifiManager::MinstrelWifiManager(ns3::MinstrelWifiManager const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::MinstrelWifiManager const &', 'arg0')])
    ## minstrel-wifi-manager.h: ns3::MinstrelWifiManager::MinstrelWifiManager() [constructor]
    cls.add_constructor([])
    ## minstrel-wifi-manager.h: void ns3::MinstrelWifiManager::AddCalcTxTime(ns3::WifiMode mode, ns3::Time t) [member function]
    cls.add_method('AddCalcTxTime', 
                   'void', 
                   [param('ns3::WifiMode', 'mode'), param('ns3::Time', 't')])
    ## minstrel-wifi-manager.h: ns3::Time ns3::MinstrelWifiManager::GetCalcTxTime(ns3::WifiMode mode) const [member function]
    cls.add_method('GetCalcTxTime', 
                   'ns3::Time', 
                   [param('ns3::WifiMode', 'mode')], 
                   is_const=True)
    ## minstrel-wifi-manager.h: static ns3::TypeId ns3::MinstrelWifiManager::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## minstrel-wifi-manager.h: void ns3::MinstrelWifiManager::SetupPhy(ns3::Ptr<ns3::WifiPhy> phy) [member function]
    cls.add_method('SetupPhy', 
                   'void', 
                   [param('ns3::Ptr< ns3::WifiPhy >', 'phy')], 
                   is_virtual=True)
    ## minstrel-wifi-manager.h: ns3::WifiRemoteStation * ns3::MinstrelWifiManager::CreateStation() [member function]
    cls.add_method('CreateStation', 
                   'ns3::WifiRemoteStation *', 
                   [], 
                   visibility='private', is_virtual=True)
    return

def register_Ns3MsduAggregator_methods(root_module, cls):
    ## msdu-aggregator.h: ns3::MsduAggregator::MsduAggregator() [constructor]
    cls.add_constructor([])
    ## msdu-aggregator.h: ns3::MsduAggregator::MsduAggregator(ns3::MsduAggregator const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::MsduAggregator const &', 'arg0')])
    ## msdu-aggregator.h: bool ns3::MsduAggregator::Aggregate(ns3::Ptr<ns3::Packet const> packet, ns3::Ptr<ns3::Packet> aggregatedPacket, ns3::Mac48Address src, ns3::Mac48Address dest) [member function]
    cls.add_method('Aggregate', 
                   'bool', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet'), param('ns3::Ptr< ns3::Packet >', 'aggregatedPacket'), param('ns3::Mac48Address', 'src'), param('ns3::Mac48Address', 'dest')], 
                   is_pure_virtual=True, is_virtual=True)
    ## msdu-aggregator.h: static std::list<std::pair<ns3::Ptr<ns3::Packet>, ns3::AmsduSubframeHeader>, std::allocator<std::pair<ns3::Ptr<ns3::Packet>, ns3::AmsduSubframeHeader> > > ns3::MsduAggregator::Deaggregate(ns3::Ptr<ns3::Packet> aggregatedPacket) [member function]
    cls.add_method('Deaggregate', 
                   'std::list< std::pair< ns3::Ptr< ns3::Packet >, ns3::AmsduSubframeHeader > >', 
                   [param('ns3::Ptr< ns3::Packet >', 'aggregatedPacket')], 
                   is_static=True)
    ## msdu-aggregator.h: static ns3::TypeId ns3::MsduAggregator::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    return

def register_Ns3NakagamiPropagationLossModel_methods(root_module, cls):
    ## propagation-loss-model.h: static ns3::TypeId ns3::NakagamiPropagationLossModel::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## propagation-loss-model.h: ns3::NakagamiPropagationLossModel::NakagamiPropagationLossModel() [constructor]
    cls.add_constructor([])
    ## propagation-loss-model.h: double ns3::NakagamiPropagationLossModel::DoCalcRxPower(double txPowerDbm, ns3::Ptr<ns3::MobilityModel> a, ns3::Ptr<ns3::MobilityModel> b) const [member function]
    cls.add_method('DoCalcRxPower', 
                   'double', 
                   [param('double', 'txPowerDbm'), param('ns3::Ptr< ns3::MobilityModel >', 'a'), param('ns3::Ptr< ns3::MobilityModel >', 'b')], 
                   is_const=True, visibility='private', is_virtual=True)
    return

def register_Ns3NqapWifiMac_methods(root_module, cls):
    ## nqap-wifi-mac.h: static ns3::TypeId ns3::NqapWifiMac::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## nqap-wifi-mac.h: ns3::NqapWifiMac::NqapWifiMac() [constructor]
    cls.add_constructor([])
    ## nqap-wifi-mac.h: void ns3::NqapWifiMac::SetSlot(ns3::Time slotTime) [member function]
    cls.add_method('SetSlot', 
                   'void', 
                   [param('ns3::Time', 'slotTime')], 
                   is_virtual=True)
    ## nqap-wifi-mac.h: void ns3::NqapWifiMac::SetSifs(ns3::Time sifs) [member function]
    cls.add_method('SetSifs', 
                   'void', 
                   [param('ns3::Time', 'sifs')], 
                   is_virtual=True)
    ## nqap-wifi-mac.h: void ns3::NqapWifiMac::SetEifsNoDifs(ns3::Time eifsNoDifs) [member function]
    cls.add_method('SetEifsNoDifs', 
                   'void', 
                   [param('ns3::Time', 'eifsNoDifs')], 
                   is_virtual=True)
    ## nqap-wifi-mac.h: void ns3::NqapWifiMac::SetAckTimeout(ns3::Time ackTimeout) [member function]
    cls.add_method('SetAckTimeout', 
                   'void', 
                   [param('ns3::Time', 'ackTimeout')], 
                   is_virtual=True)
    ## nqap-wifi-mac.h: void ns3::NqapWifiMac::SetCtsTimeout(ns3::Time ctsTimeout) [member function]
    cls.add_method('SetCtsTimeout', 
                   'void', 
                   [param('ns3::Time', 'ctsTimeout')], 
                   is_virtual=True)
    ## nqap-wifi-mac.h: void ns3::NqapWifiMac::SetPifs(ns3::Time pifs) [member function]
    cls.add_method('SetPifs', 
                   'void', 
                   [param('ns3::Time', 'pifs')], 
                   is_virtual=True)
    ## nqap-wifi-mac.h: ns3::Time ns3::NqapWifiMac::GetSlot() const [member function]
    cls.add_method('GetSlot', 
                   'ns3::Time', 
                   [], 
                   is_const=True, is_virtual=True)
    ## nqap-wifi-mac.h: ns3::Time ns3::NqapWifiMac::GetSifs() const [member function]
    cls.add_method('GetSifs', 
                   'ns3::Time', 
                   [], 
                   is_const=True, is_virtual=True)
    ## nqap-wifi-mac.h: ns3::Time ns3::NqapWifiMac::GetEifsNoDifs() const [member function]
    cls.add_method('GetEifsNoDifs', 
                   'ns3::Time', 
                   [], 
                   is_const=True, is_virtual=True)
    ## nqap-wifi-mac.h: ns3::Time ns3::NqapWifiMac::GetAckTimeout() const [member function]
    cls.add_method('GetAckTimeout', 
                   'ns3::Time', 
                   [], 
                   is_const=True, is_virtual=True)
    ## nqap-wifi-mac.h: ns3::Time ns3::NqapWifiMac::GetCtsTimeout() const [member function]
    cls.add_method('GetCtsTimeout', 
                   'ns3::Time', 
                   [], 
                   is_const=True, is_virtual=True)
    ## nqap-wifi-mac.h: ns3::Time ns3::NqapWifiMac::GetPifs() const [member function]
    cls.add_method('GetPifs', 
                   'ns3::Time', 
                   [], 
                   is_const=True, is_virtual=True)
    ## nqap-wifi-mac.h: void ns3::NqapWifiMac::SetWifiPhy(ns3::Ptr<ns3::WifiPhy> phy) [member function]
    cls.add_method('SetWifiPhy', 
                   'void', 
                   [param('ns3::Ptr< ns3::WifiPhy >', 'phy')], 
                   is_virtual=True)
    ## nqap-wifi-mac.h: void ns3::NqapWifiMac::SetWifiRemoteStationManager(ns3::Ptr<ns3::WifiRemoteStationManager> stationManager) [member function]
    cls.add_method('SetWifiRemoteStationManager', 
                   'void', 
                   [param('ns3::Ptr< ns3::WifiRemoteStationManager >', 'stationManager')], 
                   is_virtual=True)
    ## nqap-wifi-mac.h: void ns3::NqapWifiMac::Enqueue(ns3::Ptr<ns3::Packet const> packet, ns3::Mac48Address to, ns3::Mac48Address from) [member function]
    cls.add_method('Enqueue', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet'), param('ns3::Mac48Address', 'to'), param('ns3::Mac48Address', 'from')], 
                   is_virtual=True)
    ## nqap-wifi-mac.h: void ns3::NqapWifiMac::Enqueue(ns3::Ptr<ns3::Packet const> packet, ns3::Mac48Address to) [member function]
    cls.add_method('Enqueue', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet'), param('ns3::Mac48Address', 'to')], 
                   is_virtual=True)
    ## nqap-wifi-mac.h: bool ns3::NqapWifiMac::SupportsSendFrom() const [member function]
    cls.add_method('SupportsSendFrom', 
                   'bool', 
                   [], 
                   is_const=True, is_virtual=True)
    ## nqap-wifi-mac.h: void ns3::NqapWifiMac::SetForwardUpCallback(ns3::Callback<void, ns3::Ptr<ns3::Packet>, ns3::Mac48Address, ns3::Mac48Address, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> upCallback) [member function]
    cls.add_method('SetForwardUpCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::Ptr< ns3::Packet >, ns3::Mac48Address, ns3::Mac48Address, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'upCallback')], 
                   is_virtual=True)
    ## nqap-wifi-mac.h: void ns3::NqapWifiMac::SetLinkUpCallback(ns3::Callback<void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> linkUp) [member function]
    cls.add_method('SetLinkUpCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'linkUp')], 
                   is_virtual=True)
    ## nqap-wifi-mac.h: void ns3::NqapWifiMac::SetLinkDownCallback(ns3::Callback<void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> linkDown) [member function]
    cls.add_method('SetLinkDownCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'linkDown')], 
                   is_virtual=True)
    ## nqap-wifi-mac.h: ns3::Mac48Address ns3::NqapWifiMac::GetAddress() const [member function]
    cls.add_method('GetAddress', 
                   'ns3::Mac48Address', 
                   [], 
                   is_const=True, is_virtual=True)
    ## nqap-wifi-mac.h: ns3::Ssid ns3::NqapWifiMac::GetSsid() const [member function]
    cls.add_method('GetSsid', 
                   'ns3::Ssid', 
                   [], 
                   is_const=True, is_virtual=True)
    ## nqap-wifi-mac.h: void ns3::NqapWifiMac::SetAddress(ns3::Mac48Address address) [member function]
    cls.add_method('SetAddress', 
                   'void', 
                   [param('ns3::Mac48Address', 'address')], 
                   is_virtual=True)
    ## nqap-wifi-mac.h: void ns3::NqapWifiMac::SetSsid(ns3::Ssid ssid) [member function]
    cls.add_method('SetSsid', 
                   'void', 
                   [param('ns3::Ssid', 'ssid')], 
                   is_virtual=True)
    ## nqap-wifi-mac.h: ns3::Mac48Address ns3::NqapWifiMac::GetBssid() const [member function]
    cls.add_method('GetBssid', 
                   'ns3::Mac48Address', 
                   [], 
                   is_const=True, is_virtual=True)
    ## nqap-wifi-mac.h: void ns3::NqapWifiMac::SetBeaconInterval(ns3::Time interval) [member function]
    cls.add_method('SetBeaconInterval', 
                   'void', 
                   [param('ns3::Time', 'interval')])
    ## nqap-wifi-mac.h: ns3::Time ns3::NqapWifiMac::GetBeaconInterval() const [member function]
    cls.add_method('GetBeaconInterval', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    ## nqap-wifi-mac.h: void ns3::NqapWifiMac::StartBeaconing() [member function]
    cls.add_method('StartBeaconing', 
                   'void', 
                   [])
    ## nqap-wifi-mac.h: void ns3::NqapWifiMac::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   visibility='private', is_virtual=True)
    ## nqap-wifi-mac.h: void ns3::NqapWifiMac::DoStart() [member function]
    cls.add_method('DoStart', 
                   'void', 
                   [], 
                   visibility='private', is_virtual=True)
    ## nqap-wifi-mac.h: void ns3::NqapWifiMac::FinishConfigureStandard(ns3::WifiPhyStandard standard) [member function]
    cls.add_method('FinishConfigureStandard', 
                   'void', 
                   [param('ns3::WifiPhyStandard', 'standard')], 
                   visibility='private', is_virtual=True)
    return

def register_Ns3NqstaWifiMac_methods(root_module, cls):
    ## nqsta-wifi-mac.h: static ns3::TypeId ns3::NqstaWifiMac::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## nqsta-wifi-mac.h: ns3::NqstaWifiMac::NqstaWifiMac() [constructor]
    cls.add_constructor([])
    ## nqsta-wifi-mac.h: void ns3::NqstaWifiMac::SetSlot(ns3::Time slotTime) [member function]
    cls.add_method('SetSlot', 
                   'void', 
                   [param('ns3::Time', 'slotTime')], 
                   is_virtual=True)
    ## nqsta-wifi-mac.h: void ns3::NqstaWifiMac::SetSifs(ns3::Time sifs) [member function]
    cls.add_method('SetSifs', 
                   'void', 
                   [param('ns3::Time', 'sifs')], 
                   is_virtual=True)
    ## nqsta-wifi-mac.h: void ns3::NqstaWifiMac::SetEifsNoDifs(ns3::Time eifsNoDifs) [member function]
    cls.add_method('SetEifsNoDifs', 
                   'void', 
                   [param('ns3::Time', 'eifsNoDifs')], 
                   is_virtual=True)
    ## nqsta-wifi-mac.h: void ns3::NqstaWifiMac::SetAckTimeout(ns3::Time ackTimeout) [member function]
    cls.add_method('SetAckTimeout', 
                   'void', 
                   [param('ns3::Time', 'ackTimeout')], 
                   is_virtual=True)
    ## nqsta-wifi-mac.h: void ns3::NqstaWifiMac::SetCtsTimeout(ns3::Time ctsTimeout) [member function]
    cls.add_method('SetCtsTimeout', 
                   'void', 
                   [param('ns3::Time', 'ctsTimeout')], 
                   is_virtual=True)
    ## nqsta-wifi-mac.h: void ns3::NqstaWifiMac::SetPifs(ns3::Time pifs) [member function]
    cls.add_method('SetPifs', 
                   'void', 
                   [param('ns3::Time', 'pifs')], 
                   is_virtual=True)
    ## nqsta-wifi-mac.h: ns3::Time ns3::NqstaWifiMac::GetSlot() const [member function]
    cls.add_method('GetSlot', 
                   'ns3::Time', 
                   [], 
                   is_const=True, is_virtual=True)
    ## nqsta-wifi-mac.h: ns3::Time ns3::NqstaWifiMac::GetSifs() const [member function]
    cls.add_method('GetSifs', 
                   'ns3::Time', 
                   [], 
                   is_const=True, is_virtual=True)
    ## nqsta-wifi-mac.h: ns3::Time ns3::NqstaWifiMac::GetEifsNoDifs() const [member function]
    cls.add_method('GetEifsNoDifs', 
                   'ns3::Time', 
                   [], 
                   is_const=True, is_virtual=True)
    ## nqsta-wifi-mac.h: ns3::Time ns3::NqstaWifiMac::GetAckTimeout() const [member function]
    cls.add_method('GetAckTimeout', 
                   'ns3::Time', 
                   [], 
                   is_const=True, is_virtual=True)
    ## nqsta-wifi-mac.h: ns3::Time ns3::NqstaWifiMac::GetCtsTimeout() const [member function]
    cls.add_method('GetCtsTimeout', 
                   'ns3::Time', 
                   [], 
                   is_const=True, is_virtual=True)
    ## nqsta-wifi-mac.h: ns3::Time ns3::NqstaWifiMac::GetPifs() const [member function]
    cls.add_method('GetPifs', 
                   'ns3::Time', 
                   [], 
                   is_const=True, is_virtual=True)
    ## nqsta-wifi-mac.h: void ns3::NqstaWifiMac::SetWifiPhy(ns3::Ptr<ns3::WifiPhy> phy) [member function]
    cls.add_method('SetWifiPhy', 
                   'void', 
                   [param('ns3::Ptr< ns3::WifiPhy >', 'phy')], 
                   is_virtual=True)
    ## nqsta-wifi-mac.h: void ns3::NqstaWifiMac::SetWifiRemoteStationManager(ns3::Ptr<ns3::WifiRemoteStationManager> stationManager) [member function]
    cls.add_method('SetWifiRemoteStationManager', 
                   'void', 
                   [param('ns3::Ptr< ns3::WifiRemoteStationManager >', 'stationManager')], 
                   is_virtual=True)
    ## nqsta-wifi-mac.h: void ns3::NqstaWifiMac::Enqueue(ns3::Ptr<ns3::Packet const> packet, ns3::Mac48Address to, ns3::Mac48Address from) [member function]
    cls.add_method('Enqueue', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet'), param('ns3::Mac48Address', 'to'), param('ns3::Mac48Address', 'from')], 
                   is_virtual=True)
    ## nqsta-wifi-mac.h: void ns3::NqstaWifiMac::Enqueue(ns3::Ptr<ns3::Packet const> packet, ns3::Mac48Address to) [member function]
    cls.add_method('Enqueue', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet'), param('ns3::Mac48Address', 'to')], 
                   is_virtual=True)
    ## nqsta-wifi-mac.h: bool ns3::NqstaWifiMac::SupportsSendFrom() const [member function]
    cls.add_method('SupportsSendFrom', 
                   'bool', 
                   [], 
                   is_const=True, is_virtual=True)
    ## nqsta-wifi-mac.h: void ns3::NqstaWifiMac::SetForwardUpCallback(ns3::Callback<void, ns3::Ptr<ns3::Packet>, ns3::Mac48Address, ns3::Mac48Address, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> upCallback) [member function]
    cls.add_method('SetForwardUpCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::Ptr< ns3::Packet >, ns3::Mac48Address, ns3::Mac48Address, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'upCallback')], 
                   is_virtual=True)
    ## nqsta-wifi-mac.h: void ns3::NqstaWifiMac::SetLinkUpCallback(ns3::Callback<void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> linkUp) [member function]
    cls.add_method('SetLinkUpCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'linkUp')], 
                   is_virtual=True)
    ## nqsta-wifi-mac.h: void ns3::NqstaWifiMac::SetLinkDownCallback(ns3::Callback<void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> linkDown) [member function]
    cls.add_method('SetLinkDownCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'linkDown')], 
                   is_virtual=True)
    ## nqsta-wifi-mac.h: ns3::Mac48Address ns3::NqstaWifiMac::GetAddress() const [member function]
    cls.add_method('GetAddress', 
                   'ns3::Mac48Address', 
                   [], 
                   is_const=True, is_virtual=True)
    ## nqsta-wifi-mac.h: ns3::Ssid ns3::NqstaWifiMac::GetSsid() const [member function]
    cls.add_method('GetSsid', 
                   'ns3::Ssid', 
                   [], 
                   is_const=True, is_virtual=True)
    ## nqsta-wifi-mac.h: void ns3::NqstaWifiMac::SetAddress(ns3::Mac48Address address) [member function]
    cls.add_method('SetAddress', 
                   'void', 
                   [param('ns3::Mac48Address', 'address')], 
                   is_virtual=True)
    ## nqsta-wifi-mac.h: void ns3::NqstaWifiMac::SetSsid(ns3::Ssid ssid) [member function]
    cls.add_method('SetSsid', 
                   'void', 
                   [param('ns3::Ssid', 'ssid')], 
                   is_virtual=True)
    ## nqsta-wifi-mac.h: ns3::Mac48Address ns3::NqstaWifiMac::GetBssid() const [member function]
    cls.add_method('GetBssid', 
                   'ns3::Mac48Address', 
                   [], 
                   is_const=True, is_virtual=True)
    ## nqsta-wifi-mac.h: void ns3::NqstaWifiMac::SetMaxMissedBeacons(uint32_t missed) [member function]
    cls.add_method('SetMaxMissedBeacons', 
                   'void', 
                   [param('uint32_t', 'missed')])
    ## nqsta-wifi-mac.h: void ns3::NqstaWifiMac::SetProbeRequestTimeout(ns3::Time timeout) [member function]
    cls.add_method('SetProbeRequestTimeout', 
                   'void', 
                   [param('ns3::Time', 'timeout')])
    ## nqsta-wifi-mac.h: void ns3::NqstaWifiMac::SetAssocRequestTimeout(ns3::Time timeout) [member function]
    cls.add_method('SetAssocRequestTimeout', 
                   'void', 
                   [param('ns3::Time', 'timeout')])
    ## nqsta-wifi-mac.h: void ns3::NqstaWifiMac::StartActiveAssociation() [member function]
    cls.add_method('StartActiveAssociation', 
                   'void', 
                   [])
    ## nqsta-wifi-mac.h: void ns3::NqstaWifiMac::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   visibility='private', is_virtual=True)
    ## nqsta-wifi-mac.h: void ns3::NqstaWifiMac::FinishConfigureStandard(ns3::WifiPhyStandard standard) [member function]
    cls.add_method('FinishConfigureStandard', 
                   'void', 
                   [param('ns3::WifiPhyStandard', 'standard')], 
                   visibility='private', is_virtual=True)
    return

def register_Ns3OnoeWifiManager_methods(root_module, cls):
    ## onoe-wifi-manager.h: ns3::OnoeWifiManager::OnoeWifiManager(ns3::OnoeWifiManager const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::OnoeWifiManager const &', 'arg0')])
    ## onoe-wifi-manager.h: ns3::OnoeWifiManager::OnoeWifiManager() [constructor]
    cls.add_constructor([])
    ## onoe-wifi-manager.h: static ns3::TypeId ns3::OnoeWifiManager::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## onoe-wifi-manager.h: ns3::WifiRemoteStation * ns3::OnoeWifiManager::CreateStation() [member function]
    cls.add_method('CreateStation', 
                   'ns3::WifiRemoteStation *', 
                   [], 
                   visibility='private', is_virtual=True)
    return

def register_Ns3QadhocWifiMac_methods(root_module, cls):
    ## qadhoc-wifi-mac.h: static ns3::TypeId ns3::QadhocWifiMac::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## qadhoc-wifi-mac.h: ns3::QadhocWifiMac::QadhocWifiMac() [constructor]
    cls.add_constructor([])
    ## qadhoc-wifi-mac.h: void ns3::QadhocWifiMac::SetSlot(ns3::Time slotTime) [member function]
    cls.add_method('SetSlot', 
                   'void', 
                   [param('ns3::Time', 'slotTime')], 
                   is_virtual=True)
    ## qadhoc-wifi-mac.h: void ns3::QadhocWifiMac::SetSifs(ns3::Time sifs) [member function]
    cls.add_method('SetSifs', 
                   'void', 
                   [param('ns3::Time', 'sifs')], 
                   is_virtual=True)
    ## qadhoc-wifi-mac.h: void ns3::QadhocWifiMac::SetEifsNoDifs(ns3::Time eifsNoDifs) [member function]
    cls.add_method('SetEifsNoDifs', 
                   'void', 
                   [param('ns3::Time', 'eifsNoDifs')], 
                   is_virtual=True)
    ## qadhoc-wifi-mac.h: void ns3::QadhocWifiMac::SetAckTimeout(ns3::Time ackTimeout) [member function]
    cls.add_method('SetAckTimeout', 
                   'void', 
                   [param('ns3::Time', 'ackTimeout')], 
                   is_virtual=True)
    ## qadhoc-wifi-mac.h: void ns3::QadhocWifiMac::SetCtsTimeout(ns3::Time ctsTimeout) [member function]
    cls.add_method('SetCtsTimeout', 
                   'void', 
                   [param('ns3::Time', 'ctsTimeout')], 
                   is_virtual=True)
    ## qadhoc-wifi-mac.h: void ns3::QadhocWifiMac::SetPifs(ns3::Time pifs) [member function]
    cls.add_method('SetPifs', 
                   'void', 
                   [param('ns3::Time', 'pifs')], 
                   is_virtual=True)
    ## qadhoc-wifi-mac.h: ns3::Time ns3::QadhocWifiMac::GetSlot() const [member function]
    cls.add_method('GetSlot', 
                   'ns3::Time', 
                   [], 
                   is_const=True, is_virtual=True)
    ## qadhoc-wifi-mac.h: ns3::Time ns3::QadhocWifiMac::GetSifs() const [member function]
    cls.add_method('GetSifs', 
                   'ns3::Time', 
                   [], 
                   is_const=True, is_virtual=True)
    ## qadhoc-wifi-mac.h: ns3::Time ns3::QadhocWifiMac::GetEifsNoDifs() const [member function]
    cls.add_method('GetEifsNoDifs', 
                   'ns3::Time', 
                   [], 
                   is_const=True, is_virtual=True)
    ## qadhoc-wifi-mac.h: ns3::Time ns3::QadhocWifiMac::GetAckTimeout() const [member function]
    cls.add_method('GetAckTimeout', 
                   'ns3::Time', 
                   [], 
                   is_const=True, is_virtual=True)
    ## qadhoc-wifi-mac.h: ns3::Time ns3::QadhocWifiMac::GetCtsTimeout() const [member function]
    cls.add_method('GetCtsTimeout', 
                   'ns3::Time', 
                   [], 
                   is_const=True, is_virtual=True)
    ## qadhoc-wifi-mac.h: ns3::Time ns3::QadhocWifiMac::GetPifs() const [member function]
    cls.add_method('GetPifs', 
                   'ns3::Time', 
                   [], 
                   is_const=True, is_virtual=True)
    ## qadhoc-wifi-mac.h: void ns3::QadhocWifiMac::SetWifiPhy(ns3::Ptr<ns3::WifiPhy> phy) [member function]
    cls.add_method('SetWifiPhy', 
                   'void', 
                   [param('ns3::Ptr< ns3::WifiPhy >', 'phy')], 
                   is_virtual=True)
    ## qadhoc-wifi-mac.h: void ns3::QadhocWifiMac::SetWifiRemoteStationManager(ns3::Ptr<ns3::WifiRemoteStationManager> stationManager) [member function]
    cls.add_method('SetWifiRemoteStationManager', 
                   'void', 
                   [param('ns3::Ptr< ns3::WifiRemoteStationManager >', 'stationManager')], 
                   is_virtual=True)
    ## qadhoc-wifi-mac.h: void ns3::QadhocWifiMac::Enqueue(ns3::Ptr<ns3::Packet const> packet, ns3::Mac48Address to, ns3::Mac48Address from) [member function]
    cls.add_method('Enqueue', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet'), param('ns3::Mac48Address', 'to'), param('ns3::Mac48Address', 'from')], 
                   is_virtual=True)
    ## qadhoc-wifi-mac.h: void ns3::QadhocWifiMac::Enqueue(ns3::Ptr<ns3::Packet const> packet, ns3::Mac48Address to) [member function]
    cls.add_method('Enqueue', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet'), param('ns3::Mac48Address', 'to')], 
                   is_virtual=True)
    ## qadhoc-wifi-mac.h: bool ns3::QadhocWifiMac::SupportsSendFrom() const [member function]
    cls.add_method('SupportsSendFrom', 
                   'bool', 
                   [], 
                   is_const=True, is_virtual=True)
    ## qadhoc-wifi-mac.h: void ns3::QadhocWifiMac::SetForwardUpCallback(ns3::Callback<void, ns3::Ptr<ns3::Packet>, ns3::Mac48Address, ns3::Mac48Address, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> upCallback) [member function]
    cls.add_method('SetForwardUpCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::Ptr< ns3::Packet >, ns3::Mac48Address, ns3::Mac48Address, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'upCallback')], 
                   is_virtual=True)
    ## qadhoc-wifi-mac.h: void ns3::QadhocWifiMac::SetLinkUpCallback(ns3::Callback<void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> linkUp) [member function]
    cls.add_method('SetLinkUpCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'linkUp')], 
                   is_virtual=True)
    ## qadhoc-wifi-mac.h: void ns3::QadhocWifiMac::SetLinkDownCallback(ns3::Callback<void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> linkDown) [member function]
    cls.add_method('SetLinkDownCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'linkDown')], 
                   is_virtual=True)
    ## qadhoc-wifi-mac.h: ns3::Mac48Address ns3::QadhocWifiMac::GetAddress() const [member function]
    cls.add_method('GetAddress', 
                   'ns3::Mac48Address', 
                   [], 
                   is_const=True, is_virtual=True)
    ## qadhoc-wifi-mac.h: ns3::Ssid ns3::QadhocWifiMac::GetSsid() const [member function]
    cls.add_method('GetSsid', 
                   'ns3::Ssid', 
                   [], 
                   is_const=True, is_virtual=True)
    ## qadhoc-wifi-mac.h: void ns3::QadhocWifiMac::SetAddress(ns3::Mac48Address address) [member function]
    cls.add_method('SetAddress', 
                   'void', 
                   [param('ns3::Mac48Address', 'address')], 
                   is_virtual=True)
    ## qadhoc-wifi-mac.h: void ns3::QadhocWifiMac::SetSsid(ns3::Ssid ssid) [member function]
    cls.add_method('SetSsid', 
                   'void', 
                   [param('ns3::Ssid', 'ssid')], 
                   is_virtual=True)
    ## qadhoc-wifi-mac.h: ns3::Mac48Address ns3::QadhocWifiMac::GetBssid() const [member function]
    cls.add_method('GetBssid', 
                   'ns3::Mac48Address', 
                   [], 
                   is_const=True, is_virtual=True)
    ## qadhoc-wifi-mac.h: void ns3::QadhocWifiMac::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   visibility='private', is_virtual=True)
    ## qadhoc-wifi-mac.h: void ns3::QadhocWifiMac::FinishConfigureStandard(ns3::WifiPhyStandard standard) [member function]
    cls.add_method('FinishConfigureStandard', 
                   'void', 
                   [param('ns3::WifiPhyStandard', 'standard')], 
                   visibility='private', is_virtual=True)
    return

def register_Ns3QapWifiMac_methods(root_module, cls):
    ## qap-wifi-mac.h: static ns3::TypeId ns3::QapWifiMac::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## qap-wifi-mac.h: ns3::QapWifiMac::QapWifiMac() [constructor]
    cls.add_constructor([])
    ## qap-wifi-mac.h: void ns3::QapWifiMac::SetSlot(ns3::Time slotTime) [member function]
    cls.add_method('SetSlot', 
                   'void', 
                   [param('ns3::Time', 'slotTime')], 
                   is_virtual=True)
    ## qap-wifi-mac.h: void ns3::QapWifiMac::SetSifs(ns3::Time sifs) [member function]
    cls.add_method('SetSifs', 
                   'void', 
                   [param('ns3::Time', 'sifs')], 
                   is_virtual=True)
    ## qap-wifi-mac.h: void ns3::QapWifiMac::SetEifsNoDifs(ns3::Time eifsNoDifs) [member function]
    cls.add_method('SetEifsNoDifs', 
                   'void', 
                   [param('ns3::Time', 'eifsNoDifs')], 
                   is_virtual=True)
    ## qap-wifi-mac.h: void ns3::QapWifiMac::SetAckTimeout(ns3::Time ackTimeout) [member function]
    cls.add_method('SetAckTimeout', 
                   'void', 
                   [param('ns3::Time', 'ackTimeout')], 
                   is_virtual=True)
    ## qap-wifi-mac.h: void ns3::QapWifiMac::SetCtsTimeout(ns3::Time ctsTimeout) [member function]
    cls.add_method('SetCtsTimeout', 
                   'void', 
                   [param('ns3::Time', 'ctsTimeout')], 
                   is_virtual=True)
    ## qap-wifi-mac.h: void ns3::QapWifiMac::SetPifs(ns3::Time pifs) [member function]
    cls.add_method('SetPifs', 
                   'void', 
                   [param('ns3::Time', 'pifs')], 
                   is_virtual=True)
    ## qap-wifi-mac.h: ns3::Time ns3::QapWifiMac::GetSlot() const [member function]
    cls.add_method('GetSlot', 
                   'ns3::Time', 
                   [], 
                   is_const=True, is_virtual=True)
    ## qap-wifi-mac.h: ns3::Time ns3::QapWifiMac::GetSifs() const [member function]
    cls.add_method('GetSifs', 
                   'ns3::Time', 
                   [], 
                   is_const=True, is_virtual=True)
    ## qap-wifi-mac.h: ns3::Time ns3::QapWifiMac::GetEifsNoDifs() const [member function]
    cls.add_method('GetEifsNoDifs', 
                   'ns3::Time', 
                   [], 
                   is_const=True, is_virtual=True)
    ## qap-wifi-mac.h: ns3::Time ns3::QapWifiMac::GetAckTimeout() const [member function]
    cls.add_method('GetAckTimeout', 
                   'ns3::Time', 
                   [], 
                   is_const=True, is_virtual=True)
    ## qap-wifi-mac.h: ns3::Time ns3::QapWifiMac::GetCtsTimeout() const [member function]
    cls.add_method('GetCtsTimeout', 
                   'ns3::Time', 
                   [], 
                   is_const=True, is_virtual=True)
    ## qap-wifi-mac.h: ns3::Time ns3::QapWifiMac::GetPifs() const [member function]
    cls.add_method('GetPifs', 
                   'ns3::Time', 
                   [], 
                   is_const=True, is_virtual=True)
    ## qap-wifi-mac.h: void ns3::QapWifiMac::SetWifiPhy(ns3::Ptr<ns3::WifiPhy> phy) [member function]
    cls.add_method('SetWifiPhy', 
                   'void', 
                   [param('ns3::Ptr< ns3::WifiPhy >', 'phy')], 
                   is_virtual=True)
    ## qap-wifi-mac.h: void ns3::QapWifiMac::SetWifiRemoteStationManager(ns3::Ptr<ns3::WifiRemoteStationManager> stationManager) [member function]
    cls.add_method('SetWifiRemoteStationManager', 
                   'void', 
                   [param('ns3::Ptr< ns3::WifiRemoteStationManager >', 'stationManager')], 
                   is_virtual=True)
    ## qap-wifi-mac.h: void ns3::QapWifiMac::Enqueue(ns3::Ptr<ns3::Packet const> packet, ns3::Mac48Address to, ns3::Mac48Address from) [member function]
    cls.add_method('Enqueue', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet'), param('ns3::Mac48Address', 'to'), param('ns3::Mac48Address', 'from')], 
                   is_virtual=True)
    ## qap-wifi-mac.h: void ns3::QapWifiMac::Enqueue(ns3::Ptr<ns3::Packet const> packet, ns3::Mac48Address to) [member function]
    cls.add_method('Enqueue', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet'), param('ns3::Mac48Address', 'to')], 
                   is_virtual=True)
    ## qap-wifi-mac.h: bool ns3::QapWifiMac::SupportsSendFrom() const [member function]
    cls.add_method('SupportsSendFrom', 
                   'bool', 
                   [], 
                   is_const=True, is_virtual=True)
    ## qap-wifi-mac.h: void ns3::QapWifiMac::SetForwardUpCallback(ns3::Callback<void, ns3::Ptr<ns3::Packet>, ns3::Mac48Address, ns3::Mac48Address, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> upCallback) [member function]
    cls.add_method('SetForwardUpCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::Ptr< ns3::Packet >, ns3::Mac48Address, ns3::Mac48Address, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'upCallback')], 
                   is_virtual=True)
    ## qap-wifi-mac.h: void ns3::QapWifiMac::SetLinkUpCallback(ns3::Callback<void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> linkUp) [member function]
    cls.add_method('SetLinkUpCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'linkUp')], 
                   is_virtual=True)
    ## qap-wifi-mac.h: void ns3::QapWifiMac::SetLinkDownCallback(ns3::Callback<void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> linkDown) [member function]
    cls.add_method('SetLinkDownCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'linkDown')], 
                   is_virtual=True)
    ## qap-wifi-mac.h: ns3::Mac48Address ns3::QapWifiMac::GetAddress() const [member function]
    cls.add_method('GetAddress', 
                   'ns3::Mac48Address', 
                   [], 
                   is_const=True, is_virtual=True)
    ## qap-wifi-mac.h: ns3::Ssid ns3::QapWifiMac::GetSsid() const [member function]
    cls.add_method('GetSsid', 
                   'ns3::Ssid', 
                   [], 
                   is_const=True, is_virtual=True)
    ## qap-wifi-mac.h: void ns3::QapWifiMac::SetAddress(ns3::Mac48Address address) [member function]
    cls.add_method('SetAddress', 
                   'void', 
                   [param('ns3::Mac48Address', 'address')], 
                   is_virtual=True)
    ## qap-wifi-mac.h: void ns3::QapWifiMac::SetSsid(ns3::Ssid ssid) [member function]
    cls.add_method('SetSsid', 
                   'void', 
                   [param('ns3::Ssid', 'ssid')], 
                   is_virtual=True)
    ## qap-wifi-mac.h: ns3::Mac48Address ns3::QapWifiMac::GetBssid() const [member function]
    cls.add_method('GetBssid', 
                   'ns3::Mac48Address', 
                   [], 
                   is_const=True, is_virtual=True)
    ## qap-wifi-mac.h: void ns3::QapWifiMac::SetBeaconInterval(ns3::Time interval) [member function]
    cls.add_method('SetBeaconInterval', 
                   'void', 
                   [param('ns3::Time', 'interval')])
    ## qap-wifi-mac.h: ns3::Time ns3::QapWifiMac::GetBeaconInterval() const [member function]
    cls.add_method('GetBeaconInterval', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    ## qap-wifi-mac.h: void ns3::QapWifiMac::StartBeaconing() [member function]
    cls.add_method('StartBeaconing', 
                   'void', 
                   [])
    ## qap-wifi-mac.h: void ns3::QapWifiMac::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   visibility='private', is_virtual=True)
    ## qap-wifi-mac.h: void ns3::QapWifiMac::DoStart() [member function]
    cls.add_method('DoStart', 
                   'void', 
                   [], 
                   visibility='private', is_virtual=True)
    ## qap-wifi-mac.h: void ns3::QapWifiMac::FinishConfigureStandard(ns3::WifiPhyStandard standard) [member function]
    cls.add_method('FinishConfigureStandard', 
                   'void', 
                   [param('ns3::WifiPhyStandard', 'standard')], 
                   visibility='private', is_virtual=True)
    return

def register_Ns3QstaWifiMac_methods(root_module, cls):
    ## qsta-wifi-mac.h: static ns3::TypeId ns3::QstaWifiMac::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## qsta-wifi-mac.h: ns3::QstaWifiMac::QstaWifiMac() [constructor]
    cls.add_constructor([])
    ## qsta-wifi-mac.h: void ns3::QstaWifiMac::SetSlot(ns3::Time slotTime) [member function]
    cls.add_method('SetSlot', 
                   'void', 
                   [param('ns3::Time', 'slotTime')], 
                   is_virtual=True)
    ## qsta-wifi-mac.h: void ns3::QstaWifiMac::SetSifs(ns3::Time sifs) [member function]
    cls.add_method('SetSifs', 
                   'void', 
                   [param('ns3::Time', 'sifs')], 
                   is_virtual=True)
    ## qsta-wifi-mac.h: void ns3::QstaWifiMac::SetEifsNoDifs(ns3::Time eifsNoDifs) [member function]
    cls.add_method('SetEifsNoDifs', 
                   'void', 
                   [param('ns3::Time', 'eifsNoDifs')], 
                   is_virtual=True)
    ## qsta-wifi-mac.h: void ns3::QstaWifiMac::SetAckTimeout(ns3::Time ackTimeout) [member function]
    cls.add_method('SetAckTimeout', 
                   'void', 
                   [param('ns3::Time', 'ackTimeout')], 
                   is_virtual=True)
    ## qsta-wifi-mac.h: void ns3::QstaWifiMac::SetCtsTimeout(ns3::Time ctsTimeout) [member function]
    cls.add_method('SetCtsTimeout', 
                   'void', 
                   [param('ns3::Time', 'ctsTimeout')], 
                   is_virtual=True)
    ## qsta-wifi-mac.h: void ns3::QstaWifiMac::SetPifs(ns3::Time pifs) [member function]
    cls.add_method('SetPifs', 
                   'void', 
                   [param('ns3::Time', 'pifs')], 
                   is_virtual=True)
    ## qsta-wifi-mac.h: ns3::Time ns3::QstaWifiMac::GetSlot() const [member function]
    cls.add_method('GetSlot', 
                   'ns3::Time', 
                   [], 
                   is_const=True, is_virtual=True)
    ## qsta-wifi-mac.h: ns3::Time ns3::QstaWifiMac::GetSifs() const [member function]
    cls.add_method('GetSifs', 
                   'ns3::Time', 
                   [], 
                   is_const=True, is_virtual=True)
    ## qsta-wifi-mac.h: ns3::Time ns3::QstaWifiMac::GetEifsNoDifs() const [member function]
    cls.add_method('GetEifsNoDifs', 
                   'ns3::Time', 
                   [], 
                   is_const=True, is_virtual=True)
    ## qsta-wifi-mac.h: ns3::Time ns3::QstaWifiMac::GetAckTimeout() const [member function]
    cls.add_method('GetAckTimeout', 
                   'ns3::Time', 
                   [], 
                   is_const=True, is_virtual=True)
    ## qsta-wifi-mac.h: ns3::Time ns3::QstaWifiMac::GetCtsTimeout() const [member function]
    cls.add_method('GetCtsTimeout', 
                   'ns3::Time', 
                   [], 
                   is_const=True, is_virtual=True)
    ## qsta-wifi-mac.h: ns3::Time ns3::QstaWifiMac::GetPifs() const [member function]
    cls.add_method('GetPifs', 
                   'ns3::Time', 
                   [], 
                   is_const=True, is_virtual=True)
    ## qsta-wifi-mac.h: void ns3::QstaWifiMac::SetWifiPhy(ns3::Ptr<ns3::WifiPhy> phy) [member function]
    cls.add_method('SetWifiPhy', 
                   'void', 
                   [param('ns3::Ptr< ns3::WifiPhy >', 'phy')], 
                   is_virtual=True)
    ## qsta-wifi-mac.h: void ns3::QstaWifiMac::SetWifiRemoteStationManager(ns3::Ptr<ns3::WifiRemoteStationManager> stationManager) [member function]
    cls.add_method('SetWifiRemoteStationManager', 
                   'void', 
                   [param('ns3::Ptr< ns3::WifiRemoteStationManager >', 'stationManager')], 
                   is_virtual=True)
    ## qsta-wifi-mac.h: void ns3::QstaWifiMac::Enqueue(ns3::Ptr<ns3::Packet const> packet, ns3::Mac48Address to, ns3::Mac48Address from) [member function]
    cls.add_method('Enqueue', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet'), param('ns3::Mac48Address', 'to'), param('ns3::Mac48Address', 'from')], 
                   is_virtual=True)
    ## qsta-wifi-mac.h: void ns3::QstaWifiMac::Enqueue(ns3::Ptr<ns3::Packet const> packet, ns3::Mac48Address to) [member function]
    cls.add_method('Enqueue', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet'), param('ns3::Mac48Address', 'to')], 
                   is_virtual=True)
    ## qsta-wifi-mac.h: bool ns3::QstaWifiMac::SupportsSendFrom() const [member function]
    cls.add_method('SupportsSendFrom', 
                   'bool', 
                   [], 
                   is_const=True, is_virtual=True)
    ## qsta-wifi-mac.h: void ns3::QstaWifiMac::SetForwardUpCallback(ns3::Callback<void, ns3::Ptr<ns3::Packet>, ns3::Mac48Address, ns3::Mac48Address, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> upCallback) [member function]
    cls.add_method('SetForwardUpCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::Ptr< ns3::Packet >, ns3::Mac48Address, ns3::Mac48Address, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'upCallback')], 
                   is_virtual=True)
    ## qsta-wifi-mac.h: void ns3::QstaWifiMac::SetLinkUpCallback(ns3::Callback<void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> linkUp) [member function]
    cls.add_method('SetLinkUpCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'linkUp')], 
                   is_virtual=True)
    ## qsta-wifi-mac.h: void ns3::QstaWifiMac::SetLinkDownCallback(ns3::Callback<void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> linkDown) [member function]
    cls.add_method('SetLinkDownCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'linkDown')], 
                   is_virtual=True)
    ## qsta-wifi-mac.h: ns3::Mac48Address ns3::QstaWifiMac::GetAddress() const [member function]
    cls.add_method('GetAddress', 
                   'ns3::Mac48Address', 
                   [], 
                   is_const=True, is_virtual=True)
    ## qsta-wifi-mac.h: ns3::Ssid ns3::QstaWifiMac::GetSsid() const [member function]
    cls.add_method('GetSsid', 
                   'ns3::Ssid', 
                   [], 
                   is_const=True, is_virtual=True)
    ## qsta-wifi-mac.h: void ns3::QstaWifiMac::SetAddress(ns3::Mac48Address address) [member function]
    cls.add_method('SetAddress', 
                   'void', 
                   [param('ns3::Mac48Address', 'address')], 
                   is_virtual=True)
    ## qsta-wifi-mac.h: void ns3::QstaWifiMac::SetSsid(ns3::Ssid ssid) [member function]
    cls.add_method('SetSsid', 
                   'void', 
                   [param('ns3::Ssid', 'ssid')], 
                   is_virtual=True)
    ## qsta-wifi-mac.h: ns3::Mac48Address ns3::QstaWifiMac::GetBssid() const [member function]
    cls.add_method('GetBssid', 
                   'ns3::Mac48Address', 
                   [], 
                   is_const=True, is_virtual=True)
    ## qsta-wifi-mac.h: void ns3::QstaWifiMac::SetMaxMissedBeacons(uint32_t missed) [member function]
    cls.add_method('SetMaxMissedBeacons', 
                   'void', 
                   [param('uint32_t', 'missed')])
    ## qsta-wifi-mac.h: void ns3::QstaWifiMac::SetProbeRequestTimeout(ns3::Time timeout) [member function]
    cls.add_method('SetProbeRequestTimeout', 
                   'void', 
                   [param('ns3::Time', 'timeout')])
    ## qsta-wifi-mac.h: void ns3::QstaWifiMac::SetAssocRequestTimeout(ns3::Time timeout) [member function]
    cls.add_method('SetAssocRequestTimeout', 
                   'void', 
                   [param('ns3::Time', 'timeout')])
    ## qsta-wifi-mac.h: void ns3::QstaWifiMac::StartActiveAssociation() [member function]
    cls.add_method('StartActiveAssociation', 
                   'void', 
                   [])
    ## qsta-wifi-mac.h: void ns3::QstaWifiMac::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   visibility='private', is_virtual=True)
    ## qsta-wifi-mac.h: void ns3::QstaWifiMac::FinishConfigureStandard(ns3::WifiPhyStandard standard) [member function]
    cls.add_method('FinishConfigureStandard', 
                   'void', 
                   [param('ns3::WifiPhyStandard', 'standard')], 
                   visibility='private', is_virtual=True)
    return

def register_Ns3RraaWifiManager_methods(root_module, cls):
    ## rraa-wifi-manager.h: ns3::RraaWifiManager::RraaWifiManager(ns3::RraaWifiManager const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::RraaWifiManager const &', 'arg0')])
    ## rraa-wifi-manager.h: ns3::RraaWifiManager::RraaWifiManager() [constructor]
    cls.add_constructor([])
    ## rraa-wifi-manager.h: ns3::ThresholdsItem ns3::RraaWifiManager::GetThresholds(ns3::WifiMode mode) const [member function]
    cls.add_method('GetThresholds', 
                   'ns3::ThresholdsItem', 
                   [param('ns3::WifiMode', 'mode')], 
                   is_const=True)
    ## rraa-wifi-manager.h: ns3::Time ns3::RraaWifiManager::GetTimeout() const [member function]
    cls.add_method('GetTimeout', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    ## rraa-wifi-manager.h: static ns3::TypeId ns3::RraaWifiManager::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## rraa-wifi-manager.h: bool ns3::RraaWifiManager::OnlyBasic() [member function]
    cls.add_method('OnlyBasic', 
                   'bool', 
                   [])
    ## rraa-wifi-manager.h: ns3::WifiRemoteStation * ns3::RraaWifiManager::CreateStation() [member function]
    cls.add_method('CreateStation', 
                   'ns3::WifiRemoteStation *', 
                   [], 
                   visibility='private', is_virtual=True)
    return

def register_Ns3SsidChecker_methods(root_module, cls):
    ## ssid.h: ns3::SsidChecker::SsidChecker() [constructor]
    cls.add_constructor([])
    ## ssid.h: ns3::SsidChecker::SsidChecker(ns3::SsidChecker const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::SsidChecker const &', 'arg0')])
    return

def register_Ns3SsidValue_methods(root_module, cls):
    ## ssid.h: ns3::SsidValue::SsidValue() [constructor]
    cls.add_constructor([])
    ## ssid.h: ns3::SsidValue::SsidValue(ns3::SsidValue const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::SsidValue const &', 'arg0')])
    ## ssid.h: ns3::SsidValue::SsidValue(ns3::Ssid const & value) [constructor]
    cls.add_constructor([param('ns3::Ssid const &', 'value')])
    ## ssid.h: ns3::Ptr<ns3::AttributeValue> ns3::SsidValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## ssid.h: bool ns3::SsidValue::DeserializeFromString(std::string value, ns3::Ptr<ns3::AttributeChecker const> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## ssid.h: ns3::Ssid ns3::SsidValue::Get() const [member function]
    cls.add_method('Get', 
                   'ns3::Ssid', 
                   [], 
                   is_const=True)
    ## ssid.h: std::string ns3::SsidValue::SerializeToString(ns3::Ptr<ns3::AttributeChecker const> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## ssid.h: void ns3::SsidValue::Set(ns3::Ssid const & value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::Ssid const &', 'value')])
    return

def register_Ns3WifiChannel_methods(root_module, cls):
    ## wifi-channel.h: ns3::WifiChannel::WifiChannel() [constructor]
    cls.add_constructor([])
    ## wifi-channel.h: ns3::WifiChannel::WifiChannel(ns3::WifiChannel const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::WifiChannel const &', 'arg0')])
    ## wifi-channel.h: static ns3::TypeId ns3::WifiChannel::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    return

def register_Ns3WifiModeChecker_methods(root_module, cls):
    ## wifi-mode.h: ns3::WifiModeChecker::WifiModeChecker() [constructor]
    cls.add_constructor([])
    ## wifi-mode.h: ns3::WifiModeChecker::WifiModeChecker(ns3::WifiModeChecker const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::WifiModeChecker const &', 'arg0')])
    return

def register_Ns3WifiModeValue_methods(root_module, cls):
    ## wifi-mode.h: ns3::WifiModeValue::WifiModeValue() [constructor]
    cls.add_constructor([])
    ## wifi-mode.h: ns3::WifiModeValue::WifiModeValue(ns3::WifiModeValue const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::WifiModeValue const &', 'arg0')])
    ## wifi-mode.h: ns3::WifiModeValue::WifiModeValue(ns3::WifiMode const & value) [constructor]
    cls.add_constructor([param('ns3::WifiMode const &', 'value')])
    ## wifi-mode.h: ns3::Ptr<ns3::AttributeValue> ns3::WifiModeValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## wifi-mode.h: bool ns3::WifiModeValue::DeserializeFromString(std::string value, ns3::Ptr<ns3::AttributeChecker const> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## wifi-mode.h: ns3::WifiMode ns3::WifiModeValue::Get() const [member function]
    cls.add_method('Get', 
                   'ns3::WifiMode', 
                   [], 
                   is_const=True)
    ## wifi-mode.h: std::string ns3::WifiModeValue::SerializeToString(ns3::Ptr<ns3::AttributeChecker const> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## wifi-mode.h: void ns3::WifiModeValue::Set(ns3::WifiMode const & value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::WifiMode const &', 'value')])
    return

def register_Ns3WifiNetDevice_methods(root_module, cls):
    ## wifi-net-device.h: ns3::WifiNetDevice::WifiNetDevice(ns3::WifiNetDevice const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::WifiNetDevice const &', 'arg0')])
    ## wifi-net-device.h: ns3::WifiNetDevice::WifiNetDevice() [constructor]
    cls.add_constructor([])
    ## wifi-net-device.h: void ns3::WifiNetDevice::AddLinkChangeCallback(ns3::Callback<void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> callback) [member function]
    cls.add_method('AddLinkChangeCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'callback')], 
                   is_virtual=True)
    ## wifi-net-device.h: ns3::Address ns3::WifiNetDevice::GetAddress() const [member function]
    cls.add_method('GetAddress', 
                   'ns3::Address', 
                   [], 
                   is_const=True, is_virtual=True)
    ## wifi-net-device.h: ns3::Address ns3::WifiNetDevice::GetBroadcast() const [member function]
    cls.add_method('GetBroadcast', 
                   'ns3::Address', 
                   [], 
                   is_const=True, is_virtual=True)
    ## wifi-net-device.h: ns3::Ptr<ns3::Channel> ns3::WifiNetDevice::GetChannel() const [member function]
    cls.add_method('GetChannel', 
                   'ns3::Ptr< ns3::Channel >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## wifi-net-device.h: uint32_t ns3::WifiNetDevice::GetIfIndex() const [member function]
    cls.add_method('GetIfIndex', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## wifi-net-device.h: ns3::Ptr<ns3::WifiMac> ns3::WifiNetDevice::GetMac() const [member function]
    cls.add_method('GetMac', 
                   'ns3::Ptr< ns3::WifiMac >', 
                   [], 
                   is_const=True)
    ## wifi-net-device.h: uint16_t ns3::WifiNetDevice::GetMtu() const [member function]
    cls.add_method('GetMtu', 
                   'uint16_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## wifi-net-device.h: ns3::Address ns3::WifiNetDevice::GetMulticast(ns3::Ipv4Address multicastGroup) const [member function]
    cls.add_method('GetMulticast', 
                   'ns3::Address', 
                   [param('ns3::Ipv4Address', 'multicastGroup')], 
                   is_const=True, is_virtual=True)
    ## wifi-net-device.h: ns3::Address ns3::WifiNetDevice::GetMulticast(ns3::Ipv6Address addr) const [member function]
    cls.add_method('GetMulticast', 
                   'ns3::Address', 
                   [param('ns3::Ipv6Address', 'addr')], 
                   is_const=True, is_virtual=True)
    ## wifi-net-device.h: ns3::Ptr<ns3::Node> ns3::WifiNetDevice::GetNode() const [member function]
    cls.add_method('GetNode', 
                   'ns3::Ptr< ns3::Node >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## wifi-net-device.h: ns3::Ptr<ns3::WifiPhy> ns3::WifiNetDevice::GetPhy() const [member function]
    cls.add_method('GetPhy', 
                   'ns3::Ptr< ns3::WifiPhy >', 
                   [], 
                   is_const=True)
    ## wifi-net-device.h: ns3::Ptr<ns3::WifiRemoteStationManager> ns3::WifiNetDevice::GetRemoteStationManager() const [member function]
    cls.add_method('GetRemoteStationManager', 
                   'ns3::Ptr< ns3::WifiRemoteStationManager >', 
                   [], 
                   is_const=True)
    ## wifi-net-device.h: static ns3::TypeId ns3::WifiNetDevice::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## wifi-net-device.h: bool ns3::WifiNetDevice::IsBridge() const [member function]
    cls.add_method('IsBridge', 
                   'bool', 
                   [], 
                   is_const=True, is_virtual=True)
    ## wifi-net-device.h: bool ns3::WifiNetDevice::IsBroadcast() const [member function]
    cls.add_method('IsBroadcast', 
                   'bool', 
                   [], 
                   is_const=True, is_virtual=True)
    ## wifi-net-device.h: bool ns3::WifiNetDevice::IsLinkUp() const [member function]
    cls.add_method('IsLinkUp', 
                   'bool', 
                   [], 
                   is_const=True, is_virtual=True)
    ## wifi-net-device.h: bool ns3::WifiNetDevice::IsMulticast() const [member function]
    cls.add_method('IsMulticast', 
                   'bool', 
                   [], 
                   is_const=True, is_virtual=True)
    ## wifi-net-device.h: bool ns3::WifiNetDevice::IsPointToPoint() const [member function]
    cls.add_method('IsPointToPoint', 
                   'bool', 
                   [], 
                   is_const=True, is_virtual=True)
    ## wifi-net-device.h: bool ns3::WifiNetDevice::NeedsArp() const [member function]
    cls.add_method('NeedsArp', 
                   'bool', 
                   [], 
                   is_const=True, is_virtual=True)
    ## wifi-net-device.h: bool ns3::WifiNetDevice::Send(ns3::Ptr<ns3::Packet> packet, ns3::Address const & dest, uint16_t protocolNumber) [member function]
    cls.add_method('Send', 
                   'bool', 
                   [param('ns3::Ptr< ns3::Packet >', 'packet'), param('ns3::Address const &', 'dest'), param('uint16_t', 'protocolNumber')], 
                   is_virtual=True)
    ## wifi-net-device.h: bool ns3::WifiNetDevice::SendFrom(ns3::Ptr<ns3::Packet> packet, ns3::Address const & source, ns3::Address const & dest, uint16_t protocolNumber) [member function]
    cls.add_method('SendFrom', 
                   'bool', 
                   [param('ns3::Ptr< ns3::Packet >', 'packet'), param('ns3::Address const &', 'source'), param('ns3::Address const &', 'dest'), param('uint16_t', 'protocolNumber')], 
                   is_virtual=True)
    ## wifi-net-device.h: void ns3::WifiNetDevice::SetAddress(ns3::Address address) [member function]
    cls.add_method('SetAddress', 
                   'void', 
                   [param('ns3::Address', 'address')], 
                   is_virtual=True)
    ## wifi-net-device.h: void ns3::WifiNetDevice::SetIfIndex(uint32_t const index) [member function]
    cls.add_method('SetIfIndex', 
                   'void', 
                   [param('uint32_t const', 'index')], 
                   is_virtual=True)
    ## wifi-net-device.h: void ns3::WifiNetDevice::SetMac(ns3::Ptr<ns3::WifiMac> mac) [member function]
    cls.add_method('SetMac', 
                   'void', 
                   [param('ns3::Ptr< ns3::WifiMac >', 'mac')])
    ## wifi-net-device.h: bool ns3::WifiNetDevice::SetMtu(uint16_t const mtu) [member function]
    cls.add_method('SetMtu', 
                   'bool', 
                   [param('uint16_t const', 'mtu')], 
                   is_virtual=True)
    ## wifi-net-device.h: void ns3::WifiNetDevice::SetNode(ns3::Ptr<ns3::Node> node) [member function]
    cls.add_method('SetNode', 
                   'void', 
                   [param('ns3::Ptr< ns3::Node >', 'node')], 
                   is_virtual=True)
    ## wifi-net-device.h: void ns3::WifiNetDevice::SetPhy(ns3::Ptr<ns3::WifiPhy> phy) [member function]
    cls.add_method('SetPhy', 
                   'void', 
                   [param('ns3::Ptr< ns3::WifiPhy >', 'phy')])
    ## wifi-net-device.h: void ns3::WifiNetDevice::SetPromiscReceiveCallback(ns3::Callback<bool, ns3::Ptr<ns3::NetDevice>, ns3::Ptr<ns3::Packet const>, unsigned short, ns3::Address const&, ns3::Address const&, ns3::NetDevice::PacketType, ns3::empty, ns3::empty, ns3::empty> cb) [member function]
    cls.add_method('SetPromiscReceiveCallback', 
                   'void', 
                   [param('ns3::Callback< bool, ns3::Ptr< ns3::NetDevice >, ns3::Ptr< ns3::Packet const >, unsigned short, ns3::Address const &, ns3::Address const &, ns3::NetDevice::PacketType, ns3::empty, ns3::empty, ns3::empty >', 'cb')], 
                   is_virtual=True)
    ## wifi-net-device.h: void ns3::WifiNetDevice::SetReceiveCallback(ns3::Callback<bool, ns3::Ptr<ns3::NetDevice>, ns3::Ptr<ns3::Packet const>, unsigned short, ns3::Address const&, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> cb) [member function]
    cls.add_method('SetReceiveCallback', 
                   'void', 
                   [param('ns3::Callback< bool, ns3::Ptr< ns3::NetDevice >, ns3::Ptr< ns3::Packet const >, unsigned short, ns3::Address const &, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'cb')], 
                   is_virtual=True)
    ## wifi-net-device.h: void ns3::WifiNetDevice::SetRemoteStationManager(ns3::Ptr<ns3::WifiRemoteStationManager> manager) [member function]
    cls.add_method('SetRemoteStationManager', 
                   'void', 
                   [param('ns3::Ptr< ns3::WifiRemoteStationManager >', 'manager')])
    ## wifi-net-device.h: bool ns3::WifiNetDevice::SupportsSendFrom() const [member function]
    cls.add_method('SupportsSendFrom', 
                   'bool', 
                   [], 
                   is_const=True, is_virtual=True)
    ## wifi-net-device.h: void ns3::WifiNetDevice::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   visibility='private', is_virtual=True)
    ## wifi-net-device.h: void ns3::WifiNetDevice::DoStart() [member function]
    cls.add_method('DoStart', 
                   'void', 
                   [], 
                   visibility='private', is_virtual=True)
    return

def register_Ns3YansErrorRateModel_methods(root_module, cls):
    ## yans-error-rate-model.h: ns3::YansErrorRateModel::YansErrorRateModel(ns3::YansErrorRateModel const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::YansErrorRateModel const &', 'arg0')])
    ## yans-error-rate-model.h: ns3::YansErrorRateModel::YansErrorRateModel() [constructor]
    cls.add_constructor([])
    ## yans-error-rate-model.h: double ns3::YansErrorRateModel::GetChunkSuccessRate(ns3::WifiMode mode, double snr, uint32_t nbits) const [member function]
    cls.add_method('GetChunkSuccessRate', 
                   'double', 
                   [param('ns3::WifiMode', 'mode'), param('double', 'snr'), param('uint32_t', 'nbits')], 
                   is_const=True, is_virtual=True)
    ## yans-error-rate-model.h: static ns3::TypeId ns3::YansErrorRateModel::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    return

def register_Ns3YansWifiChannel_methods(root_module, cls):
    ## yans-wifi-channel.h: ns3::YansWifiChannel::YansWifiChannel(ns3::YansWifiChannel const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::YansWifiChannel const &', 'arg0')])
    ## yans-wifi-channel.h: ns3::YansWifiChannel::YansWifiChannel() [constructor]
    cls.add_constructor([])
    ## yans-wifi-channel.h: void ns3::YansWifiChannel::Add(ns3::Ptr<ns3::YansWifiPhy> phy) [member function]
    cls.add_method('Add', 
                   'void', 
                   [param('ns3::Ptr< ns3::YansWifiPhy >', 'phy')])
    ## yans-wifi-channel.h: ns3::Ptr<ns3::NetDevice> ns3::YansWifiChannel::GetDevice(uint32_t i) const [member function]
    cls.add_method('GetDevice', 
                   'ns3::Ptr< ns3::NetDevice >', 
                   [param('uint32_t', 'i')], 
                   is_const=True, is_virtual=True)
    ## yans-wifi-channel.h: uint32_t ns3::YansWifiChannel::GetNDevices() const [member function]
    cls.add_method('GetNDevices', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## yans-wifi-channel.h: static ns3::TypeId ns3::YansWifiChannel::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## yans-wifi-channel.h: void ns3::YansWifiChannel::Send(ns3::Ptr<ns3::YansWifiPhy> sender, ns3::Ptr<ns3::Packet const> packet, double txPowerDbm, ns3::WifiMode wifiMode, ns3::WifiPreamble preamble) const [member function]
    cls.add_method('Send', 
                   'void', 
                   [param('ns3::Ptr< ns3::YansWifiPhy >', 'sender'), param('ns3::Ptr< ns3::Packet const >', 'packet'), param('double', 'txPowerDbm'), param('ns3::WifiMode', 'wifiMode'), param('ns3::WifiPreamble', 'preamble')], 
                   is_const=True)
    ## yans-wifi-channel.h: void ns3::YansWifiChannel::SetPropagationDelayModel(ns3::Ptr<ns3::PropagationDelayModel> delay) [member function]
    cls.add_method('SetPropagationDelayModel', 
                   'void', 
                   [param('ns3::Ptr< ns3::PropagationDelayModel >', 'delay')])
    ## yans-wifi-channel.h: void ns3::YansWifiChannel::SetPropagationLossModel(ns3::Ptr<ns3::PropagationLossModel> loss) [member function]
    cls.add_method('SetPropagationLossModel', 
                   'void', 
                   [param('ns3::Ptr< ns3::PropagationLossModel >', 'loss')])
    return

def register_Ns3AarfWifiManager_methods(root_module, cls):
    ## aarf-wifi-manager.h: ns3::AarfWifiManager::AarfWifiManager(ns3::AarfWifiManager const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::AarfWifiManager const &', 'arg0')])
    ## aarf-wifi-manager.h: ns3::AarfWifiManager::AarfWifiManager() [constructor]
    cls.add_constructor([])
    ## aarf-wifi-manager.h: static ns3::TypeId ns3::AarfWifiManager::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## aarf-wifi-manager.h: ns3::WifiRemoteStation * ns3::AarfWifiManager::CreateStation() [member function]
    cls.add_method('CreateStation', 
                   'ns3::WifiRemoteStation *', 
                   [], 
                   visibility='private', is_virtual=True)
    return

def register_Ns3DcaTxop_methods(root_module, cls):
    ## dca-txop.h: static ns3::TypeId ns3::DcaTxop::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## dca-txop.h: ns3::DcaTxop::DcaTxop() [constructor]
    cls.add_constructor([])
    ## dca-txop.h: void ns3::DcaTxop::SetLow(ns3::Ptr<ns3::MacLow> low) [member function]
    cls.add_method('SetLow', 
                   'void', 
                   [param('ns3::Ptr< ns3::MacLow >', 'low')])
    ## dca-txop.h: void ns3::DcaTxop::SetManager(ns3::DcfManager * manager) [member function]
    cls.add_method('SetManager', 
                   'void', 
                   [param('ns3::DcfManager *', 'manager')])
    ## dca-txop.h: void ns3::DcaTxop::SetWifiRemoteStationManager(ns3::Ptr<ns3::WifiRemoteStationManager> remoteManager) [member function]
    cls.add_method('SetWifiRemoteStationManager', 
                   'void', 
                   [param('ns3::Ptr< ns3::WifiRemoteStationManager >', 'remoteManager')])
    ## dca-txop.h: void ns3::DcaTxop::SetTxOkCallback(ns3::Callback<void, ns3::WifiMacHeader const&, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> callback) [member function]
    cls.add_method('SetTxOkCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::WifiMacHeader const &, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'callback')])
    ## dca-txop.h: void ns3::DcaTxop::SetTxFailedCallback(ns3::Callback<void, ns3::WifiMacHeader const&, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> callback) [member function]
    cls.add_method('SetTxFailedCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::WifiMacHeader const &, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'callback')])
    ## dca-txop.h: void ns3::DcaTxop::SetMaxQueueSize(uint32_t size) [member function]
    cls.add_method('SetMaxQueueSize', 
                   'void', 
                   [param('uint32_t', 'size')])
    ## dca-txop.h: void ns3::DcaTxop::SetMaxQueueDelay(ns3::Time delay) [member function]
    cls.add_method('SetMaxQueueDelay', 
                   'void', 
                   [param('ns3::Time', 'delay')])
    ## dca-txop.h: void ns3::DcaTxop::SetMinCw(uint32_t minCw) [member function]
    cls.add_method('SetMinCw', 
                   'void', 
                   [param('uint32_t', 'minCw')], 
                   is_virtual=True)
    ## dca-txop.h: void ns3::DcaTxop::SetMaxCw(uint32_t maxCw) [member function]
    cls.add_method('SetMaxCw', 
                   'void', 
                   [param('uint32_t', 'maxCw')], 
                   is_virtual=True)
    ## dca-txop.h: void ns3::DcaTxop::SetAifsn(uint32_t aifsn) [member function]
    cls.add_method('SetAifsn', 
                   'void', 
                   [param('uint32_t', 'aifsn')], 
                   is_virtual=True)
    ## dca-txop.h: uint32_t ns3::DcaTxop::GetMinCw() const [member function]
    cls.add_method('GetMinCw', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## dca-txop.h: uint32_t ns3::DcaTxop::GetMaxCw() const [member function]
    cls.add_method('GetMaxCw', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## dca-txop.h: uint32_t ns3::DcaTxop::GetAifsn() const [member function]
    cls.add_method('GetAifsn', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## dca-txop.h: void ns3::DcaTxop::Queue(ns3::Ptr<ns3::Packet const> packet, ns3::WifiMacHeader const & hdr) [member function]
    cls.add_method('Queue', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet'), param('ns3::WifiMacHeader const &', 'hdr')])
    ## dca-txop.h: void ns3::DcaTxop::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   visibility='private', is_virtual=True)
    return

def register_functions(root_module):
    module = root_module
    ## ssid.h: extern ns3::Ptr<ns3::AttributeChecker const> ns3::MakeSsidChecker() [free function]
    module.add_function('MakeSsidChecker', 
                        'ns3::Ptr< ns3::AttributeChecker const >', 
                        [])
    ## wifi-mode.h: extern ns3::Ptr<ns3::AttributeChecker const> ns3::MakeWifiModeChecker() [free function]
    module.add_function('MakeWifiModeChecker', 
                        'ns3::Ptr< ns3::AttributeChecker const >', 
                        [])
    ## qos-utils.h: extern uint8_t ns3::QosUtilsGetTidForPacket(ns3::Ptr<ns3::Packet const> packet) [free function]
    module.add_function('QosUtilsGetTidForPacket', 
                        'uint8_t', 
                        [param('ns3::Ptr< ns3::Packet const >', 'packet')])
    ## qos-utils.h: extern ns3::AccessClass ns3::QosUtilsMapTidToAc(uint8_t tid) [free function]
    module.add_function('QosUtilsMapTidToAc', 
                        'ns3::AccessClass', 
                        [param('uint8_t', 'tid')])
    register_functions_ns3_Config(module.get_submodule('Config'), root_module)
    register_functions_ns3_TimeStepPrecision(module.get_submodule('TimeStepPrecision'), root_module)
    register_functions_ns3_addressUtils(module.get_submodule('addressUtils'), root_module)
    register_functions_ns3_aodv(module.get_submodule('aodv'), root_module)
    register_functions_ns3_dot11s(module.get_submodule('dot11s'), root_module)
    register_functions_ns3_flame(module.get_submodule('flame'), root_module)
    register_functions_ns3_internal(module.get_submodule('internal'), root_module)
    register_functions_ns3_olsr(module.get_submodule('olsr'), root_module)
    return

def register_functions_ns3_Config(module, root_module):
    return

def register_functions_ns3_TimeStepPrecision(module, root_module):
    return

def register_functions_ns3_addressUtils(module, root_module):
    return

def register_functions_ns3_aodv(module, root_module):
    return

def register_functions_ns3_dot11s(module, root_module):
    return

def register_functions_ns3_flame(module, root_module):
    return

def register_functions_ns3_internal(module, root_module):
    return

def register_functions_ns3_olsr(module, root_module):
    return


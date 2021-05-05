device_config = {
    'miso':12,
    'mosi':13,
    'ss':15,
    'sck':14,
    'dio_0':5,
    'reset':4,
    'led':2,
}

lora_parameters = {
    'frequency': 443E6,
    'tx_power_level': 2,
    'signal_bandwidth': 125E3,
    'spreading_factor': 8,
    'coding_rate': 5,
    'preamble_length': 8,
    'implicit_header': False,
    'sync_word': 0x12,
    'enable_CRC': False,
    'invert_IQ': False,
}
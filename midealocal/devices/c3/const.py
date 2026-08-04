"""Midea local C3 device const."""

from enum import IntEnum, StrEnum


class DeviceAttributes(StrEnum):
    """Midea C3 device attributes."""

    zone1_power = "zone1_power"
    zone2_power = "zone2_power"
    dhw_power = "dhw_power"
    zone1_curve = "zone1_curve"
    zone2_curve = "zone2_curve"
    disinfect = "disinfect"
    fast_dhw = "fast_dhw"
    zone_temp_type = "zone_temp_type"
    zone1_room_temp_mode = "zone1_room_temp_mode"
    zone2_room_temp_mode = "zone2_room_temp_mode"
    zone1_water_temp_mode = "zone1_water_temp_mode"
    zone2_water_temp_mode = "zone2_water_temp_mode"
    mode = "mode"
    mode_auto = "mode_auto"
    zone_target_temp = "zone_target_temp"
    dhw_target_temp = "dhw_target_temp"
    room_target_temp = "room_target_temp"
    zone_heating_temp_max = "zone_heating_temp_max"
    zone_heating_temp_min = "zone_heating_temp_min"
    zone_cooling_temp_max = "zone_cooling_temp_max"
    zone_cooling_temp_min = "zone_cooling_temp_min"
    tank_actual_temperature = "tank_actual_temperature"
    room_temp_max = "room_temp_max"
    room_temp_min = "room_temp_min"
    dhw_temp_max = "dhw_temp_max"
    dhw_temp_min = "dhw_temp_min"
    target_temperature = "target_temperature"
    temperature_max = "temperature_max"
    temperature_min = "temperature_min"
    status_heating = "status_heating"
    status_cool = "status_cool"
    status_dhw = "status_dhw"
    status_tbh = "status_tbh"
    status_ibh = "status_ibh"
    total_energy_consumption = "total_energy_consumption"
    total_produced_energy = "total_produced_energy"
    outdoor_temperature = "outdoor_temperature"
    temp_tw_in = "temp_tw_in"
    temp_tw_out = "temp_tw_out"
    instant_power0 = "instant_power0"
    silent_mode = "silent_mode"
    SILENT_LEVEL = "silent_level"
    eco_mode = "eco_mode"
    eco_function_state = "eco_function_state"
    eco_timer_state = "eco_timer_state"
    tbh = "tbh"
    error_code = "error_code"
    error_code_description = "error_code_description"
    holiday_on = "holiday_on"
    comp_run_freq = "comp_run_freq"
    fan_speed = "fan_speed"
    temp_t3 = "temp_t3"
    temp_ta = "temp_ta"
    pressure_high = "pressure_high"
    pressure_low = "pressure_low"
    water_flow = "water_flow"
    water_pressure = "water_pressure"
    heat_elec_total_consum0 = "heat_elec_total_consum0"
    heat_elec_total_capacity0 = "heat_elec_total_capacity0"
    heat = "heat"
    cool = "cool"
    dhw = "dhw"
    double_zone = "double_zone"
    room_thermal_support = "room_thermal_support"
    room_thermal_state = "room_thermal_state"
    time_set = "time_set"
    disinfect_run = "disinfect_run"
    remote_onoff = "remote_onoff"
    tbh_control = "tbh_control"
    SysEnergyAnaEN = "SysEnergyAnaEN"
    HMIEnergyAnaSetEN = "HMIEnergyAnaSetEN"
    current_unit_capacity = "current_unit_capacity"
    dc_current = "dc_current"
    disinfect_set_weekday = "disinfect_set_weekday"
    disinfect_start_hour = "disinfect_start_hour"
    disinfect_start_minutes = "disinfect_start_minutes"
    exv_opening = "exv_opening"
    fg_capacity_need = "fg_capacity_need"
    fg_usb_info_connect = "fg_usb_info_connect"
    hydbox_subtype = "hydbox_subtype"
    hydrobox_capacity = "hydrobox_capacity"
    idu_t1s1 = "idu_t1s1"
    idu_t1s2 = "idu_t1s2"
    instant_renew_power0 = "instant_renew_power0"
    machine_type = "machine_type"
    odu_model = "odu_model"
    odu_plan_vol_lmt = "odu_plan_vol_lmt"
    odu_target_fre = "odu_target_fre"
    odu_voltage = "odu_voltage"
    pwm_pump_out = "pwm_pump_out"
    room_rel_hum = "room_rel_hum"
    sphera_ahs_voltage = "sphera_ahs_voltage"
    t5s = "t5s"
    tas = "tas"
    temp_t1 = "temp_t1"
    temp_t2 = "temp_t2"
    temp_t2b = "temp_t2b"
    temp_t4 = "temp_t4"
    temp_t4a_ver = "temp_t4a_ver"
    temp_t5 = "temp_t5"
    temp_tb_t1 = "temp_tb_t1"
    temp_tb_t2 = "temp_tb_t2"
    temp_tf = "temp_tf"
    temp_th = "temp_th"
    temp_tp = "temp_tp"
    temp_tsolar = "temp_tsolar"
    temp_tw2 = "temp_tw2"
    total_electricity0 = "total_electricity0"
    total_renew_power0 = "total_renew_power0"
    total_thermal0 = "total_thermal0"
    unit_mode_run = "unit_mode_run"
    zone1_temp_set = "zone1_temp_set"
    zone2_temp_set = "zone2_temp_set"
    zone_terminal_type = "zone_terminal_type"


class C3SilentLevel(IntEnum):
    """C3 Silent Level."""

    OFF = 0x0
    SILENT = 0x1
    SUPER_SILENT = 0x3


class C3FanSpeed(IntEnum):
    """C3 Fan Speed level.

    POZOR: presne nazvy urovni (napr. "nizka/stredni/vysoka") nejsou
    potvrzeny zadnou verejne dostupnou dokumentaci k tomuto modelu
    (Galmet Prima 06 GT) - hodnoty 10/20/30/40 potvrdil uzivatel z pameti
    (odpovidaji tomu, co uz kod pocital jako raw_byte*10). Pojmenovano
    obecne jako LEVEL_1..4, dokud nebude k dispozici presnejsi zdroj.
    """

    LEVEL_1 = 10
    LEVEL_2 = 20
    LEVEL_3 = 30
    LEVEL_4 = 40


class C3DeviceMode(IntEnum):
    """C3 Device Mode."""

    COOL = 2
    HEAT = 3


class C3UnitRunMode(IntEnum):
    """C3 Unit actual running mode (registr 101 dle Modbus V4.7: '0: off,
    2: cooling, 3: heating').
    """

    OFF = 0
    COOL = 2
    HEAT = 3


# Error code table 1 z oficialni Modbus dokumentace (V4.7, str. 11-12).
# Format: raw_value: (kod, popis).
# POZOR: 4 kody (Hd, HE, L2, L8) maji v PDF nejasne priradeny popis kvuli
# zpusobu extrakce textu (dvousloupcovy layout) - u nich radeji necham jen
# kod bez popisu, nez abych riskoval spatnou diagnozu.
C3_ERROR_CODE_TABLE: dict[int, tuple[str, str]] = {
    1: ("E0", "Water flow fault (E8 displayed 3 times)"),
    2: ("E1", "Outlet water temp. sensor for Zone 2 (Tw2) fault"),
    3: ("E2", "Communication fault between controller and hydraulic module"),
    4: ("E3", "Final outlet water temp. sensor (T1) fault"),
    5: ("E4", "Water tank temp. sensor (T5) fault"),
    6: ("E5", "Condenser outlet refrigerant temp. sensor (T3) fault"),
    7: ("E6", "Ambient temp. sensor (T4) fault"),
    8: ("E7", "Buffer tank up temp. sensor (Tbt1) fault"),
    9: ("E8", "Water flow failure"),
    10: ("E9", "Suction temp. sensor (Th) fault"),
    11: ("EA", "Discharge temp. sensor (Tp) fault"),
    12: ("Eb", "Solar temp. sensor (Tsolar) fault"),
    13: ("Ec", "Buffer tank low temp. sensor (Tbt2) fault"),
    14: ("Ed", "Inlet water temp. sensor (Tw_in) malfunction"),
    15: ("EE", "Hydraulic module EEPROM failure"),
    20: ("P0", "Low pressure switch protection"),
    21: ("P1", "High pressure switch protection"),
    23: ("P3", "Compressor overcurrent protection"),
    24: ("P4", "High discharge temperature protection"),
    25: ("P5", "|Tw_out - Tw_in| value too big protection"),
    26: ("P6", "Inverter module protection"),
    31: ("Pb", "Anti-freeze mode"),
    33: ("Pd", "High temperature protection of refrigerant outlet temp. of condenser"),
    38: ("PP", "Tw_out - Tw_in unusual protection"),
    39: ("H0", "Communication fault between main board PCB B and hydraulic module main control board"),
    40: ("H1", "Communication fault between inverter module PCB A and main control board PCB B"),
    41: ("H2", "Refrigerant liquid temp. sensor (T2) fault"),
    42: ("H3", "Refrigerant gas temp. sensor (T2B) fault"),
    43: ("H4", "Three times P6 (L0/L1) protection"),
    44: ("H5", "Room temp. sensor (Ta) fault"),
    45: ("H6", "DC fan motor fault"),
    46: ("H7", "Voltage protection"),
    47: ("H8", "Pressure sensor fault"),
    48: ("H9", "Speed difference > 15Hz between front and back clock"),
    49: ("HA", "Speed difference > 15Hz between real and setting speed"),
    50: ("Hb", "3 times PP protection and Tw_out < 7C"),
    52: ("Hd", "Unknown / description unclear in source document"),
    53: ("HE", "Unknown / description unclear in source document"),
    54: ("HF", "Inverter module board EEPROM fault"),
    55: ("HH", "H6 displayed 10 times in 2 hours"),
    57: ("HP", "Low pressure protection (Pe<0.6) occurred 3 times in 1 hour"),
    65: ("C7", "Transducer module temperature too high protection"),
    112: ("bH", "PED PCB fault"),
    116: ("F1", "Low DC generatrix voltage protection"),
    134: ("L0", "Module protection"),
    135: ("L1", "DC generatrix low voltage protection"),
    136: ("L2", "Unknown / description unclear in source document"),
    138: ("L4", "MCE fault"),
    139: ("L5", "Zero speed protection"),
    141: ("L7", "Phase sequence fault / phase loss or neutral+live reversed (3-phase only)"),
    142: ("L8", "Unknown / description unclear in source document"),
    143: ("L9", "Unknown / description unclear in source document"),
}

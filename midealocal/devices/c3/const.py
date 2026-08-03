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
    exv_current = "exv_current"
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

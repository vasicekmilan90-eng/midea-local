"""Midea local C3 message."""

from midealocal.const import DeviceType
from midealocal.message import (
    ListTypes,
    MessageBody,
    MessageRequest,
    MessageResponse,
    MessageType,
)

from .const import C3_ERROR_CODE_TABLE, C3FanSpeed, C3SilentLevel, C3UnitRunMode

TEMP_NEG_VALUE = 127


class MessageC3Base(MessageRequest):
    """C3 message base."""

    def __init__(
        self,
        protocol_version: int,
        message_type: MessageType,
        body_type: ListTypes,
    ) -> None:
        """Initialize C3 message base."""
        super().__init__(
            device_type=DeviceType.C3,
            protocol_version=protocol_version,
            message_type=message_type,
            body_type=body_type,
        )

    @property
    def _body(self) -> bytearray:
        raise NotImplementedError


class MessageQuery(MessageC3Base):
    """C3 message query."""

    def __init__(self, protocol_version: int, body_type: ListTypes) -> None:
        """Initialize C3 message query."""
        super().__init__(
            protocol_version=protocol_version,
            message_type=MessageType.query,
            body_type=body_type,
        )

    @property
    def _body(self) -> bytearray:
        return bytearray([])


class MessageQueryBasic(MessageQuery):
    """C3 Message query basic."""

    def __init__(self, protocol_version: int) -> None:
        """Initialize C3 message query basic."""
        super().__init__(protocol_version, ListTypes.X01)


class MessageQuerySilence(MessageQuery):
    """C3 Message query silence."""

    def __init__(self, protocol_version: int) -> None:
        """Initialize C3 message query silence."""
        super().__init__(protocol_version, ListTypes.X05)


class MessageQueryECO(MessageQuery):
    """C3 Message query ECO."""

    def __init__(self, protocol_version: int) -> None:
        """Initialize C3 message query silence."""
        super().__init__(protocol_version, ListTypes.X07)


class MessageQueryInstall(MessageQuery):
    """C3 Message query INSTALL."""

    def __init__(self, protocol_version: int) -> None:
        """Initialize C3 message query silence."""
        super().__init__(protocol_version, ListTypes.X08)


class MessageQueryDisinfect(MessageQuery):
    """C3 Message query Disinfect."""

    def __init__(self, protocol_version: int) -> None:
        """Initialize C3 message query silence."""
        super().__init__(protocol_version, ListTypes.X09)


class MessageQueryUnitPara(MessageQuery):
    """C3 Message query UNITPARA."""

    def __init__(self, protocol_version: int) -> None:
        """Initialize C3 message query silence."""
        super().__init__(protocol_version, ListTypes.X10)


class MessageQueryHMIPara(MessageQuery):
    """C3 Message query HMIPARA."""

    def __init__(self, protocol_version: int) -> None:
        """Initialize C3 message query silence."""
        super().__init__(protocol_version, ListTypes.X0A)


class MessageSet(MessageC3Base):
    """C3 message set."""

    def __init__(self, protocol_version: int) -> None:
        """Initialize C3 message set."""
        super().__init__(
            protocol_version=protocol_version,
            message_type=MessageType.set,
            body_type=ListTypes.X01,
        )
        self.zone1_power = False
        self.zone2_power = False
        self.dhw_power = False
        self.mode = 0
        self.zone_target_temp = [25.0, 25.0]
        self.dhw_target_temp = 40.0
        self.room_target_temp = 25.0
        self.zone1_curve = False
        self.zone2_curve = False
        self.fast_dhw = False
        self.tbh = False

    @property
    def _body(self) -> bytearray:
        # Byte 1
        zone1_power = 0x01 if self.zone1_power else 0x00
        zone2_power = 0x02 if self.zone2_power else 0x00
        dhw_power = 0x04 if self.dhw_power else 0x00
        # Byte 7
        zone1_curve = 0x01 if self.zone1_curve else 0x00
        zone2_curve = 0x02 if self.zone2_curve else 0x00
        tbh = 0x04 if self.tbh else 0x00
        fast_dhw = 0x08 if self.fast_dhw else 0x00
        room_target_temp = int(self.room_target_temp * 2)
        zone1_target_temp = int(self.zone_target_temp[0])
        zone2_target_temp = int(self.zone_target_temp[1])
        dhw_target_temp = int(self.dhw_target_temp)
        return bytearray(
            [
                zone1_power | zone2_power | dhw_power,
                self.mode,
                zone1_target_temp,
                zone2_target_temp,
                dhw_target_temp,
                room_target_temp,
                zone1_curve | zone2_curve | tbh | fast_dhw,
            ],
        )


class MessageSetSilent(MessageC3Base):
    """C3 message set silent."""

    def __init__(self, protocol_version: int) -> None:
        """Initialize C3 message set silent."""
        super().__init__(
            protocol_version=protocol_version,
            message_type=MessageType.set,
            body_type=ListTypes.X05,
        )
        self.silent_mode = False
        self.silent_level = C3SilentLevel.OFF

    @property
    def _body(self) -> bytearray:
        return bytearray(
            [
                self.silent_level if self.silent_mode else C3SilentLevel.OFF,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
            ],
        )


class MessageSetECO(MessageC3Base):
    """C3 message set eco."""

    def __init__(self, protocol_version: int) -> None:
        """Initialize C3 message set eco."""
        super().__init__(
            protocol_version=protocol_version,
            message_type=MessageType.set,
            body_type=ListTypes.X07,
        )
        self.eco_mode = False

    @property
    def _body(self) -> bytearray:
        eco_mode = 0x01 if self.eco_mode else 0

        return bytearray([eco_mode, 0x00, 0x00, 0x00, 0x00, 0x00])


class MessageSetDisinfect(MessageC3Base):
    """C3 message set Disinfect."""

    def __init__(self, protocol_version: int) -> None:
        """Initialize C3 message set eco."""
        super().__init__(
            protocol_version=protocol_version,
            message_type=MessageType.set,
            body_type=ListTypes.X09,
        )
        self.disinfect = False

    @property
    def _body(self) -> bytearray:
        disinfect = 0x01 if self.disinfect else 0

        return bytearray([disinfect, 0x00, 0x00, 0x00])


class C3BasicBody(MessageBody):
    """C3 Basic message body."""

    def __init__(self, body: bytearray, data_offset: int = 0) -> None:
        """Initialize C3 message body."""
        super().__init__(body)
        # BodyBytes 1
        self.zone1_power = body[data_offset + 0] & 0x01 > 0
        self.zone2_power = body[data_offset + 0] & 0x02 > 0
        self.dhw_power = body[data_offset + 0] & 0x04 > 0
        self.zone1_curve = body[data_offset + 0] & 0x08 > 0
        self.zone2_curve = body[data_offset + 0] & 0x10 > 0
        self.tbh = body[data_offset + 0] & 0x20 > 0
        self.fast_dhw = body[data_offset + 0] & 0x40 > 0
        self.remote_onoff = body[data_offset + 0] & 0x80 > 0
        # BodyBytes 2
        self.heat = body[data_offset + 1] & 0x01 > 0
        self.cool = body[data_offset + 1] & 0x02 > 0
        self.dhw = body[data_offset + 1] & 0x04 > 0
        self.double_zone = body[data_offset + 1] & 0x08 > 0
        self.zone_temp_type = [
            body[data_offset + 1] & 0x10 > 0,
            body[data_offset + 1] & 0x20 > 0,
        ]
        self.room_thermal_support = body[data_offset + 1] & 0x40 > 0
        self.room_thermal_state = body[data_offset + 1] & 0x80 > 0
        # BodyBytes 3
        self.time_set = body[data_offset + 2] & 0x01 > 0
        self.silent_mode = body[data_offset + 2] & 0x02 > 0
        self.holiday_on = body[data_offset + 2] & 0x04 > 0
        self.eco_mode = body[data_offset + 2] & 0x08 > 0
        self.zone_terminal_type = body[data_offset + 2]
        # BodyBytes 4
        self.mode = body[data_offset + 3]
        self.mode_auto = body[data_offset + 4]
        # zone1, zone2
        self.zone_target_temp = [
            float(body[data_offset + 5]),
            float(body[data_offset + 6]),
        ]
        self.dhw_target_temp = float(body[data_offset + 7])
        self.room_target_temp = float(body[data_offset + 8] / 2)
        # zone1, zone2
        self.zone_heating_temp_max = [
            float(body[data_offset + 9]),
            float(body[data_offset + 13]),
        ]
        self.zone_heating_temp_min = [
            float(body[data_offset + 10]),
            float(body[data_offset + 14]),
        ]
        self.zone_cooling_temp_max = [
            float(body[data_offset + 11]),
            float(body[data_offset + 15]),
        ]
        self.zone_cooling_temp_min = [
            float(body[data_offset + 12]),
            float(body[data_offset + 16]),
        ]
        self.room_temp_max = float(body[data_offset + 17] / 2)
        self.room_temp_min = float(body[data_offset + 18] / 2)
        self.dhw_temp_max = float(body[data_offset + 19])
        self.dhw_temp_min = float(body[data_offset + 20])
        self.tank_actual_temperature = float(body[data_offset + 21])
        self.error_code = body[data_offset + 22]
        _code_info = C3_ERROR_CODE_TABLE.get(self.error_code)
        if self.error_code == 0:
            self.error_code_description = "No error"
        elif _code_info:
            self.error_code_description = f"{_code_info[0]}: {_code_info[1]}"
        else:
            self.error_code_description = f"Unknown code (raw={self.error_code})"
        self.tbh_control = body[data_offset + 23] & 0x80 > 0
        self.SysEnergyAnaEN = body[data_offset + 23] & 0x20 > 0
        self.HMIEnergyAnaSetEN = body[data_offset + 23] & 0x40 > 0


class C3EnergyBody(MessageBody):
    """C3 Energy MSG_TYPE_UP_POWER4 message body."""

    def __init__(self, body: bytearray, data_offset: int = 0) -> None:
        """Initialize C3 notify1 message body."""
        super().__init__(body)
        status_byte = body[data_offset]
        # bit0
        self.status_heating = (status_byte & 0x01) > 0
        # bit1
        self.status_cool = (status_byte & 0x02) > 0
        # bit2
        self.status_dhw = (status_byte & 0x04) > 0
        # bit3
        self.status_tbh = (status_byte & 0x08) > 0
        # bit4
        self.status_ibh = (status_byte & 0x10) > 0
        # total_energy_consumption
        self.total_energy_consumption = (
            (body[data_offset + 1] << 32)
            + (body[data_offset + 2] << 16)
            + (body[data_offset + 3] << 8)
            + (body[data_offset + 4])
        )
        # total_produced_energy
        self.total_produced_energy = (
            (body[data_offset + 5] << 32)
            + (body[data_offset + 6] << 16)
            + (body[data_offset + 7] << 8)
            + (body[data_offset + 8])
        )
        base_value = body[data_offset + 9]
        self.outdoor_temperature = float(
            (base_value - 256) if base_value > TEMP_NEG_VALUE else base_value,
        )  # outdoor_temperature is t4
        self.zone1_temp_set = float(body[data_offset + 10])
        self.zone2_temp_set = float(body[data_offset + 11])
        self.t5s = body[data_offset + 12]
        self.tas = body[data_offset + 13]


class C3SilenceBody(MessageBody):
    """C3 Silence message body."""

    def __init__(self, body: bytearray, data_offset: int = 0) -> None:
        """Initialize C3 query silence message body."""
        super().__init__(body)
        self.silent_mode = body[data_offset] & 0x1 > 0
        self.silent_level = C3SilentLevel(
            (body[data_offset] & 0x1) + ((body[data_offset] & 0x8) >> 2)
            if self.silent_mode
            else C3SilentLevel.OFF.value,
        ).name
        # Message protocol information:
        # silence_function_state: Byte 1, BIT 0
        # silence_timer1_state: Byte 1, BIT 1
        # silence_timer2_state: Byte 1, BIT 2
        # silence_function_level: Byte 1, BIT 3
        # silence_timer1_starthour: Byte 2
        # silence_timer1_startmin: Byte 3
        # silence_timer1_endhour: Byte 4
        # silence_timer1_endmin: Byte 5
        # silence_timer2_starthour: Byte 6
        # silence_timer2_startmin: Byte 7
        # silence_timer2_endhour: Byte 8
        # silence_timer2_endmin: Byte 9


class C3ECOBody(MessageBody):
    """C3 ECO message body."""

    def __init__(self, body: bytearray, data_offset: int = 0) -> None:
        """Initialize C3 ECO message body."""
        super().__init__(body)
        self.eco_function_state = body[data_offset] & 0x01 > 0
        self.eco_timer_state = body[data_offset] & 0x02 > 0


class C3DisinfectBody(MessageBody):
    """C3 Disinfect message body."""

    def __init__(self, body: bytearray, data_offset: int = 0) -> None:
        """Initialize C3 Disinfect message body."""
        super().__init__(body)
        self.disinfect = body[data_offset] & 0x01 > 0
        self.disinfect_run = body[data_offset] & 0x02 > 0
        self.disinfect_set_weekday = body[data_offset + 1]
        self.disinfect_start_hour = body[data_offset + 2]
        self.disinfect_start_minutes = body[data_offset + 3]


class C3UnitParaBody(MessageBody):
    """C3 UnitPara message body."""

    def __init__(self, body: bytearray, data_offset: int = 0) -> None:
        """Initialize C3 UnitPara message body."""
        super().__init__(body)
        self.comp_run_freq = body[data_offset]
        _unit_mode_raw = body[data_offset + 1]
        try:
            self.unit_mode_run = C3UnitRunMode(_unit_mode_raw).name
        except ValueError:
            self.unit_mode_run = _unit_mode_raw
        _fan_speed_raw = body[data_offset + 3] * 10
        try:
            self.fan_speed = C3FanSpeed(_fan_speed_raw).name
        except ValueError:
            # neznama hodnota - vratime radeji cislo nez aby to spadlo,
            # ale je to signal, ze existuje i jina uroven nez 10/20/30/40
            self.fan_speed = _fan_speed_raw
        self.fg_capacity_need = body[data_offset + 5]
        self.temp_t3 = body[data_offset + 6]
        self.temp_t4 = body[data_offset + 7]
        self.temp_tp = body[data_offset + 8]
        self.temp_tw_in = body[data_offset + 9]
        self.temp_tw_out = body[data_offset + 10]
        self.temp_tsolar = body[data_offset + 11]
        self.hydbox_subtype = body[data_offset + 12]
        self.fg_usb_info_connect = body[data_offset + 13]
        # self.usb_index_max  body[data_offset + 14]
        # self.odu_comp_current  body[data_offset + 16]
        self.odu_voltage = body[data_offset + 17] * 256 + body[data_offset + 18]
        # OPRAVENO dle oficialni Modbus dokumentace (V4.7, registr 103 "EXV1"):
        # "Openness of the expansion valve 1 of outdoor unit, P" - jde o
        # OTEVRENI/POLOHU ventilu (procenta/jednotky P), NE o elektricky proud,
        # jak naznacoval puvodni nazev "exv_current" z community projektu.
        self.exv_opening = body[data_offset + 19] * 256 + body[data_offset + 20]
        self.odu_model = body[data_offset + 21]
        # self.unit_online_num  body[data_offset + 22]
        # self.current_code  body[data_offset + 23]
        self.temp_t1 = body[data_offset + 33]
        self.temp_tw2 = body[data_offset + 34]
        self.temp_t2 = body[data_offset + 35]
        self.temp_t2b = body[data_offset + 36]
        self.temp_t5 = body[data_offset + 37]
        self.temp_ta = body[data_offset + 38]
        self.temp_tb_t1 = body[data_offset + 39]
        self.temp_tb_t2 = body[data_offset + 40]
        # POZOR: dokumentace ma DVA ruzne registry pro "kapacitu" s ruznym
        # skalovanim - "123 Unit capacity" primo (napr. 4 = 4kW), a "140
        # Capacity of hydraulic module" deleno 100. Neni jiste, ktery z nich
        # odpovida temto dvema poljim - hodnoty nize jsou RAW.
        self.hydrobox_capacity = body[data_offset + 41]
        self.pressure_high = body[data_offset + 42] * 256 + body[data_offset + 43]
        self.pressure_low = body[data_offset + 44] * 256 + body[data_offset + 45]
        self.temp_th = body[data_offset + 46]
        self.machine_type = body[data_offset + 47]
        self.odu_target_fre = body[data_offset + 48]
        # Skalovani /10 dle oficialni Modbus dokumentace (V4.7, registr 133
        # "DC bus current"): "Actual value*10, A".
        self.dc_current = body[data_offset + 49] / 10
        self.temp_tf = body[data_offset + 51]
        self.idu_t1s1 = body[data_offset + 52]
        self.idu_t1s2 = body[data_offset + 53]
        # Skalovani /100 potvrzeno empiricky (2026-08-03): displej ovladaci
        # jednotky ukazoval ~0.73 m3/h, raw hodnota v ramci byla 91-97 =>
        # 0.91-0.97 po deleni 100 - odpovida nove Modbus mape (V4.7:
        # "Actual value*100, m3/h"), stara mapa (/10) davala nesmyslnych 9+ m3/h.
        self.water_flow = (
            body[data_offset + 54] * 256 + body[data_offset + 55]
        ) / 100
        self.odu_plan_vol_lmt = body[data_offset + 56]
        self.current_unit_capacity = body[data_offset + 57]
        self.sphera_ahs_voltage = body[data_offset + 59]
        self.temp_t4a_ver = body[data_offset + 60]
        self.water_pressure = body[data_offset + 61] * 256 + body[data_offset + 62]
        self.room_rel_hum = body[data_offset + 63]
        self.pwm_pump_out = body[data_offset + 63]
        # POZOR - dle novejsi Modbus mapy (V4.7) tyto 4 kumulativni pocitadla
        # energie maji byt "For R290 units: actual value*100; for other units:
        # actual value; kWh" - tedy skalovani zavisi na typu jednotky (R290 vs.
        # jina), coz z tohoto ramce nepozname. Hodnoty nize jsou RAW.
        self.total_electricity0 = (
            (body[data_offset + 66] << 32)
            + (body[data_offset + 67] << 16)
            + (body[data_offset + 68] << 8)
            + (body[data_offset + 69])
        )
        self.total_thermal0 = (
            (body[data_offset + 70] << 32)
            + (body[data_offset + 71] << 16)
            + (body[data_offset + 72] << 8)
            + (body[data_offset + 73])
        )
        self.heat_elec_total_consum0 = (
            (body[data_offset + 74] << 32)
            + (body[data_offset + 75] << 16)
            + (body[data_offset + 76] << 8)
            + (body[data_offset + 77])
        )
        self.heat_elec_total_capacity0 = (
            (body[data_offset + 78] << 32)
            + (body[data_offset + 79] << 16)
            + (body[data_offset + 80] << 8)
            + (body[data_offset + 81])
        )
        # POZOR - novejsi Modbus mapa uvadi u obdobnych "real-time" vykonovych
        # hodnot format "Actual value*100, kW" - RAW hodnota nize neni delena,
        # potreba overit (napr. proti instant_power0 jiz vystavenemu pres HA).
        self.instant_power0 = (body[data_offset + 82] << 8) + (body[data_offset + 83])
        self.instant_renew_power0 = (body[data_offset + 84] << 8) + (
            body[data_offset + 85]
        )
        # BUGFIX: puvodne cetlo stejne bajty jako instant_renew_power0 (kopirovaci
        # chyba). Podle rozboru syroveho X10 ramce (offset+86/+87 byly dosud
        # zcela neparsovane "neznama data") jde nejspis o spravne umisteni
        # total_renew_power0 - potreba empiricky overit diff-metodou.
        self.total_renew_power0 = (body[data_offset + 86] << 8) + (
            body[data_offset + 87]
        )

        # Identifikacni retezec na konci zpravy (overeno bajt po bajtu proti
        # realne zachycene zprave: bajty 96-159 = vyplnovaci pomlcky "-",
        # 160-191 = ASCII seriove cislo/model WiFi modulu, 192-199 = nuly).
        # Hledame robustne (delka zpravy/offset se muze mezi revizemi lisit)
        # - vezmeme vse po poslednim useku pomlcek az po prvni nulovy bajt.
        dash_run = b"-" * 20
        dash_idx = body.find(dash_run, data_offset)
        self.wifi_module_serial = None
        if dash_idx != -1:
            after_dashes = body[dash_idx:]
            # najdi konec useku pomlcek
            stripped = after_dashes.lstrip(b"-")
            end_idx = stripped.find(b"\x00")
            raw_serial = stripped[: end_idx if end_idx != -1 else None]
            try:
                decoded = raw_serial.decode("ascii").strip()
                if decoded:
                    self.wifi_module_serial = decoded
            except UnicodeDecodeError:
                self.wifi_module_serial = None


class MessageC3Response(MessageResponse):
    """C3 message response."""

    def __init__(self, message: bytes) -> None:
        """Initialize C3 message response."""
        super().__init__(bytearray(message))
        if (
            self.message_type
            in [MessageType.set, MessageType.notify1, MessageType.query]
            and self.body_type == ListTypes.X01
        ) or self.message_type == MessageType.notify2:
            self.set_body(C3BasicBody(super().body, data_offset=1))
        elif (
            self.message_type == MessageType.notify1 and self.body_type == ListTypes.X04
        ):
            self.set_body(C3EnergyBody(super().body, data_offset=1))
        elif self.message_type == MessageType.query and self.body_type == ListTypes.X05:
            self.set_body(C3SilenceBody(super().body, data_offset=1))
        elif self.body_type == ListTypes.X07:
            self.set_body(C3ECOBody(super().body, data_offset=1))
        elif self.body_type == ListTypes.X09:
            self.set_body(C3DisinfectBody(super().body, data_offset=1))
        elif self.body_type == ListTypes.X10:
            self.set_body(C3UnitParaBody(super().body, data_offset=1))
        self.set_attr()

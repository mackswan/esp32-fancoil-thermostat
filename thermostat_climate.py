from homeassistant.helpers.entity_registry import async_get as er_async_get

SENSOR_F   = "sensor.smart_thermostat_indoor_temperature"
SETPOINT_F = "number.smart_thermostat_set_temperature"
RELAY      = "switch.smart_thermostat_fcu_relay"
MODE_SEL   = "select.smart_thermostat_hvac_mode"
DEADBAND_F = 1.0
UNIQUE_ID  = "ec_smart_thermostat_climate"
ENTITY_ID  = "climate.ec_thermostat"

def _register_entity():
    if hass.states.get("climate.ec_thermostat"):
        hass.states.async_remove("climate.ec_thermostat")
    if hass.states.get("climate.ec_thermostat_2"):
        hass.states.async_remove("climate.ec_thermostat_2")
    if hass.states.get("climate.ewc_thermostat"):
        hass.states.async_remove("climate.ewc_thermostat")
    if hass.states.get("climate.ewc_thermostat_2"):
        hass.states.async_remove("climate.ewc_thermostat_2")
    registry = er_async_get(hass)
    existing = registry.async_get_entity_id("climate", "pyscript", UNIQUE_ID)
    if existing:
        log.info(f"EWC: entity already registered as {existing}")
    else:
        entry = registry.async_get_or_create(
            "climate",
            "pyscript",
            UNIQUE_ID,
            suggested_object_id="ec_thermostat",
        )
        log.info(f"EWC: entity registered as {entry.entity_id}")

def _infer_state():
    relay  = state.get(RELAY)
    temp_f = state.get(SENSOR_F)
    setp_f = state.get(SETPOINT_F)
    mode   = state.get(MODE_SEL)

    if mode is None or mode in ("unavailable", "unknown", "Off"):
        return "off", "off"

    if temp_f in (None, "unavailable", "unknown") or setp_f in (None, "unavailable", "unknown"):
        return mode.lower(), "off"

    temp_f = float(temp_f)
    setp_f = float(setp_f)

    if relay == "on":
        if temp_f > setp_f:
            return "cool", "cooling"
        else:
            return "heat", "heating"
    else:
        return mode.lower(), "idle"

def _publish_state():
    temp_f = state.get(SENSOR_F)
    setp_f = state.get(SETPOINT_F)
    hvac_mode, hvac_action = _infer_state()
    current_temp = round(float(temp_f), 1) if temp_f not in (None, "unavailable", "unknown") else None
    target_temp  = float(setp_f) if setp_f not in (None, "unavailable", "unknown") else None
    log.info(f"EC: publishing state={hvac_mode} action={hvac_action} temp={current_temp} target={target_temp}")
    hass.states.async_set(
        ENTITY_ID,
        hvac_mode,
        {
            "hvac_modes": ["heat", "cool", "off"],
            "hvac_action": hvac_action,
            "current_temperature": current_temp,
            "temperature": target_temp,
            "min_temp": 60,
            "max_temp": 85,
            "target_temp_step": 1,
            "supported_features": 1,
            "friendly_name": "Thermostat",
        }
    )

@state_trigger(SENSOR_F, SETPOINT_F, RELAY, MODE_SEL)
def on_sensor_change(**kwargs):
    _publish_state()

@event_trigger("call_service", "domain == 'climate' and service == 'set_temperature'")
def on_set_temperature_event(service_data=None, **kwargs):
    if service_data is None:
        return
    entity_id = service_data.get('entity_id')
    if isinstance(entity_id, list):
        entity_id = entity_id[0]
    temperature = service_data.get('temperature')
    log.info(f"EC: call_service event entity_id={entity_id} temperature={temperature}")
    if entity_id != ENTITY_ID or temperature is None:
        return
    temp_f = round(float(temperature))
    temp_f = max(60, min(85, temp_f))
    log.info(f"EC: writing {temp_f}°F to ESPHome")
    service.call("number", "set_value", entity_id=SETPOINT_F, value=temp_f)

@event_trigger("call_service", "domain == 'climate' and service == 'set_hvac_mode'")
def on_set_hvac_mode_event(service_data=None, **kwargs):
    if service_data is None:
        return
    entity_id = service_data.get('entity_id')
    if isinstance(entity_id, list):
        entity_id = entity_id[0]
    hvac_mode = service_data.get('hvac_mode')
    if entity_id != ENTITY_ID:
        return
    log.info(f"EC: mode write '{hvac_mode}' ignored — physical device only")
    _publish_state()

_register_entity()

@time_trigger("startup")
def on_startup(**kwargs):
    task.sleep(5)
    _publish_state()

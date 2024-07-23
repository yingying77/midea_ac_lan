from homeassistant.const import (
    Platform,
    UnitOfTime,
    UnitOfTemperature,
    UnitOfPower,
    PERCENTAGE,
    UnitOfEnergy,
    CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
    CONCENTRATION_PARTS_PER_MILLION
)
from homeassistant.components.binary_sensor import BinarySensorDeviceClass
from homeassistant.components.sensor import SensorStateClass, SensorDeviceClass
from .midea.devices.ac.device import DeviceAttributes as ACAttributes
from .midea.devices.ca.device import DeviceAttributes as CAAttributes
from .midea.devices.db.device import DeviceAttributes as DBAttributes


MIDEA_DEVICES = {
    0xAC: {
        "name": "Air Conditioner",
        "entities": {
            "climate": {
                "type": Platform.CLIMATE,
                "icon": "mdi:air-conditioner",
                "default": True
            },
            "fresh_air": {
                "type": Platform.FAN,
                "icon": "mdi:fan",
                "name": "Fresh Air"
            },
            ACAttributes.aux_heating: {
                "type": Platform.SWITCH,
                "name": "Aux Heating",
                "icon": "mdi:heat-wave"
            },
            ACAttributes.boost_mode: {
                "type": Platform.SWITCH,
                "name": "Boost Mode",
                "icon": "mdi:turbine"
            },
            ACAttributes.breezeless: {
                "type": Platform.SWITCH,
                "name": "Breezeless",
                "icon": "mdi:tailwind"
            },
            ACAttributes.comfort_mode: {
                "type": Platform.SWITCH,
                "name": "Comfort Mode",
                "icon": "mdi:alpha-c-circle"
            },
            ACAttributes.dry: {
                "type": Platform.SWITCH,
                "name": "Dry",
                "icon": "mdi:air-filter"
            },
            ACAttributes.eco_mode: {
                "type": Platform.SWITCH,
                "name": "ECO Mode",
                "icon": "mdi:leaf-circle"
            },
            ACAttributes.frost_protect: {
                "type": Platform.SWITCH,
                "name": "Frost Protect",
                "icon": "mdi:snowflake-alert"
            },
            ACAttributes.indirect_wind: {
                "type": Platform.SWITCH,
                "name": "Indirect Wind",
                "icon": "mdi:tailwind"
            },
            ACAttributes.natural_wind: {
                "type": Platform.SWITCH,
                "name": "Natural Wind",
                "icon": "mdi:tailwind"
            },
            ACAttributes.prompt_tone: {
                "type": Platform.SWITCH,
                "name": "Prompt Tone",
                "icon": "mdi:bell"
            },
            ACAttributes.power: {
                "type": Platform.SWITCH,
                "name": "Power",
                "icon": "mdi:power"
            },
            ACAttributes.screen_display: {
                "type": Platform.SWITCH,
                "name": "Screen Display",
                "icon": "mdi:television-ambient-light"
            },
            ACAttributes.screen_display_alternate: {
                "type": Platform.SWITCH,
                "name": "Screen Display Alternate",
                "icon": "mdi:television-ambient-light"
            },
            ACAttributes.sleep_mode: {
                "type": Platform.SWITCH,
                "name": "Sleep Mode",
                "icon": "mdi:power-sleep"
            },
            ACAttributes.smart_eye: {
                "type": Platform.SWITCH,
                "name": "Smart Eye",
                "icon": "mdi:eye"
            },
            ACAttributes.swing_horizontal: {
                "type": Platform.SWITCH,
                "name": "Swing Horizontal",
                "icon": "mdi:arrow-split-vertical"
            },
            ACAttributes.swing_vertical: {
                "type": Platform.SWITCH,
                "name": "Swing Vertical",
                "icon": "mdi:arrow-split-horizontal"
            },
            ACAttributes.full_dust: {
                "type": Platform.BINARY_SENSOR,
                "name": "Full of Dust",
                "icon": "mdi:alert-circle",
                "device_class": BinarySensorDeviceClass.PROBLEM
            },
            ACAttributes.indoor_humidity: {
                "type": Platform.SENSOR,
                "name": "Indoor Humidity",
                "device_class": SensorDeviceClass.HUMIDITY,
                "unit": PERCENTAGE,
                "state_class": SensorStateClass.MEASUREMENT
            },
            ACAttributes.indoor_temperature: {
                "type": Platform.SENSOR,
                "name": "Indoor Temperature",
                "device_class": SensorDeviceClass.TEMPERATURE,
                "unit": UnitOfTemperature.CELSIUS,
                "state_class": SensorStateClass.MEASUREMENT
            },
            ACAttributes.outdoor_temperature: {
                "type": Platform.SENSOR,
                "name": "Outdoor Temperature",
                "device_class": SensorDeviceClass.TEMPERATURE,
                "unit": UnitOfTemperature.CELSIUS,
                "state_class": SensorStateClass.MEASUREMENT
            },
            ACAttributes.total_energy_consumption: {
                "type": Platform.SENSOR,
                "name": "Total Energy Consumption",
                "device_class": SensorDeviceClass.ENERGY,
                "unit": UnitOfEnergy.KILO_WATT_HOUR,
                "state_class": SensorStateClass.TOTAL_INCREASING
            },
            ACAttributes.current_energy_consumption: {
                "type": Platform.SENSOR,
                "name": "Current Energy Consumption",
                "device_class": SensorDeviceClass.ENERGY,
                "unit": UnitOfEnergy.KILO_WATT_HOUR,
                "state_class": SensorStateClass.TOTAL_INCREASING
            },
            ACAttributes.realtime_power: {
                "type": Platform.SENSOR,
                "name": "Realtime Power",
                "device_class": SensorDeviceClass.POWER,
                "unit": UnitOfPower.WATT,
                "state_class": SensorStateClass.MEASUREMENT
            }
        }
    },
    0xCA: {
        "name": "Refrigerator",
        "entities": {
            CAAttributes.bar_door: {
                "type": Platform.BINARY_SENSOR,
                "name": "Bar Door",
                "icon": "mdi:box-shadow",
                "device_class": BinarySensorDeviceClass.DOOR
            },
            CAAttributes.bar_door_overtime: {
                "type": Platform.BINARY_SENSOR,
                "name": "Bar Door Overtime",
                "icon": "mdi:alert-circle",
                "device_class": BinarySensorDeviceClass.PROBLEM
            },
            CAAttributes.flex_zone_door: {
                "type": Platform.BINARY_SENSOR,
                "name": "Flex Door",
                "icon": "mdi:box-shadow",
                "device_class": BinarySensorDeviceClass.DOOR
            },
            CAAttributes.flex_zone_door_overtime: {
                "type": Platform.BINARY_SENSOR,
                "name": "Flex Zone Door",
                "icon": "mdi:alert-circle",
                "device_class": BinarySensorDeviceClass.PROBLEM
            },
            CAAttributes.freezer_door: {
                "type": Platform.BINARY_SENSOR,
                "name": "Freezer Door",
                "icon": "mdi:box-shadow",
                "device_class": BinarySensorDeviceClass.DOOR
            },
            CAAttributes.freezer_door_overtime: {
                "type": Platform.BINARY_SENSOR,
                "name": "Freezer Door Overtime",
                "icon": "mdi:alert-circle",
                "device_class": BinarySensorDeviceClass.PROBLEM
            },
            CAAttributes.refrigerator_door: {
                "type": Platform.BINARY_SENSOR,
                "name": "Refrigerator Door",
                "icon": "mdi:alert-circle",
                "device_class": BinarySensorDeviceClass.PROBLEM
            },
            CAAttributes.refrigerator_door_overtime: {
                "type": Platform.BINARY_SENSOR,
                "name": "Refrigerator Door Overtime",
                "icon": "mdi:alert-circle",
                "device_class": BinarySensorDeviceClass.PROBLEM
            },
            CAAttributes.flex_zone_actual_temp: {
                "type": Platform.SENSOR,
                "name": "Flex Zone Actual Temperature",
                "device_class": SensorDeviceClass.TEMPERATURE,
                "unit": UnitOfTemperature.CELSIUS,
                "state_class": SensorStateClass.MEASUREMENT
            },
            CAAttributes.flex_zone_setting_temp: {
                "type": Platform.SENSOR,
                "name": "Flex Zone Setting Temperature",
                "device_class": SensorDeviceClass.TEMPERATURE,
                "unit": UnitOfTemperature.CELSIUS,
                "state_class": SensorStateClass.MEASUREMENT
            },
            CAAttributes.freezer_actual_temp: {
                "type": Platform.SENSOR,
                "name": "Freezer Actual Temperature",
                "device_class": SensorDeviceClass.TEMPERATURE,
                "unit": UnitOfTemperature.CELSIUS,
                "state_class": SensorStateClass.MEASUREMENT
            },
            CAAttributes.freezer_setting_temp: {
                "type": Platform.SENSOR,
                "name": "Freezer Setting Temperature",
                "device_class": SensorDeviceClass.TEMPERATURE,
                "unit": UnitOfTemperature.CELSIUS,
                "state_class": SensorStateClass.MEASUREMENT
            },
            CAAttributes.energy_consumption: {
                "type": Platform.SENSOR,
                "name": "Energy Consumption",
                "device_class": SensorDeviceClass.ENERGY,
                "unit": UnitOfEnergy.KILO_WATT_HOUR,
                "state_class": SensorStateClass.TOTAL_INCREASING
            },
            CAAttributes.refrigerator_actual_temp: {
                "type": Platform.SENSOR,
                "name": "Refrigerator Actual Temperature",
                "device_class": SensorDeviceClass.TEMPERATURE,
                "unit": UnitOfTemperature.CELSIUS,
                "state_class": SensorStateClass.MEASUREMENT
            },
            CAAttributes.refrigerator_setting_temp: {
                "type": Platform.SENSOR,
                "name": "Refrigerator Setting Temperature",
                "device_class": SensorDeviceClass.TEMPERATURE,
                "unit": UnitOfTemperature.CELSIUS,
                "state_class": SensorStateClass.MEASUREMENT
            },
            CAAttributes.right_flex_zone_actual_temp: {
                "type": Platform.SENSOR,
                "name": "Right Flex Zone Actual Temperature",
                "device_class": SensorDeviceClass.TEMPERATURE,
                "unit": UnitOfTemperature.CELSIUS,
                "state_class": SensorStateClass.MEASUREMENT
            },
            CAAttributes.right_flex_zone_setting_temp: {
                "type": Platform.SENSOR,
                "name": "Right Flex Zone Setting Temperature",
                "device_class": SensorDeviceClass.TEMPERATURE,
                "unit": UnitOfTemperature.CELSIUS,
                "state_class": SensorStateClass.MEASUREMENT
            },
        },
    },
    0xDB: {
        "name": "Front Load Washer",
        "entities": {
            DBAttributes.time_remaining: {
                "type": Platform.SENSOR,
                "name": "Time Remaining",
                "icon": "mdi:progress-clock",
                "unit": UnitOfTime.MINUTES,
                "state_class": SensorStateClass.MEASUREMENT
            },
            DBAttributes.progress: {
                "type": Platform.SENSOR,
                "name": "Progress",
                "icon": "mdi:rotate-360"
            },
            DBAttributes.power: {
                "type": Platform.SWITCH,
                "name": "Power",
                "icon": "mdi:power"
            },
            DBAttributes.start: {
                "type": Platform.SWITCH,
                "name": "Start",
                "icon": "mdi:motion-play-outline"
            },
        }
    },
}

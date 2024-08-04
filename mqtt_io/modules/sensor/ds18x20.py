"""

DS18X20 Dallas 1-Wire temperature sensor

Example configuration:

sensor_modules:
  - name: ds18x20
    module: ds18x20
    pin: 4

sensor_inputs:
  - name: temph20
    module: ds18x20
    pin: 1
    digits: 2
    interval: 5
    
"""

from typing import cast
from ...types import CerberusSchemaType, ConfigType
from . import GenericSensor

REQUIREMENTS = ("adafruit-circuitpython-ds18x20", "adafruit-circuitpython-onewire")


class Sensor(GenericSensor):
    """
    DS18X20 Dallas 1-Wire temperature sensor
    """

    SENSOR_SCHEMA: CerberusSchemaType = {
        "pin": dict(
            type="integer",
            required=True,
            empty=False,
        )
    }

    def setup_module(self) -> None:
        # pylint: disable=import-outside-toplevel,import-error
        import board
        from adafruit_onewire.bus import OneWireBus
        from adafruit_ds18x20 import DS18X20

        onewire_bus = OneWireBus(cast(int, self.config["pin"]))
        self.ds18 = DS18X20(onewire_bus, onewire_bus.scan()[0])  # Assume is only device
        # self.ds18 = DS18X20(self.onewire_bus)

    def get_value(self, sens_conf: ConfigType) -> float:
        return cast(float, self.ds18.temperature)

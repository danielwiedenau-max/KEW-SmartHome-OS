"""Status sensor for KEW Smart Home OS."""

from __future__ import annotations

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the KEW status sensor."""
    async_add_entities([KEWStatusSensor(hass, entry)])


class KEWStatusSensor(SensorEntity):
    """Represent the KEW Smart Home OS installation status."""

    _attr_has_entity_name = True
    _attr_name = "Status"
    _attr_icon = "mdi:home-assistant"

    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None:
        self.hass = hass
        self.entry = entry
        self._attr_unique_id = f"{entry.entry_id}_status"
        self._attr_device_info = {
            "identifiers": {(DOMAIN, entry.entry_id)},
            "name": "KEW Smart Home OS",
            "manufacturer": "KEW Smart Home",
            "model": "OS",
            "sw_version": "1.0.0",
        }

    @property
    def native_value(self) -> str:
        """Return installation state."""
        return "ready"

    @property
    def extra_state_attributes(self) -> dict[str, object]:
        """Return details about installed files."""
        files = self.hass.data.get(DOMAIN, {}).get(self.entry.entry_id, {}).get("installed_files", [])
        return {
            "installed_files": len(files),
            "dashboard_path": "dashboards/kew_smart_home_os/kew-dashboard.yaml",
            "theme": "KEW Premium",
        }

"""Status sensor for KEW Smart Home OS."""

from __future__ import annotations

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import EntityCategory
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType, DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback

from .const import DOMAIN


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    """Set up the KEW Smart Home OS status sensor."""

    async_add_entities(
        [
            KEWStatusSensor(hass, entry),
        ]
    )


class KEWStatusSensor(SensorEntity):
    """Represent the KEW Smart Home OS installation status."""

    _attr_has_entity_name = True
    _attr_name = "Status"
    _attr_icon = "mdi:home-assistant"
    _attr_entity_category = EntityCategory.DIAGNOSTIC

    def __init__(
        self,
        hass: HomeAssistant,
        entry: ConfigEntry,
    ) -> None:
        """Initialize the KEW status sensor."""

        self.hass = hass
        self.entry = entry

        self._attr_unique_id = f"{entry.entry_id}_status"

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, entry.entry_id)},
            name="KEW Smart Home OS",
            manufacturer="KEW Smart Home",
            model="Smart Home OS",
            sw_version="1.0.0",
            entry_type=DeviceEntryType.SERVICE,
            configuration_url=(
                "https://github.com/"
                "danielwiedenau-max/KEW-SmartHome-OS"
            ),
        )

    @property
    def native_value(self) -> str:
        """Return the installation state."""

        return "ready"

    @property
    def extra_state_attributes(self) -> dict[str, str | int]:
        """Return details about the installed KEW files."""

        files = (
            self.hass.data
            .get(DOMAIN, {})
            .get(self.entry.entry_id, {})
            .get("installed_files", [])
        )

        return {
            "installed_files": len(files),
            "dashboard_path": "dashboards/kew_smart_home_os",
            "theme": "KEW Premium",
            "version": "1.0.0",
        }

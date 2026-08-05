"""KEW Smart Home OS integration."""

from __future__ import annotations

from pathlib import Path
import shutil

import voluptuous as vol

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, ServiceCall
from homeassistant.helpers import config_validation as cv

from .const import CONF_OVERWRITE, DEFAULT_OVERWRITE, DOMAIN, SERVICE_INSTALL, SERVICE_REFRESH

PLATFORMS: list[str] = ["sensor"]


def _copy_tree(source: Path, target: Path, overwrite: bool) -> list[str]:
    """Copy bundled resources into the Home Assistant config directory."""
    copied: list[str] = []
    if not source.exists():
        return copied

    for item in source.rglob("*"):
        if item.is_dir():
            continue
        relative = item.relative_to(source)
        destination = target / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        if destination.exists() and not overwrite:
            continue
        shutil.copy2(item, destination)
        copied.append(str(destination))
    return copied


def install_assets(hass: HomeAssistant, overwrite: bool = False) -> list[str]:
    """Install bundled KEW assets."""
    integration_dir = Path(__file__).parent
    resources = integration_dir / "resources"
    config_dir = Path(hass.config.config_dir)

    mappings = {
        resources / "themes": config_dir / "themes" / "kew_smart_home_os",
        resources / "dashboards": config_dir / "dashboards" / "kew_smart_home_os",
        resources / "packages": config_dir / "packages" / "kew_smart_home_os",
        resources / "www": config_dir / "www" / "kew_smart_home_os",
    }

    copied: list[str] = []
    for source, target in mappings.items():
        copied.extend(_copy_tree(source, target, overwrite))
    return copied


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up KEW Smart Home OS from a config entry."""
    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = {
        "installed_files": await hass.async_add_executor_job(install_assets, hass, False)
    }

    async def handle_install(call: ServiceCall) -> None:
        overwrite = call.data.get(CONF_OVERWRITE, DEFAULT_OVERWRITE)
        files = await hass.async_add_executor_job(install_assets, hass, overwrite)
        hass.data[DOMAIN][entry.entry_id]["installed_files"] = files

    hass.services.async_register(
        DOMAIN,
        SERVICE_INSTALL,
        handle_install,
        schema=vol.Schema({vol.Optional(CONF_OVERWRITE, default=False): cv.boolean}),
    )
    hass.services.async_register(
        DOMAIN,
        SERVICE_REFRESH,
        handle_install,
        schema=vol.Schema({vol.Optional(CONF_OVERWRITE, default=True): cv.boolean}),
    )

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    unloaded = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unloaded:
        hass.data.get(DOMAIN, {}).pop(entry.entry_id, None)
        if not hass.data.get(DOMAIN):
            hass.services.async_remove(DOMAIN, SERVICE_INSTALL)
            hass.services.async_remove(DOMAIN, SERVICE_REFRESH)
    return unloaded

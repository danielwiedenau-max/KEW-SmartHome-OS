"""KEW Smart Home OS integration."""

from __future__ import annotations

from pathlib import Path
import shutil

import voluptuous as vol

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, ServiceCall
from homeassistant.helpers import config_validation as cv

from .const import (
    CONF_OVERWRITE,
    DEFAULT_OVERWRITE,
    DOMAIN,
    PLATFORMS,
    SERVICE_INSTALL,
    SERVICE_REFRESH,
)


def _copy_tree(source: Path, target: Path, overwrite: bool) -> list[str]:
    """Copy bundled files."""
    copied: list[str] = []

    if not source.exists():
        return copied

    for item in source.rglob("*"):
        if item.is_dir():
            continue

        destination = target / item.relative_to(source)
        destination.parent.mkdir(parents=True, exist_ok=True)

        if destination.exists() and not overwrite:
            continue

        shutil.copy2(item, destination)
        copied.append(str(destination))

    return copied


def _install_assets(config_dir: str, overwrite: bool) -> list[str]:
    """Install bundled KEW assets."""
    resources = Path(__file__).parent / "resources"
    config_path = Path(config_dir)

    mappings = {
        resources / "themes": config_path / "themes",
        resources / "dashboards": config_path / "dashboards",
        resources / "packages": config_path / "packages",
        resources / "www": config_path / "www" / "kew",
    }

    copied: list[str] = []
    for source, target in mappings.items():
        copied.extend(_copy_tree(source, target, overwrite))

    return copied


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
) -> bool:
    """Set up KEW Smart Home OS."""
    installed_files = await hass.async_add_executor_job(
        _install_assets,
        hass.config.config_dir,
        DEFAULT_OVERWRITE,
    )

    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = {
        "installed_files": installed_files,
    }

    async def handle_install(call: ServiceCall) -> None:
        overwrite = call.data.get(CONF_OVERWRITE, DEFAULT_OVERWRITE)
        files = await hass.async_add_executor_job(
            _install_assets,
            hass.config.config_dir,
            overwrite,
        )
        hass.data[DOMAIN][entry.entry_id]["installed_files"] = files

    schema = vol.Schema(
        {
            vol.Optional(
                CONF_OVERWRITE,
                default=DEFAULT_OVERWRITE,
            ): cv.boolean
        }
    )

    if not hass.services.has_service(DOMAIN, SERVICE_INSTALL):
        hass.services.async_register(
            DOMAIN,
            SERVICE_INSTALL,
            handle_install,
            schema=schema,
        )

    if not hass.services.has_service(DOMAIN, SERVICE_REFRESH):
        hass.services.async_register(
            DOMAIN,
            SERVICE_REFRESH,
            handle_install,
            schema=schema,
        )

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
) -> bool:
    """Unload KEW Smart Home OS."""
    unloaded = await hass.config_entries.async_unload_platforms(
        entry,
        PLATFORMS,
    )

    if unloaded:
        hass.data.get(DOMAIN, {}).pop(entry.entry_id, None)

        if not hass.data.get(DOMAIN):
            hass.services.async_remove(DOMAIN, SERVICE_INSTALL)
            hass.services.async_remove(DOMAIN, SERVICE_REFRESH)
            hass.data.pop(DOMAIN, None)

    return unloaded

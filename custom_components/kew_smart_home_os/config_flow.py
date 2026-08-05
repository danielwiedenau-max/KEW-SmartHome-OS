"""Config flow for KEW Smart Home OS."""

from __future__ import annotations

from homeassistant import config_entries

from .const import DOMAIN


class KEWSmartHomeOSConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for KEW Smart Home OS."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        await self.async_set_unique_id(DOMAIN)
        self._abort_if_unique_id_configured()
        if user_input is not None:
            return self.async_create_entry(title="KEW Smart Home OS", data={})
        return self.async_show_form(step_id="user")

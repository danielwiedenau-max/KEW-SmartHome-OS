"""Config flow for KEW Smart Home OS."""

from __future__ import annotations

from typing import Any

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.data_entry_flow import FlowResult

from .const import DOMAIN


class KEWSmartHomeOSConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle the KEW Smart Home OS config flow."""

    VERSION = 1

    async def async_step_user(
        self,
        user_input: dict[str, Any] | None = None,
    ) -> FlowResult:
        """Handle setup initiated by the user."""

        if user_input is not None:
            return self.async_create_entry(
                title="KEW Smart Home OS",
                data={},
            )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({}),
        )
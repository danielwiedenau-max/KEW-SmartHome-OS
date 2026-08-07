"""Constants for KEW Smart Home OS."""

DOMAIN = "kew_smart_home_os"
NAME = "KEW Smart Home OS"
VERSION = "2.0.0-alpha.1"

PLATFORMS: list[str] = ["sensor"]

SERVICE_INSTALL = "install_assets"
SERVICE_REFRESH = "refresh_assets"

CONF_OVERWRITE = "overwrite_existing"
DEFAULT_OVERWRITE = False

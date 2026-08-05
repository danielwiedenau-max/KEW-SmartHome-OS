# KEW Smart Home OS

Ein HACS-installierbares Premium-Paket für Home Assistant im dunkelblau-goldenen KEW Corporate Design.

## Enthalten

- KEW Premium Theme mit Hell-/Dunkelmodus
- Smartphone-, Tablet- und Desktop-optimierte Sections-Dashboard-Vorlage
- Seiten für Home, SENEC/PV, Shelly/Tuya, Eufy, Wärmepumpe, Pool, FRITZ!Box, Statistik und Kalender
- Optionale Helfer für Haus-, Nacht-, Gäste- und Poolmodus
- KEW Hintergrundgrafik und eigenes Integration-Branding
- Dienste zum erneuten Installieren bzw. Aktualisieren der Dateien
- Statussensor `sensor.kew_smart_home_os_status`

## Voraussetzungen

- Home Assistant 2026.3 oder neuer
- HACS 2.0 oder neuer
- Öffentlicher Zugriff auf dieses GitHub-Repository

## Installation über HACS

1. Öffne **HACS** in Home Assistant.
2. Öffne oben rechts das Drei-Punkte-Menü.
3. Wähle **Benutzerdefinierte Repositories**.
4. Trage ein: `https://github.com/danielwiedenau-max/KEW-SmartHome-OS`
5. Kategorie: **Integration**.
6. Lade **KEW Smart Home OS** herunter.
7. Starte Home Assistant neu.
8. Öffne **Einstellungen → Geräte & Dienste → Integration hinzufügen**.
9. Suche nach **KEW Smart Home OS** und bestätige die Installation.
10. Starte Home Assistant erneut.

## Home Assistant konfigurieren

Ergänze deine `configuration.yaml`:

```yaml
frontend:
  themes: !include_dir_merge_named themes

homeassistant:
  packages: !include_dir_named packages

lovelace:
  mode: storage
  dashboards:
    kew-smart-home:
      mode: yaml
      title: KEW Smart Home OS
      icon: mdi:home-assistant
      show_in_sidebar: true
      filename: dashboards/kew_smart_home_os/kew-dashboard.yaml
```

Danach Home Assistant neu starten und unter deinem Benutzerprofil das Theme **KEW Premium** auswählen.

> Die Beispiel-Entitäten im Dashboard müssen an deine echten Entitäts-IDs angepasst werden. Eine Übersicht findest du in `docs/ENTITIES.md`.

## Aktualisieren der mitgelieferten Dateien

Unter **Entwicklerwerkzeuge → Aktionen**:

```yaml
action: kew_smart_home_os.refresh_assets
data:
  overwrite_existing: true
```

Achtung: Dadurch werden lokal angepasste KEW-Dateien überschrieben.

## Verzeichnisse nach der Einrichtung

```text
/config/themes/kew_smart_home_os/
/config/dashboards/kew_smart_home_os/
/config/packages/kew_smart_home_os/
/config/www/kew_smart_home_os/
```

## Entwicklung

Die Integration befindet sich unter:

```text
custom_components/kew_smart_home_os/
```

Für eine veröffentlichte HACS-Version muss auf GitHub ein Release/Tag erstellt werden, zum Beispiel `v1.0.0`.

## Support

Fehler und Wünsche bitte über die GitHub-Issues dieses Repositories melden.

## Lizenz

MIT License

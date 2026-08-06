# KEW Smart Home OS

Home-Assistant-Integration mit KEW Premium Theme, Dashboard-Vorlage,
Helfern und Installationsservices.

## Version

`2.0.0-alpha.1`

## Installation über HACS

1. HACS öffnen.
2. Benutzerdefinierte Repositories öffnen.
3. Repository hinzufügen:
   `https://github.com/danielwiedenau-max/KEW-SmartHome-OS`
4. Typ **Integration** auswählen.
5. Integration installieren.
6. Home Assistant neu starten.
7. Unter **Einstellungen → Geräte & Dienste → Integration hinzufügen**
   nach **KEW Smart Home OS** suchen.

## Enthalten

- Einrichtungsassistent
- Diagnosesensor
- KEW Premium Theme
- Dashboard-Vorlage
- Nacht- und Urlaubsmodus-Helfer
- Pool-Solltemperatur
- Services zum Installieren und Aktualisieren der Ressourcen
- HACS- und Hassfest-Validierung

## configuration.yaml

```yaml
frontend:
  themes: !include_dir_merge_named themes

homeassistant:
  packages: !include_dir_named packages
```

## Services

```text
kew_smart_home_os.install_assets
kew_smart_home_os.refresh_assets
```

Mit `overwrite_existing: true` werden bestehende KEW-Dateien überschrieben.

## Hinweis

Die Entity-IDs im Dashboard sind Beispiele und müssen später an die
tatsächlichen Geräte in der Home-Assistant-Installation angepasst werden.

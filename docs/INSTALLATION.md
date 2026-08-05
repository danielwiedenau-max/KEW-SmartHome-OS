# Ausführliche Installation

## 1. Repository zu HACS hinzufügen

In HACS unter **Benutzerdefinierte Repositories** die Repository-URL eintragen und als Kategorie **Integration** auswählen.

## 2. Integration laden

Nach dem Download Home Assistant vollständig neu starten. Anschließend unter **Einstellungen → Geräte & Dienste** nach `KEW Smart Home OS` suchen und hinzufügen.

Beim ersten Einrichten kopiert die Integration ihre Ressourcen in die passenden Verzeichnisse innerhalb von `/config`.

## 3. YAML-Einträge ergänzen

Öffne `configuration.yaml` mit File Editor oder Studio Code Server und ergänze die Blöcke aus der README. Bereits vorhandene Schlüssel wie `frontend:`, `homeassistant:` oder `lovelace:` dürfen nicht doppelt angelegt werden. Inhalte müssen zusammengeführt werden.

## 4. Dashboard anpassen

Die mitgelieferte Vorlage enthält bewusst typische Beispiel-Entitäten. Ersetze diese in:

`/config/dashboards/kew_smart_home_os/kew-dashboard.yaml`

## 5. Theme aktivieren

Im Benutzerprofil das Theme `KEW Premium` wählen. Für alle Benutzer kann es zusätzlich über die Aktion `frontend.set_theme` gesetzt werden.

## Fehlerbehebung

- Integration nicht sichtbar: Home Assistant nach dem HACS-Download neu starten.
- Theme nicht sichtbar: YAML-Konfiguration prüfen und `frontend.reload_themes` ausführen.
- Dashboard leer oder fehlerhaft: Nicht vorhandene Beispiel-Entitäten ersetzen.
- Dateien fehlen: Aktion `kew_smart_home_os.install_assets` ausführen.

from datetime import datetime
from data.konstanten import BESCHREIBUNGEN
from zoneinfo import ZoneInfo

from datetime import datetime
from zoneinfo import ZoneInfo


def prompt_generieren(zustand, energie, ziel, kommentar="", leben=None):
    jetzt = datetime.now(ZoneInfo("Europe/Berlin"))
    uhrzeit = jetzt.strftime("%H:%M")

    leben_str = ""
    if leben:
        bewertungen = ", ".join(f"{area}: {score}" for area, score in leben.items())
        leben_str = f" Mein aktuelles Wheel of Life ist wie folgt bewertet: {bewertungen}."

    prompt = f"""
    Ich fühle mich körperlich {BESCHREIBUNGEN['Körper'][zustand['Körper']]},
    emotional {BESCHREIBUNGEN['Emotion'][zustand['Emotion']]} und
    {BESCHREIBUNGEN['Bedürfnis'][zustand['Bedürfnis']]}.
    Geistig: {BESCHREIBUNGEN['Geist'][zustand['Geist']]}.
    Mein Energielevel ist: {energie}%.
    Mein Ziel ist aktuell: {ziel}.
    {kommentar}{leben_str}
    Es ist {uhrzeit} Uhr.

    Bitte gib mir eine konkrete Empfehlung, welche Handlung oder Aufgabe ich jetzt am sinnvollsten angehen sollte, unter Berücksichtigung meines Zustands, meiner Energie und meiner aktuellen Lebensbereiche.
    """

    return prompt



# Ideen: 
# - vorher klarheit über ziele schaffen
# - mehrere aktivitäten erfragen und jeweils impact und aufwand berechnen und auswählen
# - feedbackschleife einbauen, daten speichern und mit analysieren
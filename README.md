# Zustand → Hebel

Ein minimalistisches Streamlit-Tool zur kontextbasierten Entscheidungsunterstützung.

Statt auf Motivation oder Disziplin zu setzen, erfasst die App deinen aktuellen Zustand
(Energie, Fokus, Bedürfnisse, Lebensbalance) und generiert daraus einen passenden nächsten Schritt.

Ziel: weniger Grübeln. Schnellere Klarheit. Mehr Handlung.

---

## Grundidee

Viele Aufgaben scheitern nicht an Faulheit, sondern an schlechter Passung:

- wenig Energie + große Aufgabe → Frust  
- hoher Fokus + kleine Aufgabe → Unterforderung  

Dieses Tool dreht die Logik um:

Zustand → Kontext → sinnvoller nächster Hebel

Nicht: „Was sollte ich tun?“  
Sondern: „Was passt jetzt gerade?“

---

## Funktionen

### Hebel-Tab
- kurzer Zustands-Check-in (z.B. mental, körperlich, Bedürfnis)
- Energie-Slider
- Ziel/Intention auswählen
- optionaler Freitext
- automatische Prompt-Generierung
- direkt kopierbare Handlungsempfehlung

### Wheel of Life
- Bewertung wichtiger Lebensbereiche (1–10)
- Speicherung der Werte in Google Sheets
- monatliche Erinnerung zur Aktualisierung
- Einbezug der Lebensbalance in die Empfehlung

---

## Tech Stack

- Python
- Streamlit (UI)
- Google Sheets API (Persistenz)
- modulare Struktur (data / prompt / sheet)

---

## Installation

```bash
pip install -r requirements.txt
# -----------------------
# CONFIG / KONSTANTEN
# -----------------------
ZUSTAND_KATEGORIEN = {
    "Körper": [
        "Muskelermüdet", "Leicht ermüdet / Ruhezustand", "Erschöpft (stressbedingt)",
        "Angespannt / verspannt", "Locker / wohl in Bewegung"
    ],
    "Emotion": [
        "Positiv‑ruhig", "Positiv‑aktiv", "Neutral",
        "Negativ‑ruhig", "Negativ‑aktiv"
    ],
    "Geist": [
        "Fokussiert",       # klar, kann Aufgaben erledigen
        "Leicht abgelenkt", # teilweise unruhig, Gedanken schweifen
        "Sehr abgelenkt",   # schwer zu konzentrieren, viele Gedanken
        "Flow",             # tief involviert, hoher Fokus
        "Gedanklich schwer" # Kopf fühlt sich dicht oder träge an
    ],
    "Bedürfnis": [
        "Unklar",
        "Sicherheit", "Zugehörigkeit",
        "Autonomie / Selbstbestimmung",
        "Sinn / Bedeutung", "Wachstum / Lernen",
        "Wertschätzung / Würde", "Lebendigkeit / Freude",
        "Nähe / Verbindung", "Ruhe / Regeneration",
        "Ausdruck / Ehrlichkeit"
    ]
}

BESCHREIBUNGEN = {
    "Körper": {
        "Muskelermüdet": "muskelermüdet nach körperlicher Belastung",
        "Leicht ermüdet / Ruhezustand": "leicht ermüdet, normaler Tagesverlauf",
        "Erschöpft (stressbedingt)": "körperlich erschöpft durch Stress oder Schlafmangel",
        "Angespannt / verspannt": "verspannt und angespannt, Stress im Körper spürbar",
        "Locker / wohl in Bewegung": "locker, wohl in Bewegung, energiegeladen"
    },
    "Emotion": {
        "Positiv‑ruhig": "ruhige und positive Stimmung",
        "Positiv‑aktiv": "energiegeladen und motiviert",
        "Neutral": "neutral, weder positiv noch negativ gefärbt",
        "Negativ‑ruhig": "niedergeschlagen oder traurig, ruhig",
        "Negativ‑aktiv": "gereizt, unruhig oder frustriert"
    },
    "Geist": {
        "Fokussiert": "klarer Kopf, gut konzentriert, kann Aufgaben erledigen",
        "Leicht abgelenkt": "einigermaßen konzentriert, Gedanken schweifen ab und zu",
        "Sehr abgelenkt": "schwer zu fokussieren, viele störende Gedanken",
        "Flow": "tief involviert, hoher Fokus, produktiv",
        "Gedanklich schwer": "Kopf fühlt sich dicht, träge oder blockiert an"
    },
    "Bedürfnis": {
        "Unklar": "",
        "Sicherheit": "Ich will mich geschützt, stabil und innerlich ruhig fühlen – ohne Angst oder Alarm im System.",
        "Zugehörigkeit": "Ich will mich angenommen fühlen und wissen, dass ich dazugehöre, so wie ich bin.",
        "Autonomie / Selbstbestimmung": "Ich will mein Leben selbst steuern und meine eigenen Entscheidungen treffen können.",
        "Sinn / Bedeutung": "Ich will spüren, dass das, was ich tue, Bedeutung hat und für etwas Größeres steht.",
        "Wachstum / Lernen": "Ich will lernen, mich entwickeln und weiter werden als gestern.",
        "Wertschätzung / Würde": "Ich will respektiert und ernst genommen werden – nicht übersehen oder klein gemacht.",
        "Lebendigkeit  / Freude": "Ich will mich lebendig fühlen – mit Freude, Energie und innerem Leuchten.",
        "Nähe / Verbindung": "Ich will echte Verbindung spüren, mich öffnen dürfen und jemandem nah sein.",
        "Ruhe / Regeneration": "Ich will zur Ruhe kommen, regenerieren und nicht ständig funktionieren müssen.",
        "Ausdruck / Ehrlichkeit": "Ich will sagen dürfen, was wirklich in mir ist – ehrlich und ohne Maske."
    }

}
TITEL = [
    "Was heute möglich ist, hängt nicht von Disziplin ab.",
    "Du musst dich nicht motivieren. Du musst nur passend starten.",
    "Produktivität beginnt mit Wahrnehmung.",
    "Nicht kämpfen. Justieren.",
]

ZIELE = ["Arbeiten", "Erholen", "Lernen", "Unklar"]


WHEEL_AREAS = [
    "Körper & Gesundheit",
    "Mentale Klarheit & Fokus",
    "Beruf & Lernen",
    "Finanzen & Freiheit",
    "Soziales & Beziehungen",
    "Selbstwirksamkeit & Projekte",
    "Freizeit & Spaß",
    "Sinn & Werte"
]

for area in WHEEL_AREAS:
    print(area)
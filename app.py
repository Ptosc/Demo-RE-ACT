import streamlit as st
from time import sleep
from datetime import datetime
from data.konstanten import ZUSTAND_KATEGORIEN, ZIELE, WHEEL_AREAS
from data.sheet import get_worksheet
from prompt.promt import prompt_generieren

st.set_page_config(
    page_title="Zustand → Hebel",
    layout="centered"
)

def init_score_state(latest_row):
    if latest_row and len(latest_row) > 1:
        latest_values = latest_row[1:]

        for i, key in enumerate(WHEEL_AREAS):
            if key not in st.session_state:
                try:
                    st.session_state[key] = int(latest_values[i])
                except (IndexError, ValueError):
                    st.session_state[key] = 3
    else:
        for key in WHEEL_AREAS:
            st.session_state.setdefault(key, 3)

def need_update(values):
    """
    Prüft ob Update nötig ist
    Wenn das letzte Uptate > 1 Monat her ist -> True
    Sonst -> False
    """
    if not values:
        return True
    time_str = values[-1][0]
    latest_update_time = datetime.strptime(time_str, "%d.%m.%Y %H:%M:%S")
    return latest_update_time.month != datetime.now().month

def prep_sheet():
    # ------- sheet vorbereiten -------
    sheet = get_worksheet()
    data = sheet.get_all_values()
    # verhindert IndexError, wenn liste leer ist
    if data: 
        headers = data[0]
        values = data[1:]
    else:
        headers, values = [], []

    return headers, values
        
tab1, tab2 = st.tabs(['Hebel', 'Wheel of life'])

with tab1:
    st.title("Zustand → Hebel")
    st.caption("Kurz einchecken. Klar entscheiden. Handeln.")

    headers, values = prep_sheet()

    if need_update(values):
        st.warning(f'Aktualisiere dein Wheel of Life um bessere Empfehlungen zu erhalten.')

    st.markdown('---')

    # 🧠 ZUSTAND
    with st.container():
        st.subheader("🧠 Dein aktueller Zustand")
        st.caption("Nicht analysieren. Nur ehrlich auswählen.")

        zustand = {}
        for kategorie, options in ZUSTAND_KATEGORIEN.items():
            zustand[kategorie] = st.selectbox(
                kategorie,
                options,
                index=0
            )


    # ⚡ FOKUS
    st.markdown('---')
    st.subheader("⚡ Fokus")

    col1, col2 = st.columns([4,1])

    with col1:
        energie = st.slider(
            "Energie",
            min_value=0,
            max_value=100,
            value=50,
            step=5
        )

    with col2:
        ziel = st.radio(
            "Intention",
            ZIELE
        )


    # 💬 FREIER GEDANKE
    kommentar = st.text_input(
        "Freier Gedanke (optional)",
        placeholder="z.B. müde, aber will trotzdem etwas Sinnvolles tun"
    )

    # an/aus schalter Wheel of life
    col1, col2, col3 = st.columns([2, 1, 2])
    with col2:
        on = st.toggle('Wheel of Life')

    if not on:
        leben = ""
    else:
        leben = {area: st.session_state[area] for area in WHEEL_AREAS}

    # 🚀 Button Gen. Promt
    st.markdown('---')
    generate = st.button(
        "**✨ Klarheit**",
        use_container_width=True
    )

    # ✨ OUTPUT
    if generate:
        prompt_text = prompt_generieren(
            zustand,
            energie,
            ziel,
            kommentar,
            leben
        )

        st.markdown('---')
        st.subheader("✅ Fertig")
        st.caption("Kopieren. Einfügen. Umsetzen. Nicht zerdenken.")

        st.text_area(
            label="",
            value=prompt_text,
            height=230
        )

        if st.button('Beenden'):
            st.stop()

with tab2:
    st.title("🧭 Wheel of Life")
    st.caption("Bewerte deine Lebensbereiche von 1 (schwach) bis 10 (stark)")

    # Letzte Zeile prüfen, ggf. None übergeben
    latest_row = values[-1] if values else None
    init_score_state(latest_row)

    # UI: Slider für jeden Bereich
    for area in WHEEL_AREAS:
        st.slider(
            label=area,
            min_value=1,
            max_value=10,
            value=st.session_state[area],
            key=area
        )

    # Update button
    if st.button('Neue Werte speichern', use_container_width=True):
        sheet = get_worksheet()
        # Header einmalig erstellen, falls Sheet leer
        if not sheet.get_all_values():
            sheet.append_row(['Zeitstempel'] + WHEEL_AREAS)

        # Neue Werte aus Session State hinzufügen
        sheet.append_row([datetime.now().strftime('%d.%m.%Y %H:%M:%S')] +
                         [st.session_state[area] for area in WHEEL_AREAS])

        st.success('Perfekt, deine Werte sind auf dem neusten Stand!')
        sleep(2)

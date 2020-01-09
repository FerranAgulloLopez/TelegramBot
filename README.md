# Llenguatge i bot de telegram per fer enquestes

_Aquest projecte forma part de l'assignatura de LP a la Facultat d'Informàtica de Catalunya._

## Introducció

Aquest component implementa un llenguatge per escriure enquestes i un bot telegram per realitzar-las interactivament, guardar els seus resultats i visualitzar-los de forma gràfica.

## Descripció tècnica

Els dos mòduls anteriors són totalment independents. No obstant això, es comuniquen a través dels fitxers en el directori de dades. D'aquesta manera el graf resultant de parsejar una enquesta es guarda de forma persistent i és automàticament accessible des del bot de telegram.

El nom del bot de Telegram és: t.me/FerranAgulloLPBot

### Distribució de fitxers

- cl: directori amb els fitxers relacionats amb la part de llenguatge
- bot: directori amb els fitxers relacionats amb la part del bot de telegram
- data: directori que s'utilitza per guardar les dades de forma persistent: els grafs de les enquestes i els seus resultats. També s'utilitza per guardar de forma temporal els gràfics que mostra el bot de telegram.
- requirements.txt: fitxer que indica totes les llibreries necessàries

### Com instal·lar-lo

Per configurar el component en Linux:

- Install python3, python3-venv and pip3: sudo apt-get install python3 python3-venv pip3
- Install virtualenv: python3 -m pip install --user virtualenv
- Generate a virtual environment: python3 -m venv env
- Activate the virtual environment: source env/bin/activate
- Install component dependencies with the requirements file: pip3 install -r requirements.txt

Per configurar el component en Windows

- Install python3 and pip3
- Install virtualenv: python3 -m pip install --user virtualenv
- Generate a virtual environment: python3 -m venv env
- Activate the virtual environment: source env/bin/activate
- Install component dependencies with the requirements file: pip3 install -r requirements.txt

### Com utilitzar-lo

- Generar enquesta: S'ha d'introduir el fitxer d'entrada amb el text al directori cl/input/. Després cal executar el programa cl/testEnquestes.py amb el nom del fitxer com a paràmetre:
    - `python3 cl/testEnquestes.py E.txt`

- Executar bot de telegram: S'ha d'executar el programa bot/bot.py:
    - `python3 bot/bot.py`

## License

Free use of this software is granted under the terms of the Apache License 2.0

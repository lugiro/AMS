## AMS
### Lesing av AMS-data fra HAN-plugg<br>
Løsningen her er beregnet for KAIFA 1-fase-måler, type MA105H2E<br>

Filen **AMS-tilkobling-HAN.jpg** viser tilkobling fra HAN-plugg via MBUS-TTL-converter til Raspberry Pi 3B pluss.<br>
Filen **amsGetMeterData_Vx.py** inneholder Python-program som leser telegram fra AMS-måler.<br>

Programmet lagrer data på følgende filer:<br>
ams_activ_power_pos_2sec.dat<br>
ams_meter_value_10sec.dat<br>
ams_meter_value_10sec.log<br>
ams_meter_energy_1hour.dat<br>
ams_meter_energy_1hour.log<br>

.dat filer inneholder kun "nåverdi".<br>

Data fra disse filen kan benyttes videre til visning på web etc.<br>
Filen **AMSMeterData.png** viser hvilke data som er tatt ut fra AMS-måler.<br>

Filen **AMS_telegram_Vx.pdf** viser telgramdata på hex-format for 3 telegram, 2 sek, 10 sek og 1 time.<br>

For å lese data fra GPIO15 (RXD) pinne 10 på Rasbberry må denne settes opp på riktig måte. <br>
Se https://github.com/HWal/RPi_HAN_Receive_Web_Relay_Output for mer info.<br>

Programmet **amsGetMeterData.py** utfører ikke noen form for datasjekk.<br>
Målerdata hentes direkte fra hvor de er plassert i byte-rekkefølgen.<br>
Programmet må tilpasses for å benyttes for andre typer KAIFA-målere og eventuelt andre fabrikat.<br>
Programmet har også en begrensning på 255 bytes for telegramlengde.<br>

Youtube video:<br>
https://youtu.be/juPgcLEIaek<br>
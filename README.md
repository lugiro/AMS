## AMS
### Lesing av AMS-data fra HAN-plugg<br>
Løsningen her er beregnet for for KAIFA 1-fase-måler, type MA105H2E<br>

Filen **AMS-tilkobling-HAN.jpg** viser tilkobling fra HAN-plugg via MBUS-TTL converter til Raspberry Pi 3B pluss.<br>
Filen **amsGetMeterData.py** inneholder Python-program som leser telegram fra AMS-måler.<br>

Programmet lagrer data på følgende filer:<br>
ams_activ_power_pos_2sec.dat<br>
ams_meter_value_10sec.dat<br>
ams_meter_value_10sec.log<br>
ams_meter_energy_1hour.dat<br>
ams_meter_energy_1hour.log<br>

Data fra disse filen kan benyttes videre til visning på web etc.<br>
Filen **AMSMeterData.png** viser hvilke data som er tatt ut fra AMS-måler.<br>

Filen **Telegram_2sekund.txt** viser telgramdata på hex-format for aktiv effekt oversendt hvert 2. sekund.<br>

For å lese data fra GPIO15 (RXD) pinne 10 på Rasbberry må denne settes opp på riktig måte. <br>
Se https://github.com/HWal/RPi_HAN_Receive_Web_Relay_Output for mer info.

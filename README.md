L'anode (patte longue) de la LED doit être branchée sur le GPIO au niveau du pin BCM18. Attention toutefois de mettre une résistance de ballaste (R) entre la source de tension (V_S de 3.3V au pin BCM18) et la LED pour compenser la chute de tension (V_f).

Pour une LED verte de chute de tension V_f = 1.6V qui se déclenche avec un courant I_f = 8mA, on prendra une résistance R = (3.3V - 1.6V) / 0.008A = 212.5 Ohms [ U = RI ].

```
docker build -t unisis-rpi-gpio-blink .
docker run -it --rm --privileged unisis-rpi-gpio-blink 
```

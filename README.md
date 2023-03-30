# MessageBroker
Dieses Projekt ist eine Simulation zwischen **einem Producer**, **zwei Consumern** und **einem Zwischenserver**, der die Nachrichten verwaltet 
und in die richtige Queue sendet.

## Wie man das Projekt persönlich anwenden kann 
Das Projekt ist funktioniert **natürlich** erst dann, wenn man ***Kafka*** heruntergeladen und eingerichtet hat. Ebenfalls sollten die ***3 Topics***: **hw**, **sw** 
und **zs** manuell eingerichtet sein.

*Wenn das gemacht ist, müssen einige Befehle ausgeführt werden*

Als Beispiel, wie es an Yusuf's Rechner funktioniert:
```
Unter C:\kafka :
1. .\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties
2. .\bin\windows\kafka-server-start.bat .\config\server.properties
3. .\bin\windows\kafka-console-producer.bat --topic hw --bootstrap-server localhost:9092
4. .\bin\windows\kafka-console-producer.bat --topic sw --bootstrap-server localhost:9092
5. .\bin\windows\kafka-console-producer.bat --topic zs --bootstrap-server localhost:9092
6. .\bin\windows\kafka-console-consumer.bat --topic hw --from-beginning --bootstrap-server localhost:9092
7. .\bin\windows\kafka-console-consumer.bat --topic sw --from-beginning --bootstrap-server localhost:9092
8. .\bin\windows\kafka-console-consumer.bat --topic zs --from-beginning --bootstrap-server localhost:9092

Man muss hier nicht mehr umbedingt unter C:\Kafka sein
1. C:/Users/Student/AppData/Local/Microsoft/WindowsApps/python3.11.exe c:/Users/Student/Documents/VSCode/Sprint1/consumer_hw/src/backend_func.py
2. C:/Users/Student/AppData/Local/Microsoft/WindowsApps/python3.11.exe c:/Users/Student/Documents/VSCode/Sprint1/consumer_sw/src/backend_func.py
3. C:/Users/Student/AppData/Local/Microsoft/WindowsApps/python3.11.exe c:/Users/Student/Documents/VSCode/MessageBroker/prod_cons/src/backend_func.py
```
***DAS WARS AUCH SCHON***

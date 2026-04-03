## Odabir slike
Mozemo na primer da odaberemo `amazoncorretto` iz docker-hub repozitorijuma kako bi kompajlirali nas java fajl.

## Komande
Kompajliranje - neka smo folderu `$PWD/01_intro`, onda je komanda:
```
docker run -v ${PWD}/src:/src -w /src amazoncorretto:17.0.11-alpine3.19 javac Hello.java
```
Mapiramo nas lokalni folder `${PWD}/src` na `/src` u kontejneru i `-w /src` pokrece komande odatle.

Izvrsavanje - Kada smo kreirali .class fajl, mozemo da ga pokrenemo preko:
```
docker run -v ${PWD}/src:/src -w /src amazoncorretto:17.0.11-alpine3.19 java Hello
```
Na ovaj nacin mozemo da isprobavamo razne java verzije i slike. Na prethodnom primeru je koriscena Java 17, ali samo
odaberemo drugu sliku, npr `mazoncorretto:21` i koristimo Javu 21.

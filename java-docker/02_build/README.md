# Kreiranje Java aplikacije preko Dockerfile

## Dokumentacija
https://docs.docker.com/engine/reference/builder/#from

https://docs.docker.com/engine/reference/builder/#copy

https://docs.docker.com/engine/reference/builder/#add

https://docs.docker.com/engine/reference/builder/#run

https://docs.docker.com/engine/reference/builder/#cmd

https://docs.docker.com/engine/reference/builder/#expose

https://docs.docker.com/engine/reference/builder/#user

https://docs.docker.com/engine/reference/builder/#workdir

https://docs.docker.com/engine/reference/builder/#dockerignore-file

https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#add-or-copy

https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#entrypoint

https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#volume

https://docs.docker.com/config/labels-custom-metadata/

## Primer - Dockerfile i prekompajlirana aplikacija
### Definisanje Dockerfile-a
Posto mozemo da zapakujemo aplikaciju kao .jar ili kao .web imacemo dva odgovarajuca Dockerfile-a.

Kreiramo Dockerfile za jar kao jar.Dockerfile
```dockerfile
FROM eclipse-temurin:21
RUN mkdir /app
#RUN ["executable", "param1", "param2"]
WORKDIR /app
COPY api.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
```

Za web.Dockerfile:
```dockerfile
FROM tomcat:11.0
COPY web.war ${CATALINA_HOME}/webapps/ROOT.war
EXPOSE 8080
ENTRYPOINT ["catalina.sh", "run"]
```

### Izvrsene komande
Kreiranje slike: `docker build -f jar.Dockerfile -t my-api .`

Provera da li se nalazi napravljena slika: `docker images`

Pokretanje kontejnera i mapiranje 8080 porta iz kontejnera na 9000: `docker run -p 9000:8080 -it my-api`

Listanje svih kontejnera: `docker container ls -a`

Pokretanje preko web umesto jar fajla:

`docker build -f web.Dockerfile -t my-web-app .`

`docker run -p 9001:8080 -it --rm my-web-app`

## Primer - Dockerfile i build preko Maven i Gradle
Kada imamo izvorni kod, a hocemo da ga buildujemo unutar kontejnera, mozemo da koristimo maven ili gradle za build.

### Maven primer
Primer za maven, napravimo maven. Napravili smo dva sloja u kontejneru jedan za pom i jedan za source. Ako se pom.xml promeni, maven ce da build-a sve, medjutim ako se promeni samo source, onda necemo opet da dovlacimo sve dependency. Dockerfile:
```dockerfile
FROM maven:3.9.8-eclipse-temurin-21
WORKDIR /app
COPY pom.xml .
RUN mvn dependeny:resolve

COPY src src
RUN mvn package

EXPOSE 8080
ENTRYPOINT [ "java", "-jar", "target/api.jar" ]
```
Build i pokretanje:
```bash
docker build -f maven.Dockerfile -t my-api-maven .

docker run -p 9010:8080 -it --rm my-api-maven
```

Mozemo jos vise da optimizujemo build za dependency. Ako ih imamo previse, onda nije lose da se mount-uje volume na host pa da odatle povlacimo dependecy, a ako bas neki se ne nadje tu, da se onda skida online.
```bash
docker run -it --rm \
   -v ${PWD}:/app \
   -v ${HOME}/.m2:/root/.m2 \
   -w /app \
   maven:3.9.8-eclipse-temurin-21 \
   mvn clean package
```

### Gradle primer
Gradle dockerfile (gradle.Dockerfile):
```dockerfile
FROM gradle:8.8.0-jdk21
WORKDIR /app
COPY --chown=gradle:gradle build.gradle .
COPY --chown=gradle:gradle src src
RUN chown -R gradle:gradle /app
USER gradle
RUN gradle build
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "build/libs/api.jar"]
```

Slicno kao i u prethodnom primeru:
```bash
docker build -f gradle.Dockerfile -t my-api-gradle .

docker run -p 9011:8080 -it --rm my-api-gradle
```

lokalni build:
```bash
docker run -it --rm \
   -u gradle \
   -v ${PWD}:/app \
   -v ${HOME}/.gradle:/home/gradle/.gradle \
   -w /app \
   gradle:8.8.0-jdk21 \
   gradle build
```

## Primer - Multi stage
Mozemo da kreiramo kontejner iz vise faza, odnosno da razdvojimo build fazu i fazu izvrsavanja.
Ako koristimo maven (maven.Dockerfile):
```dockerfile
FROM maven:3.9.8-eclipse-temurin-21 AS build
WORKDIR /app
COPY pom.xml .
RUN mvn dependency:resolve
COPY src src
RUN mvn package

FROM tomcat:11.0
COPY --from=build /app/target/web.war ${CATALINA_HOME}/webapps/ROOT.war
EXPOSE 8080
ENTRYPOINT ["catalina.sh", "run"]
```

Pokretanje:
```bash
docker build -f maven-multi.Dockerfile -t my-web-maven-multi .

docker images

docker run -p 9020:8080 -it --rm my-web-maven-multi
```
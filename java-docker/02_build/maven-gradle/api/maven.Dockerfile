FROM maven:3.9.8-eclipse-temurin-21
WORKDIR /app
COPY pom.xml .
RUN mvn dependeny:resolve

COPY src src
RUN mvn package

EXPOSE 8080
ENTRYPOINT [ "java", "-jar", "target/api.jar" ]
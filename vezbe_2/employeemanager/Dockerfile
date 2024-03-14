FROM openjdk:17-jdk-alpine
LABEL authors="vladimir"
ARG JAR_FILE=target/*.jar
COPY ./target/employeemanager-0.0.1-SNAPSHOT.jar app.jar
ENTRYPOINT ["java", "-jar", "/app.jar"]
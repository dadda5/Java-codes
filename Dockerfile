FROM openjdk:21
WORKDIR /app
COPY target/hello0world-1.0.jar
app.jar
CMD ["java", "-jar", "app.jar"]

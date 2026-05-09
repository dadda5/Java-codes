FROM openjdk:21
WORKDIR /app
COPY target/helloworld-1.0.jar app.jar
CMD ["java", "-jar", "app.jar"]

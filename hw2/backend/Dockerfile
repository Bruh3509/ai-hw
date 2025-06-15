# Stage 1: Build the application
FROM eclipse-temurin:17-jdk-jammy as builder
WORKDIR /app
COPY pom.xml .
# ACTION: Added these two lines to copy the Maven Wrapper scripts. This fixes the "./mvnw: not found" error.
COPY mvnw .
COPY .mvn ./.mvn
COPY src ./src
RUN ./mvnw -B package -DskipTests

# Stage 2: Create the final image
FROM eclipse-temurin:17-jre-jammy
WORKDIR /app
# Copy the executable JAR from the builder stage
COPY --from=builder /app/target/*.jar app.jar
# Expose the port the app runs on
EXPOSE 8080
# Command to run the application
ENTRYPOINT ["java", "-jar", "app.jar"]

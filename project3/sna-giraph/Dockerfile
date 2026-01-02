FROM openjdk:8-jdk

# Set working directory
WORKDIR /app

# Copy the project files
COPY . /app/

# Compile the project
RUN mkdir -p bin && \
    javac -d bin -cp "lib/*" -sourcepath src \
    src/org/apache/giraph/examples/SimpleLabelPropagationComputation.java \
    src/org/apache/giraph/io/formats/*.java \
    src/gr/aueb/sna/GiraphAppRunner.java

# Default command
CMD ["java", "-cp", "bin:lib/*", "gr.aueb.sna.GiraphAppRunner"]

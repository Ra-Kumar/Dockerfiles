# Dockerfiles Collectio

A curated collection of useful Dockerfiles for specific applications and architectures. This repository aims to provide simple, ready-to-use solutions for common containerization needs.

## Available Dockerfiles

This collection currently features:
-   **Jira on arm64 (`Jira-arm64`)**: A Dockerfile to build and run Atlassian Jira on `arm64` architecture, such as **Apple Silicon (M1/M2/M3) Macs**, where an official image is not available.
-   **Java Hello World (`Java-Hello-World`)**: A basic Dockerfile for a simple "Hello, World!" Java application.

## How to Use

To use one of the Dockerfiles:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Ra-Kumar/Dockerfiles.git
    cd Dockerfiles
    ```

2.  **Navigate to the chosen language directory:**
    ```bash
    cd <language-folder>
    # e.g., cd Java-Hello-World
    ```

3.  **Build the Docker image:**
    ```bash
    docker build -t my-app .
    ```

4.  **Run the container:**
    ```bash
    docker run --name my-app -p <host-port>:<app-port> <image-name>
    ```

## Contributing

Contributions are welcome! If you have a Dockerfile for another language or an improvement to an existing one, please feel free to submit a pull request.


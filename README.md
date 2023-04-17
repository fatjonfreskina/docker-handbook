# docker-handbook

## Commands

- `docker run <docker-image/container>`
- `docker stop <docker-container-id>`

- `docker images`: get list of images
- `docker ps -a`: get the containers that are currently running or have run in the past
- `docker exec -it <mycontainerid> bash`: get a bash in the container
- (works on Linux)`uname -a`: get info about the kernel



## Definitions

- `Container` : A container is an abstraction at the application layer that packages code and dependencies together. Instead of virtualizing the entire physical machine, containers virtualize the host operating system only.

- `Docker image`: Images are multi-layered self-contained files that act as the template for creating containers. They are like a frozen, read-only copy of a container. Images can be exchanged through registries. An image built with Docker can be used with another runtime like Podman without any additional hassle. **Containers are just images in running state.**

- `Docker Registry`: An image registry is a centralized place where you can upload your images and can also download images created by others. Docker Hub is the default public registry for Docker. You can share any number of public images on Docker Hub for free. People around the world will be able to download them and use them freely. Apart from Docker Hub or Quay, you can also create your own image registry for hosting private images.

## Docker as a Software

- **Docker Daemon**: The daemon (dockerd) is a process that keeps running in the background and waits for commands from the client. The daemon is capable of managing various Docker objects.

- **Docker client**: The client  (docker) is a command-line interface program mostly responsible for transporting commands issued by users.

- **REST API**: The REST API acts as a bridge between the daemon and the client. Any command issued using the client passes through the API to finally reach the daemon.

According to the documentation:

> "Docker uses a client-server architecture. The Docker client talks to the Docker daemon, which does the heavy lifting of building, running, and distributing your Docker containers".

<div style="text-align:center"><img src="Screenshots/Screenshot_overview.png" /></div>

1. You execute docker run hello-world command where hello-world is the name of an image.
2. Docker client reaches out to the daemon, tells it to get the hello-world image and run a container from that.
3. Docker daemon looks for the image within your local repository and realizes that it's not there, resulting in the Unable to find image 'hello-world:latest' locally that's printed on your terminal.
4. The daemon then reaches out to the default public registry which is Docker Hub and pulls in the latest copy of the hello-world image, indicated by the latest: Pulling from library/hello-world line in your terminal.
5. Docker daemon then creates a new container from the freshly pulled image.
6. Finally Docker daemon runs the container created using the hello-world image outputting the wall of text on your terminal.

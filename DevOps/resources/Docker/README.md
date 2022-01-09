# Docker :whale:

<p align="center"><img  height="150" src="https://i.ibb.co/rM23xbk/docker.jpg"></p>

Docker is a set of platform as a service products that delivers software in packages called containers. Containers are isolated from one another and bundle their own software, libraries and configuration files; they can communicate with each other through well-defined channels.

- [Official Documentation on website](https://docs.docker.com/)
- [Free Course on Youtube](https://www.youtube.com/watch?v=h0NCZbHjIpY&list=PL9ooVrP1hQOHUKuqGuiWLQoJ-LD25KxI5) :star:
- [Paid Docker Course on udemy](https://www.udemy.com/docker-tutorial-for-devops-run-docker-containers/) :heavy_dollar_sign:
- [Docker Cheat Sheet](https://gist.github.com/Nairit11/59d7ef2beca03b6a770e4c278e4b4aa9)

## Blogs

- [What is Docker?](https://dev.to/djangostars/what-is-docker-and-how-to-use-it-with-python-tutorial-87a)
- [Installation](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
- [Why Docker?](https://dev.to/abiodunjames/why-docker-creating-a-multi-container-application-with-docker--1gpb)
- [Docker Guide](https://dev.to/drminnaar/docker-guide---part-1--57c8)

## Video Tutorial
- [Free Course](https://www.youtube.com/watch?v=h0NCZbHjIpY&list=PL9ooVrP1hQOHUKuqGuiWLQoJ-LD25KxI5) :star: 
- [Free Course](https://www.youtube.com/watch?v=4G-ALqd0OZ8):star:

## Getting Started :book:

- [What is Docker](https://www.youtube.com/watch?v=lcQfQRDAMpQ)
- [Why you need to learn Docker](https://www.youtube.com/watch?v=eGz9DS-aIeY&t=796s)
- [Docker Tutorials for Beginners](https://www.youtube.com/watch?v=fqMOX6JJhGo)
- [Docker in 12 Minutes](https://www.youtube.com/watch?v=YFl2mCHdv24)

## Docker Courses :blue_book:

- [Learn from the Docker Captain](https://www.udemy.com/course/docker-mastery/)
- [Hands on Docker](https://www.udemy.com/course/hands-on-with-docker-and-docker-compose/)
- [Managing Containers](https://www.pluralsight.com/paths/managing-containers-with-docker)

## Docker Compose
Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services. Compose works in all environments: production, staging, development, testing, as well as CI workflows. With Docker Compose, you can easily deploy multiple containers with a single command.

- [Docker Compose Documentation](https://docs.docker.com/compose/)

## Repositories and people to follow :star:

- [Collabnix](https://github.com/ajeetraina/collabnix)
- [Docker Captain of India](https://github.com/ajeetraina)
- [Awesome Docker](https://github.com/veggiemonk/awesome-docker)
- [DockerLabs](https://github.com/DiptoChakrabarty/dockerlabs)

<hr>

### Learn

Name | Comments
:------ |:--------:
[Play with Docker](https://labs.play-with-docker.com) | "A simple, interactive and fun playground to learn Docker"

### Articles

Name | Comments
:------ |:--------:
[Docker CheatSheet](https://cheatsheet.dennyzhang.com/cheatsheet-docker-a4) |
[Everything you need to know about containers](https://medium.com/faun/everything-you-need-to-know-about-containers-7655badb4307) |
[A container networking overview](https://jvns.ca/blog/2016/12/22/container-networking) |
[My Docker Cheat Sheet](https://medium.com/statuscode/dockercheatsheet-9730ce03630d) |
[Docker Networking Deep Dive](http://100daysofdevops.com/21-days-of-docker-day-19-docker-networking-deep-dive/?fbclid=IwAR19KJWwhZjulbn7JNbBYLFxKFf-x0v25TSc-_bOJ6YieUND4A6UZcBSUhA) |

### Projects

Name | Comments
:------ |:--------:
[awesome-docker](https://github.com/veggiemonk/awesome-docker) | 

### Cheatsheet

* Stop and remove all containers: `docker container stop $(docker container ls -aq)`
* Check how many containers are running: `docker info`
* Check the docker images on your system: `docker images`
* Cleanup everything: `docker system prune -a -f`

#### Managing Containers

* Launch a container and attach to it: `docker container run -it ubuntu:latest /bin/bash`
* Run a command in the container: `docker exec -it <container ID/name> <commands>`
* Attaching to running container: `docker container exec -it <name> bash`
* List running containers: `docker container ls`
* List all containers (including stopped): `docker container ls -a`
* List containers (including stopped): `docker container ls -a`
* Stop a container: `docker container stop <name>`
* Remove a container: `docker container rm <name>`
* Remove all containers: `docker container rm $(docker container ls -aq) -f`
* Create, start, run command and destroy the container: `docker run --rm -it <image> <command>`

#### Images

* List images: `docker image ls`
* Pull image: `docker image pull <name>:<tag>`
* List only images tagged as "latest": `docker image ls --filter=reference="*:latest"`
* List dangling images: `docker image ls --filter dangling=true`
* Which default registry is used: `docker info`
* List supported image architectures: `docker manifest inspect golang | grep 'architecture\|os'`
* Search all repositories that contain the string 'yay': `docker search yay`
* Search only for official repositories: `docker search <name> --filter "is-official=true"`
* Build an image: `docker image build -t <name>:<tag> .`
* List images with the following data: name, tag and size: `docker image ls --format "{{.Repository}}: {{.Tag}}: {{.Size}}"`
* List images with their digests: `docker image ls --digests`
* Specify architecture when building an image: `docker buildx build --platform linux/arm/v1985 -t some_image:arm-v1985 .`
* Delete an image: `docker image rm <name or ID>:<tag>`
* Remove all images: `docker image rm $(docker image ls -q) -f`
* Tag an image: `docker tag <image name>:<tag> <repo>/<image>:<tag>`
* Push an image: `docker push <repo>/<image>:<tag>`
* Save a running container as an image: `docker commit -m "some commit message" -a "author name/username" <container ID/name> <username>/<image name>:<tag>`

#### Logs

* Print the last 100 lines from container's logs: `docker container logs --tail 100 <container name/ID>`
* Follow container logs: `docker logs -ft <container ID/name>`

#### Network

* List networks: `docker network ls`

#### Compose

* Deploy compose app: `docker-compose up`
* Stop and delete a running Compose app: `docker-compose down`
* Restart a Compose app: `docker-compose restart`
* List each container in the Compose app: `docker-compose ps`
* Stop all of the container in Compose app: `docker-compose stop`
* Delete a stopped Compose app: `docker-compose rm`

### Common Failures

#### Unable to start the Docker service

Error:

` Failed to start Docker Application Container Engine.`

Fix:

```
sudo firewall-cmd --permanent --zone=docker --change-interface=docker0
sudo firewall-cmd --reload
```

We hope you now know the roadmap to being a professional Docker Developer :v:

# Docker info

- [docker docs](https://docs.docker.com)

## Multi-container applications

**Networking**

By default, containers run in isolation. Create a network for the containers to communicate with each other. 

```bash
docker network create my-network
```

Then, run the containers with the `--network` flag.

```bash
docker run -d --network my-network --name my-container my-image
```

To test it, use `nicolaka/netshoot` which contains a lot of network tools.

```bash
docker run -it --network my-network nicolaka/netshoot
```

**Volumes**

[docs on volumes](https://docs.docker.com/storage/volumes/)*

```bash
❯ docker volume create tcn
tcn

❯ docker volume inspect tcn
[
    {
        "CreatedAt": "2024-04-26T15:51:09-04:00",
        "Driver": "local",
        "Labels": null,
        "Mountpoint": "/var/lib/docker/volumes/tcn/_data",
        "Name": "tcn",
        "Options": null,
        "Scope": "local"
    }
]

❯ docker volume rm tcn
tcn
```

## Docker Compose


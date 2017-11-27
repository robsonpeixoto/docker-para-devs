# Desenvolva usando Docker

---

# Quem somos?

- Robinho, vulgo Robson Peixoto
- Gomex, vulgo Rafael Gomes

---

# O que é Docker?

- Padroniza a entrega de software através das imagens
- Padroniza a execução de software através dos containers
- Funciona em Windows, Linux e Mac
- Permite que tudo seja facilmente versionável

---

# Hello world

```
$ docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
ca4f61b1923c: Pull complete
Digest: sha256:be0cd392e45be79ffeffa6b05338b98ebb16c87b255f48e297ec7f98e123905c
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

...
```

---

```
$ docker run -it ubuntu bash
Unable to find image 'ubuntu:latest' locally
latest: Pulling from library/ubuntu
660c48dd555d: Pull complete
4c7380416e78: Pull complete
421e436b5f80: Pull complete
e4ce6c3651b3: Pull complete
be588e74bd34: Pull complete
Digest: sha256:7c67a2206d3c04703e5c23518707bdd4916c057562dd51c74b99b2ba26af0f79
Status: Downloaded newer image for ubuntu:latest

root@da72ee310354:/# ps aux
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.1  18240  3272 pts/0    Ss   21:17   0:00 bash
root         9  0.0  0.0  34424  2920 pts/0    R+   21:20   0:00 ps aux

root@da72ee310354:/# exit
exit
```

---

# Primeira Imagem

Crie o arquivo `Dockerfile` com o conteúdo:
```Dockerfile
FROM ubuntu
CMD ["printf", "FÓRUM BAIANO DE TECNOLOGIAS ABERTAS\n"]
```

E execute o comando:
`$ docker build -t  uefs/fbta:001 .`

---

# E agora vamos criar um container

```
$ docker run  uefs/fbta:001
FÓRUM BAIANO DE TECNOLOGIAS ABERTAS
```

---

# Cadê esse container?

```
$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
```

## Morreu?

```
$ docker ps -a
CONTAINER ID  IMAGE         COMMAND                 CREATED        STATUS                     PORTS  NAMES
096e732d91b2  uefs/fbta:001 "printf 'FÓRUM BAI..."  6 seconds ago  Exited (0) 4 seconds ago          modest_golick
```

---

# Loop infinito!

Vamos criar o script `loop.sh`
```
while true ; do
    AGORA="$(date)"
    echo "${AGORA} => TOU VIVO"
    sleep 1s
done
```

---

# Loop infinito - Dockerfile

```
FROM ubuntu

WORKDIR /app
COPY loop.sh .

CMD ["sh", "loop.sh"]
```

---

# Loop infinito - criando a imagem

```
$ docker build -t  uefs/fbta:002 .
Sending build context to Docker daemon  3.072kB
Step 1/4 : FROM ubuntu
 ---> 20c44cd7596f
Step 2/4 : WORKDIR /app
 ---> f516fc326ed1
Removing intermediate container 4fa1f011c4be
Step 3/4 : COPY loop.sh .
 ---> b1c2579d9689
Step 4/4 : CMD sh loop.sh
 ---> Running in f7f6cff8695d
 ---> 894ace62e2eb
Removing intermediate container f7f6cff8695d
Successfully built 894ace62e2eb
Successfully tagged  uefs/fbta:002
```

---

# Loop infinito - rodando...

```
$ docker run  uefs/fbta:002
Mon Nov 27 02:21:56 UTC 2017 => TOU VIVO
Mon Nov 27 02:21:57 UTC 2017 => TOU VIVO
Mon Nov 27 02:21:58 UTC 2017 => TOU VIVO
Mon Nov 27 02:21:59 UTC 2017 => TOU VIVO
Mon Nov 27 02:22:00 UTC 2017 => TOU VIVO
...
```

---

# Loop infinito - em background ...

```
$ docker run -d  uefs/fbta:002
44d1c36f7faa2ade4317430bad0ae544ad20248ffc2a57f8797cb80a1a4aa6ea

$ docker ps
CONTAINER ID   IMAGE                    COMMAND             CREATED             STATUS        
44d1c36f7faa    uefs/fbta:002   "sh loop.sh"        18 seconds ago      Up 16 seconds 

$ docker logs -f --tail 2 44d1c36f7faa
Mon Nov 27 02:23:44 UTC 2017 => TOU VIVO
Mon Nov 27 02:23:45 UTC 2017 => TOU VIVO
Mon Nov 27 02:23:46 UTC 2017 => TOU VIVO
...
```

--- 

# Loop infinito - mata logo!

```
$ docker kill 44d1c36f7faa
44d1c36f7faa

$ docker ps -a
CONTAINER ID  IMAGE          COMMAND                  CREATED          STATUS                       PORTS   NAMES
4a53c0deae0b  uefs/fbta:002  "sh loop.sh"             9 seconds ago    Exited (137) 2 seconds ago           nostalgic_mirzakhani
096e732d91b2  uefs/fbta:001  "printf 'FÓRUM BAI..."   15 seconds ago   Exited (0) 13 seconds ago            modest_golick
```

---

# Limpando a casa

```
$ docker rm 4a53c0deae0b
$ docker rm 096e732d91b2
```


---

```python
>>> print("oi")
```

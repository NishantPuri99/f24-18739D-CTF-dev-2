FROM ubuntu

# You need build-essential to get "make" and "gcc", and "socat" to run
RUN apt-get update && apt-get install -y python3 build-essential gcc-multilib socat


# This is a default flag, and will be filled in with cmgr
ARG FLAG

# Challenge metadata and artifacts go here. Only root has access
RUN mkdir /challenge && chmod 700 /challenge

# Working directory for copy and commands. 
COPY dotgit.tar.gz /app/
WORKDIR /app

# Copy in files to docker image
COPY ret2win.c Makefile setup-challenge.py ./
RUN python3 setup-challenge.py
# Build CTF challenge and make flag.txt file 
RUN make && tar czvf /challenge/artifacts.tar.gz dotgit.tar.gz

EXPOSE 5555
# PUBLISH 5555 AS socat

CMD ["socat", "tcp-listen:5555,reuseaddr,fork", "EXEC:'/app/ret2win'"]
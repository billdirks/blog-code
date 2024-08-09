FROM debian:bookworm

RUN apt update && apt install -y python3-dbg strace procps emacs-nox perl man-db && apt clean
COPY ./demo.py ./gdb_cmd  ./

CMD ["bash"]

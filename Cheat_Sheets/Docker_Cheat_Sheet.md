# Docker Cheat Sheet

## Verify Installation

```bash
docker --version
docker compose version
```

---

## Start Services

```bash
docker compose up -d
```

---

## Stop Services

```bash
docker compose down
```

---

## View Containers

```bash
docker ps
```

---

## Container Logs

```bash
docker logs <container>
```

---

## Enter Container

```bash
docker exec -it <container> bash
```

---

## Copy File From Container

```bash
docker cp container:/file/path .
```

---

## Restart Container

```bash
docker restart <container>
```
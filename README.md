**Add the `.env` file with the following settings:**

```bash
# Settings Django
SECRET_KEY=
DEBUG=

# Settings Email
EMAIL_HOST=
EMAIL_PORT=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=

#Settings DB
DATABASE_ENGINE=
DATABASE_NAME=
```

---

**Note:** Ensure to keep your `.env` file secure and never commit it to the repository to protect sensitive information.

---

1. Create Docker containers to create the PostgresQL server, Redis and the applications itself with the following command:

```bash
docker-compose build
```

2. Run Docker containers:

```bash
docker-compose up
```
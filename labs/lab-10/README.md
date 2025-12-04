# Lab 10 - Docker

This lab demonstrates containerization of a Flask application with PostgreSQL using Docker.

## Prerequisites

1. Install Docker Desktop: https://docs.docker.com/get-started/get-docker/

## Setup

1. Create a `.env` file in the `labs/lab-10` directory with the following variables:

   ```
   db_name=your_database_name
   db_owner=your_database_user
   db_pass=your_database_password
   ```

2. Build and start the containers:

   ```bash
   docker-compose up --build
   ```

   Or run in detached mode:

   ```bash
   docker-compose up -d --build
   ```

3. Access the Flask application at: http://localhost:5000

## Containers

- **postgres**: PostgreSQL 15 database container
- **flask**: Flask application container

## Volumes

- **postgres_data**: Persistent volume for PostgreSQL data

## Viewing Running Containers

To view running containers:

```bash
docker ps
```

Or use Docker Desktop GUI.

## Accessing PostgreSQL

To access PostgreSQL using psql:

### Using Docker CLI:

```bash
docker exec -it lab10-postgres psql -U <db_owner> -d <db_name>
```

### Using local psql (if installed):

```bash
psql -h localhost -U <db_owner> -d <db_name>
```

## Stopping Containers

To stop the containers:

```bash
docker-compose down
```

To stop and remove volumes (⚠️ this will delete database data):

```bash
docker-compose down -v
```

## Viewing Logs

To view logs from all containers:

```bash
docker-compose logs
```

To view logs from a specific container:

```bash
docker-compose logs flask
docker-compose logs postgres
```

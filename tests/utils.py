import docker
from docker import DockerClient
from docker.models.containers import Container


def create_db():
    client: DockerClient = docker.from_env()
    container_name = "test-db"
    try:
        container: Container = client.containers.get(container_name)
        print("Remove existing container")
        container.stop()
        container.remove()

    except Exception as ex:
        print(f"Error: {str(ex)}")

    container_config = {
        "name": container_name,
        "image": "postgres:14.5-alpine3.16",
        "detach": True,
        "ports": {"5433": "5432"},
        "environment": {
            "POSTGRES_USER": "postgres",
            "POSTGRES_PASSWORD": "postgres",
        }
    }
    container: Container = client.containers.run(**container_config)
    return container

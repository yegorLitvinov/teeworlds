from fabric import api
from fabricio import docker, tasks


host = '195.201.27.44'


@api.hosts(f'root@{host}')
@api.task
def create_docker_network():
    api.run(
        'docker network create --subnet 172.20.0.0/24 --gateway 172.20.0.1 teeworlds',
    )


teeworlds = tasks.ImageBuildDockerTasks(
    service=docker.Container(
        name='teeworlds',
        image='teeworlds',
        options=dict(
            network='teeworlds',
            ip='172.20.0.2',
            publish='8303:8303/udp',
        ),
    ),
    ssh_tunnel='5000:5000',
    registry='localhost:5000',
    hosts=[f'root@{host}'],
    build_path='teeworlds',
)

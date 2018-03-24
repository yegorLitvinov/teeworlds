teeworlds-deploy:
	fab teeworlds

teeworlds-init:
	fab create_docker_network
	fab user_add

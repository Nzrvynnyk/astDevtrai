Create Master VM 
Setup two VM(manager, Worker) with ansible, installed docker, and list of programs, open ports for http, https, and for docker swarm.
Ansible playbook for up docker container with jenkins on Manager VM.
Ansible playbook for docker swarm init, and connect node as worker.
Jenkins pipeline, Docker build image with last updates pushed to docker io then create docker stack on Vm.
Setup git polling check git repo every 15 minutes.


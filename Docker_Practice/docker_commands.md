These are the Docker commands which can be very useful

1. Build A Docker image -> docker build -t <image_name>:<image_tag>
2. Run a Docker image -> docker run <image_name>:<image_tag>
3. Create a container with name -> docker run --name <container_name> <image_name>:<image_tag>
4. Run a docker container in background -> docker run -d <image_name>:<image_tag>
5. Attach a docker image in terminal -> docker attach <container_name>
6. Check the running docker containers -> docker ps 
7. Stop a docker container -> docker stop <container_name>
8. Remove a docker container -> docker rm <container_name>
9. Auto remove a docker container after it is stopped -> 
   1. Run the docker image with autoremove functionality -> docker run --rm <container_name>
   2. Stop the docker image -> docker stop <container_name>
   3. Check the docker processes -> docker ps -a  (Should not see the docker container here should be autodeleted)
10. Check logs of a docker container -> docker logs -f <container_name>
11. Check live logs of a docker container -> docker logs <container_name>
12. Check already running images in docker container -> docker ps -a
13. Transfer a file from local to a docker container -> docker cp <file_path and name> <container_name>:<path>
14. Transfer a file from the docker container to local -> docker cp <container_name>:<file_path> <local_file_path>
15. See the shell inside the docker container -> docker exec -it <container_name> bash
16. Execute a command inside the docker container shell -> docker exec <container_name> ls / 
17. Check the dir structure inside a docker container without going inside it -> docker exec <container_name> ls /app
18. View the docker images -> docker images
19. Determine if the container is running in the background -> docker ps
20. start a docker container again -> docker start <container_name>
21. remove a docker image forcefully ona  running container -> docker rm -f <container_name>
22. Port bind a docker container for the application -> docker run -p <exposed_port>:<port_exposed in dockerfile> <image_name>:<image_tag>
23. Inspect a docker image -> docker inspect <container_name> 
24. 
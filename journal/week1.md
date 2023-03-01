# Week 1 — App Containerization

21/FEB/2023
Completed watching: How to Ask for Technical Help (Before You Ask For Help Watch This)
https://www.youtube.com/watch?v=tDPqmwKMP7Y
Study Notes:
    Detail the error, incl screenshots
    Steps taken to reproduce the error
    Upload file(s) as a gist (gist.github.ciom...)
    gitpod + public repo = easy for someone else to launch your code and assist
    Use web browser inspector (console) to look at any errors
    Use print statements in code to help debug
    Use breakpoints to help debug

23/FEB/2023
Completed watching: Grading Homework Summaries (Grading Homework Summaries)
https://www.youtube.com/watch?v=FKAScachFgk&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=26
Study Notes:
    Some specific highlights is nice
    No need to repeat items from the checklist
    Create Sections to help readability

23/FEB/2023
Completed watching: Remember to Commit Your Code (Week 1- After Stream - Commit Your Code)
https://www.youtube.com/watch?v=b-idMgFFcpg&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=24
Study Notes:
    Don't forget to commit your changes!
    If you do forget and you are using GitPod - reopen the Workspace you were using and you should be able to commit the code

23/FEB/2023
Watching: Week 1 - Live Streamed Video (Week 1 - App Containerization)
https://www.youtube.com/watch?v=zJnNe5Nv4tE&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=23 (00h:00m to 00h:45m)
Study Notes:
    Why Containerise the application
        Makes application portable
        Avoid envionrment configuration repition work
        Consistent environment between developers
        Consistent environment between dev -> uat -> prd
        
    Recommended	by @jamesspurin: linuxserver.io
    Docker Hub = Container Registry hosted by Docker co.
    OCI = Open Container Initiative, Docker Hub meets OCI standard

    Action: confirmed I have dockerhub account
    Action: checked for extension, but Gitpod did not have the VSCode extension for Docker installed
    Action: installed VSCode Docker extension for local install and gitpod workspace

    Docker image "scratch" = official base image
    Dockers layers = union filesystem

    **What is a docker "volume" = volume local to the running container
     
#Note
Got Codespaces up and running with config that matches GitPod Workspace
Interesting to note that when choosing to launch to local VSCode instance the extensions I defined get installed, I don't think I saw that with GitPod when launching VSCode locally (the terminal was still going to GitPod hosted container)

28/FEB/2023
Worked on learning GitPod Workspace configuration

01/03/2023
Worked on learning GitHub CodeSpaces configuration

#Note
I accidentally deleted my Workspace and when I started a new one I saw that I have lost my local install and extensions, so I went down the rabbit hole of gitpod.yml and devcontainer.json configuration, so that AWS CLI is always installed locally, and VSCode extensions do not need reinstalling.

Ref: https://www.gitpod.io/docs/references/ides-and-editors/vscode-extensions

I found the same functionality difference, in that with CodeSpaces I can see and use "add extension to devcontainer" in browser or local VScode, whereas in gitpod I only see "add to gitpod.yml" in the browser.

It has been a fun exercise learning how to configure gitpod and codespaces so that installations and extensions are preserved if I start from a new Github CodeSpace or GitPod Workspace.

Additionally, by having out of sync local repos running in parallel in CodeSpaces and GitPod due to updating their config files, I learn the "git pull --rebase" command to fix my repo sync issues (successfully!)

Interesting references whilst researching:
https://code.visualstudio.com/docs/sourcecontrol/github
https://vscode.github.com/

01/MAR/2023
Watching: Week 1 - Live Streamed Video (Week 1 - App Containerization)
https://www.youtube.com/watch?v=zJnNe5Nv4tE&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=23 (00h:45m to 01h:40m)
Study Notes:
Action: pip3 install -r requirements.txt
(this was executed in dev env)

note: need to this in gitpod to stay in sync

web server is running but 404'ing due to frontend_url and backend_url env var not being configured
the proper URL is /api/activities/home

Action: (locally)
export FRONTEND_URL="*"
export BACKEND_URL="*"
python3 -m flask run --host=0.0.0.0 --port=4567
(make sure the port is unlocked/public)

RUN = cmd creating a layer in the image
CMD = cmd executed once the container is running

unset FRONTEND_URL
unset BACKEND_URL
env | grep FRONTEND_URL
env | grep BACKEND_URL

Action: (locally - starting from home dir)
docker build -t backend-flask ./backend-flask

-t is tagging the container (name:tag so backend-flask:latest by default)
./ from home/subdirectory

Action: (run the container)
docker run --rm -p 4567:4567 -it backend-flask

Problem due to missingg ENV VARS

Action: (lets looks inside the container to see if ENV VARS are set)
1. docker exec -it <container_ID> /bin/bash
2. attach shell using the Docker extension
ENV (and you can see the two URL vars are not set)

Solution
1. Add the ENV VARS in the Dockerfile
2. Pass the ENV VARS to the docker 
if the ENV VARS are already set locally, you don't even need to explicitly pass the full VAR to the docker run command, so;
docker run --rm -p 4567:4567 -it -e FRONTEND_URL='*' -e BACKEND_URL='*' backend-flask
is the same as
docker run --rm -p 4567:4567 -it -e FRONTEND_URL -e BACKEND_URL backend-flask
single-quote the var value due to shell interpretation of what is in " "



#TASKS
- Containerize Application (Dockerfiles, Docker Compose)
- Document the Notification Endpoint for the OpenAI Document
- Write a Flask Backend Endpoint for Notifications
- Write a React Page for Notifications
- Run DynamoDB Local Container and ensure it works
- Run Postgres Container and ensure it works

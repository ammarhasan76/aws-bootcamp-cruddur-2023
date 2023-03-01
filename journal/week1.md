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
https://www.youtube.com/watch?v=zJnNe5Nv4tE&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=23 (00h:45m to 02h:00m)
Study Notes:




#TASKS
- Containerize Application (Dockerfiles, Docker Compose)
- Document the Notification Endpoint for the OpenAI Document
- Write a Flask Backend Endpoint for Notifications
- Write a React Page for Notifications
- Run DynamoDB Local Container and ensure it works
- Run Postgres Container and ensure it works

# Environment variables
## Required
- POSTGRES_USER - Postgresql database user
- POSTGRES_PASSWORD - Postgresql database user password
- POSTGRES_DB - Postgresql database name
# How to start application with Docker
## 1. Install Docker and docker-compose
    Ubuntu:
        1. Set up Docker's apt repository.
            # Add Docker's official GPG key:
            sudo apt-get update
            sudo apt-get install ca-certificates curl
            sudo install -m 0755 -d /etc/apt/keyrings
            sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
            sudo chmod a+r /etc/apt/keyrings/docker.asc

            # Add the repository to Apt sources:
            echo \
                "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
                $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
                sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
            sudo apt-get update 
        2. Install docker packages
             sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
        3. Verify that the installation is successful by running the hello-world image
            sudo docker run hello-world
    Windows:
        1. Install Docker Desktop (https://docs.docker.com/desktop/setup/install/windows-install/)
## 2. Setup environment
    1. Setup REQUIRED environment variables. You can set them in console or you can create separate .env file in docker folder
## 3. Run application with Docker
    1. Go to docker folder
        cd docker
    2. Run application
        docker compose up    OR     docker-compose up
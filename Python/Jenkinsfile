pipeline {
    agent {
        label 'master'
    }

    options {
        skipDefaultCheckout true
        timestamps()
    }

    environment {
        IMAGE_NAME="python.app"
        //REGISTRY_HOST="docker.io"
    }

    parameters {
        gitParameter branch: '',
                branchFilter: 'origin/(.*)',
                defaultValue: 'master',
                description: '',
                name: 'branchName',
                quickFilterEnabled: true,
                selectedValue: 'DEFAULT',
                sortMode: 'ASCENDING_SMART',
                tagFilter: '*',
                type: 'PT_BRANCH_TAG'
    }

    stages {
        stage ('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: params.branchName ]], extensions: [], userRemoteConfigs: [[url: 'https://github.com/Nzrvynnyk/Python.app.git']]])
            }
        }


        stage ('Docker Image Build/Push') {    
            steps {
                script {
                    withDockerRegistry(credentialsId: "dockerhub") {
                        sh "docker build -t ${IMAGE_NAME} -f Dockerfile ." 
                        sh "docker tag ${IMAGE_NAME}:latest nvynnyk/${IMAGE_NAME}:latest"
                        sh "docker push nvynnyk/${IMAGE_NAME}:latest"
                    }
                }
            }
            
        }
        stage ('Docker deploy swarm'){
            steps {
                script  {
                    sh "docker stack deploy -c docker-stack.yml latest"
                }
            }
        }


    }
    
}

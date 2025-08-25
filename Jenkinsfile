#!groovy
//  groovy Jenkinsfile
//  groovy Jenkinsfile
pipeline  {
    agent any;
    stages {
        stage("Automated docker image build") {
            steps {
                echo 'Creating docker image ...'
                sh "docker build -t ish337/test_project_1 -f Dockerfile ."
            }
        }
        stage("docker login") {
            steps {
                echo " ============== docker login =================="
                withCredentials([usernamePassword(credentialsId: 'DockerHub-Credentials', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    sh '''
                    docker login -u $USERNAME -p $PASSWORD
                    '''
                }
            }
        }
        stage("docker image push") {
            steps {
                echo " ============== pushing webserver image =================="
                sh '''
                docker push ish337/test_site
                '''
            }
        }
        stage("docker image webserver run") {
            steps {
                echo " ============== Run webserer  =================="
                sh '''
                docker rm -f test_1 || true
                docker run -d --name=test_1 --restart=always -p 5000:5000  ish337/test_project_1
                '''
            }
        }

    }
}

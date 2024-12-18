pipeline {
    agent any
    stages {
        stage('Enable virtual environment pyats') {
            steps {
                echo 'Setup PYATS environment'
                sh 'python3 -m venv pyats'
                sh 'source pyats/bin/activate'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install netmiko'
            }
        }                        
        stage('List files in Directory') {
            steps {
                echo 'Confirm required files are cloned'
                sh 'ls -la'
            }
        }
        stage('Start the backup of configuration') {
            steps {
                echo 'Backing up config of network devices'
                sh 'python3 backup-config.py'
            }
        }
    }
    post {
        always{
            cleanWs(cleanWhenNotBuilt: false,
                    deleteDirs: true,
                    disableDeferredWipeout: true,
                    notFailBuild: true)
        }
    }
}


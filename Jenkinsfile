pipeline {
    agent any
    stages {
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
    post {
        always{
            cleanWs(cleanWhenNotBuilt: false,
                    deleteDirs: true,
                    disableDeferredWipeout: true,
                    notFailBuild: true)
        }
    }
}

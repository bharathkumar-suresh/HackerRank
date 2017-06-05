pipeline
{
    agent {docker 'docker_slave'}
    stages
    {
        stage('Build')
        {
            steps
            {
                echo 'Building'
                sh 'python helloWorldJenkins.py'
            }
        }
        stage('Test')
        {
            steps
            {
                echo 'Testing'
            }
        }
    }
}    

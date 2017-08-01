pipeline
{
    agent {docker 'bharaths30/dockercontainer1'}
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

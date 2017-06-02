pipeline
{
    agent any
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

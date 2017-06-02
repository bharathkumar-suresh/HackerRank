pipeline
{
    agent any
    stages
    {
        stage('Build')
        {
            steps
            {
                echo 'BUilding'
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

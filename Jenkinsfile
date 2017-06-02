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
                sh 'python hac_3.py'
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

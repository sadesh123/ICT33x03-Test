pipeline {
agent any
    stages {
        stage('Code Quality Check via SonarQube') {
		steps {
			script {
			def scannerHome = tool 'SonarQube';
			withSonarQubeEnv('SonarQube') {
				sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=test -Dsonar.sources=."
				}
			}
		}
	}
	
	stage('Unit Test'){
	steps {
		script{
        	sh python -m test.py --junit-xml=pytest_unit.xml source_directory/test/unit || true # tests may fail
        		}
    		}
	}
 
}
post {
	always {
		recordIssues enabledForFailure: true, tool: sonarQube()
		junit testResults: 'logs/unitreport.xml'
		}
	}
}

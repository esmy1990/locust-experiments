pipeline {
agent any
stages {

    stage('plot')
	{
		steps
		{
		 plot csvFileName: 'plot-a7542f0a-6f4d-45ec-9847-8cee9c060d00.csv', csvSeries: [[displayTableFlag: false, exclusionValues: '', file: 'new.csv', inclusionFlag: 'OFF', url: '']], group: 'Locust', numBuilds: '5', style: 'lineSimple', title: 'Average Response Time', yaxis: 'Name'
						

		} 
	}
}

}

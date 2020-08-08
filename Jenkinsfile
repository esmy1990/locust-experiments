pipeline {
agent any
stages {

    stage('plot')
	{
		steps
		{
			
			plot csvFileName: 'plot-58be76af-b0a3-48c3-83ae-f6d32d15c94c.csv', csvSeries: [[displayTableFlag: false, exclusionValues: 'Average Response Time', file: 'example_stats.csv', inclusionFlag: 'INCLUDE_BY_STRING', url: '']], group: 'Locust', numBuilds: '5', style: 'lineSimple', title: 'Name'
		} 
	}
}

}

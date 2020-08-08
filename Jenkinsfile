pipeline {
agent any
stages {

    stage('plot')
	{
		steps
		{
			
			plot csvFileName: 'plot-919e442c-3e2a-42d7-9174-5e2c4e4ccaeb.csv', csvSeries: [[displayTableFlag: false, exclusionValues: '', file: 'example_stats.csv', inclusionFlag: 'OFF', url: '']], group: 'Locust', numBuilds: '2', style: 'lineSimple', title: 'Name'
		} 
	}
}

}

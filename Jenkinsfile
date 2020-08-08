pipeline {
agent any
stages {

    stage('plot')
	{
		steps
		{
			
			perfReport filterRegex: '', sourceDataFiles: "${currentWorkspace}/example_stats.csv"
			plot csvFileName: 'plot-d5cef80c-b67f-4bcd-9597-cbcf92431178.csv', csvSeries: [[displayTableFlag: false, exclusionValues: '', file: 'example_stats.csv', inclusionFlag: 'OFF', url: '']], group: 'locust', numBuilds: '10', style: 'bar3d', title: 'Name', yaxis: 'Avg response time', yaxisMinimum: '0'
		} 
	}
}

}

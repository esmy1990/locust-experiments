pipeline {
agent any
stages {

    stage('plot')
	{
		steps
		{
			
						plot csvFileName: 'plot-b3474800-6fe5-4e9b-abd2-15805bb2d735.csv', csvSeries: [[displayTableFlag: false, exclusionValues: '', file: 'new.csv', inclusionFlag: 'OFF', url: '']], group: 'Locust', style: 'lineSimple', title: 'Average_response_time', yaxis: 'Name'

		} 
	}
}

}

pipeline {
agent any
stages {

    stage('plot')
	{
		steps
		{
			
						plot csvFileName: 'plot-0b0e87fc-d4ad-4763-9a39-102199893938.csv', csvSeries: [[displayTableFlag: false, exclusionValues: '', file: 'ew.csv', inclusionFlag: 'OFF', url: '']], group: 'locust', numBuilds: '2', style: 'line'

		} 
	}
}

}

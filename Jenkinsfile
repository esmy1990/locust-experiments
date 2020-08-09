pipeline {
agent any
stages {

    stage('plot')
	{
		steps
		{
		 plot csvFileName: 'plot-2b95ec28-0e83-497c-993a-3e35157de7f7.csv', csvSeries: [[displayTableFlag: false, exclusionValues: '', file: 'new.csv', inclusionFlag: 'OFF', url: '']], group: 'Locust', style: 'line', title: 'Avg response time'
						

		} 
	}
}

}

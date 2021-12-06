
Notes:

	As detailed in our report, our raw data is in .fcs files which are specific files for flow cytometry and are unreadable as text files. Due to this format, we cannot create our own mock data and instead, worked to change and edit the code during the replication process to only retrieve the smallest portion (one subpopulation) to be downloaded during our Matlab script. Our project required running information from multiple programs (Matlab, R, as well as Python) and so while we have tried to piece together to the best of our ability the ability to run it, DSMLP probably will not be possible. We reached out however and as it was mentioned that 'even if you can't get a build script working, you should still turn in your code. It should be clear what the scripts are that you didn't write and what you did write', we are submitting what we do have. The matlab scripts are mainly not written by us and by the original authors though we did edit certain lines for them to work, and the python code was written by us. 

 

MATLAB dependencies:

	"Statistics and Machine Learning Toolbox" must be installed
 
R dependencies: 

	Trying to install R dependencies through the Python launch script broke the code, so these should be manually installed before running
	Move evallf.dll and analyzeMC_0.1.1.tar.gz into same directory as scripts
	Install the following dependencies with these RStudio commands:
		install.packages("devtools")
		install_github("christinaheinze/CompareCausalNetworks", build = FALSE)
		install.packages("backShift", dependencies = TRUE)
		install.packages("path_to/analyzeMC_0.1.1.tar.gz", type = "source", repos = NULL) 
		install.packages("fields", dependencies = TRUE)
		install.packages("hmisc", dependencies = TRUE)
		install.packages("reshape2", dependencies = TRUE)

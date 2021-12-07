
Notes:

	As detailed in our report, our raw data is in .fcs files which are specific files for flow cytometry and are unreadable as text files. 
	Due to this unique format, we cannot create our own mock data and instead, worked to change and edit the code during the replication process 
	to only retrieve the smallest portion of our data (one subpopulation) to be used as test data. Our project required running information from
	multiple programs (Matlab, R, as well as Python) and so while we have tried to piece them together into a build script to the best of our 
	ability, there is a possibility it may not run smoothly (especially on DSMLP). We reached out however and it was mentioned that 'even if you 
	can't get a build script working, you should still turn in your code. It should be clear what the scripts are that you didn't write and what 
	you did write'. Therefore, even if the build script does not end up functioning all the individual scripts we used are still available here to 
	be examined. The Matlab and R scripts are primarily written by the authors of the study (we had to do some editing here and there) and the 
	python scripts are written entirely by us. 
 

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
		
Python dependencies:

```pip install -r requirements.txt```

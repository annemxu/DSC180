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

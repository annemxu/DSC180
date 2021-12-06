scrT = tic;
% Set and cd to the main directory
testDir = pwd; 
mainDir = [testDir '\test'];
%addpath(genpath(curPath));

% Where the code is
codeDir = [testDir '\test\_code'];
addpath(genpath(codeDir));


% Where you want to save all data
dataDir = [mainDir filesep 'data'];
if ~isdir(dataDir);mkdir(dataDir);end


% Fcs file folder
fcsDir = [dataDir filesep '_fcs'];
if ~isdir(fcsDir);mkdir(fcsDir);end


% Download zip files
urlFile = [dataDir filesep 'BMreport.html'];
url = 'http://supplemental.cytobank.org/report_data/report_105/fcs_file_downloads.html';
urlwrite(url,urlFile);

inhibitors = {'Akti'};
inhibitorUrls = cell(27,1);
iInh =0;

urlFid = fopen(urlFile, 'r');
zipFile = [testDir '\test\data\Akti.zip'];
fprintf('Downloading %s\n', zipFile);
dT = tic;
fprintf('\n')
fprintf('Getting %s, may take a bit but this was the smallest piece of data we could retrieve due to the pipeline process \n', 'https://s3.amazonaws.com/reports.public.cytobank.org/105/AKTi.zip');
fprintf('\n')
urlwrite('https://s3.amazonaws.com/reports.public.cytobank.org/105/AKTi.zip', zipFile);
fprintf('\t Unzipping %s\n', zipFile);
fprintf('\n')
zT =tic;
fprintf('\n')
unzip(zipFile, fcsDir);
fprintf( 'Unzipped %s in %s, %.3f sec\n', zipFile, fcsDir, toc(zT));
 
fprintf( '\n=======================================================================================\n');
fprintf( '            Finished downloading, time elapsed: %.3f sec                  \n', toc(scrT));
fprintf( '\n=======================================================================================\n');

fclose(urlFid);

clearvars -except *Dir inhibitors logFile



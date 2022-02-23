(fcb-access-aspera)=
# Downloading data with Aspera

````{panels_fairplus}
:identifier_text: FCB015
:identifier_link: http://w3id.org/faircookbook/FCB015
:difficulty_level: 2
:recipe_type: hands_on
:reading_time_minutes: 15
:intended_audience: principal_investigator, data_manager, data_scientist  
:has_executable_code: yeah
:recipe_name: Downloading data with Aspera 
```` 


## Main objectives

This recipe covers documentation of the popular Aspera Fast Transfer Protocol and complements related recipes concerned with efficient files uploads and downloads. While the Aspera protocol is used by major public scientific data repositories such as NCBI SRA and EMBL ENA, it is important to note that the communication protocol is **proprietary**. The recipe will therefore also cover some of the implications of using a closed protocol in terms of achieving FAIR compliance.


## Graphical overview

```{figure_fairplus} aspera.md-figure1.mmd
name: aspera-figure1
subtitle: Aspera Data Transfer Process.
```

---
## Obtain Aspera services

### Get accounts permissions
* Apply for access.
* Pay attention to the conditions.
* Sign up if you are the appropriate person for this download/upload. 
* Typically Aspera sites are locked down and need a username and password.
* For some sites, local rules are in place covering user access. For example only one username may be allowed per organisation, and the users must have demonstrable technical competencies and necessary familiarity with the data, and rules should be in place how to distribute the downloaded data further.
 
### Decide how you are going to access the data
* A Web browser is great for initial browsing and downloading of small occasional files. It will automatically prompt you to download the Aspera broswer plugin to be able to do download any files.
* For heavy duty downloading an Aspera command line client is needed. e.g. to download gigabytes or even terabytes of data.
 
### Decide on software needed and get it installed
 
* For Linux:
  * Aspera ascp. This can be downloaded from:  https://downloads.asperasoft.com/
  * Documentation:
    * General: https://download.asperasoft.com/download/docs/ascp/2.7/html/index.html
    * Examples https://download.asperasoft.com/download/docs/ascp/2.7/html/fasp/ascp-examples.html
 
#### Get the firewall configured as required to allow downloading and or uploading
* You may need to have firewall exceptions raised to unblock ports 3301 and 22, with your organisation IT's network perimeter team. 
* Try connecting first in case they are already not blocked.

#### Work out the appropriate command line options
* For the Aspera command line, there are a large variety of options for downloading and uploading. See the download documentation above.
* Considerations:
  * Use the `-k {1,2,3}`  option to allow restarts without re-downloading all the data.
  * Run it using something like screen, so that it can be running in the background on a server.
  * On the command line you can choose a preferred transfer rate. Please be careful to not hog the network bandwidth (we found up to about 100Mbps is okay).
 
#### Worked-out example for downloading
* These are the download command options we used. (and both ports 3301 and 22 were unblocked)

```bash
#set the password variable corresponding to your Aspera account.
export ASPERA_SCP_FILEPASS="mypassword"
 
#example to download the files recursively from a specific directory on the Aspera server to
$ /hpc/apps/current/aspera/v3.9.6.app/bin/ascp -k 1 -P 33001  -o FileCrypt=decrypt aspera.myacc@aspera-immport.niaid.nih.gov:dir_to_download ./
```
 
* Ascp Version we used:
```bash
$ ascp --version
IBM Aspera Desktop Client version 3.9.6.176292
ascp version 3.9.6.176292
...
```

### Monitoring connections and file transfers

* Observe the  download/upload speed e.g. 100Mbs and then you can estimate the finish time.
* Have some automated monitoring on the download process to  notify you if it  stops/finishes.  Even an hourly `du -sh` from a cron job.
* Also typically you are pulling down many directories and files. On completion, it may be worth doing a recursive file listing to a file e.g. `ls -ltR > file_listing.txt` to give you and your "customers" a simple file catalogue.

### Considerations for uploading

* For uploading much of the above applies. The main differences are:
  * Be aware of geographical zoning and which areas to upload to.
  * Prepare data for ease of tranfer, for instance, organize data in directories or consider data compression prior to transfer (note that this transfers a computational burden of decompression).

<!-- TODO (needed - no real example yet)
* Example command line for uploading
  * 
  -->


## Conclusion

* Aspera is commercial software
* Is this still okay as part of FAIR principles? As long as the instution with the server has paid for the licence, clients for the protocol are available at no fee.


### What to read next?

  - {ref}`fcb-sftp` 
  - <!-- TODO (which recipe would that reference to? why is FAIR evaluation needed here?) --> FAIR Evaluation

---

## Authors

````{authors_fairplus}
Peter: Writing - Original Draft
Philippe: Writing - Review & Editing, Conceptualization
````

--- 

## License

````{license_fairplus}
CC-BY-4.0
````

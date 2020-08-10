---
recipe_metadata:
  - identifier: "none"
  - version: 1.0
difficulty_level: 3
reading_time_in_minutes: 20
type_of_document: "hands on, step-by-step recipe"
document_contains_executable_code: false
intended_audience:
  - "data scientists"
---


# How to download files with Aspera
___

<div class="row">

  <div class="column">
    <div class="card">
      <div class="container">
        <i class="fa fa-qrcode fa-2x" style="color:#7e0038;"></i>
        <h4><b>Recipe metadata</b></h4>
        <p> identifier: <a href="">RX.X</a> </p>
        <p> version: <a href="">v1.0</a> </p>
      </div>
    </div>
  </div>
  <div class="column">
    <div class="card">
      <div class="container">
        <i class="fa fa-fire fa-2x" style="color:#7e0038;"></i>
        <h4><b>Difficulty level</b></h4>
        <i class="fa fa-fire fa-lg" style="color:#7e0038;"></i>
        <i class="fa fa-fire fa-lg" style="color:#7e0038;"></i>
        <i class="fa fa-fire fa-lg" style="color:lightgrey"></i>
        <i class="fa fa-fire fa-lg" style="color:lightgrey"></i>
        <i class="fa fa-fire fa-lg" style="color:lightgrey"></i>
  <!--       <p><span data-v-013baba1="" title="" class=""><svg data-v-013baba1="" viewBox="0 0 16 16" width="1em" height="1em" focusable="false" role="img" alt="icon" xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="bi-bar-chart-fill b-icon bi medium-level"><g data-v-013baba1=""><rect width="4" height="5" x="1" y="10" rx="1"></rect><rect width="4" height="9" x="6" y="6" rx="1"></rect><rect width="4" height="14" x="11" y="1" rx="1"></rect></g></svg> Medium </span></p> -->
      </div>
    </div>
  </div>  
  <div class="column">
    <div class="card">
      <div class="container">
        <i class="fa fa-clock-o fa-2x" style="color:#7e0038;"></i>
        <h4><b>Reading Time</b></h4>
        <p><i class="fa fa-clock-o fa-lg" style="color:#7e0038;"></i> 15 minutes</p>
        <h4><b>Recipe Type</b></h4>
        <p><i class="fa fa-laptop fa-lg" style="color:#7e0038;"></i> Hands-on</p>
        <h4><b>Executable Code</b></h4>
        <p><i class="fa fa-play-circle fa-lg" style="color:#7e0038;"></i> Yes</p>
      </div>
    </div>
  </div>
  <div class="column">
    <div class="card">
      <div class="container">
        <i class="fa fa-group fa-2x" style="color:#7e0038;"></i>
        <h4><b>Intended Audience</b></h4>
        <p> <i class="fa fa-user-md fa-lg" style="color:#7e0038;"></i> Principal Investigators </p>
        <p> <i class="fa fa-database fa-lg" style="color:#7e0038;"></i> Data Managers </p>
        <p> <i class="fa fa-wrench fa-lg" style="color:#7e0038;"></i> Data Scientists </p>
      <!--   <p> <i class="fa fa-money fa-lg" style="color:#7e0038;"></i> Funders</p> -->
      </div>
    </div>
  </div>
</div>
 

___

## Abstract

A recipe to download files from an Aspera Site, it will also help with the uploading. Providing some guidance on how to do this.
This is part of  a group of other related recipes such as the ftp upload/download to help us all more efficiently get to be uploading and downloading files .

## Graphical overview of the Recipe

[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggTFI7XG5cbiBBW0RhdGEgb24gc291cmNlIHJlcG9zaXRvcnldIC0tPkIoRGVjaWRlIGluIG5lZWRlZCBsb2NhdGlvbilcbiAgICBCIC0tPiBDe0RvIHlvdSBoYXZlIGFuIGFjY291bnQgb24gc291cmNlIHJlcG9zaXRvcnk_fVxuICAgIEMgLS0-fFllc3wgRFtEZWNpZGUgaG93IHlvdSBhcmUgeW91IGdvaW5nIGFjY2VzcyB0aGUgZGF0YV1cbiAgICBDIC0tPnxOb3wgRVtHZXQgYW4gYWNjb3VudCBpZiB5b3UgYXJlIHRoZSBhcHBsaWNhYmxlIHBlcnNvbl1cbiAgICBEIC0tPkh7SW5zdGFsbCBkb3dubG9hZC91cGxvYWQgc29mdHdhcmV9XG4gICAgSCAtLT5Je1dvcmsgb3V0IHRoZSBhcHByb3ByaWF0ZSBjb21tYW5kIGxpbmUgb3B0aW9uc31cbiAgICBJIC0tPlp7RG9lcyB5b3VyIHN5c3RlbSBoYXZlIHRoZSBhcHBsaWNhYmxlIGZpcmV3YWxsIGhvbGVzP31cbiAgICBaIC0tPnxZZXN8IEZbSGF2ZSB0aGUgZmlyZXdhbGwgaG9sZXNdXG4gICAgWiAtLT58Tm98IEdbR2V0IGZpcmV3YWxsIGhvbGVzXVxuICAgIEYgLS0-SntTdGFydCBkb3dubG9hZH1cbiAgICBKIC0tPkt7TW9uaXRvciBkb3dubG9hZCBhbmQgY2hlY2sgZG93bmxvYWQgc3BlZWR9XG4gICAgSyAtLT5Me0NoZWNrIGRvd25sb2FkIGFuZCBjcmVhdGUgYSBtaW5pIGRhdGEgY2F0YWxvZ3VlfVxuXG4iLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiZ3JhcGggTFI7XG5cbiBBW0RhdGEgb24gc291cmNlIHJlcG9zaXRvcnldIC0tPkIoRGVjaWRlIGluIG5lZWRlZCBsb2NhdGlvbilcbiAgICBCIC0tPiBDe0RvIHlvdSBoYXZlIGFuIGFjY291bnQgb24gc291cmNlIHJlcG9zaXRvcnk_fVxuICAgIEMgLS0-fFllc3wgRFtEZWNpZGUgaG93IHlvdSBhcmUgeW91IGdvaW5nIGFjY2VzcyB0aGUgZGF0YV1cbiAgICBDIC0tPnxOb3wgRVtHZXQgYW4gYWNjb3VudCBpZiB5b3UgYXJlIHRoZSBhcHBsaWNhYmxlIHBlcnNvbl1cbiAgICBEIC0tPkh7SW5zdGFsbCBkb3dubG9hZC91cGxvYWQgc29mdHdhcmV9XG4gICAgSCAtLT5Je1dvcmsgb3V0IHRoZSBhcHByb3ByaWF0ZSBjb21tYW5kIGxpbmUgb3B0aW9uc31cbiAgICBJIC0tPlp7RG9lcyB5b3VyIHN5c3RlbSBoYXZlIHRoZSBhcHBsaWNhYmxlIGZpcmV3YWxsIGhvbGVzP31cbiAgICBaIC0tPnxZZXN8IEZbSGF2ZSB0aGUgZmlyZXdhbGwgaG9sZXNdXG4gICAgWiAtLT58Tm98IEdbR2V0IGZpcmV3YWxsIGhvbGVzXVxuICAgIEYgLS0-SntTdGFydCBkb3dubG9hZH1cbiAgICBKIC0tPkt7TW9uaXRvciBkb3dubG9hZCBhbmQgY2hlY2sgZG93bmxvYWQgc3BlZWR9XG4gICAgSyAtLT5Me0NoZWNrIGRvd25sb2FkIGFuZCBjcmVhdGUgYSBtaW5pIGRhdGEgY2F0YWxvZ3VlfVxuXG4iLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)

<div class="mermaid">
graph LR;

 A[Data on source repository] -->B(Decide in needed location)
    B --> C{Do you have an account on source repository?}
    C -->|Yes| D[Decide how you are you going access the data]
    C -->|No| E[Get an account if you are the applicable person]
    D -->H{Install download/upload software}
    H -->I{Work out the appropriate command line options}
    I -->Z{Does your system have the applicable firewall holes?}
    Z -->|Yes| F[Have the firewall holes]
    Z -->|No| G[Get firewall holes]
    F -->J{Start download}
    J -->K{Monitor download and check download speed}
    K -->L{Check download and create a mini data catalogue}
</div>
## Capability & Maturity Table

| Capability  | Initial Maturity Level | Final Maturity Level  |
| :------------- | :------------- | :------------- |
| Interoperability | minimal | repeatable |

----
## Get Accounts Permissions:
* Apply for access
* Pay attention to the conditions
* Sign up if you are the appropriate person for this download/upload 
* Typically Aspera sites are locked down and need a username and password.
* For some sites, only one username is allowed per organisation, so it is worth making sure that that person is technically capable of uploading or downloading data, and also understands the data a little.
 
## Decide how you are going to access the data:
* A Web browser is great for initial browsing and downloading of small occasional files. It will automatically prompt you to download the Aspera broswer plugin to be able to do download any files.
* For heavy duty downloading an Aspera command line client is needed. e.g. to download gigabytes or even terrabytes of data.
 
## Decide on Software needed and get it installed:
 
* For linux:
  * Aspera ascp This can be downloaded from:  https://downloads.asperasoft.com/
  * Documentation:
    * General: https://download.asperasoft.com/download/docs/ascp/2.7/html/index.html
    * Examples https://download.asperasoft.com/download/docs/ascp/2.7/html/fasp/ascp-examples.html
 
## Get the Firewall Configured as required to allow downloading and or uploading:
* You may need to have firewall exceptions raised to unblock ports 3301 and 22, with your organisation IT's network perimeter team. 
* Try connecting first in case they are already not blocked

## Work out the appropriate command line options:
* For the Aspera command line, there are a large variety of options for downloading and uploading. See the download documentation above.
* Considerations:
  * Use the `-k {1,2,3}`  option to allow restarts without re-downloading all the data.
  * Run it using something like screen, so that it can be running in the background on a server
  * On the command line you can choose a preferred transfer rate. Please be careful to not hog the network bandwidth (we found up to about 100Mbps is okay).
 
## Download Example command line:
* These are the download command options we used. (and both ports 3301 and 22 were unblocked)
```#set the password variable corresponding to your Aspera account.
export ASPERA_SCP_FILEPASS="mypassword"
 
#example to download the files recursively from a specific directory on the Aspera server to
$ /hpc/apps/current/aspera/v3.9.6.app/bin/ascp -k 1 -P 33001  -o FileCrypt=decrypt aspera.myacc@aspera-immport.niaid.nih.gov:dir_to_download ./
```
 
* Ascp Version we used:
```$ ascp --version
IBM Aspera Desktop Client version 3.9.6.176292
ascp version 3.9.6.176292
...
```

## Other suggestions:
* Observe the  download/upload speed e.g. 100Mbs and then you can estimate the finish time
* Have some automated monitoring on the download process to  notify you if it  stops/finishes.  Even an hourly `du -sh` from a cron job
* Also typically you are pulling down many directories and files. On completion, it may be worth doing a recursive file listing to a file e.g. `ls -ltR > file_listing.txt` to give you and your "customers" a simple file catalogue.

## Considerations for uploading
* For uploading much of the above will apply. the main differences:
  * know which area to upload to
  * prepare your data for ease of loading. E.G. directories? Or compression if needed.
* Example command line for uploading
  * (Needed - no real example yet)

## TO DO:
* Aspera is commercial software
* Is this still okay as part of FAIR principles? As long as the instution with the server has paid for the licence
* Action : ask EBI e.g. Tony or Fuqi (in the presentation)
* Action Philippe: will ask Mark Wilkinson if Aspera is compliant? and how it would work with his evaluator?
* Look at the dockerised version of the client?
* write a new recipe for uploading - probably update this.


## Authors:

| Name           | Affiliation    | orcid          | CrediT role   |
| :------------- | :------------- | :------------- |:------------- |
| Peter Woollard  | GSK, metadata group in R&D Data and Computational Sciences  |  0000-0002-7654-6902 |  Writing - Original Draft |
| Philippe Rocca-Sera | Oxford University| | reviewer |
| | | | |
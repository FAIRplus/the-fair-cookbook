(fcb-sftp)=
# Transferring data with SFTP

````{panels_fairplus}
:identifier_text: FCB014
:identifier_link: http://w3id.org/faircookbook/FCB014
:difficulty_level: 2
:recipe_type: hands_on
:reading_time_minutes: 15
:intended_audience: principal_investigator, data_manager, data_scientist
:has_executable_code: yeah
:recipe_name: Transferring data with SFTP
```` 


`````{margin}
````{panels}
:column: col-4
:card: border-2
:header: bg-primary darkgrey

```{image} RDMkit_logo_inverted.svg
:height: 25px
:class: bg-primary darkgrey
:name: rdmtoolkit_logo
```
^^^ 
[More about `Data Transfer` from the `RDM Toolkit`](https://rdmkit.elixir-europe.org/data_transfer.html)

````
`````




## Abstract

Collaborating teams at two or more organizations often need to transfer and share data files. There are a number of ways to share files, all with various degrees of ease and usability.
The particular information security risk management (ISRM) protocols at the sending and receiving institutions need to be considered when one chooses and optimizes file-transfer solutions.
One common method for transferring files is SFTP or scp (Secure Copy).



## Background info
- SFTP: Secure or SSH File Transfer protocol is a standard way to transfer files securely using a remote server.
- SFTP is not to be confused with FTP or FTPS. While FTP does not use encryption at all and therefore can be considered insecure, FTPS adds a layer of encryption on top of FTP but it still comes with a number of drawbacks from the FTP protocol, e.g. requiring a range of open ports. SFTP uses an entirely different protocol based on SSH (secure shell) and uses strong encryption for authentication information as well as the data transferred.
- In order to upload and download files, the client needs to communicate with the server over port 22 (which is the default port for SFTP) and the network configurations on the sender as well as the recipient side need to allow this traffic. If network restrictions block this communication, one might try to run the SFTP server on a different port (e.g. 443).
- In this scenario, a SFTP server is a pure file transfer server, i.e. it lives outside of any sensitive network area and both parties (the sender and recipient) need to use a SFTP client to upload from and download to their internal storage systems. After transfer and integrity check, files would be typically removed by the receiver.


<!-- ## Graphical Overview

not existent

---

## Capability and Maturity Table.


| Capability  | Initial Maturity Level | Final Maturity Level  |
| :------------- | :------------- | :------------- |
| Interoperability | minimal | repeatable |


## FAIRification Objectives, Inputs and Outputs

COMMENT: the concepts in this recipe did not map to any terms from the EDAM ontology. 

---

## Table of Data Standards

COMMENT: the concepts in this recipe did not map to any terms from the FAIRsharing.org database.-->


## Requirements

For client (receiver/sender):
-	Basic understanding of SFTP client configurations
-	(optional) Basic programming skills to automate upload or download process

For server (system administrator):
-	Compliance with company IT-security policies
-	Understanding firewall configurations
-	Ability to use terminal (bash)


## Recipe instructions

Overview:

- (1)	Setting up SFTP server
  - 1.a.	Instructions
  - 1.b.	Security considerations
- (2)	Data upload/download
  - 2a.	Manual
  - 2b.	Automatic
- (3) Correctness and completeness of transfer

### Setting up a SFTP server

You can run an SFTP server in a Windows environment, e.g. using the open source software FileZilla Server. A Linux server can be set-up  after installing the required libraries (libssh2, OpenSSH). Following is a step-by-step summary for a CentOS server:

a.	Create a dedicated group for all future SFTP users:

```bash
$ groupadd sftpusers
```

b.	First create a folder on a volume with sufficient free space:

```bash
$ mkdir -p /data/sftp
```

c.	Set permissions:

```bash
$ chown root:sftpusers /data/sftp
$ chmod 775 /data/sftp
```

d.	Create one or more SFTP users, assigning them to the previously created group:

```bash
$ useradd -g sftpusers -d / -s /sbin/nologin USERNAME
```

e.	Set the password for the new user:

```bash
$ passwd USERNAME
```

f.	Edit the SSHD configuration at /etc/ssh/sshd_config (e.g. using vi or nano) by adding the following lines:

```bash
Match Group sftpusers
ChrootDirectory /data/sftp
ForceCommand internal-sftp
```

g.	Restart the SSH services

```bash
$ service sshd restart
```

h.	Now you have to make sure you open port 22 in your network to the outside world under a specific domain name or static IP address.


### Data upload and download

#### Manual, i.e. drag'n'drop

Data could be transferred to/from SFTP server using multiple clients. Here there are some examples:

FileZilla

OS: Windows, Mac OS, Linux

License: Free Software (GPL)

Pros:
- easy to setup;
- portable version available (no installation, i.e. administrator rights, required)
- cross-platform

Cons:
-	By default installs adware


WinSCP

OS: Windows

License: Free Software (GPL)

Pros:
- easy to setup;
- portable version available (no installation, i.e. administrator rights, required)

Cons:
-	Only Windows
-	No x64 version (as of 07.07.2020)


Other SFTP clients: Cyberduck, MonstaFTP (Free and paid) and many others

```
{admonition} tip:
The portable version of WinSCP can be preconfigured so that a user only needs to enter the password, without requiring knowledge of host names, protocols, ports or user name!
```

#### Automatic

Libraries implementing SFTP are available for different programming languages.

- Python - pysftp (https://pysftp.readthedocs.io/en/release_0.2.8/index.html#)
- Perl - Net::SFTP (https://metacpan.org/pod/Net::SFTP)
- JavaScript - ssh2-sftp-client (https://www.npmjs.com/package/ssh2-sftp-client)
- Bash - sftp (similar to scp)


### Correctness and completeness of transfer

It is a good practice to ensure that file transfer is correct and complete.

Sender should calculate checksum (md5, sha512, etc) for every file:

```bash
bash: md5sum * > md5sum.txt
```
or
```bash
bash: sha512sum * > sha512sum.txt
```

Windows: CertUtil -hashfile FILENAME MD5
Recipient compares checksums:
```bash
Bash: md5sum -c md5sum.txt *
```
or

```bash
Bash: sha512sum -c sha512sum.txt *
```


The sender can use the sender organization’s HPC node to
- (1)	set up a shell which runs in the background,
- (2)	launch the FTP session in the same local network as the server and directory of files to be transferred.
- (3)	Transfer the files via the filesystem on both the local and remote system

For example, an IMI collaboration project requires transfer and sharing of a number of image data folders, each approximately ~300-500 GB.
The process involved copying the files over to a secure FTP server, the receiving institution copies to their server, then the sender deletes the files on the FTP server.

Pros and cons:
- Double copy process with an intermediate space
- Cumbersome
- Works for mid size data (Gigabyte range)
- It works in most cases, especially if the file transfer is "one-time" batch of files.
- It can be considered a good short term or “one-off” solution.

This common process is described in a number of publically available resources, examples in the Further Reading section below.


## Possible improvements from the state of this recipe:

- One could provide for increased automation by writing a small script to iterate through each directory when one is transferring a set of directories, each containing a number of data files.

---

## Conclusion

This content is a simple guideline for using a well known secure file transfer protocol.
More modern solutions and tools exist for fast transfer or mounting of remote drive. For example [Rclone](https://rclone.org) is one such tool, allowing interaction with cloud storage solutions from a wide array of providers.

### What to read next?

> [Wikipedia article on SFTP](https://en.wikipedia.org/wiki/SSH_File_Transfer_Protocol)
> [The Geek Stuff, FTP and SFTP Beginners guide with 10 examples](https://www.thegeekstuff.com/2010/06/ftp-sftp-tutorial/)
> [Example of customization for a specific institution: University of Luxembourg File Transfer](https://hpc.uni.lu/users/docs/filetransfer.html)
> [Setting up an SFTP server on CentOS](https://www.howtoforge.com/tutorial/how-to-setup-an-sftp-server-on-centos/)
> {ref}`fcb-access-aspera`
> [Rclone](https://rclone.org)


---

## Authors

````{authors_fairplus}
Dorothy: Writing - Original Draft
Vitaly: Writing - Original Draft
Ulrich: Writing - Original Draft
Philippe: Writing - Review & Editing
````


---

## License

````{license_fairplus}
CC-BY-4.0
````

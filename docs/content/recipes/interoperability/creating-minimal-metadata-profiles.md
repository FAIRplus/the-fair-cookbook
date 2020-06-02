# Creating a Metadata Profile 

**identifier:** [RX.X.X](RX.X.X)

**version:** [v0.1](v0.1)

___


**_Difficulty level:_** :triangular_flag_on_post: :triangular_flag_on_post: :triangular_flag_on_post: :triangular_flag_on_post: :white_circle:

**_Reading time:_** 45 minutes

**_Intended Audience:_** 

> :heavy_check_mark:  Terminology Manager

> :heavy_check_mark:  Ontologist

> :heavy_check_mark:  Data Scientist


**_Recipe Type_**: Practical 

**_Executable code_**: No

___

## Graphical Overview:
```
graph TD
  A[Defining a Metadata Requirement Profile: Transcriptomics Data]:::box --> Z:::box
  Z(fa:fa-pie-chart Requirement  Analysis) --> W[fa:fa-file-text fa:fa-bars List of  Requirements: Minimal vs Recommended]

  W:::box --> |Survey State of the Art| C{fa:fa-binoculars <br> Is there<br> prior work?}:::box


  C --> |No| E[fa:fa-magic Create Checklist <br>fa:fa-check-square<br>fa:fa-check-square<br>fa:fa-square-o<br>fa:fa-check-square]:::box
  C --> |Yes| D[Minimum Information Checklist]:::box
  D --> G{Evaluation:<br> is it enough?}:::box
  G --> |Yes| H[fa:fa-recycle Reuse Checklist <br>fa:fa-check-square<br>fa:fa-check-square<br>fa:fa-square-o<br>fa:fa-check-square]:::box
  G --> |No| I[fa:fa-code-fork Extend Checklist <br>fa:fa-check-square<br>fa:fa-check-square<br>fa:fa-square-o<br>fa:fa-check-square<br>fa:fa-check-square]:::box
  H --> K{Machine<br> actionable<br> checklist?<br>fa:fa-code<br> fa:fa-cogs}:::box
  E --> K{Machine<br> actionable<br> checklist?<br>fa:fa-code<br> fa:fa-cogs}:::box
  I --> K{Machine<br> actionable<br> checklist?<br>fa:fa-code<br> fa:fa-cogs}:::box
  K --> |Entity Mapping to Ontology| L[ontology<br> tagged <br>requirements]:::box

  K --> |Entity Data Typing| M[Data<br> typed<br> requirements]:::box
  M --> |Definition of value sets| N[Ontology<br> constrained<br> fa:fa-link requirements]:::box
  K --> |Formalization| J[Machine Readable Metadata Profile <br>fa:fa-code<br> fa:fa-cogs<br>fa:fa-code]:::box
  J --> |Implementation| O[User Friendly Metadata Collection <br> e.g. Form, Tabular template <br> fa:fa-file-excel-o fa:fa-file-excel-o fa:fa-file-excel-o<br> fa:fa-group fa:fa-group fa:fa-group]:::box
  
  linkStyle 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15 stroke:#2a9fc9,stroke-width:1px,color:#2a9fc9,font-family:avenir;
  classDef box font-family:avenir,font-size:14px,fill:#2a9fc9,stroke:#222,color:#fff,stroke-width:1px

```

[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggVERcbiAgQVtEZWZpbmluZyBhIE1ldGFkYXRhIFJlcXVpcmVtZW50IFByb2ZpbGU6IFRyYW5zY3JpcHRvbWljcyBEYXRhXTo6OmJveCAtLT4gWjo6OmJveFxuICBaKGZhOmZhLXBpZS1jaGFydCBSZXF1aXJlbWVudCAgQW5hbHlzaXMpIC0tPiBXW2ZhOmZhLWZpbGUtdGV4dCBmYTpmYS1iYXJzIExpc3Qgb2YgIFJlcXVpcmVtZW50czogTWluaW1hbCB2cyBSZWNvbW1lbmRlZF1cblxuICBXOjo6Ym94IC0tPiB8U3VydmV5IFN0YXRlIG9mIHRoZSBBcnR8IEN7ZmE6ZmEtYmlub2N1bGFycyA8YnI-IElzIHRoZXJlPGJyPiBwcmlvciB3b3JrP306Ojpib3hcblxuXG4gIEMgLS0-IHxOb3wgRVtmYTpmYS1tYWdpYyBDcmVhdGUgQ2hlY2tsaXN0IDxicj5mYTpmYS1jaGVjay1zcXVhcmU8YnI-ZmE6ZmEtY2hlY2stc3F1YXJlPGJyPmZhOmZhLXNxdWFyZS1vPGJyPmZhOmZhLWNoZWNrLXNxdWFyZV06Ojpib3hcbiAgQyAtLT4gfFllc3wgRFtNaW5pbXVtIEluZm9ybWF0aW9uIENoZWNrbGlzdF06Ojpib3hcbiAgRCAtLT4gR3tFdmFsdWF0aW9uOjxicj4gaXMgaXQgZW5vdWdoP306Ojpib3hcbiAgRyAtLT4gfFllc3wgSFtmYTpmYS1yZWN5Y2xlIFJldXNlIENoZWNrbGlzdCA8YnI-ZmE6ZmEtY2hlY2stc3F1YXJlPGJyPmZhOmZhLWNoZWNrLXNxdWFyZTxicj5mYTpmYS1zcXVhcmUtbzxicj5mYTpmYS1jaGVjay1zcXVhcmVdOjo6Ym94XG4gIEcgLS0-IHxOb3wgSVtmYTpmYS1jb2RlLWZvcmsgRXh0ZW5kIENoZWNrbGlzdCA8YnI-ZmE6ZmEtY2hlY2stc3F1YXJlPGJyPmZhOmZhLWNoZWNrLXNxdWFyZTxicj5mYTpmYS1zcXVhcmUtbzxicj5mYTpmYS1jaGVjay1zcXVhcmU8YnI-ZmE6ZmEtY2hlY2stc3F1YXJlXTo6OmJveFxuICBIIC0tPiBLe01hY2hpbmU8YnI-IGFjdGlvbmFibGU8YnI-IGNoZWNrbGlzdD88YnI-ZmE6ZmEtY29kZTxicj4gZmE6ZmEtY29nc306Ojpib3hcbiAgRSAtLT4gS3tNYWNoaW5lPGJyPiBhY3Rpb25hYmxlPGJyPiBjaGVja2xpc3Q_PGJyPmZhOmZhLWNvZGU8YnI-IGZhOmZhLWNvZ3N9Ojo6Ym94XG4gIEkgLS0-IEt7TWFjaGluZTxicj4gYWN0aW9uYWJsZTxicj4gY2hlY2tsaXN0Pzxicj5mYTpmYS1jb2RlPGJyPiBmYTpmYS1jb2dzfTo6OmJveFxuICBLIC0tPiB8RW50aXR5IE1hcHBpbmcgdG8gT250b2xvZ3l8IExbb250b2xvZ3k8YnI-IHRhZ2dlZCA8YnI-cmVxdWlyZW1lbnRzXTo6OmJveFxuXG4gIEsgLS0-IHxFbnRpdHkgRGF0YSBUeXBpbmd8IE1bRGF0YTxicj4gdHlwZWQ8YnI-IHJlcXVpcmVtZW50c106Ojpib3hcbiAgTSAtLT4gfERlZmluaXRpb24gb2YgdmFsdWUgc2V0c3wgTltPbnRvbG9neTxicj4gY29uc3RyYWluZWQ8YnI-IGZhOmZhLWxpbmsgcmVxdWlyZW1lbnRzXTo6OmJveFxuICBLIC0tPiB8Rm9ybWFsaXphdGlvbnwgSltNYWNoaW5lIFJlYWRhYmxlIE1ldGFkYXRhIFByb2ZpbGUgPGJyPmZhOmZhLWNvZGU8YnI-IGZhOmZhLWNvZ3M8YnI-ZmE6ZmEtY29kZV06Ojpib3hcbiAgSiAtLT4gfEltcGxlbWVudGF0aW9ufCBPW1VzZXIgRnJpZW5kbHkgTWV0YWRhdGEgQ29sbGVjdGlvbiA8YnI-IGUuZy4gRm9ybSwgVGFidWxhciB0ZW1wbGF0ZSA8YnI-IGZhOmZhLWZpbGUtZXhjZWwtbyBmYTpmYS1maWxlLWV4Y2VsLW8gZmE6ZmEtZmlsZS1leGNlbC1vPGJyPiBmYTpmYS1ncm91cCBmYTpmYS1ncm91cCBmYTpmYS1ncm91cF06Ojpib3hcbiAgXG4gIGxpbmtTdHlsZSAwLDEsMiwzLDQsNSw2LDcsOCw5LDEwLDExLDEyLDEzLDE0LDE1IHN0cm9rZTojMmE5ZmM5LHN0cm9rZS13aWR0aDoxcHgsY29sb3I6IzJhOWZjOSxmb250LWZhbWlseTphdmVuaXI7XG4gIGNsYXNzRGVmIGJveCBmb250LWZhbWlseTphdmVuaXIsZm9udC1zaXplOjE0cHgsZmlsbDojMmE5ZmM5LHN0cm9rZTojMjIyLGNvbG9yOiNmZmYsc3Ryb2tlLXdpZHRoOjFweFxuXG5cblxuICAiLCJtZXJtYWlkIjp7InRoZW1lIjoibmV1dHJhbCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiZ3JhcGggVERcbiAgQVtEZWZpbmluZyBhIE1ldGFkYXRhIFJlcXVpcmVtZW50IFByb2ZpbGU6IFRyYW5zY3JpcHRvbWljcyBEYXRhXTo6OmJveCAtLT4gWjo6OmJveFxuICBaKGZhOmZhLXBpZS1jaGFydCBSZXF1aXJlbWVudCAgQW5hbHlzaXMpIC0tPiBXW2ZhOmZhLWZpbGUtdGV4dCBmYTpmYS1iYXJzIExpc3Qgb2YgIFJlcXVpcmVtZW50czogTWluaW1hbCB2cyBSZWNvbW1lbmRlZF1cblxuICBXOjo6Ym94IC0tPiB8U3VydmV5IFN0YXRlIG9mIHRoZSBBcnR8IEN7ZmE6ZmEtYmlub2N1bGFycyA8YnI-IElzIHRoZXJlPGJyPiBwcmlvciB3b3JrP306Ojpib3hcblxuXG4gIEMgLS0-IHxOb3wgRVtmYTpmYS1tYWdpYyBDcmVhdGUgQ2hlY2tsaXN0IDxicj5mYTpmYS1jaGVjay1zcXVhcmU8YnI-ZmE6ZmEtY2hlY2stc3F1YXJlPGJyPmZhOmZhLXNxdWFyZS1vPGJyPmZhOmZhLWNoZWNrLXNxdWFyZV06Ojpib3hcbiAgQyAtLT4gfFllc3wgRFtNaW5pbXVtIEluZm9ybWF0aW9uIENoZWNrbGlzdF06Ojpib3hcbiAgRCAtLT4gR3tFdmFsdWF0aW9uOjxicj4gaXMgaXQgZW5vdWdoP306Ojpib3hcbiAgRyAtLT4gfFllc3wgSFtmYTpmYS1yZWN5Y2xlIFJldXNlIENoZWNrbGlzdCA8YnI-ZmE6ZmEtY2hlY2stc3F1YXJlPGJyPmZhOmZhLWNoZWNrLXNxdWFyZTxicj5mYTpmYS1zcXVhcmUtbzxicj5mYTpmYS1jaGVjay1zcXVhcmVdOjo6Ym94XG4gIEcgLS0-IHxOb3wgSVtmYTpmYS1jb2RlLWZvcmsgRXh0ZW5kIENoZWNrbGlzdCA8YnI-ZmE6ZmEtY2hlY2stc3F1YXJlPGJyPmZhOmZhLWNoZWNrLXNxdWFyZTxicj5mYTpmYS1zcXVhcmUtbzxicj5mYTpmYS1jaGVjay1zcXVhcmU8YnI-ZmE6ZmEtY2hlY2stc3F1YXJlXTo6OmJveFxuICBIIC0tPiBLe01hY2hpbmU8YnI-IGFjdGlvbmFibGU8YnI-IGNoZWNrbGlzdD88YnI-ZmE6ZmEtY29kZTxicj4gZmE6ZmEtY29nc306Ojpib3hcbiAgRSAtLT4gS3tNYWNoaW5lPGJyPiBhY3Rpb25hYmxlPGJyPiBjaGVja2xpc3Q_PGJyPmZhOmZhLWNvZGU8YnI-IGZhOmZhLWNvZ3N9Ojo6Ym94XG4gIEkgLS0-IEt7TWFjaGluZTxicj4gYWN0aW9uYWJsZTxicj4gY2hlY2tsaXN0Pzxicj5mYTpmYS1jb2RlPGJyPiBmYTpmYS1jb2dzfTo6OmJveFxuICBLIC0tPiB8RW50aXR5IE1hcHBpbmcgdG8gT250b2xvZ3l8IExbb250b2xvZ3k8YnI-IHRhZ2dlZCA8YnI-cmVxdWlyZW1lbnRzXTo6OmJveFxuXG4gIEsgLS0-IHxFbnRpdHkgRGF0YSBUeXBpbmd8IE1bRGF0YTxicj4gdHlwZWQ8YnI-IHJlcXVpcmVtZW50c106Ojpib3hcbiAgTSAtLT4gfERlZmluaXRpb24gb2YgdmFsdWUgc2V0c3wgTltPbnRvbG9neTxicj4gY29uc3RyYWluZWQ8YnI-IGZhOmZhLWxpbmsgcmVxdWlyZW1lbnRzXTo6OmJveFxuICBLIC0tPiB8Rm9ybWFsaXphdGlvbnwgSltNYWNoaW5lIFJlYWRhYmxlIE1ldGFkYXRhIFByb2ZpbGUgPGJyPmZhOmZhLWNvZGU8YnI-IGZhOmZhLWNvZ3M8YnI-ZmE6ZmEtY29kZV06Ojpib3hcbiAgSiAtLT4gfEltcGxlbWVudGF0aW9ufCBPW1VzZXIgRnJpZW5kbHkgTWV0YWRhdGEgQ29sbGVjdGlvbiA8YnI-IGUuZy4gRm9ybSwgVGFidWxhciB0ZW1wbGF0ZSA8YnI-IGZhOmZhLWZpbGUtZXhjZWwtbyBmYTpmYS1maWxlLWV4Y2VsLW8gZmE6ZmEtZmlsZS1leGNlbC1vPGJyPiBmYTpmYS1ncm91cCBmYTpmYS1ncm91cCBmYTpmYS1ncm91cF06Ojpib3hcbiAgXG4gIGxpbmtTdHlsZSAwLDEsMiwzLDQsNSw2LDcsOCw5LDEwLDExLDEyLDEzLDE0LDE1IHN0cm9rZTojMmE5ZmM5LHN0cm9rZS13aWR0aDoxcHgsY29sb3I6IzJhOWZjOSxmb250LWZhbWlseTphdmVuaXI7XG4gIGNsYXNzRGVmIGJveCBmb250LWZhbWlseTphdmVuaXIsZm9udC1zaXplOjE0cHgsZmlsbDojMmE5ZmM5LHN0cm9rZTojMjIyLGNvbG9yOiNmZmYsc3Ryb2tlLXdpZHRoOjFweFxuXG5cblxuICAiLCJtZXJtYWlkIjp7InRoZW1lIjoibmV1dHJhbCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)

<!--
[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggVERcbiAgQVtEZWZpbmluZyBhIE1ldGFkYXRhIFJlcXVpcmVtZW50IFByb2ZpbGU6IFRyYW5zY3JpcHRvbWljcyBEYXRhXSAtLT4gWlxuICBaKGZhOmZhLXBpZS1jaGFydCBSZXF1aXJlbWVudCAgQW5hbHlzaXMpIC0tPiBXW2ZhOmZhLWZpbGUtdGV4dCBmYTpmYS1iYXJzIExpc3Qgb2YgIFJlcXVpcmVtZW50czogTWluaW1hbCB2cyBSZWNvbW1lbmRlZF1cblxuICBXIC0tPiB8U3VydmV5IFN0YXRlIG9mIHRoZSBBcnR8IEN7ZmE6ZmEtYmlub2N1bGFycyA8YnI-IElzIHRoZXJlPGJyPiBwcmlvciB3b3JrP31cblxuXG4gIEMgLS0-IHxOb3wgRVtmYTpmYS1tYWdpYyBDcmVhdGUgQ2hlY2tsaXN0IDxicj5mYTpmYS1jaGVjay1zcXVhcmU8YnI-ZmE6ZmEtY2hlY2stc3F1YXJlPGJyPmZhOmZhLXNxdWFyZS1vPGJyPmZhOmZhLWNoZWNrLXNxdWFyZV1cbiAgQyAtLT4gfFllc3wgRFtNaW5pbXVtIEluZm9ybWF0aW9uIENoZWNrbGlzdF1cbiAgRCAtLT4gR3tFdmFsdWF0aW9uOjxicj4gaXMgaXQgZW5vdWdoP31cbiAgRyAtLT4gfFllc3wgSFtmYTpmYS1yZWN5Y2xlIFJldXNlIENoZWNrbGlzdCA8YnI-ZmE6ZmEtY2hlY2stc3F1YXJlPGJyPmZhOmZhLWNoZWNrLXNxdWFyZTxicj5mYTpmYS1zcXVhcmUtbzxicj5mYTpmYS1jaGVjay1zcXVhcmVdXG4gIEcgLS0-IHxOb3wgSVtmYTpmYS1jb2RlLWZvcmsgRXh0ZW5kIENoZWNrbGlzdCA8YnI-ZmE6ZmEtY2hlY2stc3F1YXJlPGJyPmZhOmZhLWNoZWNrLXNxdWFyZTxicj5mYTpmYS1zcXVhcmUtbzxicj5mYTpmYS1jaGVjay1zcXVhcmU8YnI-ZmE6ZmEtY2hlY2stc3F1YXJlXVxuICBIIC0tPiBLe01hY2hpbmU8YnI-IGFjdGlvbmFibGU8YnI-IGNoZWNrbGlzdD88YnI-ZmE6ZmEtY29kZTxicj4gZmE6ZmEtY29nc31cbiAgRSAtLT4gS3tNYWNoaW5lPGJyPiBhY3Rpb25hYmxlPGJyPiBjaGVja2xpc3Q_PGJyPmZhOmZhLWNvZGU8YnI-IGZhOmZhLWNvZ3N9XG4gIEkgLS0-IEt7TWFjaGluZTxicj4gYWN0aW9uYWJsZTxicj4gY2hlY2tsaXN0Pzxicj5mYTpmYS1jb2RlPGJyPiBmYTpmYS1jb2dzfVxuICBLIC0tPiB8RW50aXR5IE1hcHBpbmcgdG8gT250b2xvZ3l8IExbb250b2xvZ3k8YnI-IHRhZ2dlZCA8YnI-cmVxdWlyZW1lbnRzXVxuXG4gIEsgLS0-IHxFbnRpdHkgRGF0YSBUeXBpbmd8IE1bRGF0YTxicj4gdHlwZWQ8YnI-IHJlcXVpcmVtZW50c11cbiAgTSAtLT4gfERlZmluaXRpb24gb2YgdmFsdWUgc2V0c3wgTltPbnRvbG9neTxicj4gY29uc3RyYWluZWQ8YnI-IGZhOmZhLWxpbmsgcmVxdWlyZW1lbnRzXVxuICBLIC0tPiB8Rm9ybWFsaXphdGlvbnwgSltNYWNoaW5lIFJlYWRhYmxlIE1ldGFkYXRhIFByb2ZpbGUgPGJyPmZhOmZhLWNvZGU8YnI-IGZhOmZhLWNvZ3M8YnI-ZmE6ZmEtY29kZV1cbiAgSiAtLT4gfEltcGxlbWVudGF0aW9ufCBPW1VzZXIgRnJpZW5kbHkgTWV0YWRhdGEgQ29sbGVjdGlvbiA8YnI-IGUuZy4gRm9ybSwgVGFidWxhciB0ZW1wbGF0ZSA8YnI-IGZhOmZhLWZpbGUtZXhjZWwtbyBmYTpmYS1maWxlLWV4Y2VsLW8gZmE6ZmEtZmlsZS1leGNlbC1vPGJyPiBmYTpmYS1ncm91cCBmYTpmYS1ncm91cCBmYTpmYS1ncm91cF1cblxuXG5cblxuICAiLCJtZXJtYWlkIjp7InRoZW1lIjoibmV1dHJhbCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiZ3JhcGggVERcbiAgQVtEZWZpbmluZyBhIE1ldGFkYXRhIFJlcXVpcmVtZW50IFByb2ZpbGU6IFRyYW5zY3JpcHRvbWljcyBEYXRhXSAtLT4gWlxuICBaKGZhOmZhLXBpZS1jaGFydCBSZXF1aXJlbWVudCAgQW5hbHlzaXMpIC0tPiBXW2ZhOmZhLWZpbGUtdGV4dCBmYTpmYS1iYXJzIExpc3Qgb2YgIFJlcXVpcmVtZW50czogTWluaW1hbCB2cyBSZWNvbW1lbmRlZF1cblxuICBXIC0tPiB8U3VydmV5IFN0YXRlIG9mIHRoZSBBcnR8IEN7ZmE6ZmEtYmlub2N1bGFycyA8YnI-IElzIHRoZXJlPGJyPiBwcmlvciB3b3JrP31cblxuXG4gIEMgLS0-IHxOb3wgRVtmYTpmYS1tYWdpYyBDcmVhdGUgQ2hlY2tsaXN0IDxicj5mYTpmYS1jaGVjay1zcXVhcmU8YnI-ZmE6ZmEtY2hlY2stc3F1YXJlPGJyPmZhOmZhLXNxdWFyZS1vPGJyPmZhOmZhLWNoZWNrLXNxdWFyZV1cbiAgQyAtLT4gfFllc3wgRFtNaW5pbXVtIEluZm9ybWF0aW9uIENoZWNrbGlzdF1cbiAgRCAtLT4gR3tFdmFsdWF0aW9uOjxicj4gaXMgaXQgZW5vdWdoP31cbiAgRyAtLT4gfFllc3wgSFtmYTpmYS1yZWN5Y2xlIFJldXNlIENoZWNrbGlzdCA8YnI-ZmE6ZmEtY2hlY2stc3F1YXJlPGJyPmZhOmZhLWNoZWNrLXNxdWFyZTxicj5mYTpmYS1zcXVhcmUtbzxicj5mYTpmYS1jaGVjay1zcXVhcmVdXG4gIEcgLS0-IHxOb3wgSVtmYTpmYS1jb2RlLWZvcmsgRXh0ZW5kIENoZWNrbGlzdCA8YnI-ZmE6ZmEtY2hlY2stc3F1YXJlPGJyPmZhOmZhLWNoZWNrLXNxdWFyZTxicj5mYTpmYS1zcXVhcmUtbzxicj5mYTpmYS1jaGVjay1zcXVhcmU8YnI-ZmE6ZmEtY2hlY2stc3F1YXJlXVxuICBIIC0tPiBLe01hY2hpbmU8YnI-IGFjdGlvbmFibGU8YnI-IGNoZWNrbGlzdD88YnI-ZmE6ZmEtY29kZTxicj4gZmE6ZmEtY29nc31cbiAgRSAtLT4gS3tNYWNoaW5lPGJyPiBhY3Rpb25hYmxlPGJyPiBjaGVja2xpc3Q_PGJyPmZhOmZhLWNvZGU8YnI-IGZhOmZhLWNvZ3N9XG4gIEkgLS0-IEt7TWFjaGluZTxicj4gYWN0aW9uYWJsZTxicj4gY2hlY2tsaXN0Pzxicj5mYTpmYS1jb2RlPGJyPiBmYTpmYS1jb2dzfVxuICBLIC0tPiB8RW50aXR5IE1hcHBpbmcgdG8gT250b2xvZ3l8IExbb250b2xvZ3k8YnI-IHRhZ2dlZCA8YnI-cmVxdWlyZW1lbnRzXVxuXG4gIEsgLS0-IHxFbnRpdHkgRGF0YSBUeXBpbmd8IE1bRGF0YTxicj4gdHlwZWQ8YnI-IHJlcXVpcmVtZW50c11cbiAgTSAtLT4gfERlZmluaXRpb24gb2YgdmFsdWUgc2V0c3wgTltPbnRvbG9neTxicj4gY29uc3RyYWluZWQ8YnI-IGZhOmZhLWxpbmsgcmVxdWlyZW1lbnRzXVxuICBLIC0tPiB8Rm9ybWFsaXphdGlvbnwgSltNYWNoaW5lIFJlYWRhYmxlIE1ldGFkYXRhIFByb2ZpbGUgPGJyPmZhOmZhLWNvZGU8YnI-IGZhOmZhLWNvZ3M8YnI-ZmE6ZmEtY29kZV1cbiAgSiAtLT4gfEltcGxlbWVudGF0aW9ufCBPW1VzZXIgRnJpZW5kbHkgTWV0YWRhdGEgQ29sbGVjdGlvbiA8YnI-IGUuZy4gRm9ybSwgVGFidWxhciB0ZW1wbGF0ZSA8YnI-IGZhOmZhLWZpbGUtZXhjZWwtbyBmYTpmYS1maWxlLWV4Y2VsLW8gZmE6ZmEtZmlsZS1leGNlbC1vPGJyPiBmYTpmYS1ncm91cCBmYTpmYS1ncm91cCBmYTpmYS1ncm91cF1cblxuXG5cblxuICAiLCJtZXJtYWlkIjp7InRoZW1lIjoibmV1dHJhbCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)
-->

<!--__Copied from [slides](https://docs.google.com/presentation/d/1zdGdkCGzL2XFUNf4bUMeOXIEX6I8iBlL4-b5a5oV0F4/edit#slide=id.g752ddb65ea_0_3) and [squad2 issue #75](https://github.com/FAIRplus/FAIRPlus_squad2/issues/75)__-->

___


## How to generate a metadata template

The following steps are intended as a starting point to guide the generation of a metadata template. 

### Step 1: Define competency questions
- What are the questions you would like to address with the template?
Without a set of a competency questions, important variables may easily be forgotten. It is equally possible to collect too much metadata, making the resulting metadata model opaque and difficult to navigate. Competency questions serve as a guide to identify the most relevant experimental factors.

### Step 2: Define a Minimal Set Of Metadata (MSOM) according to these questions
- Compile metadata from different sources
- Generate consolidated view on metadata by merging attributes as far as possible
- Differentiate metadata available for most of the studies from metadata occurring rarely (sparse matrix)
- Identify gaps in the metadata available for most of the studies comprising data that is considered important but has not been captured in the past
- Define a MSOM to be captured in the future from the metadata that is available for most of the studies and the metadata considered to be important
- Identify available community standards regarding minimal sets of metadata
- Add metadata attributes from those community standards to the MSOM, if they are not yet included
- Assign cardinality to the MSOM (identify mandatory metadata and how many times the attributes may be reported. Some metadata might not be mandatory but are still important to capture, if available)
- Identify appropriate ontologies representing your data and establish an application ontology (see recipe 4 of UC3)
- Assign, as far as possible, ontologies to the MSOM and the sparse matrix 

### Step 3: Introduce semantics into the template
- Identify most important objects to be represented in the model (e.g. study, sample, treatment, result, etc.)
- Make sure to have an appropriate naming strategy for the objects (e.g. an NGSstudy is an OMICSstudy is a Study; do not call an NGSstudy a Study; make sure the granularity fits your purposes)
- Assign MSOM and sparse matrix attributes to the respective objects
- Identify and introduce relationships among the identified objects (e.g. “an NGSstudy contains samples”, “a result is derived from a sample”) 
- Identify dependencies to data not represented as objects at this point in time, but, e.g. as termlists
- Make sure that your model can be expanded subsequently to represent those data as objects, as well
- Integrate the sparse matrix of metadata not contained in the MSOM in the model

### Step 4:  Reality check
- Introduce measures allowing identifying errors in reported data according to your model
- Expose your model to actual data delivered by independent colleagues and capture the errors and gaps that occurred
- Identify errors and gaps that are related to the model and not occurring due to errors in the data
- Adjust the model according to these errors and gaps
- Re-iterate the reality check until no more severe errors and gaps are occurring that are relevant for the previously defined competency questions


## Authors

| Name | Affiliation  | ORCID | CRediT role  |
| :------------- | :------------- | :------------- |:------------- |
| <name> | <institution> | [0000-0000-0000-0000](https://orcid.org/0000-0000-0000-0000) | Writing - Original Draft |
|  | | | Writing - Original Draft | 

## License

<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by-sa.png" height="20"/></a>




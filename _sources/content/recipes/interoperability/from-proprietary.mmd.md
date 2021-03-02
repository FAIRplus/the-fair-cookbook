graph LR;
    A[Data Acquisition]:::box -->B(Raw Data):::box
    B --> C{FAIR by Design}:::box1
    C -->|Yes| D[Standard Compliant Data]:::box
    C -->|No| E[Vendor locked Data]:::box
    F[Metadata available]:::box --> G(sample metadata):::box
    G

linkStyle 0,1,2,3,4,5 stroke:#B30000,stroke-width:1px,color:#B30000,font-family:avenir;

classDef box font-family:avenir,font-size:14px,fill:#B30000,stroke:#222,color:#fff,stroke-width:1px
classDef box1 font-family:avenir,font-size:14px,fill:orange,stroke:#222,color:#fff,stroke-width:1px
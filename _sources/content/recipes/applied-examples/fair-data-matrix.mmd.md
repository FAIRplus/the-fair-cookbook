graph TD;
    A(Excel Document):::box -->B(Raw Data):::box
    B --> C{is wide table?}:::box1
    C -->|Yes| D(perform wide to long table conversion):::box
    C -->|No| E(proceed to semantic markup):::box
    A --> F{has PID?}:::box1
    F -->|Yes| G(perform a curl to test URI):::box
    F -->|No| H(upload to zenodo and obtain DOI):::box

classDef box font-family:avenir,font-size:14px,fill:#B30000,stroke:#222,color:#fff,stroke-width:1px
classDef box1 font-family:avenir,font-size:14px,fill:orange,stroke:#222,color:#fff,stroke-width:1px
linkStyle 0,1,2,3,4 stroke:#B30000,stroke-width:1px,color:#B30000,font-family:avenir;
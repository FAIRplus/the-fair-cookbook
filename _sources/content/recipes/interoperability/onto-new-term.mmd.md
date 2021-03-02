graph TD;
    A(target <br> ontology:::box --> B[identify <br> missing term]:::box
    B --> C(description of <br> requested term):::box
    C --> D{identify <br> request <br> process}:::box1
    A --> D:::box
    D -->|formal <br> process| E[follow <br> guidelines]:::box
    D -->|GitHub with <br> explicit guidelines| F[post GitHub issue <br> following guidelines]:::box
    D -->|GitHub without <br> guidelines| G[post GitHub issue]:::box
    D -->|email| H[write email to <br> editor/owner]:::box
    E --> I{decision <br> on request}:::box1
    F --> I:::box
    G --> I
    H --> I
    I -->|positive| J[use new term]:::box
    I -->|negative| K[find alternative]:::box

linkStyle 0,1,2,3,4,5,6 stroke:#B30000,stroke-width:1px,color:#B30000,font-family:avenir;

classDef box font-family:avenir,font-size:14px,fill:#B30000,stroke:#222,color:#fff,stroke-width:1px
classDef box2 font-family:avenir,font-size:14px,fill:orange,stroke:#222,color:#fff,stroke-width:1px
classDef box1 font-family:avenir,font-size:14px,fill:purple,stroke:#222,color:#fff,stroke-width:1px
classDef box5 font-family:avenir,font-size:14px,fill:#FF3371,stroke:#222,color:#fff,stroke-width:1px
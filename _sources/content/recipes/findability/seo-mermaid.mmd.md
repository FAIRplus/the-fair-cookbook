graph TD
  A(HTML page):::box -->| Search Engine Optimization| B{What <br>type <br> of<br> page?}:::box
  B --> C(Dataset):::box
  B --> D(Data catalog):::box
  B --> E(Data page):::box
  E --> F{What <br> type of <br> data <br> page}:::box
  F --> G(Chemical Substance):::box
  F --> H(Gene):::box
  F --> I(Molecular entity):::box
  F --> J(Protein):::box
  F --> K(Sample):::box
  F --> L(Taxon):::box
  C --> M
  D --> M
  G --> M
  H --> M
  I --> M
  J --> M
  K --> M
  L --> M(Schema.org augmented HTML page):::box
  M --> N(fa:fa-search fa:fa-cog fa:fa-fighter-jet improved discoverability):::box
classDef box font-family:avenir,font-size:14px,fill:#300861,stroke:#222,color:#fff,stroke-width:1px
linkStyle 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19 stroke:#2a9fc9,stroke-width:1px,color:#2a9fc9,font-family:avenir;
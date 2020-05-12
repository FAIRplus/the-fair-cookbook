# FAIR cookbook development roadmap

An overview of the work planned for the coming year.

<div class="mermaid">
gantt
    title A Gantt Diagram
    dateFormat  YYYY-MM-DD
    section Section
    A task           :a1, 2014-01-01, 30d
    Another task     :after a1  , 20d
    section Another
    Task in sec      :2014-01-12  , 12d
    another task      : 24d
</div>


An alternative plan

<div class="mermaid">
gantt
    title Another Gantt Diagram
    dateFormat  YYYY-MM-DD
    section DataCatalog
    model selection and design        :a1, 2020-01-28, 90d
    curatorial policy              :a2, after a1, 5d
    implementation                  :a3, after a2 , 60d
    section Terminology Service
    deploy        :a4, 2020-01-28, 90d
    test               :a5, after a4, 5d
    documentation                  :a6, after a5 , 60d
</div>
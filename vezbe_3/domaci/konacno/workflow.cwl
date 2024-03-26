cwlVersion: v1.0
class: Workflow

inputs: 
  csvFile: File
  kolona: string
  procenat_trening: float

outputs:
  csvOut: 
    type: File
    outputSource: korak-2/csvOut

steps:
  korak-1:
    run: korak-1/korak1.cwl
    in: 
      csvFile: csvFile
    out: [csv]
  korak-2:
    run: korak-2/korak2.cwl
    in:
      csvIn: korak-1/csv
      kolona: kolona
      procenat_trening: procenat_trening
    out: [csvOut]
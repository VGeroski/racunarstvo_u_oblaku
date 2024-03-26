cwlVersion: v1.0
class: CommandLineTool

hints:
  DockerRequirement:
    dockerPull: python-ml
    
inputs:
  script:
    type: File
    inputBinding:
      position: 1

  csvFile:
    type: File
    inputBinding:
      position: 2

outputs:
  csv:
    type: File
    outputBinding:
      glob: "output.csv"
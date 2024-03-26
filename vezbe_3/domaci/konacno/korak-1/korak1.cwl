cwlVersion: v1.0
class: CommandLineTool

hints:
  DockerRequirement:
    dockerPull: vgeroski/dr3-korak-1
    
inputs:
  csvFile:
    type: File
    inputBinding:
      position: 1

outputs:
  csv:
    type: File
    outputBinding:
      glob: "output.csv"

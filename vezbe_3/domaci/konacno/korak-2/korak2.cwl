cwlVersion: v1.0
class: CommandLineTool

hints:
  DockerRequirement:
    dockerPull: vgeroski/dr3-korak-2
    
inputs:
  csvIn:
    type: File
    inputBinding:
      position: 1
  
  kolona:
    type: string
    inputBinding:
      position: 2

  procenat_trening:
    type: float
    inputBinding:
      position: 3

outputs:
  csvOut:
    type: File
    outputBinding:
      glob: "out.txt"

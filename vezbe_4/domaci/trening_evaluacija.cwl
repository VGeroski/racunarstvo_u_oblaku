cwlVersion: v1.0
class: CommandLineTool
baseCommand: python
inputs:
  train_file:
    type: File
    inputBinding:
      position: 1
  test_file:
    type: File
    inputBinding:
      position: 2
  target_column:
    type: string
    inputBinding:
      position: 3
outputs:
  model:
    type: File
    outputBinding:
      glob: "model.pkl"
  performance_file:
    type: File
    outputBinding:
      glob: "performance.txt"

requirements:
  DockerRequirement:
    dockerPull: vgeroski/vezba4-trening-eval

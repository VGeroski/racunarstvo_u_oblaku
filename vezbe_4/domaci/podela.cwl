cwlVersion: v1.0
class: CommandLineTool
baseCommand: python
inputs:
  csv_file:
    type: File
    inputBinding:
      position: 1
  target_column:
    type: string
    inputBinding:
      position: 2
  k_folds:
    type: int
    inputBinding:
      position: 3
outputs:
  train_folds:
    type: File[]
    outputBinding:
      glob: train_fold*.csv
  test_folds:
    type: File[]
    outputBinding:
      glob: test_fold*.csv

requirements:
  DockerRequirement:
    dockerPull: vgeroski/vezba4-podela

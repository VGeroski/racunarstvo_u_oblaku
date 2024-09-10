cwlVersion: v1.0
class: Workflow
inputs:
  csv_file:
    type: File
  target_column:
    type: string
  k_folds:
    type: int

outputs:
  # model_files:
  #   type: File[]
  #   outputSource: train_and_evaluate/model
  model_performance:
    type: File[]
    outputSource: train_and_evaluate/performance_file

steps:
  split_data:
    run: podela.cwl
    in:
      csv_file: csv_file
      target_column: target_column
      k_folds: k_folds
    out: [train_folds, test_folds]

  train_and_evaluate:
    run: trening_evaluacija.cwl
    scatter: [train_file, test_file]
    scatterMethod: dotproduct
    in:
      train_file: split_data/train_folds
      test_file: split_data/test_folds
      target_column: target_column
    out: [model, performance_file]

requirements:
  - class: ScatterFeatureRequirement

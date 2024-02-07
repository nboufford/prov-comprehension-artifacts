# Reproducibility Artifacts for "The Case for Comprehension via Provenance"

In the paper "The Case for Comprehension via Provenance", we present a text-based summarization method for provenance graphs and perform a user study to evaluate users' preference compared to node-link diagrams for reproducibility tasks.

We provide the resources to reproduce our summarization.
Our evaluation uses a Jupyter notebook to anayze and plot the study data.

### Text Summarization

The intructions for text summarization are located in [summarization](https://github.com/nboufford/prov-comprehension-artifacts/tree/main/summarization).

### Node-link Diagram Generation

We manually generated the node-link diagrams for our study. The node-link diagrams are located in the example_workflow directories in [workflows](https://github.com/nboufford/prov-comprehension-artifacts/tree/main/workflows).

### Study Workflows
| Workflow | Title |  Description | 
|---|--|---|
| example_workflow_0  | Task 1 | Single Python script |  
| example_workflow_1  | Task 2 | R preprocessing script followed by Python model training |   
| example_workflow_2  | Task 3 | Running the same train_model script with 3 different cli args, then evaluating which model is best |
| example_workflow_3  | Task 4 | Running a py preprocess script, running a train_model which doesn't output anything, running train_model a second time to get output, then running an evaluation on the model |

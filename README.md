# Reproducibility Artifacts for "The Case for Comprehension via Provenance"

In the paper "The Case for Comprehension via Provenance", we present a text-based summarization method for provenance graphs and perform a user study to evaluate users' preference compared to node-link diagrams for reproducibility tasks.

We provide the resources to reproduce our summarization.
Our evaluation uses a Jupyter notebook to anayze and plot the study data.

### Table of Contents
1. [Introduction](https://github.com/nboufford/prov-comprehension-artifacts/tree/main?tab=readme-ov-file#reproducibility-artifacts-for-the-case-for-comprehension-via-provenance)
2. [Table of Contents](https://github.com/nboufford/prov-comprehension-artifacts/tree/main?tab=readme-ov-file#table-of-contents)
3. [Estimated Time and Resources](https://github.com/nboufford/prov-comprehension-artifacts/tree/main?tab=readme-ov-file#estimated-time-and-resources)
4. [User Study Materials](https://github.com/nboufford/prov-comprehension-artifacts/tree/main?tab=readme-ov-file#user-study-materials)
6. [Reproducing the User Study Evaluation](https://github.com/nboufford/prov-comprehension-artifacts/tree/main?tab=readme-ov-file#reproducing-the-user-study-evaluation)

### Estimated Time and Resources

## User Study Materials

PDF of the user study survey: [qualtrics_survey.pdf](https://github.com/nboufford/prov-comprehension-artifacts/blob/main/qualtrics_survey.pdf).

### Study Workflows
| Workflow | Title |  Description | 
|---|--|---|
| [example_workflow_0](https://github.com/nboufford/prov-comprehension-artifacts/tree/main/workflows/example_workflow_0)  | Task 1 | Single Python script |  
| [example_workflow_1](https://github.com/nboufford/prov-comprehension-artifacts/tree/main/workflows/example_workflow_1)  | Task 2 | R preprocessing script followed by Python model training |   
| [example_workflow_2](https://github.com/nboufford/prov-comprehension-artifacts/tree/main/workflows/example_workflow_2)  | Task 3 | Running the same train_model script with 3 different cli args, then evaluating which model is best |
| [example_workflow_3](https://github.com/nboufford/prov-comprehension-artifacts/tree/main/workflows/example_workflow_3)  | Task 4 | Running a py preprocess script, running a train_model which doesn't output anything, running train_model a second time to get output, then running an evaluation on the model |

### Text Summary Generation
To generate the text summaries in the user study, we used Thoth to collect provenance for the workflows.
We then summarized the provenance using our preprocessing scripts.
We then took the preprocessed provenance and input this to GPT with our prompt.

The intructions for text summarization are located in [summarization](https://github.com/nboufford/prov-comprehension-artifacts/tree/main/summarization).

### Node-link Diagram Generation

We manually generated the node-link diagrams for our study. The node-link diagrams are located in the example_workflow directories in [workflows](https://github.com/nboufford/prov-comprehension-artifacts/tree/main/workflows).

## Reproducing the User Study Evaluation
We ran our user study evaluation using a Jupyter Notebook. 

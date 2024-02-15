# Reproducibility Artifacts for "Computational Experiment Comprehension using Provenance Summarization"

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10627858.svg)](https://doi.org/10.5281/zenodo.10627858)

In the paper "Computational Experiment Comprehension using Provenance Summarization", we present a text-based summarization method for provenance graphs and perform a user study to evaluate users' preference compared to node-link diagrams for reproducibility tasks.

Our evaluation uses a Jupyter notebook to anayze and plot the study data.
We also provide our code for summarizing provenance graphs.

## Table of Contents
1. [Introduction](https://github.com/nboufford/prov-comprehension-artifacts/tree/main?tab=readme-ov-file#reproducibility-artifacts-for-the-case-for-comprehension-via-provenance)
2. [Table of Contents](https://github.com/nboufford/prov-comprehension-artifacts/tree/main?tab=readme-ov-file#table-of-contents)
3. [Estimated Time and Resources](https://github.com/nboufford/prov-comprehension-artifacts/tree/main?tab=readme-ov-file#estimated-time-and-resources)
4. [Reproducing the User Study Evaluation](https://github.com/nboufford/prov-comprehension-artifacts/tree/main?tab=readme-ov-file#reproducing-the-user-study-evaluation)
5. [User Study Materials](https://github.com/nboufford/prov-comprehension-artifacts/tree/main?tab=readme-ov-file#user-study-materials)

## Estimated Time and Resources

The instructions have been tested using Jupyter Lab. The Python environment is provided in [study-evaluation/requirements.txt](https://github.com/nboufford/prov-comprehension-artifacts/tree/main/study-evaluation/requirements.txt). 
We reproduced the evaluation using the following instructions in approximately 10 minutes. This included downloading the notebook, running the notebook, and checking the results.

## Reproducing the User Study Evaluation
We ran our user study evaluation using a Jupyter Notebook. The data and notebook can be found in [study-evaluation](https://github.com/nboufford/prov-comprehension-artifacts/tree/main/study-evaluation). Running the notebook top to bottom will produce the figures in the paper. 

To create your own environment using conda to run this analysis use the following instructions from the top-level directory of this repository:

```{bash}
conda create --name comprehension python=3.9

conda activate comprehension

pip install -r study-evaluation/requirements.txt

jupyter lab
```

Once Jupyter is running, open it in your browser and navigate to the `study-evaluation/eval.ipynb` notebook. This notebook can be run from top to bottom, and it will generate new figures within a new directory: `study-evaluation/fig`. The results saved to this folder can then be compared to the authors results saved in `paper-figures`. 

### Text Summary Generation
To generate the text summaries in the user study, we used [Thoth](https://github.com/ubc-systopia/thoth) to collect provenance for the workflows.
We then summarized the provenance using our preprocessing scripts.
We then took the preprocessed provenance and input this to GPT with our prompt.

We provide our complete set of raw provenance, intermediate processed logs, and final GPT-4 output in the `workflows` directory. The instructions for text summarization, including a step-by-step example to reproduce the log we create as input to GPT-4, are located in [summarization](https://github.com/nboufford/prov-comprehension-artifacts/tree/main/summarization).

## User Study Materials

PDF of the full user study survey: [qualtrics_survey.pdf](https://github.com/nboufford/prov-comprehension-artifacts/blob/main/qualtrics_survey.pdf).

### Study Workflows
| Workflow | Title |  Description | 
|---|--|---|
| [example_workflow_0](https://github.com/nboufford/prov-comprehension-artifacts/tree/main/workflows/example_workflow_0)  | Task 1 | Single Python script |  
| [example_workflow_1](https://github.com/nboufford/prov-comprehension-artifacts/tree/main/workflows/example_workflow_1)  | Task 2 | R preprocessing script followed by Python model training |   
| [example_workflow_2](https://github.com/nboufford/prov-comprehension-artifacts/tree/main/workflows/example_workflow_2)  | Task 3 | Running the same train_model script with 3 different cli args, then evaluating which model is best |
| [example_workflow_3](https://github.com/nboufford/prov-comprehension-artifacts/tree/main/workflows/example_workflow_3)  | Task 4 | Running a py preprocess script, running a train_model which doesn't output anything, running train_model a second time to get output, then running an evaluation on the model |

### Node-link Diagram Generation

We manually generated the node-link diagrams for our study. The node-link diagrams are located in the example_workflow directories in [workflows](https://github.com/nboufford/prov-comprehension-artifacts/tree/main/workflows).

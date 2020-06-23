# Data Labeling Service

## Table of Content

1. Usage

2. Billing

3. Setup

4. Steps

5. 



## Usage

AI Platform Data Labeling Service let you work with human labeler to generate labels for a collection of data that you can use in machine learning models



## Billing

Data Labeling Service pricing depends on 

- Labeling task type: classification, bounding box, tracking etc.

- Units of labels generated

One can look at [https://cloud.google.com/ai-platform/data-labeling/pricing](https://cloud.google.com/ai-platform/data-labeling/pricing) for more infos.



## Setup

To start, you need to add your user account and your service account to the **Data Labeling Editor** IAM role.



## Steps

**Create resources for labelers**

The followings are main steps for creating the resources for labelers

1. [Create datasets to be labelled]([https://cloud.google.com/ai-platform/data-labeling/docs/datasets](https://cloud.google.com/ai-platform/data-labeling/docs/datasets)

2. [Create label sets]([https://cloud.google.com/ai-platform/data-labeling/docs/label-sets](https://cloud.google.com/ai-platform/data-labeling/docs/label-sets)

3. [Create instruction for labelers]([https://cloud.google.com/ai-platform/data-labeling/docs/instructions](https://cloud.google.com/ai-platform/data-labeling/docs/instructions)

**Submit labeling request**

Once resources are created, you can submit your labeling request. Google suggest sending a small dataset first, get labeling results, review them, identify missing cases, then refine your instructions. It usually takes several iterations to get good instructions.

To ensure labeling quality, Google will also contact requester to clarify cases that are not covered by the instructions or are unclear. If human labelers aren't able to complete your task due to lack of understandable instructions, data or instructions submitted in an unsupported language, a requirement for specific domain knowledge in order to complete the data labeling task, or similar reasons, the task might be canceled.

**Review and Export labeled data**

After the labeling task is accomplished, one can review and export the labeled data as csv or json files.

**Evaluate your model using labeled data**

The dataset created can be then used with AI Platform Prediction for evaluating model.





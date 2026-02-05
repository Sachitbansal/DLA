# Deep Learning & Applications – Assignment 1  
## Fully Connected Neural Networks on MNIST

This assignment explores the behavior of **Fully Connected Neural Networks (FCNNs)** on image data and highlights their limitations in understanding spatial structure. All experiments are performed on the **MNIST handwritten digits dataset** using PyTorch.

---

## Dataset

**MNIST Handwritten Digits**
- Grayscale images of size **28 × 28**
- 10 classes (digits 0–9)
- Images are normalized to the range **[0, 1]**
- Each image is flattened into a **784-dimensional feature vector** before being fed into the network

---

## Model Architecture

A simple Fully Connected Neural Network is used throughout all experiments:

- Input Layer : 784 neurons (flattened pixels)
- Hidden Layer : 128 neurons + ReLU activation
- Output Layer : 10 neurons (logits)
- Loss Function: `CrossEntropyLoss`
- Optimizer: `Adam`
- Learning Rate: `1e-3`
- Training Epochs: 5
- Batch Size: 128

No softmax is applied in the model’s forward pass, as `CrossEntropyLoss` internally performs `LogSoftmax`.

---

## Question 2.1 – Weight Visualization

### Objective

To understand **what patterns a Fully Connected Network learns** from raw pixel data by visualizing the weights of the first hidden layer.

---

### Method

- After training the FCNN on MNIST, the weight matrix of the first hidden layer is extracted.
- The weight matrix has shape `(H, 784)`, where each **row corresponds to one hidden neuron**.
- For visualization:
  - We select **10 hidden neurons**
  - Each neuron’s 784 weights are reshaped into a **28 × 28 grid**
  - The reshaped weights are visualized as **heatmaps**

---

### Observations

- Several neurons learn **stroke-like patterns**, such as:
  - vertical lines
  - diagonal strokes
  - curved segments
- Some neurons appear **noisy or unstructured**.
- No neuron learns a complete digit; instead, each learns a **partial feature**.

---

### Interpretation

Each hidden neuron acts as a **template matcher**, firing strongly when the input image aligns with the pattern encoded in its weights.  
However, because FCNNs lack spatial inductive bias, the learned features are **global and less structured** compared to convolutional networks.

The presence of noisy neurons can be attributed to:
- Redundant capacity in the hidden layer
- Neurons that are rarely activated and therefore receive weak gradient updates
- Pixels (e.g., image corners) that are almost always inactive in MNIST

---

## Question 2.2 – The “Flattening” Experiment

### Objective

To demonstrate that Fully Connected Neural Networks **do not utilize spatial information**, by showing that pixel order does not significantly affect performance.

---

### Method

- A **single fixed random permutation** of the 784 pixel indices is generated.
- This permutation is applied to **every image** in both the training and test sets.
- The same FCNN architecture and training setup are used.
- Performance is compared between:
  - Normal MNIST
  - Scrambled MNIST

---

### Results

| Dataset           | Test Accuracy |
|-------------------|---------------|
| Normal MNIST      | **97.80%**    |
| Scrambled MNIST   | **97.57%**    |

---

### Observations

- The FCNN achieves **almost identical accuracy** on both normal and scrambled MNIST.
- This contrasts sharply with human perception, where scrambled images are unrecognizable.

---

### Explanation

A Fully Connected Neural Network treats input as a **784-dimensional feature vector**, with no understanding of spatial relationships between pixels.  
Scrambling the pixels simply reorders the input features, and the network learns a new set of weights corresponding to this ordering.

Humans, on the other hand, rely heavily on **spatial continuity, edges, and local structure**, which are completely destroyed by pixel scrambling.

---

### Key Insight

> Fully Connected Neural Networks lack spatial awareness.  
> Their performance depends on feature correlations rather than spatial structure.

This experiment highlights why **Convolutional Neural Networks (CNNs)** are better suited for image-based tasks, as they explicitly encode locality and spatial relationships.

---

## Conclusion

Through these experiments, we observe that:
- FCNNs can learn meaningful patterns from pixel data
- They do not exploit spatial structure
- High accuracy does not imply human-like understanding
- Architectural inductive bias is crucial for vision tasks

These findings motivate the use of convolutional architectures for image recognition problems.

---

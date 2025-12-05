# SelfAug
SelfAug: Mitigating Catastrophic Forgetting in Retrieval-Augmented Generation via Distribution Self-Alignment

## Method
![method](./Figures/Method.png)

SelfAug mitigates catastrophic forgetting by leveraging the original model’s input sequence logits during fine-tuning, allowing the model to learn downstream task responses while preserving its original distribution. The total loss combines the negative log-likelihood loss for the task and the KL divergence loss for the input sequence logits, with a hyperparameter balancing the two. Unlike methods that require data replay or response generation, SelfAug requires no additional data or complex validation steps, simplifying implementation and reducing computational overhead, while effectively maintaining the model’s general knowledge and adaptability.

## File Description

- `update_module.py`: The main script used for copying files to their respective target paths.
- `modeling_qwen2.py`: The file that needs to be copied to the `transformers/models/qwen2` directory in the Python package.
- `layer.py`: The file that needs to be copied to the `peft/tuners/lora` directory in the Python package.

## Execution Instructions

1. Ensure that the files `modeling_qwen2.py` and `layer.py` are present in the current directory.

2. Before performing LoRA fine-tuning, run the `update_module.py` script to replace the necessary files in the `transformers` package.

Command to execute:

```bash
python update_module.py
```

3. After updating, proceed with LoRA fine-tuning using the `transformers` package as usual.

## Citation
@article{huang2025selfaug,
  title={Selfaug: Mitigating catastrophic forgetting in retrieval-augmented generation via distribution self-alignment},
  author={Huang, Yuqing and Zhang, Rongyang and Wang, Qimeng and Lu, Chengqiang and Gao, Yan and Wu, Yi and Hu, Yao and Zhi, Xuyang and Liu, Guiquan and Li, Xin and others},
  journal={arXiv preprint arXiv:2509.03934},
  year={2025}
}

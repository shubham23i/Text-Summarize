import os
import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from transformers import DataCollatorForSeq2Seq
from transformers import Seq2SeqTrainingArguments, Seq2SeqTrainer
from datasets import load_from_disk
from textSummarizer.entity import ModelTrainerConfig


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):

        print("CUDA Available:", torch.cuda.is_available())

        if torch.cuda.is_available():
            print("GPU Name:", torch.cuda.get_device_name(0))
        else:
            print("Training on CPU")

        # Device setup
        device = "cuda" if torch.cuda.is_available() else "cpu"

        # Load tokenizer and model
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)

        model = AutoModelForSeq2SeqLM.from_pretrained(
            self.config.model_ckpt
        ).to(device)

        # Data collator
        seq2seq_data_collator = DataCollatorForSeq2Seq(
            tokenizer,
            model=model
        )

        # Load dataset
        dataset_samsum_pt = load_from_disk(self.config.data_path)

        # OPTIONAL: Reduce dataset size for faster CPU training
        dataset_samsum_pt["train"] = dataset_samsum_pt["train"].select(range(1000))
        dataset_samsum_pt["validation"] = dataset_samsum_pt["validation"].select(range(200))

        # Training arguments
        trainer_args = Seq2SeqTrainingArguments(
            output_dir=str(self.config.root_dir),

            num_train_epochs=self.config.num_train_epochs,

            warmup_steps=self.config.warmup_steps,

            per_device_train_batch_size=self.config.per_device_train_batch_size,

            per_device_eval_batch_size=self.config.per_device_train_batch_size,

            weight_decay=self.config.weight_decay,

            logging_steps=self.config.logging_steps,

            eval_strategy=self.config.evaluation_strategy,

            save_steps=self.config.save_steps,

            gradient_accumulation_steps=self.config.gradient_accumulation_steps,

            fp16=False,

            dataloader_num_workers=0,

            report_to=[],

            logging_dir=None
        )
        trainer = Seq2SeqTrainer(
            model=model,
            args=trainer_args,
            data_collator=seq2seq_data_collator,
            train_dataset=dataset_samsum_pt["train"],
            eval_dataset=dataset_samsum_pt["validation"],
            tokenizer=tokenizer
        )
        # Start training
        trainer.train()

        # Save model
        model_save_path = os.path.join(
            self.config.root_dir,
            "t5-samsum-model"
        )

        tokenizer_save_path = os.path.join(
            self.config.root_dir,
            "tokenizer"
        )

        model.save_pretrained(model_save_path)
        tokenizer.save_pretrained(tokenizer_save_path)

        print("Model saved successfully")
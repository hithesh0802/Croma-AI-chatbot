from transformers import T5Tokenizer, T5ForConditionalGeneration, Seq2SeqTrainer, Seq2SeqTrainingArguments
from datasets import load_from_disk

def train_t5_model(processed_data_path, model_output_dir):
    # Load the preprocessed dataset
    dataset = load_from_disk(processed_data_path)
    
    # Load T5 model and tokenizer
    model_name = "t5-base"
    tokenizer = T5Tokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name)
    
    # Preprocess data into tokenized format
    def preprocess_function(examples):
        inputs = examples['input_text']
        targets = examples['target_text']
        
        # Tokenize inputs and targets with padding and truncation
        model_inputs = tokenizer(inputs, max_length=512, truncation=True, padding="max_length")
        labels = tokenizer(targets, max_length=512, truncation=True, padding="max_length")
        
        model_inputs['labels'] = labels['input_ids']
        return model_inputs


    # Tokenize the dataset
    tokenized_dataset = dataset.map(preprocess_function, batched=True)
    
    # Set up training arguments
    training_args = Seq2SeqTrainingArguments(
        output_dir=model_output_dir,
        evaluation_strategy="epoch",
        learning_rate=2e-5,
        per_device_train_batch_size=2,  # Change from 4 to 2
        per_device_eval_batch_size=2,    # Change from 4 to 2
        weight_decay=0.01,
        save_total_limit=3,
        num_train_epochs=1,
        predict_with_generate=True
    )

    # Initialize trainer
    trainer = Seq2SeqTrainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset,
        eval_dataset=tokenized_dataset,
        tokenizer=tokenizer
    )
    
    # Fine-tune the model
    trainer.train()

if __name__ == "__main__":
    train_t5_model("processed_dataset", "./trained_t5_model")

from utils.seeds import set_global_seed
from training.trainer import Trainer
from evaluation.evaluator import Evaluator

def main(cfg):
    set_global_seed(cfg.seed)

    trainer = Trainer(...)
    evaluator = Evaluator()

    for epoch in range(cfg.epochs):
        train_loss = trainer.train_epoch(cfg.train_loader)
        val_loss = trainer.evaluate(cfg.val_loader)

    y_hat = trainer.model.predict(cfg.X_test)
    metrics = evaluator.evaluate(y_hat, cfg.y_test)

    print(metrics)

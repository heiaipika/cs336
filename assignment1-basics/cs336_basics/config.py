




class ModelConfig:
    max_seq_len: int = 256
    vocab_size: int = 10000
    d_model: int = 512
    num_heads: int = 16
    use_rope: bool = True
    theta: float = 10000.0
    max_seq_len: int = 256
    d_ff: int = 1344
    num_layers: int = 4
    tie_weights: bool = False
    use_final_norm: bool = False
import pandas as pd
from expert_systems_project import balance_dataset

def test_balance_dataset_downsample_and_upsample():
    # Create a small sample dataframe with an "unknown" class and another intent
    df = pd.DataFrame({
        "intent": ["unknown", "unknown", "unknown", "intent1", "intent1"],
        "text": ["u1", "u2", "u3", "i1a", "i1b"]
    })

    # Balance dataset with specific limits
    balanced = balance_dataset(df, unknown_limit=2, target_samples=5)

    # Check that unknown class was downsampled to the limit
    assert (balanced['intent'] == 'unknown').sum() == 2

    # Check that other intent was upsampled to the target_samples
    assert (balanced['intent'] == 'intent1').sum() == 5

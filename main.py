import pandas as pd
from utils import validate_inputs, test_stationarity
from config import CONFIG

def main():
    # Example inputs: Replace these with real data or dynamic input handling
    returns_data = pd.DataFrame({
        'Date': ['2023-01-01', '2023-01-02', '2023-01-03'],
        'Returns': [0.02, 0.01, -0.01]
    })

    try:
        validated_returns = validate_inputs(returns_data)

        # Perform stationarity test
        print("\nStationarity Test Results:")
        stationarity_results = test_stationarity(validated_returns)
        print(stationarity_results)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

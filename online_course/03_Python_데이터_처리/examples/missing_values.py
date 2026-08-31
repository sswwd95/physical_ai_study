"""Pandas에서 결측치를 확인하고 간단히 처리하는 예제."""
import pandas as pd


def main():
    df = pd.DataFrame({
        "temperature": [20.1, None, 21.7, 22.0],
        "humidity": [40.0, 42.0, None, 45.0],
    })

    print("missing values")
    print(df.isna().sum())

    filled = df.copy()
    filled["temperature"] = filled["temperature"].fillna(filled["temperature"].mean())
    filled["humidity"] = filled["humidity"].interpolate()

    print("\nfilled")
    print(filled)


if __name__ == "__main__":
    main()

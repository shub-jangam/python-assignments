from project.dataloading import load_data
from project.preProcoessing import preprocess_data , perform_eda
from project.modlebuilding import build_model
from project.evaluation import evaluate_model


def main():
    print("--- Load Data ---")
    df = load_data()
    
    print("--- Perform EDA ---")
    perform_eda(df)

    print("--- Preprocess Data ---")
    X, y = preprocess_data(df)

    print("---Build and Train Model ---")
    model, X_test, y_test = build_model(X, y)

    print("--- Evaluate Model ---")
    evaluate_model(model, X_test, y_test)

if __name__ == "__main__":
    main()

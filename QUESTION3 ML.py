{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b1255bca",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mean Squared Error: 33596915.851361476\n",
      "R-squared Score: 0.7835929767120722\n",
      "Sample Predictions: [ 8969.55027444  7068.74744287 36858.41091155  9454.67850053\n",
      " 26973.17345656]\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "from sklearn.preprocessing import StandardScaler\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.linear_model import LinearRegression\n",
    "from sklearn.metrics import mean_squared_error, r2_score\n",
    "\n",
    "# Load the dataset\n",
    "data = pd.read_csv('insurance.csv')\n",
    "\n",
    "# Step 1: Encode categorical variables\n",
    "categorical_features = ['sex', 'smoker', 'region']\n",
    "data_encoded = pd.get_dummies(data, columns=categorical_features, drop_first=True)\n",
    "\n",
    "# Step 2: Feature selection\n",
    "X = data_encoded.drop(columns=['charges'])  # Input features\n",
    "y = data_encoded['charges']  # Target variable\n",
    "\n",
    "# Step 3: Standardize the features\n",
    "scaler = StandardScaler()\n",
    "X_scaled = scaler.fit_transform(X)\n",
    "\n",
    "# Step 4: Split the data into training and testing sets\n",
    "X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)\n",
    "\n",
    "# Step 5: Train the Linear Regression model\n",
    "model = LinearRegression()\n",
    "model.fit(X_train, y_train)\n",
    "\n",
    "# Step 6: Evaluate the model\n",
    "y_pred = model.predict(X_test)\n",
    "mse = mean_squared_error(y_test, y_pred)\n",
    "r2 = r2_score(y_test, y_pred)\n",
    "\n",
    "print(f\"Mean Squared Error: {mse}\")\n",
    "print(f\"R-squared Score: {r2}\")\n",
    "\n",
    "# Step 7: Predict charges using the model\n",
    "predictions = model.predict(X_test)\n",
    "print(\"Sample Predictions:\", predictions[:5])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a62fad8b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

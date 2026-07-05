Getting Started with Sycophant-Zero
To get the engine running, follow these steps to set up your environment:
1. Install Dependencies
Ensure you have Python 3 installed. Open your terminal or command prompt, navigate to the project directory, and install the required libraries:
pip install -r requirements.txt
2. API Configuration
You will need to provide your Groq API keys for the engine to function.
Create a file named api_keys.txt in the project root directory.
Paste your Groq API keys into this file, one per line.
Recommendation: Use a minimum of 10 keys to handle rate limiting effectively; 20 keys are highly recommended for uninterrupted performance during intensive tasks.
3. Executing the Engine
Once configured, simply launch the tool with the following command:
python3 Sycophant.py
4. Interactive Setup
Upon launching, the engine will prompt you for the following information to initialize the session:
Endpoint: api endpint of the model
Model Name: Enter the specific model you wish to target .
